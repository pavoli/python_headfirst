# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name

johny = NamedList('John Paul Jones')
johny.append('Dass player')
johny.extend(['Composer', 'Arrabger', 'Musician'])

print(johny)
print(johny.name)

for attr in johny:
    print(johny.name + " is a " + attr + '.')