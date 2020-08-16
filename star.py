from settings import *
import math, random

star_max_size = 3
ex = 30 #the bigger the number the less large stars

class Star:
    def __init__(self, x, y, settings):
        self.x = x
        self.y = y
        self.location = (x,y)
        self.size = int(math.floor(random.random() ** ex * star_max_size))
        if self.size == 1:
            self.size = 0
        #find better way of getting color data from settings
        
        self.color = settings.star_color
        self.amp = random.randint(self.size+1, star_max_size)/star_max_size
        self.color = [self.color[0]*self.amp, self.color[1]*self.amp, self.color[2]*self.amp]