#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:08:25 2019

@author: ivanarevalo
"""

import FamilyMember as fm

class Family():
    
    def __init__(self, family_name):
        self.family_name = family_name
        self.members = []

    def addMember(self, newFamilyMember):
        if not isinstance(newFamilyMember, fm.FamilyMember):
            raise TypeError("Parent must be set to a FamilyMember")
        if newFamilyMember in self.members:
            print("new FamilyMember already in the list")
            return
        self.members.append(newFamilyMember)
        
    def addMemberTree(self, newFamilyMember):
        if not isinstance(newFamilyMember, fm.FamilyMember):
            raise TypeError("newFamilyMember must be set to a FamilyMember")
        if newFamilyMember in self.members:
            print("new FamilyMember already in the list")
            return
        self.members.append(newFamilyMember)
        self.members.extend(self.getDescendants(newFamilyMember))
        self.members.extend(self.getAscendants(newFamilyMember))
        for sibling in newFamilyMember.siblings():
                self.members.append(sibling)
                self.members.extend(self.getDescendants(sibling))
        self.members = dict.fromkeys(self.members)
        
            
    def getDescendants(self, oldestMember):
        if not isinstance(oldestMember, fm.FamilyMember):
            raise TypeError("oldestMember must be set to a FamilyMember")
        descendants = []
        for child in oldestMember.children:
            descendants.append(child)
            if len(child.parents)>1:
                for parent in child.parents:
                    if (parent != oldestMember) and (parent not in descendants):
                        descendants.append(parent)
                        descendants.extend(self.getAscendants(parent))
            if child.children:
                descendants.extend(self.getDescendants(child))
        return descendants
    
    def getAscendants(self, youngestMember):
        if not isinstance(youngestMember, fm.FamilyMember):
            raise TypeError("youngestMember must be set to a FamilyMember")
        ascendants = []
        for parent in youngestMember.parents:
            ascendants.append(parent)
            if parent.parents:
                ascendants.extend(self.getAscendants(parent))
            for sibling in parent.siblings():
                ascendants.append(sibling)
                ascendants.extend(self.getDescendants(sibling))
                
                
        return ascendants
        
    
    