import pygame, sys
from settings import *
from draw import *

settings_data = Settings()

make_stars(settings_data)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    draw_view()
    '''
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for area in click_areas:
                if area[0][0] <= mouse[0] <=area[1][0] and area[0][1] <= mouse[1] <=area[1][1]:
                    if not display_changed:
                        draw_initial()
                        display_changed = True
                    star_generator()
    if display_changed:
        display_changed = False
        draw_surfaces()
    '''
    pygame.display.update()