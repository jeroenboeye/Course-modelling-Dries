# -*- coding: utf-8 -*-
"""
Created on Mon May 05 09:52:09 2014

@author: Jboeye
"""

import random as rnd

maxtime = 100
title  = 'random_output.txt'
output=open(title,'w')

for t in range(maxtime):
    output.write(str(t) + '\t' + str(rnd.randint(0, 15)) + '\n')
    
output.close()
        
        