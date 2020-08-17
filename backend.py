from draw import make_stars

def perform_action(action, settings):
    if action == "reset":
        make_stars(settings)