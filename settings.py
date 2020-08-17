class Settings:
    def __init__(self):
        self.text_input = ""                    #text box (maybe add numbers later)
        self.text_size = 1                      #slider
        self.text_location = (0, 0)             #four buttons (arrows -- move the center)
        self.number_of_constellations = 5       #slider
        self.show_constellation_lines = True    #button
        self.number_of_stars = 5000             #text box (int only)
        self.star_color = (153, 230, 255)       #color box
        self.back_color = (7, 11, 15)           #color box
        self.outline_color = (100, 100, 100)    #color box
        self.show_grid = True                  #button
