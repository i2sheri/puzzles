#!/usr/bin/python

"""Generate a list of menus in random."""

from random import randrange, shuffle


class MenuGenerator(object):
    """Generate a Random Menu CSV file."""

    __MAX_RESTAURANTS = 1000 #Min value 1
    __MAX_ITEMS = 100 #Min value 1, MaX Value 26 + 26 + 10 + 55
    __MAX_PRICE = 10 #Min 1
    __CSV_NAME = 'random_menu.csv'
    __CITY_MENU = {}
    #Using ASCII codes to create menu labels: [A-z] + [0-9] + special chars.
    __POSSIBLE_MENU_ITEMS = ([chr(x) for x in xrange(65, 91)] +
                          [chr(x) for x in xrange(97, 123)] +
                          [chr(x) for x in xrange(48, 58)] +
                          [chr(x) for x in xrange(200, 255)])
    __GET_RANDINT = lambda self, x, y: randrange(x, y+1)

    def __init__(self):
        pass

    def get_combo(self):
        """Return a random value meal."""
        shuffle(self.__POSSIBLE_MENU_ITEMS)
        return tuple(self.__POSSIBLE_MENU_ITEMS[:self.__GET_RANDINT(2, 5)])

    def generate(self):
        """Generate Random Menus for all restaurants."""
        for rest_id in xrange(1, self.__MAX_RESTAURANTS):
            # print rest_id
            rest_menu = {}
            menu_size = self.__GET_RANDINT(2, self.__MAX_ITEMS)
            shuffle(self.__POSSIBLE_MENU_ITEMS)
            for item in self.__POSSIBLE_MENU_ITEMS[:menu_size]:
                rest_menu[item] = self.__GET_RANDINT(2, self.__MAX_PRICE)
            combo_menu = {}
            combos = int(menu_size/10.0*1.5) if menu_size > 10 else 0
            if combos > 2:
                for combo in xrange(1, self.__GET_RANDINT(2, combos)):
                    combo_menu[self.get_combo()] = self.__GET_RANDINT(2, 10)

                rest_menu['combo'] = combo_menu
            self.__CITY_MENU[rest_id] = rest_menu

        with open(self.__CSV_NAME, 'wb') as csv:
            for rest_id in self.__CITY_MENU:
                for item in self.__CITY_MENU.get(rest_id):
                    if item == 'combo':
                        cmenu = self.__CITY_MENU.get(rest_id).get('combo')
                        for citem in cmenu:
                            csv.write("%s,%s,%s\n" %(rest_id, cmenu.get(citem),
                                                     ",".join(citem)))
                    else:
                        csv.write("%s,%s,%s\n"
                                  %(rest_id,
                                    self.__CITY_MENU.get(rest_id).get(item),
                                    item))

if __name__ == "__main__":
    MenuGenerator().generate()
