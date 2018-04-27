from src.ui.button import Button
from src.common.constants import *
import pygame


class PopUp:

    def __init__(self, runtime, text, buttons, width, height):
        self._runtime = runtime
        self.shadow_padding = int(self._runtime.config.values[CONFIG_POPUP_SHADOW_PADDING])
        self.background_color = (
            int(self._runtime.config.values[CONFIG_POPUP_BACKGROUND_COLOR_R]),
            int(self._runtime.config.values[CONFIG_POPUP_BACKGROUND_COLOR_G]),
            int(self._runtime.config.values[CONFIG_POPUP_BACKGROUND_COLOR_B])
        )
        self.border_color = (
            int(self._runtime.config.values[CONFIG_POPUP_BORDER_COLOR_R]),
            int(self._runtime.config.values[CONFIG_POPUP_BORDER_COLOR_G]),
            int(self._runtime.config.values[CONFIG_POPUP_BORDER_COLOR_B])
        )
        self.shadow_color = (
            int(self._runtime.config.values[CONFIG_POPUP_SHADOW_COLOR_R]),
            int(self._runtime.config.values[CONFIG_POPUP_SHADOW_COLOR_G]),
            int(self._runtime.config.values[CONFIG_POPUP_SHADOW_COLOR_B])
        )
        self.text_object = self._runtime.config.popup_font.render(text, False, self._runtime.config.popup_font_color)
        self.width = width
        self.height = height
        self.center_x = self._runtime.width / 2
        self.center_y = self._runtime.height / 2
        self.x = int(self.center_x-self.width/2)
        self.y = int(self.center_y-self.height/2)
        self.buttons = list()
        self.button_width_total = -(int(self._runtime.config.values[CONFIG_BUTTON_PADDING]))
        self.button_count = 0
        if buttons is not None:
            for button_data in buttons:
                button = Button(self._runtime, button_data[0], button_data[1])
                self.buttons.append(button)
                self.button_width_total += button.width + int(self._runtime.config.values[CONFIG_BUTTON_PADDING])
                self.button_count += 1

    def display(self):
        while True:
            pygame.draw.rect(self._runtime.screen,
                             self.shadow_color,
                             (self.x - 8 + self.shadow_padding, self.y - 8 + self.shadow_padding, self.width + 16, self.height + 16))
            pygame.draw.rect(self._runtime.screen,
                             self.background_color,
                             (self.x-8, self.y-8, self.width+16, self.height+16))
            pygame.draw.rect(self._runtime.screen,
                             self.border_color,
                             (self.x-4, self.y-4, self.width+8, self.height+8))
            pygame.draw.rect(self._runtime.screen,
                             self.background_color,
                             (self.x, self.y, self.width, self.height))
            self._runtime.screen.blit(self.text_object, (self.center_x-self.text_object.get_width()/2, self.y+25))
            x = self.center_x - (self.button_width_total/2)
            for button in self.buttons:
                y = self.y + self.height - button.height - int(self._runtime.config.values[CONFIG_BUTTON_PADDING])
                button.display(x, y)
                x += button.width + int(self._runtime.config.values[CONFIG_BUTTON_PADDING])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.mouse_over():
                            return button.element_id
