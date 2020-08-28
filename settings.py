class Settings:
    def __init__(self):

        #Main display
        self.text_input = '' #"Welcome"             #text box (maybe add numbers later)
        self.text_size = 35                      #slider
        self.text_location = (0, 60)             #four buttons (arrows -- move the center)

        #Options display
        #self.show_letter_constellations = True  #button --> turn on/off letter constellations
        #self.show_pther_constellations = True   #button --> turn on/off other constellations
        self.show_constellations = True         #button --> turn on/off constellations
        self.show_grid = True                   #button
        self.constellation_density = 0          #slider
        self.number_of_constellations = 1 # fix using density and size later
        self.number_of_stars = 5000             #text box (int only)

        #Backend
        self.star_color = (153, 230, 255)       #color box
        self.back_color = (10, 0, 10)           #color box
