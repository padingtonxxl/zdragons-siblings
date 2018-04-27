class DisplayElement:

    def __init__(self, runtime, x, y):
        self.runtime = runtime
        self.rect = None
        self.x = x
        self.y = y

    def display(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        generic_display = True
