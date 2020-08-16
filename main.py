import pygame, sys
from settings import *
from draw import *
from pygame.locals import *

settings_data = Settings()
make_stars(settings_data)
click_areas = define_interactions()

display_changed = True
click_action = ("", 0)
initialize_view()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            click_active = False
            if click_action[0] == "Button":
                Button_List[click_action[1]].active = False
                click_action = ("", 0)
            if not display_changed:
                initialize_view()
                display_changed = True
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for entry in click_areas:
                if entry[1][0][0] <= mouse[0] <=entry[1][1][0] and entry[1][0][1] <= mouse[1] <=entry[1][1][1]:
                    if entry[0] == "Button":
                        Button_List[entry[3]].active = True
                        click_active = True
                        click_action = ("Button", entry[3])
                    if not display_changed:
                        initialize_view()
                        display_changed = True
    if display_changed:
        display_changed = False
        draw_view()
    pygame.display.update()