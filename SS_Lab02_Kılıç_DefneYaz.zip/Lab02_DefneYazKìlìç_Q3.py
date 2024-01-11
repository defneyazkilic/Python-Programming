# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:38:19 2021

@author: defne
"""

import random

random_num=1
dice1 = 0
dice2 = 0 
A = 1 

while random_num != 0 :
    random_num = int(input("Desired dice sum: "))
    if random_num == 0:
        print("bye")
        break
    if random_num < 2 or random_num > 12:
        print("Invalid Dice Sum, please try again")
        continue 
    while dice1 + dice2 != random_num:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        A += 1
        
    
    print(f"{A} rolls")
    A=0
    dice1= 0
    dice2= 0