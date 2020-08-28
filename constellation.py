import pygame
import random
from star import Star

class Constellation():

    def __init__(self, size, center, settings):
        self.size = size #side length of the 5x5 grid
        self.center = center #x,y pos of the center of the grid
        self.grid_points = [] #list of list of points on the 5x5 grid
        self.grid_lines = [] #list with each item being a pair of points on the 5x5 grid
        self.point_spacing = self.size // 4
        self.star_points = [] #list of star objects that are placed at the right points
        self.star_lines = [] #list of pairs of points ready to be drawn into star objects and lines using the pygame draw.lines function
        self.point_dict = {}

    ### This function can draw the constellation using its own data (self)
    def draw(self, main_surface, settings):

        ### This function will add some noise to the location of the stars in each constellation
        def shift_points(input):
            scale = 3 # the bigger the number the more ridged the letter constellations look
            return input + random.randint(-self.point_spacing//scale, self.point_spacing//scale)

        ### This function will take the points on the 5x5 grid and make Star objects with proper centers and sizes for the constellation
        def grid_to_star_points():
            for list_of_points in self.grid_points:
                for point in list_of_points:
                    tempx = (point - 1) % 5
                    tempy = (point - tempx - 1) // 5
                    offsetX = shift_points((tempx - 2) * self.point_spacing)
                    offsetY = shift_points((tempy - 2) * self.point_spacing)
                    temp_star = Star(int(self.center[0] + offsetX), int(self.center[1] + offsetY), settings)
                    temp_star.size = 2
                    temp_star.color = settings.star_color
                    self.star_points.append(temp_star)
                    self.point_dict.update({point:(offsetX, offsetY)})

        ### rework this later!
        def grid_to_star_lines():
            for list_of_lines in self.grid_lines:
                for pair in list_of_lines:
                    '''
                    tempx1 = (pair[0] - 1) % 5
                    tempy1 = (pair[0] - tempx1 - 1) // 5
                    tempx2 = (pair[1] - 1) % 5
                    tempy2 = (pair[1] - tempx2 - 1) // 5
                    '''
                    offsetX1 = self.point_dict[pair[0]][0]
                    offsetY1 = self.point_dict[pair[0]][1]
                    offsetX2 = self.point_dict[pair[1]][0]
                    offsetY2 = self.point_dict[pair[1]][1]
                    self.star_lines.append(((self.center[0] + offsetX1, self.center[1] + offsetY1), (self.center[0] + offsetX2, self.center[1] + offsetY2)))

        ### Run all the methods and draw it all
        grid_to_star_points()
        grid_to_star_lines()
        for star in self.star_points:
            pygame.draw.circle(main_surface, star.color, (star.x, star.y), star.size, 0)
        for line in self.star_lines:
            pygame.draw.lines(main_surface, settings.star_color, False, line, 1)



class Random_Constellation(Constellation):

    def __init__(self, size, center, settings, orientation=0, is_inverted=False):
        self.orientation = orientation
        self.is_inverted = is_inverted
        super().__init__(size, center, settings)

    def change_orientation(self, shift): # num can be [0,3] and will indicate the orientation -- 0 is default and it rotates clockwise as num increases
        def translate(num, shift):
            oldX = (num - 1) % 5 + 1
            oldY = (num - 1) // 5 + 1
            if shift == 1:
                newX = oldY
                newY = 5 - ((oldX - 1) % 5)
            elif shift == 2:
                newX = 5 - ((oldX - 1) % 5)
                newY = 5 - ((oldY - 1) % 5)
            elif shift == 3:
                newX = 5 - ((oldY - 1) % 5)
                newY = oldX
            return (newY - 1) * 5 + newX

        new_grid_points = []
        for group in self.grid_points:
            temp_group = []
            for num in group:
                temp_group.append(translate(num, shift))
            new_grid_points.append(temp_group)
        self.grid_points = new_grid_points        
        new_grid_lines = []
        for group in self.grid_lines:
            temp_group = []
            for num in group:
                temp_group.append((translate(num[0], shift), translate(num[1], shift)))
            new_grid_lines.append(temp_group)
        self.grid_lines = new_grid_lines

    def invert(self):
        new_grid_points = []
        for group in self.grid_points:
            temp_group = []
            for num in group:
                temp_group.append(((num - 1) // 5) * 5 + (5 - ((num - 1) % 5)))
            new_grid_points.append(temp_group)
        self.grid_points = new_grid_points        
        new_grid_lines = []
        for group in self.grid_lines:
            temp_group = []
            for num in group:
                temp_group.append((((num[0] - 1) // 5) * 5 + (5 - ((num[0] - 1) % 5)), ((num[1] - 1) // 5) * 5 + (5 - ((num[1] - 1) % 5))))
            new_grid_lines.append(temp_group)
        self.grid_lines = new_grid_lines
        

    def draw(self, main_surface, settings):
        if self.is_inverted:
            self.invert()
        if self.orientation != 0:
            self.change_orientation(self.orientation)
        super().draw(main_surface, settings)

