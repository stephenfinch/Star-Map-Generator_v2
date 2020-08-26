from draw import make_stars, swap_settings, query_input, get_input_object

def perform_action(action, settings):
    if action == "reset":
        textbox = get_input_object("textString")
        temp_string = query_input("textString")
        temp_text = ""
        for char in temp_string:
            if char.isalpha() or char == " ":
                temp_text += char
        settings.text_input = temp_text.strip()
        textbox.text_object.input_string = temp_text.strip()
        textbox.text_object.cursor_position = len(temp_text.strip())
        textbox.text_object.update([])
        perform_action("starcount", settings)
        make_stars(settings)
    if action == "settings":
        swap_settings()
    if action == "R" or action == "G" or action == "B":
        color_r = query_input("R")
        color_g = query_input("G")
        color_b = query_input("B")
        get_input_object("colorbox").color = (color_r, color_g, color_b)
        get_input_object("colorbox").color_active = (color_r, color_g, color_b)
    if action == "starcolor":
        settings.star_color = get_input_object("colorbox").color
        get_input_object("starcolor").color = get_input_object("colorbox").color
        get_input_object("starcolor").color_active = get_input_object("colorbox").color
    if action == "backgroundcolor":
        settings.back_color = get_input_object("colorbox").color
        get_input_object("backgroundcolor").color = get_input_object("colorbox").color
        get_input_object("backgroundcolor").color_active = get_input_object("colorbox").color
    if action == "starcount":
        temp_num, temp_text = query_input("starcount"), ''
        for char in temp_num:
            if char.isdigit():
                temp_text += char
        if temp_text:
            settings.number_of_stars = int(temp_text)
        textbox = get_input_object("starcount")
        textbox.text_object.input_string = temp_text
        textbox.text_object.cursor_position = len(temp_text.strip())
        textbox.text_object.update([])
        