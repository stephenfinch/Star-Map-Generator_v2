from star import Star
from constellation import Constellation

#create lots of star objects
#use those star objets to make constellation objects


class Map:
    def __init__(self, field_x, field_y):
        self.star_list = []
        self.field_x = field_x
        self.field_y = field_y
        
        self.field_buffer = 50 #gap between display edge and circle
        self.field_inner_buffer = 3 #gap between circle and outer stars
        self.r = self.field_x / 2 - self.field_inner_buffer #raduis
        self.Xcenter = self.Ycenter = self.field_x / 2 + self.field_buffer

## STARS ## makes a list of Star objects and adds them to a list
    def place_stars(self, number_of_stars):
        self.number_of_stars = number_of_stars
        stars_added = 0
        while stars_added < self.number_of_stars:
            x, y = random.randint(0, self.field_x), random.randint(0, self.field_y)
            if is_in_circle(x,y):
                self.star_list.append(Star(x,y))
                stars_added += 1

    def is_in_circle(x, y):
        return (x - self.Xcenter) ** 2 + (y - self.Ycenter) ** 2 <= r ** 2


## CONSTELLATIONS ## uses the list of Star objects and connects them into constellations
    def place_constellations(self, size, ):
        self.size = size
        pass


our_map = Map(1,1,1,1)

for i in range(settings_number_of_constellations):
    our_map.place_constellations(random.randint(1,5))