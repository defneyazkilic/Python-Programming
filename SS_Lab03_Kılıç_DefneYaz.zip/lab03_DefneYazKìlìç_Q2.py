# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:18:33 2021

@author: defne
"""

def uppercase_word_at(x, index):
    """parameters: a string and an integer
       arguments:
           arg(1): while the i(index number) is smaller than the lenght of the string,
           add 1 to i to find the space,
                  arg 1.2= if i is equal to space's string number, break the loop
                  so we find the string number of space which is now equal to our i number.
           arg(2): the letters until our index number will be lowercase,numbers between index and i(which is equal to space) will be uppercase and the rest will be lowercase aswell.
          type: string 
    """
    x = x + " " 
    i= index
    while i < len(x):
        i = i + 1
        if(x[i]== " "):
           space = i
           break
    print(x[0:index] + x[index:space].upper() + x[space:len(x)])
   
uppercase_word_at("there are many trees",3)


  