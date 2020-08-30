class Settings:
    def __init__(self):

        #Main display
        self.text_input = "Welcome"              #text box (maybe add numbers later)
        self.text_size = 60                      #slider
        self.text_location = (0, 45)             #x and y text box input (int only)

        #Options display
        self.show_constellations = True         #button --> turn on/off constellations
        self.show_grid = True                   #button --> turn on/off grid
        self.number_of_constellations = 8       #((PI * r^2) // self.text_size^2) * (self.constellation_density + 1)
        self.number_of_stars = 5000             #text box (int only)

        #Backend
        self.star_color = (153, 230, 255)       #color box
        self.back_color = (10, 0, 10)           #color box
        self.max_constellation_size = 100
        self.min_constellation_size = 30
        self.starfield = None
        self.default = None

    def reset(self):
        self.__init__()
