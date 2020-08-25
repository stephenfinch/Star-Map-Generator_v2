import math, pygame
from pygame_textinput import TextInput

pygame.init()

class Label:
    def __init__(self, text = "", text_color = (0, 0, 0), background_color = (255, 255, 255), font_size = 25, pos = (0, 0)):
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont('Times New Roman', font_size)
        self.pos = pos
        self.background_color = background_color

    def draw(self, main_surface):
        text_surf = self.font.render(self.text, True, self.text_color, self.background_color)
        main_surface.blit(text_surf, self.pos)


class Button:
    def __init__(self, action = "", font_size = 32, bold_on_active = False,\
        display_text_color = (0, 0, 0), text = "",\
        text_active = "", border_size = 1,\
        border_color = (0, 0, 0), color = (255, 255, 255),\
        color_active = (255, 255, 255), area = ((0, 0), (0, 0))):
        self.action = action
        self.text = text
        self.font = pygame.font.SysFont('Times New Roman', font_size)
        self.bold_on_active = bold_on_active
        if text_active == "":
            self.text_active = self.text
        else:
            self.text_active = text_active
        self.border_size = border_size
        self.border_color = border_color
        self.color = color
        self.display_text_color = display_text_color
        self.color_active = color_active
        self.area = area
        self.active = False

    def draw(self, main_surface):
        pygame.draw.rect(main_surface, self.border_color, self.area)
        new_area = ((self.area[0][0] + self.border_size, self.area[0][1] + self.border_size),\
        (self.area[1][0] - (2*self.border_size), self.area[1][1] - (2*self.border_size)))
        if self.bold_on_active:
            self.font.set_bold(self.active)
        if self.active:
            pygame.draw.rect(main_surface, self.color_active, new_area)
            text_surf = self.font.render(self.text_active, True, self.display_text_color, self.color_active)
        else:
            pygame.draw.rect(main_surface, self.color, new_area)
            text_surf = self.font.render(self.text, True, self.display_text_color, self.color)
        new_area2 = (new_area[0][0] + (new_area[1][0] - text_surf.get_width()) // 2,\
        new_area[0][1] + (new_area[1][1] - text_surf.get_height()) // 2)
        main_surface.blit(text_surf, new_area2)



class Toggle(Button):
    def draw(self, main_surface):
        pass


class Slider:
    def __init__(self, action="", min_value=0, max_value=255, increment = 1, border_size = 1,\
        border_color = (0, 0, 0), background_color = (255, 255, 255),\
        area = ((0, 0), (0, 0)), slider_rail = ((0, 0), (0, 0)), rail_color = (50, 50, 50),\
        slider_size = (0, 0), slider_color = (0, 0, 0), is_vertical = False,\
        label_position = (0, 0), label_color = (255, 255, 255)):
        self.min_value = min_value
        self.max_value = max_value
        self.increment = increment
        self.action = action
        self.increment = increment
        self.border_size = border_size
        self.border_color = border_color
        self.background_color = background_color
        self.area = area
        self.slider_rail = slider_rail
        self.rail_color = rail_color
        self.slider_size = slider_size
        self.slider_color = slider_color
        self.is_vertical = is_vertical
        self.value = min_value
        '''
        if is_vertical:
            self.slide_area = (((slider_rail[0][0] + slider_rail[1][0] - slider_size[0]) / 2,slider_rail[0][1] - (slider_size[1]) / 2),\
                (slider_size[0],slider_size[1] + slider_rail[1][1])
                )
        else:
            self.slide_area = ((slider_rail[0][0] - (slider_size[0]) / 2,(slider_rail[0][1] + slider_rail[1][1] - slider_size[1]) / 2),\
                (slider_size[0] + slider_rail[1][0], slider_size[1])
                )
        '''
        self.slide_area = area
        self.label = Label(text = str(self.value), pos = label_position, background_color = self.background_color, text_color=label_color)

    def update(self, new_value):
        self.value = new_value
        self.label.text = str(new_value)

    def slide(self, mouse):
        if self.is_vertical:
            entry = 1
        else:
            entry = 0
        smin = self.slider_rail[0][entry]
        smax = smin + self.slider_rail[1][entry]
        pos = mouse[entry]
        if pos < smin:
            pos = smin
        if pos > smax:
            pos = smax
        p = (pos - smin) / (smax - smin)
        self.value = int(math.floor(self.min_value + p * (self.max_value - self.min_value)))
        self.label.text = str(self.value)

    def draw(self, main_surface):
        pygame.draw.rect(main_surface, self.border_color, self.area)
        new_area = ((self.area[0][0] + self.border_size, self.area[0][1] + self.border_size),\
        (self.area[1][0] - (2*self.border_size), self.area[1][1] - (2*self.border_size)))
        pygame.draw.rect(main_surface, self.background_color, new_area)
        pygame.draw.rect(main_surface, self.rail_color, self.slider_rail)
        p = (self.value - self.min_value) / (self.max_value - self.min_value)
        if self.is_vertical:
            pos = ((((self.slider_rail[0][0] + self.slider_rail[1][0]) / 2), self.slider_rail[0][1] - (self.slider_size[1] / 2) + (self.slider_rail[1][1] * p)), self.slider_size)
        else:
            pos = ((self.slider_rail[0][0] - (self.slider_size[0] / 2) + (self.slider_rail[1][0] * p), (self.slider_rail[0][1] + self.slider_rail[1][1]) / 2), self.slider_size)
        pygame.draw.rect(main_surface, self.slider_color, pos)
        self.label.draw(main_surface)



class Textbox:
    def __init__(self, max_length = -1, numbers_only = False, english_only = False, action = "",\
        display_text_color = (0, 0, 0), border_size = 1, border_color = (0, 0, 0),\
        color = (255, 255, 255), area = ((0, 0), (0, 0)), spacing = 0):
        self.text_object = TextInput(text_color=display_text_color, max_string_length=max_length, font_size=22)
        self.max_length = max_length
        self.action = action
        self.numbers_only = numbers_only
        self.english_only = english_only
        self.border_size = border_size
        self.border_color = border_color
        self.color = color
        self.display_text_color = display_text_color
        self.area = area
        self.spacing = spacing
        self.active = False

    def update(self, events):
        is_enter_pressed = self.text_object.update(events)
        if self.english_only:
            pass
        if self.numbers_only:
            pass
        return is_enter_pressed

    def draw(self, main_surface):
        pygame.draw.rect(main_surface, self.border_color, self.area)
        new_area = ((self.area[0][0] + self.border_size, self.area[0][1] + self.border_size),\
        (self.area[1][0] - (2*self.border_size), self.area[1][1] - (2*self.border_size)))
        pygame.draw.rect(main_surface, self.color, new_area)
        text_surf = self.text_object.get_surface()
        new_spot = (new_area[0][0] + self.spacing, new_area[0][1] + ((new_area[1][1] - text_surf.get_height()) / 2))
        main_surface.blit(text_surf, new_spot)

class Colorbox:
    def __init__(self, border_size = 1, border_color = (0, 0, 0), color = (255, 255, 255), area = ((0, 0), (0, 0))):
        self.border_size = border_size
        self.border_color = border_color
        self.color = color
        self.area = area