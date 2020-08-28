from draw import make_stars, swap_settings, query_input, get_input_object, star_map

def perform_action(action, settings):
    if action == "reset":
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
    elif action == "showconstellations":
        settings.show_constellations = not settings.show_constellations
    elif action == "textSizeUp":
        if settings.text_size < 100:
            settings.text_size += 5
        perform_action("rewrite", settings)
    elif action == "textSizeDown":
        if settings.text_size > 20:
            settings.text_size -= 5
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
            change_textbox("textPosX", strX)
        if abs(int(strX)) > 999:
            if int(strX) < 0:
                strX = "-999"
            else:
                strX = "999"
            change_textbox("textPosX", strX)
        strY = ""
        posY = query_input("textPosY")
        for char in posY:
            if char.isdigit() or char == "-":
                strY += char
        if not strY:
            strY = "0"
            change_textbox("textPosY", strY)
        if abs(int(strY)) > 999:
            if int(strY) < 0:
                strY = "-999"
            else:
                strY = "999"
            change_textbox("textPosY", strY)
        settings.text_location = star_map.coerce_to_center(int(strX),int(strY))
    
def change_textbox(textbox, string):
    textbox = get_input_object(textbox)
    textbox.text_object.input_string = string
    textbox.text_object.cursor_position = len(string)
    textbox.text_object.update([])