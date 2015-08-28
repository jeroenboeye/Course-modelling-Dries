# -*- coding: utf-8 -*-
"""
Created on Mon May 05 09:52:09 2014

@author: Jboeye
"""

import random as rnd
import pylab as plt

x=[]
y=[]
z=[]
plt.ion()
maxtime = 20
title  = 'random_output.txt'
output=open(title,'w')
import random
r = lambda: random.randint(0,255)
print()
for t in range(maxtime):
    y_value = rnd.randint(0, 15)
    z_value = rnd.randint(0, 15)
    #output.write(str(t) + '\t' + str(y_value) + '\n')
    x.append(t)
    y.append(y_value)
    z.append(z_value)
    if t%5 == 0:
        plt.clf()
        plt.plot(x,y,'#%02X%02X%02X' % (r(),r(),r()),label='player1')
        plt.plot(x,z,'g',label='player2')
        plt.legend()
        plt.draw()
        plt.pause(1.0001)   

output.close()