# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:18:48 2021

@author: defne

"""

from Cab import*
"""

---------------------------------------
read_file
parameters:File
Using data in the file, returns a
list of Cab objects (Sedan or Hatchback). 
----------------------------------------

"""
def read_file( filename ):


    lst = []
    file = open( filename, 'r' )
    for line in file:
        line = line.strip()
        data = line.split( ';' )
        cabtype = data[0]
        km = int(data[1])
        year = int(data[2])
        if cabtype == 'Sedan':
            car = sedan("Sedan",km,year)
            
        elif cabtype == "Hatchback":
            car = hatchback("hatchback", km,year)
        lst.append(car)
    file.close()
    return lst
            
    


"""
---------------------------
parameters: list, object
The function should find and return the number of Cabs in the list with the same type
as cab and whose year is more than the year of the cab
passed as a parameter.
--------------------------- 

"""

def find_greater(lst,cab):


   
    cab_count = 0
    for c in lst:
        if c.get_typeOfCab()==cab.get_typeOfCab() and c > cab:
            cab_count += 1
    return cab_count
           
cabs = read_file("cabs.txt")
num= 1
for i in cabs:
    if i.get_typeOfCab() == "Sedan":
        print("Sedan",num,"will pay", i.calculate_fare())
        

        num+=1


a = find_greater(cabs, sedan("Sedan", 0, 2015))
print("There are", a ,"sedan cars newer than 2015")

"""
----------------------------------------------------------------------------------------------
Uses a loop to find all the kms travelled by the cars in the wanted type in the wanted year.
---------------------------------------------------------------------------------------------- 
"""

total= 0
for i in cabs:
    if i.get_year()== 2020 and i.get_typeOfCab()== "hatchback":
        total += i.get_kms()


print ("All Hatchback cars of year 2020 have travelled",total, "kms")



















