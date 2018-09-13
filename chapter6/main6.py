# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

import helper

sarah = helper.get_coach_data('sarah.txt')
sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Time'] = sarah
print(sarah_data['Name'] + "'s fastest tiems are: " + str(sorted(set([helper.sanitize(t) for t in sarah_data['Time']]))[0:3]))