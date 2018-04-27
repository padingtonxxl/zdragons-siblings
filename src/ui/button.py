import pygame
from src.ui.inputelement import InputElement
from src.common.constants import *


class Button(InputElement):

    def __init__(self, runtime, element_id, text, x=None, y=None):
        super(self.__class__, self).__init__(runtime, x, y, element_id)
        self._runtime = runtime
        self.element_id = element_id
        self.x = x
        self.y = y
        self.text_object = self._runtime.config.button_font.render(text, True, self._runtime.config.button_font_color)
        self.width = self.text_object.get_width() + 10
        if self.width < int(self._runtime.config.values[CONFIG_BUTTON_WIDTH_MIN]):
            self.width = int(self._runtime.config.values[CONFIG_BUTTON_WIDTH_MIN])
        self.height = 35

    def display(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self._runtime.screen,
                         self._runtime.config.button_shadow_color,
                         (self.x - 8 + int(self._runtime.config.values[CONFIG_BUTTON_SHADOW_PADDING]),
                          self.y - 8 + int(self._runtime.config.values[CONFIG_BUTTON_SHADOW_PADDING]),
                          self.width + 16,
                          self.height + 16))
        pygame.draw.rect(self._runtime.screen,
                         self._runtime.config.button_background_color,
                         (self.x - 8, self.y - 8, self.width + 16, self.height + 16))
        if self.mouse_over():
            pygame.draw.rect(self._runtime.screen,
                             self._runtime.config.button_border_mouseover_color,
                             (self.x - 4, self.y - 4, self.width + 8, self.height + 8))
            pygame.draw.rect(self._runtime.screen,
                             self._runtime.config.button_background_mouseover_color,
                             (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self._runtime.screen,
                             self._runtime.config.button_border_color,
                             (self.x - 4, self.y - 4, self.width + 8, self.height + 8))
            pygame.draw.rect(self._runtime.screen,
                             self._runtime.config.button_background_color,
                             (self.x, self.y, self.width, self.height))
        self._runtime.screen.blit(
            self.text_object,
            (self.x + self.width/2 - self.text_object.get_width() / 2,
             self.y + self.height/2 - self.text_object.get_height()/2))
