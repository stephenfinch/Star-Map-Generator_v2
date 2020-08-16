import math, pygame

pygame.init()

class Button:
    def __init__(self, name = "", font_size = 32, bold_on_active = False,\
        display_text_color = (0, 0, 0), text = "",\
        text_active = "", border_size = 1,\
        border_color = (0, 0, 0), color = (255, 255, 255),\
        color_active = (255, 255, 255), area = ((0, 0), (0, 0)),\
        size = (0, 0)):
        self.name = name
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
        self.size = size
        self.active = False

    def draw(self, main_surface):
        pygame.draw.rect(main_surface, self.border_color, ((0, 0) ,self.size))
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
        main_surface.blit(text_surf, (int(math.ceil((new_area[0][0] + new_area[1][0] - text_surf.get_width()) / 2)),\
        int(math.ceil((new_area[0][1] + new_area[1][1] - text_surf.get_height()) / 2))))