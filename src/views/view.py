class View:

    def __init__(self, screen_controller):
        self._screen_controller = screen_controller

    def display(self):
        self._screen_controller.runtime.screen.fill((63, 72, 204))
