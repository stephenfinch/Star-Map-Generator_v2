from star import Star
from constellation import Constellation
import random

#create lots of star objects                                ### list_of_stars
#use those star objets to make constellation objects        
#create lots of constellation objects                       ### list_of_constellations

class Map:
    def __init__(self, field_x, field_y):
        self.field_x = field_x
        self.field_y = field_y
        
        self.field_buffer = 50 #gap between display edge and circle
        self.field_inner_buffer = 3 #gap between circle and outer stars
        self.r = self.field_x / 2 - self.field_inner_buffer #raduis
        self.Xcenter = self.Ycenter = self.field_x / 2 + self.field_buffer

## STARS ## makes a list of Star objects and adds them to a list


    def place_stars(self, settings):
        self.number_of_stars = settings.number_of_stars
        self.list_of_stars = []
        stars_added = 0

        def is_in_circle(x, y):
            return (x - self.Xcenter) ** 2 + (y - self.Ycenter) ** 2 <= self.r ** 2

        while stars_added < self.number_of_stars:
            x, y = random.randint(self.field_buffer, self.field_buffer + self.field_x), random.randint(self.field_buffer, self.field_buffer + self.field_y)
            if is_in_circle(x, y):
                self.list_of_stars.append(Star(x, y, settings))
                stars_added += 1


## CONSTELLATIONS ## uses the list of Star objects and connects them into constellations
    def place_constellations(self, size, settings=None):
        if settings:
            for char in settings.text_input.upper():



        self.size = size
        self.list_of_constellations = []
        else:

        pass


LETTERS = {
    'A':[],
    'B':[],
    'C':[],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[],
    'M':[],
    'N':[],
    'O':[],
    'P':[],
    'Q':[],
    'R':[],
    'S':[],
    'T':[],
    'U':[],
    'V':[],
    'W':[],
    'X':[],
    'Y':[],
    'Z':[],
    }


'''
*   *   *

*   *   *

*   *   *

'''

#   F
'''
*---*---*
|
*---*---*
|
*   *   *
'''

#   E
'''
*---*---*
|
*---*---*
|
*---*---*
'''

#   S
'''
*---*---*
|
*---*---*
        |
*---*---*
'''

#   T
'''
*---*---*
    |
*   *   *
    |
*   *   *
'''

#   O
'''
*---*---*
|       |
*   *   *
|       |
*---*---*
'''

#   P
'''
*---*---*
|       |
*---*---*
|
*   *   *
'''

#   L
'''
*   *   *
|
*   *   *
|
*---*---*
'''

#   Q
'''
*---*---*
|       |
*   *   *
|    `-_|
*---*---*
'''