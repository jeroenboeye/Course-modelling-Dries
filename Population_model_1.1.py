import Tkinter as tk
import numpy as np

class Visual:
    '''This class arranges the visual output.'''
    def __init__(self, max_x, max_y):
        '''Initialize the visual class'''
        self.zoom = 20
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
         
class Metapopulation:
    '''Contains the local environment'''
    def __init__(self, 
                 max_x, 
                 max_y):
        '''Initialization'''                     
        self.max_x = max_x
        self.max_y = max_y             
        self.n_patches = self.max_x * self.max_y
        self.visual = Visual(self.max_x, self.max_y)
        initial_resources = 10
        self.environment = np.zeros((self.max_x,self.max_y)) + initial_resources
                                             
    def a_day_in_the_life(self):
        '''Replenish patches and draw visual'''
        for x in xrange(self.max_x):
            for y in xrange(self.max_y):
                self.visual.color_square(self.environment[x,y], x, y)                
        self.environment += 1
        self.visual.canvas.update()
        
        
meta = Metapopulation(30,30)
for timer in xrange(100):
    meta.a_day_in_the_life()
    
    