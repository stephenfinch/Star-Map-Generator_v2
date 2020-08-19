import pygame, sys
from settings import *
from draw import *
from backend import *
from pygame.locals import *

settings_data = Settings()
make_stars(settings_data)
click_areas = define_interactions()
clock = pygame.time.Clock()
display_changed = True
textbox_clicked = False
click_action = ("", 0)
action_list = []
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            if click_action[0] == "Button":
                button_list[click_action[1]].active = False
                click_action = ("", 0)
                display_changed = True
            if click_action[0] == "Slider":
                slider_list[click_action[1]].active = False
                click_action = ("", 0)
                display_changed = True
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for entry in click_areas:
                if entry[1][0][0] <= mouse[0] <= entry[1][1][0] + entry[1][0][0] and entry[1][0][1] <= mouse[1] <= entry[1][1][1] + entry[1][0][1]:
                    if entry[0] == "Button":
                        button_list[entry[3]].active = True
                        click_action = ("Button", entry[3])
                        action_list.append(entry[2])
                        display_changed = True
                    if entry[0] == "Textbox":
                        textbox_list[entry[3]].active = True
                        display_changed = True
                        textbox_clicked = True
                    if entry[0] == "Slider":
                        slider_list[entry[3]].active = True
                        display_changed = True
                        click_action = ("Slider", entry[3])
                        slider_list[entry[3]].slide(event.pos)
                else:
                    swap_settings()
                    display_changed = True
            if not textbox_clicked:
                for textbox in textbox_list:
                    textbox.active = False
            else:
                textbox_clicked = False
        if click_action[0] == "Slider" and event.type == MOUSEMOTION:
            slider_list[click_action[1]].slide(event.pos)
            display_changed = True
    for textbox in textbox_list:
        if textbox.active:
            if textbox.text_object.update(events):
                textbox.text_object.update([pygame.event.Event(KEYUP, key=13)])
                textbox.active = False
            display_changed = True
    if display_changed:
        initialize_view(settings_data)
        for action in action_list:
            perform_action(action, settings_data)
        action_list = []
        display_changed = False
        draw_view()
    
    pygame.display.update()
    clock.tick(25)






### REVIEWS
# From: Emma,
# 13/10
# 5 stars on yelp
# THE YEET CONSTELLATION
# i change my review; 16/10