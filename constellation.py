class Constellation():

    def __init__(self, type, size, center, settings):
        self.size = size
        self.center = center
        self.points = [] #list of Star objects
        self.lines = [] #list with each item being a line -- a line is a pair of points
    
    
    def draw(self):
        temp_min_value = 50 #place holder -- need to relook at this logic
        for star in self.stars_list: #could optimize this line more by only looking through stars that already near by the center
            if abs(star.x - self.center[0]) + abs(star.y - self.center[1]) < temp_min_value:
                self.center = star.location
                star.size = 3 #this wont work, need to find way to edit the real Star instance

        self.points.append(self.center)

        #find way to draw lines smarter -- different shapes? no crossing lines, no lines that are too short/long
        #its not just about the distance a star is away from another star