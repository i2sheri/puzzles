#!/usr/bin/python

"""
    Find missing term in Arithematic Progression.
    nth term in AP = a+(n-1)d
    WHERE
        a = initial term
        d = common difference
"""

class MissingTerm(object):
    """Find missing term in AP."""

    __terms = None

    def __init__(self, n):
        self.__terms = n

    def find(self, input_series):
        """Find the term."""
        #ap_series = map(int, input_series)
        ap_series = [int(i) for i in input_series]
        diff = []
        for i in xrange(0, self.__terms-1):
            diff.append(ap_series[i+1]-ap_series[i])
        index = 0
        common_difference = 0
        for i in xrange(0, self.__terms-2):
            if diff[i] == diff[i+1]:
                common_difference = diff[i]
            else:
                index = i+2
        return ap_series[0] + (index-1)*common_difference


if __name__ == '__main__':
    print MissingTerm(int(raw_input())).find(raw_input().split())
