from star_map import Map
from interface import *
from pygame import Surface
from settings import *
import math

#create a map object and "draw" it
#map object has list of stars and lines ready to draw
# ---list_of_stars -- list of star (x,y) points
# ---list_of_constellations -- list_of_lines -- pairs of points

field_x, field_y = 650, 650
options_width = 200
field_buffer = 50
screen_x, screen_y = field_x + options_width + 2 * field_buffer, field_y + 2 * field_buffer
field_point = (int(screen_x - field_x - 2 * field_buffer), int((screen_y - field_y - 2 * field_buffer) / 2))
DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y), 0, 32)                                          #Main Display
STARFIELDSURF = Surface((field_x + (2 * field_buffer), field_y + (2 * field_buffer)))                       #Starfield
STARFIELDSURF_HOLD = STARFIELDSURF.copy()                                                                   #Holdover
OPTIONSURF = Surface((screen_x - field_x - 2 * field_buffer, screen_y))                                     #Option Bar
OPTIONSURF_HOLD = OPTIONSURF.copy()
SETTINGSURF = Surface((screen_x, screen_y))
star_map = Map(field_x, field_y)
settings_show = False
input_dict = {}

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NIGHTSKY = (7, 11, 15)
GRAY = (100, 100, 100)
LIGHTGRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NEWBLUE = (43, 67, 244)
NEWESTBLUE = (153, 230, 255) #gucci

#buttons --> [4x text position, show constellations, generate]
main_button_list = [
    Button(action="reset", text="Generate", text_active="Generating", color=(127, 127, 127), area=((1, 1), (198, 75)), border_size=2),
    #show constellations
    #push position up
    #push position down
    #push position left
    #push position right
    Button(action="settings", text="Settings", color=(127, 127, 127), area=((1, 161), (198, 75)), border_size=2)
]

settings_button_list = [
    Button(action="settings", text="Settings", color=(127, 127, 127), area=((1, 161), (198, 75)), border_size=2)
]

#sliders --> [R,G,B,number_of_constellations,text_size]
'''
slider_list = [
    Slider('R', 0, 255, 1),
    Slider('G', 0, 255, 1),
    Slider('B', 0, 255, 1),
    Slider('Constellations', 0, 100, 1),
    Slider('Text Size', 1, 10, 1)
]
'''
main_slider_list = [

]

settings_slider_list = [
    Slider(action="R", area = ((10, 400), (50, 315)), slider_rail=((20, 445), (20, 256)), is_vertical=True, slider_size=(20,10), slider_color=(127, 0, 0), label_position=(18, 410), label_color=(127, 0, 0))
]

#text boxes --> [num of stars, constellation text]
main_textbox_list = [
    Textbox(action="textString", area=((1, 130), (198, 25)), border_size=2, spacing=1, max_length=15)
]

settings_textbox_list = [

]

main_label_list = [
    Label(text = "Input string:", font_size = 32, pos = (25, 90))
]

settings_label_list = [

]

def define_main_interactions():
    temp_list = []
    temp_dict = {}
    entry = 0
    for button in main_button_list:
        temp_list.append(("Button", button.area, button.action, entry))
        entry += 1
    entry = 0
    for textbox in main_textbox_list:
        temp_list.append(("Textbox", textbox.area, textbox.action, entry))
        temp_dict.update({textbox.action:("mTextbox", entry)})
        entry += 1
    entry = 0
    for slider in main_slider_list:
        temp_list.append(("Slider", slider.slide_area, slider.action, entry))
        temp_dict.update({slider.action:("mSlider", entry)})
        entry += 1
    input_dict.update(temp_dict)
    return temp_list

def define_settings_interactions():
    temp_list = []
    temp_dict = {}
    entry = 0
    for button in settings_button_list:
        temp_list.append(("Button", button.area, button.action, entry))
        entry += 1
    entry = 0
    for textbox in settings_textbox_list:
        temp_list.append(("Textbox", textbox.area, textbox.action, entry))
        temp_dict.update({textbox.action:("sTextbox", entry)})
        entry += 1
    entry = 0
    for slider in settings_slider_list:
        temp_list.append(("Slider", slider.slide_area, slider.action, entry))
        temp_dict.update({slider.action:("sSlider", entry)})
        entry += 1
    input_dict.update(temp_dict)
    return temp_list

def draw_outline(settings):
    pygame.draw.circle(STARFIELDSURF, NIGHTSKY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), int(field_x / 2), 0)
    pygame.draw.circle(STARFIELDSURF, GRAY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), int(field_x / 2), 1)
    if settings.show_grid:
        circle_count = 8
        line_count = 12
        for i in range(1, circle_count + 1):
            pygame.draw.circle(STARFIELDSURF, LIGHTGRAY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), int(field_x / (circle_count + 1) / 2) * i, 1)
        for i in range(line_count):
            x1 = field_x * math.cos(math.pi * i / line_count) / 2
            y1 = field_y * math.sin(math.pi * i / line_count) / 2
            point_list = ((STARFIELDSURF.get_width() / 2 + x1,STARFIELDSURF.get_height() / 2 + y1), (STARFIELDSURF.get_width() / 2 - x1,STARFIELDSURF.get_height() / 2 - y1))
            pygame.draw.aalines(STARFIELDSURF, LIGHTGRAY, False, point_list)

def make_stars(settings):
    star_map.place_stars(settings)

### Star objects have a .draw() method that can be used to draw them
def draw_stars():
    for star in star_map.list_of_stars:
        star.draw(STARFIELDSURF)

def swap_settings():
    global settings_show
    settings_show = not settings_show

def query_settings():
    global settings_show
    return settings_show

def query_input(var):
    global input_dict
    control = input_dict[var]
    if control[0] == "mTextbox":
        return main_textbox_list[control[1]].text_object.input_string

def set_input(var, new_value):
    global input_dict
    control = input_dict[var]
    if control[0] == "mTextbox":
        main_textbox_list[control[1]].text_object.input_string = new_value
        main_textbox_list[control[1]].text_object.cursor_position = len(new_value)
        main_textbox_list[control[1]].text_object.update([])
    if control[0] == "sTextbox":
        settings_textbox_list[control[1]].text_object.input_string = new_value
        settings_textbox_list[control[1]].text_object.cursor_position = len(new_value)
        settings_textbox_list[control[1]].text_object.update([])
    if control[0] == "mSlider":
        main_slider_list[control[1]].update(new_value)
    if control[0] == "sSlider":
        settings_slider_list[control[1]].update(new_value)

def load_inputs(settings):
    set_input("textString", settings.text_input)
    set_input("R", settings.star_color[0])

def initialize_view(new_starfield, settings):
    #settings_show = False
    global STARFIELDSURF, STARFIELDSURF_HOLD
    DISPLAYSURF.fill(BLACK)
    if settings_show:
        SETTINGSURF.fill(WHITE)
        for button in settings_button_list:
            button.draw(SETTINGSURF)
        for textbox in settings_textbox_list:
            textbox.draw(SETTINGSURF)
        for slider in settings_slider_list:
            slider.draw(SETTINGSURF)
        for label in settings_label_list:
            label.draw(SETTINGSURF)
    else:
        if new_starfield:
            STARFIELDSURF.fill(BLACK)
            draw_outline(settings)
            draw_stars()
            draw_constellations(settings)
            STARFIELDSURF_HOLD = STARFIELDSURF.copy()
        else:
            STARFIELDSURF = STARFIELDSURF_HOLD.copy()
        OPTIONSURF.fill(WHITE)
        for button in main_button_list:
            button.draw(OPTIONSURF)
        for textbox in main_textbox_list:
            textbox.draw(OPTIONSURF)
        for slider in main_slider_list:
            slider.draw(OPTIONSURF)
        for label in main_label_list:
            label.draw(OPTIONSURF)

def draw_view():
    if settings_show:
        DISPLAYSURF.blit(SETTINGSURF, (0, 0))
    else:
        DISPLAYSURF.blit(STARFIELDSURF, field_point)
        DISPLAYSURF.blit(OPTIONSURF, (0, 0))

### Constellation objects have a .draw() method that can be used to draw them
def draw_constellations(settings):
    star_map.place_constellations(40, settings)
    for constellation in star_map.list_of_constellations:
        constellation.draw(STARFIELDSURF, settings)