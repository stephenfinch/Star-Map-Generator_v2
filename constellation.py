import pygame
from star import Star

class Constellation():

    def __init__(self, type, size, center, settings):
        self.size = size
        self.center = center
        self.points = [] #list of Star objects
        self.lines = [] #list with each item being a line -- a line is a pair of points
    
    ### This function can draw the constellation using its own data (self)
    def draw(self, main_surface, settings):
        for line in self.lines:
            pygame.draw.aalines(main_surface, settings.star_color, False, line)
        for point in self.points:
            temp_star = Star(point[0], point[1], settings)
            temp_star.size = 3
            temp_star.color = settings.star_color
            pygame.draw.circle(main_surface, temp_star.color, (temp_star.x, temp_star.y), temp_star.size, 0)



        #find way to draw lines smarter -- different shapes? no crossing lines, no lines that are too short/long
        #its not just about the distance a star is away from another star