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
        
    def draw_resources(self, resources, x_coord, y_coord):
        '''Draws a local patch with a color depending on the local density'''
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
        self.canvas.create_rectangle(self.zoom * x_coord,
                                     self.zoom * y_coord, 
                                     self.zoom * x_coord + self.zoom, 
                                     self.zoom * y_coord + self.zoom, 
                                     outline = str(hex_code), 
                                     fill = str(hex_code))
                         
    def draw_grid(self):
        '''Draws a grid of black lines around the patches'''
        for x in xrange(self.max_x):
            self.canvas.create_line(x*self.zoom,
                                    0,
                                    x*self.zoom,
                                    self.max_y * self.zoom,
                                    fill=str('black'),width=self.zoom/15.)
        for y in xrange(self.max_y):
            self.canvas.create_line(0,
                                    y * self.zoom,
                                    self.max_x * self.zoom,
                                    y * self.zoom,
                                    fill=str('black'),width=self.zoom/10.)            
      

    def update(self):
        '''Updates the visual'''
        self.draw_grid()
        self.canvas.update()
    
    def reset(self):
        '''Resets the visual'''
        self.canvas.delete(tk.ALL)
         
class Metapopulation:
    '''The metapopulation level, contains the physical environment (climate) 
    and all populations'''
    def __init__(self, 
                 max_x, 
                 max_y):
        self.max_x = max_x
        self.max_y = max_y             
        self.n_patches = self.max_x * self.max_y
        self.visual = Visual(self.max_x, self.max_y)
        initial_resources = 10
        self.environment = np.zeros((self.max_x,self.max_y)) + initial_resources
                                             
    def a_day_in_the_life(self):
        '''Replenish patches and draw visual'''
        self.visual.reset()  
        for x in xrange(self.max_x):
            for y in xrange(self.max_y):
                self.visual.draw_resources(self.environment[x,y], x, y)                
        self.environment+=1
        self.visual.update()
        
        
meta = Metapopulation(10,10)
for timer in xrange(100):
    meta.a_day_in_the_life()