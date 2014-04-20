#!/usr/bin/python

import argparse
import csv
import itertools

__author__ = 'Sharath Kumar Suroju'
__email__ = 'i2sheri@gmail.com'
__date__ = '2014-04-18'


class Restaurant:

    menu_file = None
    menu = {}

    def __init__(self, menu_file):
        self.menu_file = menu_file

    def populate_menu(self):
        """Parse CSV file and populate City Menu."""

        try:
            with open(self.menu_file, 'rb') as m:
                reader = csv.reader(m)
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
        except:
            print "Error"

    def __get_item(self, row):
        if len(row) == 3:
            return row[2], False
        else:
            return tuple(row[2:]), True

    __add = lambda self, op1, op2: op1 + op2

    def __menu_exists(self, order):
        """Return restaurants which can serve the order.
           Include value meals if any restaurant serves."""

        m = []
        combos = {}
        for rest in iter(self.menu):
            rest_menu = self.menu.get(rest)
            items = set(rest_menu)
            combo_items = ()
            if rest_menu.get('combo'):
                combo_list = []
                combo_items = reduce(self.__add, rest_menu.get('combo'))
                for c in rest_menu.get('combo'):
                    if any(o in c for o in order) and order <= items | set(c):
                        combo_list.append(c)
                if combo_list:
                    combos[rest] = combo_list
                else:
                    if (any(o in combo_items for o in order) and
                        order <= items | set(combo_items)):
                        combos[rest] = ['ALL']
            if order <= items:
                m.append(rest)
        return (m, combos)

    def __print_price(self, menus, order):
        """Print most economic price and restaurant of the order."""

        price = None
        restaurant = None
        for m in menus[0]:
            p = reduce(self.__add, (self.menu.get(m).get(o) for o in order))
            if not price:
                price = p
                restaurant = m
            if p < price:
                price = p
                restaurant = m

        for m in menus[1]:
            mul_combos = []
            rest_menu = self.menu.get(m)
            for v in menus[1].get(m):
                if v == 'ALL':
                    iterable = rest_menu.get('combo')
                    for s in xrange(len(iterable), 1, -1):
                        for comb in itertools.combinations(iterable, s):
                            if (order <= set(reduce(self.__add, comb)) |
                                set(rest_menu)):
                                p = reduce(self.__add,
                                           (iterable.get(c) for c in comb))
                                if not price:
                                    price = p
                                    restaurant = m
                                if p < price:
                                    price = p
                                    restaurant = m
                else:
                    p = rest_menu.get('combo').get(v)
                    if price and p > price:
                        continue
                    else:
                        mul_combos.append((v, p))
                        c = [o for o in order if o in v]
                        r_order = order - set(c)
                        if r_order:
                            p += reduce(self.__add,
                                        (rest_menu.get(o) for o in r_order))
                        if not price:
                            price = p
                            restaurant = m
                        if p < price:
                            price = p
                            restaurant = m
            if len(mul_combos) > 1:
                iterable = mul_combos
                for s in xrange(len(iterable), 1, -1):
                    for comb in itertools.combinations(iterable, s):
                        p = reduce(self.__add, (c[1] for c in comb))
                        if price > p:
                            r_order = order - set(reduce(self.__add,
                                                         (c[0] for c in comb)))
                            if r_order:
                                p += reduce(self.__add,
                                            (rest_menu.get(o) for o in r_order))
                            if not price:
                                price = p
                                restaurant = m
                            if p < price:
                                price = p
                                restaurant = m
        print '%s, %s' % (restaurant, price)

    def resolve_order(self, order):
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
    params = parse_arguments()
    if params.menu and params.order:
        Restaurant(params.menu).resolve_order(params.order)
    else:
        print "Please provide Menu CSV and order, use -h for help."
        
