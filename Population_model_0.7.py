# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 08:39:37 2014

@author: Jboeye
"""

import random as rnd

class Individual:
    '''Class that regulates individuals and their properties'''
    def __init__(self,
                 x,
                 y,
                 resources):
        '''Initialization'''
        self.x = x
        self.y = y
        self.resources = resources
        self.age = 0
        
    def move(self):
        '''Calculates movement'''
        dx = rnd.random()
        dy = rnd.random()       
        self.x = self.x + dx
        self.y = self.y + dy
        
   
class Metapopulation:
    '''Contains the whole population, regulates daily affairs'''
    def __init__(self):
        '''Initialization'''           
        self.population = []
        self.initialize_pop()
        
    def initialize_pop(self):
        '''Initialize individuals'''
        startpop = 10
        start_resources = 10
        for n in xrange(startpop):
            x = rnd.uniform(0,10)
            y = rnd.uniform(0,10)
            self.population.append(Individual(x, y, 
                                              start_resources))
                                      
    def a_day_in_the_life(self):
        '''Replenish patches and draw visual'''
        oldpop = self.population[:]
        del self.population[:]
        for indiv in oldpop:
                if indiv.resources >= 0:
                    indiv.move()
                    if rnd.random() < 0.3:                    
                        indiv.resources += 5
                    indiv.age += 1
                    indiv.resources -= 2
                    print indiv.x, indiv.y
                    self.population.append(indiv)                    
        print len(self.population)
        
        
meta = Metapopulation()
for timer in xrange(40):
    meta.a_day_in_the_life()