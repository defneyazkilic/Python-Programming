# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:49:46 2021

@author: defne
"""




x= "aa:"
while x != '':
    x= str(input("Enter a string : "))
    for i in range(0,len(x),2):
        print(x[i],end="")
    
    for i in range (1,len(x),2):
        print(x[i],end="")
        
if x == '':
    print("done!")
