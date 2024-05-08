# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:33:13 2024

@author: ghosh
Monte Carlo Simulation
"""
import numpy as np
sim=1000000
A=np.random.uniform(1,5,sim)
B=np.random.uniform(2,6,sim)
duration=A+B
import matplotlib.pyplot as plt

plt.hist(duration,density= True)
plt.axvline(9,color='g')
plt.show()
print((duration>9).sum()/sim)
