import pygame
from src.ui.display_element import DisplayElement
from src.common.constants import *


class InputElement(DisplayElement):

    def __init__(self, runtime, x, y, element_id):
        super(InputElement, self).__init__(runtime, x, y)
        self.rect = None
        self.element_id = element_id
        self.value = ''

    def mouse_over(self):
        mouse_position = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_position)

    def handle_input(self, input_value, input_type=INPUT_ADD):
        if input_type == INPUT_SET:
            self.value = input_value
        elif input_type == INPUT_ADD:
            self.value += input_value
        elif input_type == INPUT_BACKSPACE:
            self.value = self.value[:-1]
        elif input_type == INPUT_CLEAR:
            self.value = ''
