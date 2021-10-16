# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 01:00:41 2021

@author: gunen
"""

def author(string):
    def new_func(func):
        func._author = string
        return func
    return new_func
@author("Yana")
def add2(num: int) -> int:
    return num + 2
print(add2._author)
        