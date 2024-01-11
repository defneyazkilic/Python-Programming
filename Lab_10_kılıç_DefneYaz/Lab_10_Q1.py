# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:40:43 2021

@author: defne
"""

import numpy as np
import matplotlib.pyplot as plt

in_height = np.arange(30,71,5)
b_height = np.array([22,26,29,34,38,40,45,50,52])

plt.clf()
plt.plot(in_height,b_height, "b.")
plt.xlabel("Initial Height")
plt.ylabel("Bounce Height")
plt.title("Initial Height vs. Bounce Height")

fit = np.polyfit(in_height,b_height,1)
best_line= np.polyval(fit,in_height)
plt.plot(in_height, best_line, "r")
