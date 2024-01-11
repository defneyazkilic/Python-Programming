# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:45:49 2021

@author: defne
"""

class Cab:
    def __init__(self,typeOfCab,kms,year):
        self.__typeOfCab = typeOfCab
        self.__kms = kms
        self.__year = year
    
    def get_typeOfCab(self):
        return self.__typeOfCab
    
    def get_kms(self):
        return int(self.__kms)

    def get_year(self):
        return self.__year
   
    def __gt__(self,other):
        if self.get_typeOfCab()== other.get_typeOfCab():
            return self.get_year() > other.get_year()
    
    def __eq__(self,other):
        if self.get_typeOfCab()== other.get_typeOfCab() and self.get_year() == other.get_year() :
            
            return True
        else:
            return False
    def __repr__(self):
        pass
    
class sedan(Cab):
    
    def __init__(self,typeOfCab,kms,year,price_per_kms = 2.5):
        super().__init__(typeOfCab,kms,year)
        self.__price_per_kms = price_per_kms
        
    def get_price(self):
        return self.__price_per_kms
        
        
    def calculate_fare(self):
        return self.get_kms() * self.get_price()


class hatchback( Cab ):
    
     def __init__(self,typeOfCab,kms,year,price_per_kms = 2.2):
         super().__init__(typeOfCab,kms,year)
         self.__price_per_kms = price_per_kms
     
     def get_price( self ):
        return self.__price_per_km
     
     def calculate_fare( self ):
        return self.get_price() * self.get_kms()

         
    
    
    
        
        
        
    