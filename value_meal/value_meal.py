#!/usr/bin/python

"""Chose the best value meal in town."""

import argparse
import csv
import itertools

__author__ = 'Sharath Kumar Suroju'
__email__ = 'i2sheri@gmail.com'
__date__ = '2014-04-18'


class Restaurant(object):
    """Chose the best value meal in town."""
    __menu_file = None
    menu = {}

    __add = lambda self, op1, op2: op1 + op2

    def __init__(self, menu_file):
        self.__menu_file = menu_file

    def populate_menu(self):
        """Parse CSV file and populate City Menu."""
        with open(self.__menu_file, 'rb') as menu_file:
            reader = csv.reader(menu_file)
            for row in reader:
                rest = int(row[0])
                item, is_combo = self.__get_item(row)
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


    def __get_item(self, row):
        """Parse input line."""
        if len(row) == 3:
            return row[2], False
        else:
            return tuple(row[2:]), True

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

    def __print_price(self, menus, order):
        """Print most economic price and restaurant of the order."""
        price = None
        restaurant = None
        for rest_id in menus[0]:
            new_price = reduce(self.__add,
                               (self.menu.get(rest_id).get(o) for o in order))
            if not price or new_price < price:
                price, restaurant = new_price, rest_id

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
                                new_price = reduce(self.__add,
                                           (iterable.get(c) for c in comb))
                                if not price or new_price < price:
                                    price, restaurant = new_price, rest_id
                else:
                    new_price = rest_menu.get('combo').get(c_option)
                    if price and new_price > price:
                        continue
                    else:
                        mul_combos.append((c_option, new_price))
                        # c = [j for j in order if j in c_option]
                        r_order = order - set(c_option)
                        if r_order:
                            new_price += reduce(self.__add,
                                        (rest_menu.get(o) for o in r_order))
                        if not price or new_price < price:
                            price, restaurant = new_price, rest_id

            if len(mul_combos) > 1:
                for k in xrange(len(mul_combos), 1, -1):
                    for comb in itertools.combinations(mul_combos, k):
                        new_price = reduce(self.__add, (c[1] for c in comb))
                        if price > new_price:
                            r_order = order - set(reduce(self.__add,
                                                         (c[0] for c in comb)))
                            if r_order:
                                new_price += reduce(self.__add,
                                            (rest_menu.get(o) for o in r_order))
                            if not price or new_price < price:
                                price, restaurant = new_price, rest_id

        print '%s, %s' % (restaurant, price)

    def resolve_order(self, order):
        """Get Best Value Meal from all menus."""
        # Parse given XML menu and populate menu
        self.populate_menu()

        order = set(order.strip().split(' '))

        # Get Restaurants which can serve order and possible ways of serving
        menus = self.__menu_exists(order)

        if menus[0] or menus[1]:
            self.__print_price(menus, order)
        else:
            print 'Menu does not exist'


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--menu', help="Menu CSV File", action="store")
    parser.add_argument('-o', '--order',
                        help="Place your order",
                        action="store")
    return parser.parse_args()


if __name__ == "__main__":
    __PARAMS = parse_arguments()
    if __PARAMS.menu and __PARAMS.order:
        Restaurant(__PARAMS.menu).resolve_order(__PARAMS.order)
    else:
        print "Please provide Menu CSV and order, use -h for help."
