import matplotlib.pyplot as plt
'''
The color class creates a color from 3 values, r, g, and b (red, green, and blue).

attributes:
    r - a value between 0-255 for red
    g - a value between 0-255 for green
    b - a value between 0-255 for blue
'''
    
class Color(object):
    
    # __init__ is called when a color is constructed using color.Color(_, _, _)
    def __init__(self, r, g, b):
        # Setting the r value
        self.r = r
        self.g = g
        self.b = b

    # __repr__ is called when a color is printed using print(some_color)
    # It must return a string
    def __repr__(self):
        '''Display a color swatch and then return a text description of r,g,b values.'''
        
        plt.imshow([[(self.r/255, self.g/255, self.b/255)]])
        
        ## Write a string representation for the color
        ## ex. "rgb = [self.r, self.g, self.b]"
        ## Right now this returns an empty string
        string = f'RGB = [r = {self.r}, g = {self.g}, b = {self.b}]'
        
        return string
    
    # __add__ is called when we add two or more colord color1 + color2
    # It must return a color
    def __add__(self, other):
        '''Add two color Class objects.'''
        new_r = (self.r + other.r) / 2
        new_g = (self.g + other.g) / 2
        new_b = (self.b + other.b) / 2

        return Color(new_r, new_g, new_b)
    