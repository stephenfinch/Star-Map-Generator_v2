from star_map import Map
from interface import *
import pygame
from pygame import Surface
from pygame.locals import *

#create a map object and "draw" it
#map object has list of stars and lines ready to draw
# ---list_of_stars -- list of star (x,y) points
# ---list_of_constellations -- list_of_lines -- pairs of points


field_x, field_y = 650, 650
options_width = 200
field_buffer = 50
screen_x, screen_y = field_x + options_width + 2 * field_buffer, field_y + 2 * field_buffer
field_point = (int(screen_x - field_x - 2 * field_buffer), int((screen_y - field_y - 2 * field_buffer) / 2))
DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y), 0, 32)                               #Main Display
STARFIELDSURF = Surface((field_x + (2 * field_buffer), field_y + (2 * field_buffer)))  #Starfield
STARFIELDSURF_HOLD = STARFIELDSURF.copy()                                                             #Holdover
OPTIONSURF = Surface((screen_x - field_x - 2 * field_buffer, screen_y))                #Option Bar
OPTIONSURF_HOLD = OPTIONSURF.copy()
star_map = Map(field_x, field_y)

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
NIGHTSKY = (7, 11, 15)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NEWBLUE = (43, 67, 244)

Button_List = [Button(name="reset", text="Generate", text_active="Generating", color=(127, 127, 127), area=((0, 0), (200, 75)), size=(200, 75), border_size=4)]

def define_interactions():
    temp_list = []
    entry = 0
    for button in Button_List:
        temp_list.append(("Button", button.area, button.name, entry))
        entry += 1
    return temp_list

def draw_outline():
    pygame.draw.circle(STARFIELDSURF, NIGHTSKY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), int(field_x / 2), 0)
    pygame.draw.circle(STARFIELDSURF, GRAY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), int(field_x / 2), 1)

def make_stars(settings):
    star_map.place_stars(settings)

def draw_stars():
    for star in star_map.list_of_stars:
        pygame.draw.circle(STARFIELDSURF, star.color, (star.x, star.y), star.size, 0)

def initialize_view():
    DISPLAYSURF.fill(BLACK)
    STARFIELDSURF.fill(BLACK)
    OPTIONSURF.fill(WHITE)
    draw_outline()
    draw_stars()
    for button in Button_List:
        button.draw(OPTIONSURF)


def draw_view():
    DISPLAYSURF.blit(STARFIELDSURF, field_point)
    DISPLAYSURF.blit(OPTIONSURF, (0, 0))



def draw_constellations(self, settings):
    for constellation in self.star_map.list_of_constellations:
        for line in constellation.lines:
            pygame.draw.aalines(surface, color, line)
        for point in constellation.points:
            pygame.draw.circle(STARFIELDSURF, point.color, (point.x, point.y), 3, 0)
