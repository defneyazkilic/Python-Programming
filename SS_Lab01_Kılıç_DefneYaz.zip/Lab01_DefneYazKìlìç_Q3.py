# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:37:36 2021

@author: defne
"""

"""Write a program, Lab01_yourname_Q3.py,that prompts the user for three names:
displays the longest name (the name that contains the most characters) in the format as
shown in the sample runs below.
"""


n1=input( "Enter your name: ")
n2=input( "Enter your name: ")
n3=input( "Enter your name: ")


if len(n1)>len(n3) and len(n1)>len(n2) :
    print (f" {n1}'s name is the longest")
elif len(n2)>len(n3) and len(n2)>len(n1):
    print (f" {n2}'s name is the longest")
elif len(n3)>len(n2) and len(n3)>len(n1):
    print (f" {n2}'s name is the longest")
elif len(n1)==len(n2) or len(n1)==len(n3):
    print (f" {n1}'s name is the longest but there is a tie!")
elif len(n3)==len(n2) :
    print(f" {n2}'s name is the longest but there is a tie!")