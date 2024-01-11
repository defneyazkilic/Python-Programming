# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:52:03 2021

@author: defne
"""
"""
 that takes a two-dimensional list of words
(inList) and a String (searchChr) as parameters. The function will check all words rowwise in inList and form a sentence from the words that start with the given character by
putting a space between the words. The function should return the sentence formed. 
"""
list_2d = [['This', 'is', 'lab', 'Script'],
           ['We', 'should', 'finish', 'it'],
           ['we', 'solve', 'some', 'questions']]



def formSentence( inList, searchChr ):
    
    '''
    
   ***************************************************************************************
    Takes a 2d List and a charachter as a parameters
    and returns a sentence that contains the the words which starts by the given charachter.
    ***************************************************************************************
    inList: 2D list
    searchChr: string
    
    '''
    
    snt = ''
    for i in range( len( inList)):
        for n in range( len(inList[i])):
           pos = inList[i][n].lower().find(searchChr)
           if pos == 0:
               if snt == '':
                   firstword = inList[i][n].replace(inList[i][n][0], inList[i][n][0].upper())
                   snt = snt + firstword
               else:
                   snt = snt + ' ' + inList[i][n]
    return snt

print( formSentence(list_2d, 's'))
