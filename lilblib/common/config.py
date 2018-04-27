from lilblib.common.constants import *
import pygame


class Config:

    def __init__(self, db_connection):
        self.values = dict()
        self._db_connection = db_connection
        with self._db_connection.cursor() as cursor:
            sql = "SELECT * FROM parameters where `area` = %s"
            cursor.execute(sql, (AREA_CONFIG,))
            for result in cursor.fetchall():
                self.values[result['parameter']] = result['value']
        self.salt = 'nnks#flkjsfw htru423awd8ksjfkljhgtt9rgfsdasd128lkfgm'

        self.form_font = pygame.font.SysFont(self.values[CONFIG_FONT_FORM], int(self.values[CONFIG_FONT_FORM_SIZE]))
        self.form_font_color = (int(self.values[CONFIG_FONT_FORM_COLOR_R]),
                                 int(self.values[CONFIG_FONT_FORM_COLOR_G]),
                                 int(self.values[CONFIG_FONT_FORM_COLOR_B]))

        self.popup_font = pygame.font.SysFont(self.values[CONFIG_FONT_POPUP], int(self.values[CONFIG_FONT_POPUP_SIZE]))
        self.popup_font_color = (int(self.values[CONFIG_FONT_POPUP_COLOR_R]),
                                 int(self.values[CONFIG_FONT_POPUP_COLOR_G]),
                                 int(self.values[CONFIG_FONT_POPUP_COLOR_B]))
        self.button_font = pygame.font.SysFont(self.values[CONFIG_FONT_BUTTON],
                                               int(self.values[CONFIG_FONT_BUTTON_SIZE]))
        self.button_font_color = (int(self.values[CONFIG_FONT_BUTTON_COLOR_R]),
                                  int(self.values[CONFIG_FONT_BUTTON_COLOR_G]),
                                  int(self.values[CONFIG_FONT_BUTTON_COLOR_B]))
        self.button_width_min = int(self.values[CONFIG_BUTTON_WIDTH_MIN])
        self.button_shadow_padding = int(self.values[CONFIG_BUTTON_SHADOW_PADDING])
        self.button_background_color = (
            int(self.values[CONFIG_BUTTON_BACKGROUND_COLOR_R]),
            int(self.values[CONFIG_BUTTON_BACKGROUND_COLOR_G]),
            int(self.values[CONFIG_BUTTON_BACKGROUND_COLOR_B])
        )
        self.button_border_color = (
            int(self.values[CONFIG_BUTTON_BORDER_COLOR_R]),
            int(self.values[CONFIG_BUTTON_BORDER_COLOR_G]),
            int(self.values[CONFIG_BUTTON_BORDER_COLOR_B])
        )
        self.button_background_mouseover_color = (
            int(self.values[CONFIG_BUTTON_MOUSEOVER_BACKGROUND_COLOR_R]),
            int(self.values[CONFIG_BUTTON_MOUSEOVER_BACKGROUND_COLOR_G]),
            int(self.values[CONFIG_BUTTON_MOUSEOVER_BACKGROUND_COLOR_B])
        )
        self.button_border_mouseover_color = (
            int(self.values[CONFIG_BUTTON_MOUSEOVER_BORDER_COLOR_R]),
            int(self.values[CONFIG_BUTTON_MOUSEOVER_BORDER_COLOR_G]),
            int(self.values[CONFIG_BUTTON_MOUSEOVER_BORDER_COLOR_B])
        )
        self.button_shadow_color = (
            int(self.values[CONFIG_BUTTON_SHADOW_COLOR_R]),
            int(self.values[CONFIG_BUTTON_SHADOW_COLOR_G]),
            int(self.values[CONFIG_BUTTON_SHADOW_COLOR_B])
        )

        self.title_font = pygame.font.SysFont(self.values[CONFIG_FONT_POPUP], int(self.values[CONFIG_FONT_TITLE_SIZE]))
        self.title_font_color = (int(self.values[CONFIG_FONT_TITLE_COLOR_R]),
                                 int(self.values[CONFIG_FONT_TITLE_COLOR_G]),
                                 int(self.values[CONFIG_FONT_TITLE_COLOR_B]))

