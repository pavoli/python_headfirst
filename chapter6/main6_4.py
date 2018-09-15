# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

import helper

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([helper.sanitize(t) for t in self]))[0:3])

vera = AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', '1-21', '2:22'])
print(vera.top3())