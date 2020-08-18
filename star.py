from settings import *
import math, random, pygame


star_max_size = 3
ex = 30 #the bigger the number the less large stars

class Star:
    def __init__(self, x, y, settings):
        self.x = x
        self.y = y
        self.location = (x, y)
        self.size = int(math.floor(random.random() ** ex * star_max_size))
        if self.size == 1:
            self.size = 0
        
        self.color = settings.star_color
        self.amp = random.randint(self.size + 1, star_max_size + 1)/(star_max_size + 1)
        self.color = [self.color[0]*self.amp, self.color[1]*self.amp, self.color[2]*self.amp]

    ### draw the star with the pygame draw method
    def draw(self, main_surface):
        pygame.draw.circle(main_surface, self.color, (self.x, self.y), self.size, 0)