# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:04:10 2021

@author: defne
"""





x=int(input("Enter an int: "))
print(f"Factors of {x}: ")
for i in range (1, x+1):
    if x%i == 0:
        print(i, end=",")
