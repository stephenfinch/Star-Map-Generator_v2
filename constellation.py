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
    def draw(self, main_surface, settings, center, radius, buffer):

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

        def is_in_circle(self, x, y, center, radius):
            return (x - center) ** 2 + (y - center) ** 2 <= radius ** 2

        ### Run all the methods and draw it all
        grid_to_star_points()
        grid_to_star_lines()
        for star in self.star_points:
            if is_in_circle(self, star.x, star.y, center, radius - buffer):
                pygame.draw.circle(main_surface, star.color, (star.x, star.y), star.size, 0)
        for line in self.star_lines:
            p1 = is_in_circle(self, line[0][0], line[0][1], center, radius - buffer)
            p2 = is_in_circle(self, line[1][0], line[1][1], center, radius - buffer)
            if p1 and p2:
                pygame.draw.lines(main_surface, settings.star_color, False, line, 1)
            elif not p1 == p2:
                #following calculations derived from https://stackoverflow.com/a/59582674
                (p1x, p1y), (p2x, p2y), (cx, cy) = line[0], line[1], (center, center)
                (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
                dx, dy = (x2 - x1), (y2 - y1)
                dr = (dx ** 2 + dy ** 2)**.5
                big_d = x1 * y2 - x2 * y1
                discriminant = (radius - 1) ** 2 * dr ** 2 - big_d ** 2
                if discriminant > 0:
                    intersections = [
                        (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**.5) / dr ** 2,
                        cy + (-big_d * dx + sign * abs(dy) * discriminant**.5) / dr ** 2)
                        for sign in ((1, -1) if dy < 0 else (-1, 1))]
                    fraction_along_segment = [(xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in intersections]
                    intersections = [pt for pt, frac in zip(intersections, fraction_along_segment) if 0 <= frac <= 1]
                    if not len(intersections) == 0:
                        intersections = intersections[0]
                        if p1 and not p2:
                            pygame.draw.lines(main_surface, settings.star_color, False, (line[0],(int(intersections[0]),int(intersections[1]))), 1)
                        else:
                            pygame.draw.lines(main_surface, settings.star_color, False, (line[1],(int(intersections[0]),int(intersections[1]))), 1)



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
        

    def draw(self, main_surface, settings, center, radius, buffer):
        if self.is_inverted:
            self.invert()
        if self.orientation != 0:
            self.change_orientation(self.orientation)
        super().draw(main_surface, settings, center, radius, buffer)

