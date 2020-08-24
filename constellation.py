import pygame
from star import Star

class Constellation():

    def __init__(self, size, center, settings):
        self.size = size #side length of the 5x5 grid
        self.center = center
        self.grid_points = [] #list of list of points on the 5x5 grid
        self.grid_lines = [] #list with each item being a line -- a line is a pair of points
        self.point_spacing = self.size // 4
        self.star_points = []
        self.star_lines = []

    ### This function can draw the constellation using its own data (self)
    def draw(self, main_surface, settings):

        #def 

        ### This function will take the points on the 5x5 grid and make Star objects with proper centers and sizes for the constellation
        def grid_to_star_points():
            for list_of_points in self.grid_points:
                for point in list_of_points:
                    tempx = (point - 1) % 5
                    tempy = (point - tempx - 1) // 5
                    offsetX = (tempx - 2) * self.point_spacing
                    offsetY = (tempy - 2) * self.point_spacing
                    temp_star = Star(int(self.center[0] + offsetX), int(self.center[1] + offsetY), settings)
                    temp_star.size = 3
                    temp_star.color = settings.star_color
                    self.star_points.append(temp_star)

        def grid_to_star_lines():
            for list_of_lines in self.grid_lines:
                for pair in list_of_lines:
                    tempx1 = (pair[0] - 1) % 5
                    tempy1 = (pair[0] - tempx1 - 1) // 5
                    tempx2 = (pair[1] - 1) % 5
                    tempy2 = (pair[1] - tempx2 - 1) // 5
                    offsetX1 = (tempx1 - 2) * self.point_spacing
                    offsetY1 = (tempy1 - 2) * self.point_spacing
                    offsetX2 = (tempx2 - 2) * self.point_spacing
                    offsetY2 = (tempy2 - 2) * self.point_spacing
                    self.star_lines.append(((self.center[0] + offsetX1, self.center[1] + offsetY1), (self.center[0] + offsetX2, self.center[1] + offsetY2)))

        grid_to_star_points()
        grid_to_star_lines()
        for star in self.star_points:
            pygame.draw.circle(main_surface, star.color, (star.x, star.y), star.size, 0)
        for line in self.star_lines:
            pygame.draw.lines(main_surface, (255, 255, 255), False, line, 1)

