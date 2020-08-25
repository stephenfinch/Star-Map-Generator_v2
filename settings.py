class Settings:
    def __init__(self):

        #Main display
        self.text_input = "Welcome"             #text box (maybe add numbers later)
        self.text_size = 1                      #slider
        self.text_height_offset = 0             #four buttons (arrows -- move the center)

        #Options display
        self.show_letter_constellations = True  #button --> turn on/off letter constellations
        self.show_other_constellations = True   #button --> turn on/off other constellations
        self.show_grid = True                   #button
        self.constellation_density = 0          #slider
        self.number_of_stars = 8000             #text box (int only)

        #Backend
        self.star_color = (153, 230, 255)       #color box
        self.back_color = (7, 11, 15)           #color box
