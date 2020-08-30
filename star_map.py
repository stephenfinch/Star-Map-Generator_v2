from star import Star
from constellation import Constellation, Random_Constellation
import random, math

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

    ### given an (x,y) point it will return True/False if the point is in the circle drawn
    def is_in_circle(self, x, y):
        return (x - self.Xcenter) ** 2 + (y - self.Ycenter) ** 2 <= self.r ** 2


    def coerce_to_center(self, x, y):
        newx, newy = self.Xcenter + int(x / 100 * ((self.field_x / 2) - self.field_inner_buffer)), self.Ycenter - int(y / 100 * ((self.field_y / 2) - self.field_inner_buffer))
        if self.is_in_circle(newx, newy):
            return (x, y)
        else:
            angle = math.atan2((newy - self.Ycenter), (newx - self.Xcenter))
            coercex, coercey = int(100 * math.cos(angle)), -int(100 * math.sin(angle))
            print(coercex,coercey)
            return (coercex, coercey)

    def no_overlap(self, x, y, size, settings):
        buffer = 5
        X1L =  x - (size / 2) - buffer
        X1R =  x + (size / 2) + buffer
        Y1U =  y - (size / 2) - buffer
        Y1D =  y + (size / 2) + buffer
        for constellation in self.list_of_constellations:
            centerX, centerY = constellation.center[0], constellation.center[1]
            X2L =  centerX - (constellation.size / 2) - buffer
            X2R =  centerX + (constellation.size / 2) + buffer
            Y2U =  centerY - (constellation.size / 2) - buffer
            Y2D =  centerY + (constellation.size / 2) + buffer
            if X1L < X2R and X1R > X2L and Y1U < Y2D and Y1D > Y2U:
                return False
            '''
            if ((X1L < X2R and X1L > X2L) or (X1R < X2R and X1R > X2L)) and ((Y1U < Y2D and Y1U > Y2U) or (Y1D < Y2D and Y1D > Y2U)):
                return False
            
            if abs(centerX - x) < settings.text_size * 2 and abs(centerY - y) < settings.text_size * 2:
                return False
            '''
        return True


## STARS ## makes a list of Star objects and adds them to a list
    def place_stars(self, settings):
        self.number_of_stars = settings.number_of_stars
        self.list_of_stars = []
        stars_added = 0

        while stars_added < self.number_of_stars:
            x, y = random.randint(self.field_buffer, self.field_buffer + self.field_x), random.randint(self.field_buffer, self.field_buffer + self.field_y)
            if self.is_in_circle(x, y):
                self.list_of_stars.append(Star(x, y, settings))
                stars_added += 1


## CONSTELLATIONS ## makes constellation objects and edits their center/size to fit them where they need to go
    def place_constellations(self, constellation_size, settings):
        self.constellation_size = constellation_size #side length of the 5x5 grid
        self.list_of_constellations = []
        
        ### adds the point/line data for that letter to the list of constellations
        string_length = len(settings.text_input.upper())
        string_index = 0
        self.letter_spacing = constellation_size // 4
        for char in settings.text_input.upper():
            centerX = (self.constellation_size + self.letter_spacing) * (string_index - (string_length - 1) / 2) + int(self.Xcenter + settings.text_location[0] / 100 * ((self.field_x / 2) - self.field_inner_buffer))
            centerY = self.Ycenter - int(settings.text_location[1] / 100 * ((self.field_y / 2) - self.field_inner_buffer))
            temp_letter_constellation = Constellation(self.constellation_size, (centerX, centerY), settings)
            temp_letter_constellation.grid_points.append(LETTER_CONSTELLATIONS.get(char)[0])
            temp_letter_constellation.grid_lines.append(LETTER_CONSTELLATIONS.get(char)[1])
            string_index += 1
            self.list_of_constellations.append(temp_letter_constellation)
        
        ### creates and adds point/line data for each random constellations
        if settings.show_constellations:
            constellations_placed, failed_tries = 0, 0
            while constellations_placed < settings.number_of_constellations and failed_tries < 1000:
                constellation_pick = random.randint(0, len(OTHER_CONSTELLATIONS) - 1)
                x, y = random.randint(self.field_buffer, self.field_buffer + self.field_x), random.randint(self.field_buffer, self.field_buffer + self.field_y)
                random_constellation_size = random.randint(self.constellation_size, self.constellation_size + 50)
                if self.is_in_circle(x, y) and self.no_overlap(x, y, random_constellation_size, settings):
                    temp_other_constellation = Random_Constellation(random_constellation_size, (x,y), settings, orientation=random.randint(0,3), is_inverted=random.randint(0,1))
                    temp_other_constellation.grid_points.append(OTHER_CONSTELLATIONS.get(constellation_pick)[0])
                    temp_other_constellation.grid_lines.append(OTHER_CONSTELLATIONS.get(constellation_pick)[1])
                    self.list_of_constellations.append(temp_other_constellation)
                    constellations_placed += 1
                else:
                    failed_tries += 1


LETTER_CONSTELLATIONS = {
    'A':([3,12,14,21,25],[(3,12),(3,14),(12,14),(12,21),(14,25)]),
    'B':([1,3,9,11,13,19,21,23],[(1,3),(1,11),(11,21),(21,23),(11,13),(3,9),(9,13),(13,19),(19,23)]),
    'C':([2,4,6,16,22,24],[(2,4),(2,6),(6,16),(16,22),(22,24)]),
    'D':([1,3,9,19,21,23],[(1,21),(1,3),(3,9),(9,19),(19,23),(21,23)]),
    'E':([2,4,12,14,22,24],[(2,12),(12,22),(2,4),(12,14),(22,24)]),
    'F':([2,4,12,14,22],[(2,12),(12,22),(2,4),(12,14)]),
    'G':([2,4,6,10,16,18,20,22,24],[(2,4),(2,6),(4,10),(6,16),(16,22),(18,20),(20,24),(22,24)]),
    'H':([2,4,12,14,22,24],[(2,12),(12,22),(4,14),(14,24),(12,14)]),
    'I':([2,3,4,13,22,23,24],[(2,3),(3,4),(3,13),(13,23),(22,23),(23,24)]),
    'J':([1,3,4,16,18,22],[(1,3),(3,4),(3,18),(18,22),(22,16)]),
    'K':([2,4,12,22,24],[(2,12),(4,12),(12,22),(12,24)]),
    'L':([2,12,22,24],[(2,12),(12,22),(22,24)]),
    'M':([2,4,21,23,25],[(2,21),(2,23),(4,23),(4,25)]),
    'N':([1,4,21,24],[(1,21),(1,24),(24,4)]),
    'O':([2,4,6,10,16,20,22,24],[(2,4),(2,6),(4,10),(6,16),(10,20),(16,22),(20,24),(22,24)]),
    'P':([2,3,9,12,13,22],[(2,12),(12,22),(2,3),(3,9),(9,13),(12,13)]),
    'Q':([2,4,6,10,16,19,20,22,24,25],[(2,4),(2,6),(4,10),(6,16),(10,20),(16,22),(19,25),(20,24),(22,24)]),
    'R':([1,3,9,11,13,21,23],[(1,3),(1,11),(3,9),(9,13),(11,13),(11,21),(11,23)]),
    'S':([2,4,6,12,14,20,22,24],[(2,4),(2,6),(6,12),(12,14),(14,20),(20,24),(22,24)]),
    'T':([1,3,5,23],[(1,3),(3,5),(3,23)]),
    'U':([1,5,16,20,22,24],[(1,16),(5,20),(16,22),(20,24),(22,24)]),
    'V':([1,5,23],[(1,23),(5,23)]),
    'W':([1,8,5,22,24],[(1,22),(8,22),(8,24),(5,24)]),
    'X':([1,4,21,24],[(1,24),(4,21)]),
    'Y':([2,4,13,23],[(2,13),(4,13),(13,23)]),
    'Z':([2,4,22,24],[(2,4),(4,22),(22,24)]),
    ' ':([],[])
}


OTHER_CONSTELLATIONS = {
    0: ([3, 5, 11, 15, 21, 23], [(3, 15), (3, 21), (5, 23), (11, 23)]),
    1: ([1, 3, 4, 11, 13, 14, 23, 25], [(1, 3), (3, 4), (3, 13), (11, 13), (13, 23), (14, 23), (14, 25)]),
    2: ([1, 5, 12, 21, 25], [(1, 5), (1, 12), (5, 12), (5, 21), (5, 25), (21, 25)]),
    3: ([1, 3, 12, 25], [(1, 12), (3, 12), (3, 25)]),
    4: ([1, 3, 5, 13, 22, 24], [(1, 13), (3, 13), (5, 13), (13, 22), (13, 24)]),
    5: ([1, 5, 14, 22, 23, 25, 26], [(1, 14), (1, 26), (5, 14), (14, 25), (22, 23)]),
    6: ([2, 4, 9, 11, 21], [(2, 4), (2, 9), (2, 11), (9, 11), (9, 21)]),
    7: ([1, 3, 7, 11, 19, 20, 25], [(1, 3), (3, 7), (3, 20), (7, 11), (19, 20), (20, 25)]),
    8: ([3, 10, 12, 19, 21, 22, 25], [(3, 12), (3, 19), (10, 12), (10, 25), (12, 21), (12, 22), (21, 22)]),
    9: ([1, 3, 10, 16, 17, 19], [(1, 10), (3, 17), (3, 19), (10, 17), (16, 17), (17, 19)]),
    10: ([9, 14, 17, 22, 24, 25, 26], [(9, 14), (9, 25), (9, 26), (17, 22), (17, 26), (24, 25), (24, 26)]),
    11: ([8, 9, 17, 21, 22, 25, 26], [(8, 9), (8, 22), (9, 17), (21, 22), (21, 25), (22, 26)]),
    12: ([6, 7, 9, 18, 20, 22, 24], [(6, 7), (7, 18), (9, 18), (9, 24), (20, 22), (20, 24)]),
    13: ([1, 9, 12, 14, 20], [(1, 9), (1, 12), (1, 14), (9, 20), (12, 20)]),
    14: ([6, 16, 18, 20, 22, 24], [(6, 16), (6, 22), (6, 24), (16, 18), (20, 22)]),
    15: ([15, 22, 23, 24, 25], [(15, 22), (15, 24), (15, 25), (22, 25), (23, 24)]),
    16: ([12, 13, 19, 20, 21, 22, 25], [(12, 25), (13, 22), (19, 20), (19, 25), (21, 22), (22, 25)]),
    17: ([1, 26, 18, 23], [(1, 23), (1, 26), (18, 23), (18, 26)]),
    18: ([1, 4, 6, 11, 14, 22], [(1, 4), (4, 11), (4, 14), (6, 14), (14, 22)]),
    19: ([1, 12, 13, 21, 23], [(1, 23), (12, 21), (12, 23), (13, 23), (21, 23)]),
    20: ([7, 11, 18, 19, 21, 22], [(7, 11), (11, 22), (18, 19), (19, 21)]),
    21: ([8, 9, 16, 18, 22, 23], [(8, 22), (9, 18), (16, 22), (18, 23)]),
    22: ([1, 3, 7, 8, 12, 13, 21, 22], [(1, 3), (1, 8), (1, 22), (3, 7), (3, 12), (3, 13), (21, 22)]),
    23: ([2, 3, 5, 7, 10, 22], [(2, 10), (3, 7), (3, 22), (5, 10), (10, 22)]),
    24: ([5, 11, 16, 22, 23], [(5, 11), (5, 16), (11, 16), (11, 22), (11, 23)]),
    25: ([13, 12, 21, 6], [(6, 12), (6, 21), (12, 13), (13, 21)]),
    26: ([6, 11, 12, 14, 19, 25], [(6, 11), (6, 12), (6, 14), (6, 19), (14, 19), (14, 25)]),
    27: ([3, 7, 10, 11, 14, 23], [(3, 10), (7, 10), (7, 11), (7, 14), (10, 23)]),
    28: ([1, 10, 13, 19, 21, 24], [(1, 10), (1, 13), (10, 13), (10, 19), (13, 19), (13, 21), (19, 24)]),
    29: ([5, 13, 20, 22, 24], [(5, 24), (13, 20), (20, 22), (22, 24)]),
    30: ([3, 16, 20, 25, 26], [(3, 20), (3, 25), (16, 25), (20, 25), (20, 26)]),
    31: ([3, 4, 12, 14, 17, 18], [(3, 12), (3, 14), (3, 18), (4, 14), (12, 17), (17, 18)]),
    32: ([4, 14, 15, 16, 25], [(4, 16), (14, 16), (15, 25), (16, 25)]),
    33: ([2, 5, 13, 14, 19, 21], [(2, 21), (5, 14), (5, 19), (13, 14), (13, 21)]),
    34: ([2, 10, 13, 15, 19, 26], [(2, 10), (10, 13), (13, 15), (19, 26)]),
    35: ([4, 13, 15, 17, 20, 24], [(4, 15), (4, 24), (13, 15), (17, 20)])
    } #36: ([1 ,5, 21, 25], [(1, 5), (1, 21), (21, 25), (5, 25)])