# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:11:27 2021

@author: defne
"""

x= float(input("enter a float number x:"))
y= float(input("enter a float number y:"))
z= float(input("enter a float number z:"))

f= ((x+y*z)*(x*y+z))/(x*y*z)
print(f"f({x},{y},{z})={f:.2f}")