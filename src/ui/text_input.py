from src.ui.inputelement import InputElement
from src.ui.cursor import Cursor


class TextInput(InputElement):

    def __init__(self, runtime, x, y, element_id, label):
        super(self.__class__, self).__init__(runtime, x, y, element_id)
        self._cursor = Cursor(self.runtime, self.runtime.config.form_font, self.x+5, self.y+2)
        self._label = self.runtime.config.form_font.render(label, False, self.runtime.config.form_font_color)

    def update(self):
        return self._cursor.update()

    def display(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        self.runtime.screen.blit(self._label, (self.x, self.y))
        self._cursor.display(self.x+self._label.get_width()+5, self.y)
