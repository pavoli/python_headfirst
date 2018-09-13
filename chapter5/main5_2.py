# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

from helper import get_coach_data

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

print(james, end='')
print(julie, end='')
print(mikey, end='')
print(sarah, end='')