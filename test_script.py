#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:31:31 2019

@author: ivanarevalo
"""

import time
from datetime import date
import FamilyMember as fm


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

aunt = fm.FamilyMember("Martha", "FEMALE")
aunt.setBirthDate(date(1960,4,4))

abu.setChild(aunt)
mum.setParent(abu)

sis = fm.FamilyMember("Sandra", "FEMALE")
aunt.setBirthDate(date(1980,5,14))

sis.setParent(dad)