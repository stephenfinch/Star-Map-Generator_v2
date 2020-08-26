import pygame, sys
from settings import *
from draw import *
from backend import *
from pygame.locals import *

settings_data = Settings()
make_stars(settings_data)
main_click_areas = define_main_interactions()
settings_click_areas = define_settings_interactions()
load_inputs(settings_data)
setting_show_temp = False
clock = pygame.time.Clock()
display_changed = True
starfield_changed = True
textbox_clicked = False
click_action = ("", 0)
action_list = []
while True:
    events = pygame.event.get()
    settings_show = query_settings()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            if click_action[0] == "Button":
                if not settings_show == setting_show_temp:
                    if settings_show:
                        main_button_list[click_action[1]].active = False
                    else:
                        settings_button_list[click_action[1]].active = False
                elif settings_show:
                    settings_button_list[click_action[1]].active = False
                else:
                    main_button_list[click_action[1]].active = False
                click_action = ("", 0)
                display_changed = True
                setting_show_temp = settings_show
            if click_action[0] == "Slider":
                if settings_show:
                    settings_slider_list[click_action[1]].active = False
                else:
                    main_slider_list[click_action[1]].active = False
                click_action = ("", 0)
                display_changed = True
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if settings_show:
                selected_click_areas = settings_click_areas
            else:
                selected_click_areas = main_click_areas
            for entry in selected_click_areas:
                if entry[1][0][0] <= mouse[0] <= entry[1][1][0] + entry[1][0][0] and entry[1][0][1] <= mouse[1] <= entry[1][1][1] + entry[1][0][1]:
                    if entry[0] == "Button":
                        if settings_show:
                            settings_button_list[entry[3]].active = True
                        else:
                            main_button_list[entry[3]].active = True
                        click_action = ("Button", entry[3])
                        action_list.append(entry[2])
                        display_changed = True
                        if entry[2] == "reset":
                            starfield_changed = True
                    if entry[0] == "Textbox":
                        if settings_show:
                            settings_textbox_list[entry[3]].active = True
                        else:
                            main_textbox_list[entry[3]].active = True
                        display_changed = True
                        textbox_clicked = True
                    if entry[0] == "Slider":
                        if settings_show:
                            settings_slider_list[entry[3]].active = True
                        else:
                            main_slider_list[entry[3]].active = True
                        display_changed = True
                        click_action = ("Slider", entry[3])
                        if settings_show:
                            settings_slider_list[entry[3]].slide(event.pos)
                        else:
                            main_slider_list[entry[3]].slide(event.pos)
            if not textbox_clicked:
                if settings_show:
                    for textbox in settings_textbox_list:
                        textbox.active = False
                else:
                    for textbox in main_textbox_list:
                        textbox.active = False
            else:
                textbox_clicked = False
        if click_action[0] == "Slider" and event.type == MOUSEMOTION:
            if settings_show:
                settings_slider_list[click_action[1]].slide(event.pos)
                action_list.append(settings_slider_list[click_action[1]].action)
            else:
                main_slider_list[click_action[1]].slide(event.pos)
                action_list.append(main_slider_list[click_action[1]].action)
            display_changed = True
    if settings_show:
        for textbox in settings_textbox_list:
            if textbox.active:
                if textbox.text_object.update(events):
                    perform_action(textbox.action, settings_data)
                    if textbox.action == "reset":
                        starfield_changed = True
                    textbox.active = False
                display_changed = True
    else:
        for textbox in main_textbox_list:
            if textbox.active:
                if textbox.text_object.update(events):
                    perform_action("reset", settings_data)
                    starfield_changed = True
                    textbox.active = False
                display_changed = True

    if display_changed:
        for action in action_list:
            perform_action(action, settings_data)
        initialize_view(starfield_changed, settings_data)
        action_list = []
        display_changed = False
        starfield_changed = False
        draw_view()
    
    pygame.display.update()
    clock.tick(25)

