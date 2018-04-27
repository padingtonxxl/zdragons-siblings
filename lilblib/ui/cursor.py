from lilblib.ui.display_element import DisplayElement
from lilblib.common.constants import *
from datetime import datetime


class Cursor(DisplayElement):

    def __init__(self, runtime, font, x, y, display_duration = 500, pause_duration = 300):
        super(Cursor, self).__init__(runtime, x, y)
        self.font = font
        self._cursor_text_object = None
        self._display_duration = display_duration
        self._pause_duration = pause_duration
        self._last_switch = datetime.now()
        self.mode = CURSOR_OFF
        self._switch()

    def update(self):
        time_since_last_switch = datetime.now() - self._last_switch
        if self.mode == CURSOR_ON:
            switch_time = self._display_duration
        else:
            switch_time = self._pause_duration
        if time_since_last_switch.microseconds/1000 >= switch_time:
            self._switch()
            return True

    def display(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        self.runtime.screen.blit(self._cursor_text_object, (self.x, self.y))

    def _switch(self):
        if self.mode == CURSOR_ON:
            self.mode = CURSOR_OFF
        else:
            self.mode = CURSOR_ON
        self._cursor_text_object = self.font.render(self.mode, False, self.runtime.config.form_font_color)
        self._last_switch = datetime.now()

