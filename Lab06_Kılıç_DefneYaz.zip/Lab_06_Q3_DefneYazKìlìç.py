# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:40:18 2021

@author: defne
"""

from Instructor import*

def read_file(filename):
    """
    Uses file as parameter
    creates an empty dict. 
    converts file datas into a list using for loop
    classifies the datas 
    filles the empty dict.sing the key[id] and stored objects of instructor class.
    Returns dict.
    """
    file = open(filename, 'r')
    dct = {}
    for line in file:
        data = line.split(';')
        id = int(data[0])
        instructor = data[1]
        status = data[2]
        hours = int(data[3].strip('\n'))
        t = Instructor(id, instructor, status, hours)
        dct[id] = t
    return dct



i = int(input('Enter instructor id: '))
print(read_file('instructor.txt')[i])
s = str(input('Enter status (F - Full-time / P - Part-time): '))
if s == 'P':
    print(f'Part-time Instructors:')
if s == 'F':
    print(f'Full-time Instructors:')

lst = []
for k in read_file('Instructor.txt'):
    if read_file('Instructor.txt')[k].get_status() == s:
        lst.append(read_file('Instructor.txt')[k])

print(lst)
