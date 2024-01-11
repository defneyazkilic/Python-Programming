# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:22:58 2021

@author: defne
"""

class Instructor():
    def __init__(self, id, name, status, hours):
        self.__id = id
        self.__name = name
        self.__status = status
        self.__hours = hours
        
    def get_id(self):
        return self.__id
#method for returning id number
    
    def get_name(self):
        return self.__name
#method to get the name attitude 
    def get_status(self):
        return self.__status
#method to get status
    
    def get_hours(self):
        return self.__hours
#method to get hours
    
    def calculate_salary(self):
        if self.get_status() == 'F':
            salary = float(5000 + (self.get_hours() * 500))
        if self.get_status() == 'P':
            salary = float(self.get_hours() * 400)
        return salary
    #method to calculte salary by status
    def __str__(self):
        return f'Name: {self.get_name()}\nStatus: {self.get_status()}\nSalary: {self.calculate_salary()} TL\n'
    def __repr__(self):
        return f'Id: {self.get_id()} Name: {self.get_name()} Salary: {self.calculate_salary()} TL'
