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
        self.field_inner_buffer = 5 #gap between circle and outer stars, bigger number --> bigger gap
        self.r = self.field_x / 2 - self.field_inner_buffer #raduis
        self.Xcenter = self.Ycenter = self.field_x / 2 + self.field_buffer

## STARS ## makes a list of Star objects and adds them to a list
    def place_stars(self, settings):
        self.number_of_stars = settings.number_of_stars
        self.list_of_stars = []
        stars_added = 0

        ### given an (x,y) pair it will return True/False if the pair is in the circle drawn
        def is_in_circle(x, y):
            return (x - self.Xcenter) ** 2 + (y - self.Ycenter) ** 2 <= self.r ** 2

        while stars_added < self.number_of_stars:
            x, y = random.randint(self.field_buffer, self.field_buffer + self.field_x), random.randint(self.field_buffer, self.field_buffer + self.field_y)
            if is_in_circle(x, y):
                self.list_of_stars.append(Star(x, y, settings))
                stars_added += 1


## CONSTELLATIONS ## makes constellation objects and edits their center/size to fit them where they need to go
    def place_constellations(self, constellation_size, settings):
        self.constellation_size = constellation_size #side length of the 5x5 grid
        self.list_of_constellations = []
        if settings.text_input:
            
            ### adds the point/line data for that letter to the list of constellations
            string_length = len(settings.text_input.upper())
            string_index = 0
            self.letter_spacing = 4
            for char in settings.text_input.upper():
                temp_letter_constellation = Constellation(self.constellation_size, (200,200), settings)
                temp_letter_constellation.grid_points.append(LETTER_CONSTELLATIONS.get(char)[0])
                temp_letter_constellation.grid_lines.append(LETTER_CONSTELLATIONS.get(char)[1])
                centerX = (string_length - 1) * (self.constellation_size + self.letter_spacing) * (string_index - 1) + self.Xcenter
                centerY = 220 - settings.text_height_offset
                temp_letter_constellation.center = (centerX, centerY)
                string_index += 1
                self.list_of_constellations.append(temp_letter_constellation)
        else:
            
            # do something else for this part
            for i in range(settings.number_of_constellations):
                constellation_pick = random.randint(5,9)
                temp_other_constellation = Constellation(self.constellation_size, (i*40 + self.Xcenter,i*40 + self.Ycenter), settings)
                temp_other_constellation.grid_points.append(OTHER_CONSTELLATIONS.get(constellation_pick)[0])
                temp_other_constellation.grid_lines.append(OTHER_CONSTELLATIONS.get(constellation_pick)[1])
                self.list_of_constellations.append(temp_other_constellation)


LETTER_CONSTELLATIONS = {
    'A':([3,12,14,21,25],[(3,12),(3,14),(12,14),(12,21),(14,25)]),
    'B':([1,3,9,11,13,19,21,23],[(1,3),(1,11),(11,21),(21,23),(11,13),(3,9),(9,13),(13,19),(19,23)]),
    'C':([2,4,6,16,22,24],[]),
    'D':([1,3,9,19,21,23],[]),
    'E':([2,4,12,14,22,24],[]),
    'F':([2,4,12,14,22],[]),
    'G':([2,4,6,10,16,19,20,22,24],[]),
    'H':([2,4,12,14,22,24],[]),
    'I':([2,3,4,22,23,24],[]),
    'J':([1,3,4,16,18,22],[]),
    'K':([2,4,12,22,24],[]),
    'L':([2,12,22,24],[]),
    'M':([1,5,21,23,25],[]),
    'N':([1,4,21,24],[]),
    'O':([2,4,6,10,16,20,22,24],[]),
    'P':([2,3,9,12,13,22],[]),
    'Q':([2,4,6,10,16,19,20,22,24,25],[]),
    'R':([1,3,9,11,13,21,23],[]),
    'S':([2,4,6,12,14,20,22,24],[]),
    'T':([1,3,5,23],[]),
    'U':([1,5,16,20,22,24],[]),
    'V':([1,5,23],[]),
    'W':([1,3,5,21,25],[]),
    'X':([1,4,21,24],[]),
    'Y':([2,4,13,23],[]),
    'Z':([2,4,22,24],),
    ' ': None
}

OTHER_CONSTELLATIONS = {
    0:([],[]),
    1:([],[]),
    2:([],[]),
    3:([],[]),
    4:([],[]),
    5:([3,5,11,15,21,23],[(11,23),(23,5),(21,3),(3,15)]),
    6:([1,3,4,11,13,14,23,25],[(1,4),(3,23),(11,13),(23,14),(14,25)]),
    7:([1,5,12,21,25],[(1,5),(1,12),(5,12),(5,21),(5,25),(21,25)]),
    8:([1,3,12,25],[(1,12),(12,3),(3,25)]),
    9:([1,3,5,13,22,24],[(1,13),(3,13),(5,13),(22,13),(24,13)]),
}