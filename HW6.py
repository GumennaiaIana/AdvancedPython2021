# -*- coding: utf-8 -*-

import math

class Point:
    def __init__(self, r, phi):
        self.r = r
        self.phi = phi
        
    def __add__(self, other):
        r_res = round((self.r**2 + other.r**2 + 2*self.r*other.r*math.cos(math.pi/180*(self.phi-other.phi)))**(1/2), 2)
        phi_res = round(180/math.pi*math.atan2(self.r*math.sin(math.pi/180*self.phi) + other.r*math.sin(math.pi/180*other.phi), self.r*math.cos(math.pi/180*self.phi) + other.r*math.cos(math.pi/180*other.phi)), 2)
        if phi_res < 0:
            return Point(r_res, 360 + phi_res)
        else:
            return Point(r_res, phi_res)
       
    def from_cartesian(x, y):
        r_res_cart = (x**2 + y**2)**(1/2)
        phi_res_cart = 180/math.pi*math.atan2(y, x)
        if phi_res_cart < 0:
            return Point(r_res_cart, 360 + phi_res_cart)
        else:
            return Point(r_res_cart, phi_res_cart)
    
    def __eq__(self, other):
        return (self.r == other.r) and (self.phi % 360 == other.phi % 360)
    
    def __str__(self):
        return f"r={self.r}, phi={self.phi}"
    
    def __repr__(self):
        return f"Point({self.r}, {self.phi})"


p1 = Point(r=1, phi=0)
p2 = Point(r=1, phi=90)
p3 = p1 + p2
print (p3)
print(repr(p3))
print(p1 == p2)
p4 = Point.from_cartesian(x=1, y=0)
print (p4)