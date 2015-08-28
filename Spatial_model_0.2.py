# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 08:39:37 2014

@author: Jboeye
"""

import random as rnd
import Tkinter as tk
import numpy as np

class Visual:
    '''This class arranges the visual output.'''
    def __init__(self, max_x, max_y):
        '''Initialize the visual class'''
        self.zoom = 15
        self.max_x = max_x
        self.max_y = max_y
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, 
                                width =  self.max_x * self.zoom, 
                                height = self.max_y * self.zoom) #create window
        self.canvas.pack()
        self.canvas.config(background = 'white')
        #self.squares = np.empty((self.max_x, self.max_y),dtype=object)
        #self.initialize_squares()
        
    def create_individual(self,x,y):       
        '''Create circle for individual'''
        radius = 0.1
        return self.canvas.create_oval((x - radius) * self.zoom,
                                       (y - radius) * self.zoom,
                                       (x + radius) * self.zoom,
                                       (y + radius) * self.zoom,
                                       outline='black', 
                                       fill='black')
                                       
    def move_drawing(self,drawing, x, y):
        radius= 0.1
        self.canvas.coords(drawing,(x - radius) * self.zoom,
                                   (y - radius) * self.zoom,
                                   (x + radius) * self.zoom,
                                   (y + radius) * self.zoom)                                       
        
    def color_square(self, resources, x, y):
        '''Changes the color of the square'''        
        color = (resources)/float(100)
        if color < 0:
            color = 0
        elif color > 1:
            color = 1  
        green = int(255 * color)
        red = 255 - green        
        blue = 0
        rgb = red, green, blue     
        hex_code = '#%02x%02x%02x' % rgb        
        self.canvas.itemconfigure(self.squares[x, y],fill=str(hex_code))
        
    def initialize_squares(self):
        '''returns a square (drawing object)'''
        for x in xrange(self.max_x):
            for y in xrange(self.max_y):
                self.squares[x, y] = self.canvas.create_rectangle(self.zoom * x,
                                                     self.zoom * y, 
                                                     self.zoom * x + self.zoom,
                                                     self.zoom * y + self.zoom,
                                                     outline = 'black', 
                                                     fill = 'black')


class Individual:
    '''Class that regulates individuals and their properties'''
    def __init__(self,
                 x,
                 y,
                 resources,
                 drawing):
        '''Initialization'''
        self.x = x
        self.y = y
        self.resources = resources
        self.drawing = drawing        
        self.age = 0
        
    def move(self):
        '''Calculates movement'''
        dx = rnd.uniform(-1,1)
        dy = rnd.uniform(-1,1)      
        self.x = self.x + dx
        self.y = self.y + dy
        
   
class Metapopulation:
    '''Contains the whole population, regulates daily affairs'''
    def __init__(self, 
                 max_x, 
                 max_y):
        '''Initialization'''           
        self.max_x = max_x
        self.max_y = max_y      
        self.visual = Visual(self.max_x, self.max_y)        
        self.population = []
        self.initialize_pop()
        
    def initialize_pop(self):
        '''Initialize individuals'''
        startpop = 1000
        start_resources = 10
        for n in range(startpop):
            x = rnd.uniform(0,self.max_x)
            y = rnd.uniform(0,self.max_y)
            drawing = self.visual.create_individual(x, y)
            self.population.append(Individual(x, y, 
                                              start_resources,
                                              drawing))
                                      
    def a_day_in_the_life(self):
        '''Replenish patches and draw visual'''
        oldpop = self.population[:]
        del self.population[:]
        for indiv in oldpop:
                if indiv.resources >= 0:
                    indiv.move()
                    self.visual.move_drawing(indiv.drawing, 
                         indiv.x, 
                         indiv.y)
                    if rnd.random() < 0.3:                    
                        indiv.resources += 5
                    indiv.age += 1
                    indiv.resources -= 2
                    self.population.append(indiv)  
                else:
                    self.visual.canvas.delete(indiv.drawing)
        print len(self.population)
        self.visual.canvas.update()
        
        
meta = Metapopulation(40,40)
for timer in range(40):
    meta.a_day_in_the_life()
tk.mainloop()
