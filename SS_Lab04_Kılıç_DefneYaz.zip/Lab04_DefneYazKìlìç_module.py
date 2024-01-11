# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:50:53 2021

@author: defne
"""

cityName = str(input('Enter city to search (“quit” to exit): '))
Name_file= open("city_districts.txt",'r')
Data_file= open("city_values.txt",'r')
outfile= open(cityName +'density.txt','w')


   
for name in Name_file:
    search1 = name.find(cityName)
    if search1 == 0:
       search1 = name.find('')+7
       outfile.write(name[search1:len(name)])
       
       
     
       










Name_file.close()
Data_file.close()
outfile.close()
           
    
   
#density:population/area

    
    
   
    
  