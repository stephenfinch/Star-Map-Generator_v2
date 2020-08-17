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

        def is_in_circle(x, y):
            return (x - self.Xcenter) ** 2 + (y - self.Ycenter) ** 2 <= self.r ** 2

        while stars_added < self.number_of_stars:
            x, y = random.randint(self.field_buffer, self.field_buffer + self.field_x), random.randint(self.field_buffer, self.field_buffer + self.field_y)
            if is_in_circle(x, y):
                self.list_of_stars.append(Star(x, y, settings))
                stars_added += 1


## CONSTELLATIONS ## uses the list of Star objects and connects them into constellations
    def place_constellations(self, size, settings):
        self.size = size
        self.list_of_constellations = []
        if settings.text_input:
            for char in settings.text_input.upper():
                self.list_of_constellations.append(LETTER_CONSTELLATIONS.get(char)) #adds the point/line data for that letter to the list of constellations
        
        for i in range(settings.number_of_constellations):
            self.list_of_constellations.append(OTHER_CONSTELLATIONS.get(random.randint(0,9)))


LETTER_CONSTELLATIONS = {
    'A':([3,12,14,21,25],[(3,12),(3,14),(12,14),(12,21),(14,25)]),
    'B':[], #'B':([1,3,9,11,13,19,21,23],[])
    'C':[], #'C':([2,4,6,16,22,24],[])
    'D':[], #'D':([1,3,9,19,21,23],[])
    'E':[], #'E':([2,4,12,14,22,24],[])
    'F':[], #'F':([2,4,12,14,22],[])
    'G':[], #'G':([2,4,6,10,16,19,20,22,24],[])
    'H':[], #'H':([2,4,12,14,22,24],[])
    'I':[], #'I':([2,3,4,22,23,24],[])
    'J':[], #'J':([1,3,4,16,18,22],[])
    'K':[], #'K':([2,4,12,22,24],[])
    'L':[], #'L':([2,12,22,24],[])
    'M':[], #'M':([1,5,21,23,25],[])
    'N':[], #'N':([1,4,21,24],[])
    'O':[], #'O':([2,4,6,10,16,20,22,24],[])
    'P':[], #'P':([2,3,9,12,13,22],[])
    'Q':[], #'Q':([2,4,6,10,16,19,20,22,24,25],[])
    'R':[], #'R':([1,3,9,11,13,21,23],[])
    'S':[], #'S':([2,4,6,12,14,20,22,24],[])
    'T':[], #'T':([1,3,5,23],[])
    'U':[], #'U':([1,5,16,20,22,24],[])
    'V':[], #'V':([1,5,23],[])
    'W':[], #'W':([1,3,5,21,25],[])
    'X':[], #'X':([1,4,21,24],[])
    'Y':[], #'Y':([2,4,13,23],[])
    'Z':[], #'Z':([2,4,22,24],)
    ' ':[]
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