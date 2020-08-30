import pygame
from draw import make_stars, swap_settings, query_input, get_input_object, star_map, STARFIELDSURF
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.overrideredirect(True)
root.geometry('0x0+0+0')

def perform_action(action, settings):
    if action == "reset" or action == "textString":
        perform_action("rewrite", settings)
        make_stars(settings)
    elif action == "settings":
        swap_settings()
    elif action == "R" or action == "G" or action == "B":
        color_r = query_input("R")
        color_g = query_input("G")
        color_b = query_input("B")
        get_input_object("colorbox").color = (color_r, color_g, color_b)
        get_input_object("colorbox").color_active = (color_r, color_g, color_b)
    elif action == "starcolor":
        settings.star_color = get_input_object("colorbox").color
        get_input_object("starcolor").color = get_input_object("colorbox").color
        get_input_object("starcolor").color_active = get_input_object("colorbox").color
    elif action == "backgroundcolor":
        settings.back_color = get_input_object("colorbox").color
        get_input_object("backgroundcolor").color = get_input_object("colorbox").color
        get_input_object("backgroundcolor").color_active = get_input_object("colorbox").color
    elif action == "starcount":
        temp_num, temp_text = query_input("starcount"), ''
        for char in temp_num:
            if char.isdigit():
                temp_text += char
        if temp_text:
            settings.number_of_stars = int(temp_text)
        else:
            settings.number_of_stars = 0
            temp_text = "0"
        change_textbox("starcount", temp_text.strip())
    elif action == "showgrid":
        settings.show_grid = not settings.show_grid
        if settings.show_grid:
            get_input_object("showgrid").display_text_color = (0, 0, 0)
        else:
            get_input_object("showgrid").display_text_color = (63, 63, 63)
    elif action == "showconstellations":
        settings.show_constellations = not settings.show_constellations
        if settings.show_constellations:
            get_input_object("showconstellations").display_text_color = (0, 0, 0)
        else:
            get_input_object("showconstellations").display_text_color = (63, 63, 63)
    elif action == "textSizeUp":
        settings.text_size = min((settings.text_size + 5), settings.max_constellation_size)
        perform_action("rewrite", settings)
    elif action == "textSizeDown":
        settings.text_size = max((settings.text_size - 5), settings.min_constellation_size)
        perform_action("rewrite", settings)
    elif action == "rewrite":
        temp_string = query_input("textString")
        temp_text = ""
        for char in temp_string:
            if char.isalpha() or char == " ":
                temp_text += char
        settings.text_input = temp_text.strip()
        change_textbox("textString", temp_text.strip())
        perform_action("starcount", settings)
        perform_action("textPosX", settings)
    elif action == "textPosX" or action == "textPosY":
        strX = ""
        posX = query_input("textPosX")
        for char in posX:
            if char.isdigit() or char == "-":
                strX += char
        if not strX:
            strX = "0"
        change_textbox("textPosX", str(int(strX)))
        if abs(int(strX)) > 100:
            if int(strX) < 0:
                strX = "-100"
            else:
                strX = "100"
        change_textbox("textPosX", str(int(strX)))
        strY = ""
        posY = query_input("textPosY")
        for char in posY:
            if char.isdigit() or char == "-":
                strY += char
        if not strY:
            strY = "0"
        change_textbox("textPosY", str(int(strY)))
        if abs(int(strY)) > 100:
            if int(strY) < 0:
                strY = "-100"
            else:
                strY = "100"
        change_textbox("textPosY", str(int(strY)))
        settings.text_location = star_map.coerce_to_center(int(strX),int(strY))
    elif action == "savefile":
        save_file()
    elif action == "constellation_density":
        settings.constellation_density = query_input("constellation_density")

def change_textbox(textbox, string):
    textbox = get_input_object(textbox)
    textbox.text_object.input_string = string
    textbox.text_object.cursor_position = len(string)
    textbox.text_object.update([])

def save_file():
    #pygame.display.iconify()
    '''
    pygame.display.set_mode((0,0), pygame.NOFRAME, 32) 
    pygame.display.update()
    root.deiconify()
    root.lift()
    root.focus_force()
    '''
    file_path = filedialog.asksaveasfilename(parent=root,title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    '''
    field_x, field_y = 650, 650
    options_width = 200
    field_buffer = 50
    field_inner_buffer = 5
    screen_x, screen_y = field_x + options_width + 2 * field_buffer, field_y + 2 * field_buffer
    DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y), 0, 32)
    pygame.display.update()
    '''
    if file_path:
        pygame.image.save(STARFIELDSURF, file_path + ".jpg")


