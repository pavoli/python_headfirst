# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

import sys

def print_lol(the_list, indent=False, level=0, fn = sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='', file=fn)
                print(each_item, file=fn)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)