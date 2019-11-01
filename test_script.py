#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:31:31 2019

@author: ivanarevalo
"""

import time
from datetime import date
import FamilyMember as fm
import Family as fam


me = fm.FamilyMember("Ivan" , "MALE")
me.setBirthDate(date(1995,3,16))

dad = fm.FamilyMember("Marco", "MALE")
dad.setBirthDate(date(1957,3,21))

mum = fm.FamilyMember("Miryam", "FEMALE")
mum.setBirthDate(date(1960,4,4))


me.setParent(dad)
me.setParent(mum)

bro = fm.FamilyMember("Juan", "MALE")
bro.setBirthDate(date(1991,12,14))

dad.setChild(bro)
mum.setChild(bro)

abu = fm.FamilyMember("Soledad", "FEMALE")
abu.setBirthDate(date(1930,2,20))

mabu = fm.FamilyMember("MamaSoledad", "FEMALE")
pabu = fm.FamilyMember("PapaSoledad", "MALE")
abu.setParent(mabu)
abu.setParent(pabu)
Broabu = fm.FamilyMember("BroSoledad", "MALE")
Broabu.setParent(mabu)
Broabu.setParent(pabu)

aunt = fm.FamilyMember("Martha", "FEMALE")
aunt.setBirthDate(date(1960,4,4))

abu.setChild(aunt)
mum.setParent(abu)

sis = fm.FamilyMember("Sandra", "FEMALE")
aunt.setBirthDate(date(1980,5,14))

sis.setParent(dad)

p1  = fm.FamilyMember("Oscar", "MALE")
p2  = fm.FamilyMember("Andres", "MALE")
e1  = fm.FamilyMember("Erika", "FEMALE")
e2  = fm.FamilyMember("Jurieth", "FEMALE")
o1  = fm.FamilyMember("Juand", "MALE")
o2  = fm.FamilyMember("sebastian", "MALE")
o3  = fm.FamilyMember("Luci", "FEMALE")
a1  = fm.FamilyMember("Daniel", "MALE")
a2  = fm.FamilyMember("Isabela", "FEMALE")
hum = fm.FamilyMember("Humberto", "MALE")

p1.setParent(aunt)
p2.setParent(aunt)
p1.setParent(hum)
p2.setParent(hum)
o1.setParent(p1)
o1.setParent(e1)
o2.setParent(p1)
o2.setParent(e1)
o3.setParent(p1)
o3.setParent(e1)
a1.setParent(p2)
a1.setParent(e2)
a2.setParent(p2)
a2.setParent(e2)


arevalos = fam.Family("arevalos")
arevalos.addMemberTree(mum)

for members in arevalos.members:
    print(members.name)

