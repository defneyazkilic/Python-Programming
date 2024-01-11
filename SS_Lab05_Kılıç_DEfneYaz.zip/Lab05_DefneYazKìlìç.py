# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 14:14:16 2021

@author: defne
"""






def load_movies(file):
    l=[]
    d={}
    
    for i in file: 
        blank = i.find(',')
        year = i[:blank]
        movieName = i[blank + 1:len(i)-1]
        data = (year,movieName)
        if year in d:
            d[year].append(data)
        else:
            l.append(data)
            d[year]= l
            l= []
        
        return d
    
def get_movies_by_year(d,year):
    l=[]
    for y in d:
        for a in d[y]:
            if a[0] == year:
                l.append(a[1])
    return l


def get_movies_by_keyword(d,keyWord):
    l = []
    for b in d:
        for c in d[b]:
            p = c[1].find(keyWord)
            if p != -1 :
               info = (c[0],c[1]) 
               l.append(info)
    return l          
    
    
def print_list(l):
    for x in l:
        print(x)
        
        
        
file = open('/Users/defne/.ipython/extensions/movie_data.csv', 'r')
diction= load_movies(file) 
year= int(input("enter a year to search:  "))      
if get_movies_by_year(diction,year) != []:
    print ("MOvies made in", year, ":")
    print_list(get_movies_by_year(diction,year))
else:
    print('no movies from the year','"'+str(year)+'" found')
          
keyword = input('Enter a keyword to search:')
if get_movies_by_keyword(diction,keyword) != [] :
    print_list(get_movies_by_keyword(diction,keyword))
else:
    print("no movies with keyword", '"'+keyword+'" found')
    



file.close()
        
        

    
    