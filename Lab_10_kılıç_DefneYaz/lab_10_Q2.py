# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:10:36 2021

@author: defne
"""

import numpy as np
import matplotlib.pyplot as plt

student = np.loadtxt('students.txt', skiprows = 1)
full = student[student[:,0]==1] 
half = student[student[:,0]==2] 
non = student[student[:,0]==3]
nums = [len(full) , len(half) , len(non)]
plt.clf()
plt.figure("figure2")
 
#histogram
plt.subplot(2,2,1)
plt.hist(half[:,3],4)
plt.title('Frequency of Writing Gr. of Half Sc. Students')
plt.xticks([50,75])


#plot
plt.subplot(2,2,2)
plt.plot(half[:,1],"m.:")
plt.plot(half[:,2],"cx-")
plt.ylabel('Grades')
plt.title('Math vs Reading  gr. of Full Sc. Students')
plt.legend(['Reading','Math'])

#chart
plt.subplot(2,2,3)
plt.pie(nums,labels=("full","half","non"), explode=(0,0,0.09),autopct='%.1f%%')
plt.title('Scholarship Percentages')

#bar
plt.subplot(2,2,4)
label_bar = 'Half-Sc.','All'
bar_data = [np.mean(half[:,1]),np.mean(student[:,1])]
plt.bar(label_bar[0],bar_data[0])
plt.bar(label_bar[1],bar_data[1])
plt.ylabel('Average of Grades')
plt.title('Comparison of Math Grades: Half Sc. vs All Students')

