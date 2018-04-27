from src.ui.button import Button
from src.common.constants import *
import pygame


class Window:

    def __init__(self, runtime, title, width, height, column_count=1, padding=25):
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
        self.title_object = self._runtime.config.title_font.render(title, False, self._runtime.config.title_font_color)
        self.width = width
        self.height = height
        self.center_x = self._runtime.width / 2
        self.center_y = self._runtime.height / 2
        self.x = int(self.center_x-self.width/2)
        self.y = int(self.center_y-self.height/2)
        self.padding = padding
        self.column_count = column_count
        self.column_xs = dict()
        self.column_width = self.width / self.column_count
        for column_number in range(self.column_count):
            x_left = self.x + (self.width/self.column_count)*column_number
            self.column_xs[column_number] = {
                LEFT: x_left,
                CENTER: x_left + self.column_width/2,
                RIGHT: x_left + self.column_width
            }
        self.display_elements = list()
        # self.buttons = list()
        # self.button_width_total = -(int(self._runtime.config.values[CONFIG_BUTTON_PADDING]))
        # self.button_count = 0
        # for button_data in buttons:
        #     button = Button(self._runtime, button_data[0], button_data[1])
        #     self.buttons.append(button)
        #     self.button_width_total += button.width + int(self._runtime.config.values[CONFIG_BUTTON_PADDING])
        #     self.button_count += 1

    def add_display_element(self, display_element, alignment=CENTER, offset_x=0, offset_y=0):
        self.display_elements.append((display_element, alignment, offset_x, offset_y))

    def display(self):
        pygame.draw.rect(self._runtime.screen,
                         self.shadow_color,
                         (self.x - 8 + self.shadow_padding,
                          self.y - 8 + self.shadow_padding,
                          self.width + 16,
                          self.height + 16))
        pygame.draw.rect(self._runtime.screen,
                         self.background_color,
                         (self.x-8, self.y-8, self.width+16, self.height+16))
        pygame.draw.rect(self._runtime.screen,
                         self.border_color,
                         (self.x-4, self.y-4, self.width+8, self.height+8))
        pygame.draw.rect(self._runtime.screen,
                         self.background_color,
                         (self.x, self.y, self.width, self.height))
        self._runtime.screen.blit(self.title_object,
                                  (self.center_x-self.title_object.get_width()/2, self.y+self.padding))
        current_column = 0
        y = self.title_object.get_height() + self.y + 2*self.padding
        highest_per_column = 0
        for display_element in self.display_elements:
            column_xs = self.column_xs[current_column]
            if display_element[0].width > highest_per_column:
                highest_per_column = display_element[0].height
            x = column_xs[display_element[1]]
            if display_element[1] == LEFT:
                x = column_xs[display_element[1]]
            elif display_element[1] == CENTER:
                x -= display_element[0].width/2
            elif display_element[1] == RIGHT:
                x -= display_element(0).width
            display_element[0].display(x, y)
            if current_column == self.column_count-1:
                current_column = 0
                y += highest_per_column + self.padding
                highest_per_column = 0
            else:
                current_column += 1


        pygame.display.flip()
        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         for button in self.buttons:
        #             if button.mouse_over():
        #                 return button.element_id
