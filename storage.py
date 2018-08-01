class Storage:
    def __init__(self):
        self.words = {}
        self.colour = 0, 0, 0
        self.mode = 1

    def set_words(self, words):
        self.words = words

    def set_colour(self, colour):
        self.colour = colour

    def set_mode(self, mode):
        self.mode = mode


class Singleword:
    def __init__(self, text, x_pos, y_pos, column_width):
        self.is_active = False
        self.colour = 0, 0, 0
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.column_width = column_width
