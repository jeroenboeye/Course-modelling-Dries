import math as math
import Tkinter as tk
import random as rnd
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
        self.canvas.config(background = 'black')
        self.squares = np.empty((self.max_x, self.max_y),dtype=object)
        self.initialize_squares()
        
    def create_individual(self,x,y):       
        '''Create circle for individual'''
        radius = 0.25
        return self.canvas.create_oval((x - radius) * self.zoom,
                                       (y - radius) * self.zoom,
                                       (x + radius) * self.zoom,
                                       (y + radius) * self.zoom,
                                       outline='black', 
                                       fill='black')
                                       
    def move_drawing(self,drawing, x, y):
        radius= 0.25
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
        self.angle = rnd.uniform(0, 2 * math.pi)
        self.resources = resources
        self.drawing = drawing
        self.age = 0
        self.reproductive_age = rnd.randint(10, 20)
        
    def move(self, max_x, max_y):
        '''Calculates movement'''
        diversion = math.pi / 3.0
        self.angle += rnd.uniform(-diversion,diversion)
        speed = 0.2
        dx = speed * math.cos(self.angle)
        dy = speed * math.sin(self.angle)        
        self.x = (self.x + dx) % max_x
        self.y = (self.y + dy) % max_y
        
   
class Metapopulation:
    '''Contains the local environment and the whole population, regulates
    daily affairs'''
    def __init__(self, 
                 max_x, 
                 max_y):
        '''Initialization'''
        self.max_x = max_x
        self.max_y = max_y             
        self.n_patches = self.max_x * self.max_y
        self.visual = Visual(self.max_x, self.max_y)
        initial_resources = 70
        self.environment = np.zeros((self.max_x,self.max_y)) + initial_resources
        self.population = []
        self.initialize_pop()
        
    def initialize_pop(self):
        '''Initialize individuals'''
        startpop = 10
        start_resources = 10
        for n in xrange(startpop):
            x = rnd.uniform(0,self.max_x)
            y = rnd.uniform(0,self.max_y)
            drawing = self.visual.create_individual(x, y)
            self.population.append(Individual(x, y, start_resources, drawing))
                                      
    def a_day_in_the_life(self):
        '''Replenish patches and draw visual'''
        print len(self.population)
        #rnd.shuffle(self.population) 
        cost_of_offspring = 20
        start_resources = 10
        #shuffle population so that individuals in the beginning of the list
        #don't get an advantage
        oldpop = self.population[:]
        del self.population[:]
        for indiv in oldpop:
            indiv.resources -= indiv.speed * 10 
            #individuals lose energy, this is linked to movement distance
            if indiv.age>=indiv.reproductive_age:
                n_offspring = int(indiv.resources) // cost_of_offspring
                for n in xrange(n_offspring):
                    drawing = self.visual.create_individual(indiv.x, indiv.y)
                    self.population.append(Individual(indiv.x,
                                                      indiv.y,
                                                      start_resources,
                                                      drawing))
                self.visual.canvas.delete(indiv.drawing)
            else:
                if indiv.resources >= 0:
                    indiv.move(self.max_x, self.max_y)
                    self.visual.move_drawing(indiv.drawing, 
                                             indiv.x, 
                                             indiv.y)
                    if self.environment[indiv.x, indiv.y]>0:
                        if self.environment[indiv.x, indiv.y] > 10:
                            self.environment[indiv.x, indiv.y] -= 10
                            indiv.resources += 10
                        else:
                            indiv.resources += self.environment[indiv.x, indiv.y]
                            self.environment[indiv.x, indiv.y] = 0
                    indiv.age += 1
                    self.population.append(indiv)
                else:
                    self.visual.canvas.delete(indiv.drawing)
            
        for x in xrange(self.max_x):
            for y in xrange(self.max_y):
                self.visual.color_square(self.environment[x,y], x, y)              
        self.environment += .35 #replenish resources in patches
        np.clip(self.environment, 0, 100, out = self.environment)
        self.visual.canvas.update()
        
        
meta = Metapopulation(30,30)
for timer in xrange(10000):
    meta.a_day_in_the_life()