from draw import make_stars, swap_settings, query_input

def perform_action(action, settings):
    if action == "reset":
        settings.text_input = query_input("textString")
        make_stars(settings)
    if action == "settings":
        swap_settings()