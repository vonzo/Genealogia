#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:24:42 2019

@author: ivanarevalo
"""

from datetime import date

class FamilyMember():
    
    def __init__(self, name, gender = None):
        self.name = name
        self.member_id = ""
        self.children = []
        self.parents = []
        if((gender!= None) and (gender!= "MALE") and (gender!= "FEMALE")):
            raise TypeError("gender must be set to a MALE or FEMALE")
        self.gender = gender

    def setBirthDate(self, birthDate):
        if not isinstance(birthDate, date):
            raise TypeError("birthDate must be set to a date")
        self.birthDate = birthDate
        
    def setParent(self, parent):
        if not isinstance(parent, FamilyMember):
            raise TypeError("Parent must be set to a FamilyMember")
        if parent in self.parents:
            print("parent already in the list")
            return
        parent.setChild(self)
        
        
    def setChild(self, child):
        if not isinstance(child, FamilyMember):
            raise TypeError("child must be set to a FamilyMember")
        if child in self.children:
            print("child already in the list")
            return
        self.children.append(child) 
        child.parents.append(self)
        
        
    def age(self):
        ageInDays = (date.today() - self.birthDate)
        print(self.name + " has lived " + str(ageInDays.days) + " days")
        return ageInDays.days
    
    def siblings(self):
        siblings = []
        for parent in self.parents:
            for child in parent.children:
                if ((child != self) and not(child in siblings)):
                    siblings.append(child)
        return siblings
            
        
    
    
