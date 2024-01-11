# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:53:43 2021

@author: defne
"""

"""Write a program, Lab01_yourname_Q2.py, that inputs three integers from the user
and reports the largest even input and the sum of even inputs"""

num1= int(input(" write an integer number: "))
num2=int(input(" write another integer number: "))
num3=int(input(" write another integer number: "))
total=0
minvalue= -900000*10000
if num1 % 2 == 0:
     total+= num1
     minvalue= num1
if num2 %  2 == 0:
    total+= num2
    if num2 > minvalue:
        minvalue = num2
if num3 % 2 == 0 :
    total += num3
    if num3 > minvalue:
        minvalue=num3
        
if num1 != 0 and num2 != 0 and num3 != 0:
    print("No even integer is entered")
else:
    print( "sum of even is " + str(total))
    print("even max is "+ str(minvalue))