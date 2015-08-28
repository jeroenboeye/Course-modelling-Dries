# -*- coding: utf-8 -*-
"""
Created on Mon May 05 09:52:09 2014

@author: Jboeye
"""

import random as rnd
import pylab as plt

x=[]
y=[]
plt.ion()
maxtime = 2000
title  = 'random_output.txt'
output=open(title,'w')

for t in range(maxtime):
    y_value = rnd.randint(0, 15)
    output.write(str(t) + '\t' + str(y_value) + '\n')
    x.append(t)
    y.append(y_value)
    if t%5 == 0:
        plt.clf()
        graph = plt.plot(x,y,'r')[0]    
        plt.draw()
        plt.pause(0.0001)   
    
output.close()