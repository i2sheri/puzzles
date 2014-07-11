#!/usr/bin/python

"""Chose the best value meal in town."""

import csv
import itertools
import sys

__author__ = 'Sharath Kumar Suroju'
__email__ = 'i2sheri@gmail.com'
__date__ = '2014-04-18'


class Restaurant(object):
    """Chose the best value meal in town."""
    __menu_file = None
    menu = {}

    __add = lambda self, op1, op2: op1 + op2
    __red = lambda self, c_menu, c_order: reduce(self.__add,
                                             (c_menu.get(o) for o in c_order))

    def __init__(self, menu_file):
        self.__menu_file = menu_file
        self.price = None
        self.restaurant = None

    def populate_menu(self):
        """Parse CSV file and populate City Menu."""
        with open(self.__menu_file, 'rb') as menu_file:
            reader = csv.reader(menu_file)
            for row in reader:
                if len(row) > 0:
                    rest = int(row[0])
                    item, is_combo = get_item(row)
                    rest_menu = self.menu.get(rest)
                    if is_combo:
                        if rest_menu:
                            combo = rest_menu.get('combo')
                            if combo:
                                combo[item] = float(row[1])
                            else:
                                rest_menu['combo'] = {item: float(row[1])}
                        else:
                            rest_menu = {'combo': {item: float(row[1])}}
                    else:
                        if rest_menu:
                            rest_menu[item] = float(row[1])
                        else:
                            rest_menu = {item: float(row[1])}
                    self.menu[rest] = rest_menu

    def __menu_exists(self, order):
        """Return restaurants which can serve the order.
           Include value meals if any restaurant serves."""
        menus = []
        combos = {}
        for rest in iter(self.menu):
            rest_menu = self.menu.get(rest)
            items = set(rest_menu)
            combo_items = ()
            if rest_menu.get('combo'):
                combo_list = []
                combo_items = reduce(self.__add, rest_menu.get('combo'))
                for combo in rest_menu.get('combo'):
                    if (any(o in combo for o in order) and
                       order <= items | set(combo)):
                        combo_list.append(combo)
                if combo_list:
                    combos[rest] = combo_list
                else:
                    if (any(o in combo_items for o in order) and
                        order <= items | set(combo_items)):
                        combos[rest] = ['ALL']
            if order <= items:
                menus.append(rest)
        return (menus, combos)

    def __set_result(self, new_price, rest_id):
        """Update price and restaurant."""
        if not self.price or new_price < self.price:
            self.price, self.restaurant = new_price, rest_id

    def __print_price(self, menus, order):
        """Print most economic price and restaurant of the order."""
        for rest_id in menus[0]:
            new_price = self.__red(self.menu.get(rest_id), order)
            self.__set_result(new_price, rest_id)

        for rest_id in menus[1]:
            mul_combos = []
            rest_menu = self.menu.get(rest_id)
            for c_option in menus[1].get(rest_id):
                if c_option == 'ALL':
                    iterable = rest_menu.get('combo')
                    for i in xrange(len(iterable), 1, -1):
                        for comb in itertools.combinations(iterable, i):
                            if (order <= set(reduce(self.__add, comb)) |
                                set(rest_menu)):
                                # new_price = self.__red(iterable, order)
                                new_price = reduce(self.__add,
                                                   (c[1] for c in comb))
                                self.__set_result(new_price, rest_id)
                else:
                    new_price = rest_menu.get('combo').get(c_option)
                    if self.price and new_price > self.price:
                        continue
                    else:
                        mul_combos.append((c_option, new_price))
                        r_order = order - set(c_option)
                        if r_order:
                            new_price += self.__red(rest_menu, r_order)
                        self.__set_result(new_price, rest_id)

            if len(mul_combos) > 1:
                for k in xrange(len(mul_combos), 1, -1):
                    for comb in itertools.combinations(mul_combos, k):
                        new_price = reduce(self.__add, (c[1] for c in comb))
                        if self.price > new_price:
                            r_order = order - set(reduce(self.__add,
                                                         (c[0] for c in comb)))
                            if r_order:
                                new_price += self.__red(rest_menu, r_order)
                                self.__set_result(new_price, rest_id)

        print '%s, %s' % (self.restaurant, self.price)

    def resolve_order(self, order):
        """Get Best Value Meal from all menus."""
        # Parse given XML menu and populate menu
        self.populate_menu()

        # Get Restaurants which can serve order and possible ways of serving
        menus = self.__menu_exists(order)

        if menus[0] or menus[1]:
            self.__print_price(menus, order)
        else:
            print 'Menu does not exist'

def get_item(row):
    """Parse input line."""
    if len(row) == 3:
        return row[2].strip(), False
    else:
        return tuple([x.strip() for x in row[2:]]), True

if __name__ == "__main__":
    Restaurant(sys.argv[1]).resolve_order(set(sys.argv[2:]))
