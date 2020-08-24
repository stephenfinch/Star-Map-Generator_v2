class Settings:
    def __init__(self):

        #Main display
        self.text_input = "NP"                    #text box (maybe add numbers later)
        self.text_size = 1                      #slider
        self.text_height_offset = 0             #four buttons (arrows -- move the center)

        #Options display
        self.show_constellation = True          #button --> turn on/off all types of constellations at once
        self.show_constellation_lines = True    #button
        self.show_grid = True                   #button
        self.number_of_constellations = 1       #slider
        self.number_of_stars = 8000             #text box (int only)
        self.star_color = (153, 230, 255)       #color box
        self.back_color = (7, 11, 15)           #color box
