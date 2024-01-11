# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:46:15 2021

@author: defne
"""
 

def is_neat_reversible(s):
    """ """
    if s == " ":
        return False
    elif s[1:len(s)] == s[-1:-(len(s)):-1]:
       return True
    else:
       return False
s=input("Write a string:")   
   
print(is_neat_reversible(s))
  


              

    
    
    
    
    
    
 
        
        
        
    
    