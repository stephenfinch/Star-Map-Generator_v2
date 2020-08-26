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
LIGHTGRAY = (30, 30, 30)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NEWBLUE = (43, 67, 244)
NEWESTBLUE = (153, 230, 255) #gucci

#buttons --> [4x text position, generate]
main_button_list = [
    Button(action="reset", text="Generate", text_active="Generating", color=(127, 127, 127), area=((1, 1), (198, 75)), border_size=2),
    Button(action="settings", text="Settings", color=(127, 127, 127), area=((1, 674), (198, 75)), border_size=2),
    Button(action="textSizeUp", text="+", color=(127, 127, 127), area=((75, 280), (50, 50)), border_size=2),
    Button(action="textSizeDown", text="-", color=(127, 127, 127), area=((75, 390), (50, 50)), border_size=2)
]

#button --> [show constellations]
settings_button_list = [
    Button(action="settings", text="Back", color=(127, 127, 127), area=((1, 674), (198, 75)), border_size=2),
    Button(action="colorbox", text="", color=(127, 127, 127), area=((360, 10), (152, 152)), border_size=2),
    Button(action="starcolor", text="", color=(127, 127, 127), area=((850, 20), (60, 60)), border_size=2),
    Button(action="backgroundcolor", text="", color=(127, 127, 127), area=((850, 90), (60, 60)), border_size=2),
    Button(action="showgrid", text="Show Grid", color=(127, 127, 127), area=((100, 450), (198, 75)), border_size=2),
    Button(action="showconstellations", text="Show Constellations", color=(127, 127, 127), area=((500, 450), (300, 75)), border_size=2)
]


main_slider_list = [

]

#sliders --> [R,G,B,number_of_constellations,text_size]
settings_slider_list = [
    Slider(action="R", area = ((10, 10), (330, 32)), slider_rail=((65, 25), (256, 2)), slider_size=(10,20), slider_color=(200, 0, 0), label_position=(15, 12), label_color=(127, 0, 0)),
    Slider(action="G", area = ((10, 70), (330, 32)), slider_rail=((65, 85), (256, 2)), slider_size=(10,20), slider_color=(0, 200, 0), label_position=(15, 72), label_color=(0, 127, 0)),
    Slider(action="B", area = ((10, 130), (330, 32)), slider_rail=((65, 145), (256, 2)), slider_size=(10,20), slider_color=(0, 0, 200), label_position=(15, 132), label_color=(0, 0, 127)),
    Slider(action="constellation_density", area = ((500, 300), (285, 32)), slider_rail=((515, 315), (256, 2)), slider_size=(10,20), slider_color=(0, 0, 0), max_value=3)
]

#text boxes --> [num of stars, constellation text]
main_textbox_list = [
    Textbox(action="textString", area=((1, 130), (198, 25)), border_size=2, spacing=1, max_length=15),
    Textbox(action="textPosX", area=((25, 235), (65, 25)), border_size=2, spacing=1, max_length=3),
    Textbox(action="textPosY", area=((110, 235), (65, 25)), border_size=2, spacing=1, max_length=3)
]

settings_textbox_list = [
    Textbox(action="starcount", area=((100, 300), (198, 25)), border_size=2, spacing=1, max_length=5)
]

main_label_list = [
    Label(text = "Input Text:", font_size = 32, pos = (25, 85)),
    Label(text = "Text Position:", font_size = 32, pos = (15, 165)),
    Label(text = "    x         y", font_size = 32, pos = (19, 195)),
    Label(text = "Text Size", font_size = 32, pos = (40, 340))
]

settings_label_list = [
    Label(text = ">>>       Use for Stars       >>>", font_size = 24, pos = (530, 35)),
    Label(text = ">>> Use for Background >>>", font_size = 24, pos = (530, 105)),
    Label(text = "Number of Stars", font_size = 24, pos = (100, 260)),
    Label(text = "Constellation Density", font_size = 24, pos = (500, 260))
]

def define_main_interactions():
    temp_list = []
    temp_dict = {}
    entry = 0
    for button in main_button_list:
        temp_list.append(("Button", button.area, button.action, entry))
        temp_dict.update({button.action:("mButton", entry)})
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
        temp_dict.update({button.action:("sButton", entry)})
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
    pygame.draw.circle(STARFIELDSURF, settings.back_color, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), int(field_x / 2), 0)
    pygame.draw.circle(STARFIELDSURF, GRAY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), int(field_x / 2), 1)
    if settings.show_grid:
        circle_count = 8
        line_count = 24
        for i in range(1, circle_count + 1):
            pygame.draw.circle(STARFIELDSURF, LIGHTGRAY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), field_x // (2 * (circle_count + 1)) * i, 1)
        for i in range(line_count):
            xmult = math.cos(math.pi * 2 * i / line_count)
            ymult = math.sin(math.pi * 2 * i / line_count)
            point_list = ((STARFIELDSURF.get_width() / 2 + (xmult * field_x / 2),STARFIELDSURF.get_height() / 2 + (ymult * field_y / 2)), (STARFIELDSURF.get_width() / 2 + xmult * (field_x // (2 * (circle_count + 1))),STARFIELDSURF.get_height() / 2 + ymult * (field_y // (2 * (circle_count + 1)))))
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
    elif control[0] == "sTextbox":
        return settings_textbox_list[control[1]].text_object.input_string
    elif control[0] == "mSlider":
        return main_slider_list[control[1]].value
    elif control[0] == "sSlider":
        return settings_slider_list[control[1]].value

def get_input_object(var):
    global input_dict
    control = input_dict[var]
    if control[0] == "mButton":
        return main_button_list[control[1]]
    if control[0] == "sButton":
        return settings_button_list[control[1]]
    if control[0] == "mTextbox":
        return main_textbox_list[control[1]]
    elif control[0] == "sTextbox":
        return settings_textbox_list[control[1]]
    elif control[0] == "mSlider":
        return main_slider_list[control[1]]
    elif control[0] == "sSlider":
        return settings_slider_list[control[1]]

def set_input(var, new_value):
    global input_dict
    control = input_dict[var]
    if control[0] == "mTextbox":
        main_textbox_list[control[1]].text_object.input_string = new_value
        main_textbox_list[control[1]].text_object.cursor_position = len(new_value)
        main_textbox_list[control[1]].text_object.update([])
    elif control[0] == "sTextbox":
        settings_textbox_list[control[1]].text_object.input_string = new_value
        settings_textbox_list[control[1]].text_object.cursor_position = len(new_value)
        settings_textbox_list[control[1]].text_object.update([])
    elif control[0] == "mSlider":
        main_slider_list[control[1]].update(new_value)
    elif control[0] == "sSlider":
        settings_slider_list[control[1]].update(new_value)

def load_inputs(settings):
    set_input("textString", settings.text_input)
    set_input("R", settings.star_color[0])
    set_input("G", settings.star_color[1])
    set_input("B", settings.star_color[2])
    color_r = query_input("R")
    color_g = query_input("G")
    color_b = query_input("B")
    get_input_object("colorbox").color = (color_r, color_g, color_b)
    get_input_object("colorbox").color_active = (color_r, color_g, color_b)
    get_input_object("starcolor").color = settings.star_color
    get_input_object("starcolor").color_active = settings.star_color
    get_input_object("backgroundcolor").color = settings.back_color
    get_input_object("backgroundcolor").color_active = settings.back_color
    set_input("starcount", str(settings.number_of_stars))
    set_input("textPosX", "0")
    set_input("textPosY", "0")

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
    star_map.place_constellations(settings.text_size, settings)
    for constellation in star_map.list_of_constellations:
        constellation.draw(STARFIELDSURF, settings)

