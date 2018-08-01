from tkinter import *
from Utility import *
from ColorCalculation import *


class UI:
    firstTime = False
    listOfWordsOnCanvas = []

    def __init__(self, storage):
        self.is_ready = False
        self.storage = storage
        self.window = Tk()
        frame = Frame(self.window)
        self.sliders = SliderContainer(frame, self.slider_callback)
        self.radioButtons = RadioButtonsContainer(frame, self.radioButton_callback)
        frame.grid(row=0, column=0, sticky=N)

        self.canvas = Canvas(self.window,
                             width=750,
                             height=500)

        self.canvas.grid(row=0, column=1)

    def slider_callback(self, value):
        self.storage.set_colour(self.sliders.get_colours())

    def radioButton_callback(self):
        self.storage.set_mode(self.radioButtons.get_selected_button())

    def start_ui(self):
        self.is_ready = True
        self.window.mainloop()

    def redraw(self):
        if self.is_ready:
            font_color = self.calculate_color_of_words()
            if not self.firstTime:
                self.firstTime = True
                self.draw_words_on_canvas(font_color)
            else:
                self.reconfigure_words_on_canvas(font_color)

    def calculate_color_of_words(self):

        red, green, blue = self.storage.colour
        red, green, blue = ColorCalculator.calculateColor(self.storage.mode, red, green, blue)
        font_color = "#" + Utility.decimalToHex(red) + Utility.decimalToHex(green) + Utility.decimalToHex(blue)
        return font_color

    def draw_words_on_canvas(self, font_color):
        for key, word in self.storage.words.items():
            size = 40
            text = self.canvas.create_text(50 + word.x_pos * (size * 0.75), word.y_pos * (size * 1.2),
                                           text=word.text, anchor=NW,
                                           fill=font_color,
                                           tag="word", font=("comic sans ms", str(size)))
            self.listOfWordsOnCanvas.append(text)

    def reconfigure_words_on_canvas(self, font_color):
        for word in self.listOfWordsOnCanvas:
            self.canvas.itemconfigure(word, fill=font_color, )

    @staticmethod
    def create_label(master, text, x, y):
        Label(master, text=text).grid(row=y, column=x, sticky='N')


class SliderContainer:

    def __init__(self, master, listener):
        self.red_slider = self.create_slider(master, 1, 0, listener)
        self.green_slider = self.create_slider(master, 1, 1, listener)
        self.blue_slider = self.create_slider(master, 1, 2, listener)

        UI.create_label(master, "Rot: ", 0, getAndIncrementY())
        UI.create_label(master, "Grün: ", 0, getAndIncrementY())
        UI.create_label(master, "Blau: ", 0, getAndIncrementY())

    @staticmethod
    def create_slider(master, x, y, listener):
        slider = Scale(master, command=listener, orient=HORIZONTAL, tickinterval=50, length=200, to=255)
        slider.grid(row=y, column=x, sticky=N)
        return slider

    def get_colours(self):
        return self.red_slider.get(), self.green_slider.get(), self.blue_slider.get()


class RadioButtonsContainer:
    STATIC = 1
    BREATHING = 2

    def __init__(self, master, listener):
        self.selectedButton = IntVar(master=master, value=RadioButtonsContainer.STATIC)
        UI.create_label(master, "Darstellung:", 0, getAndIncrementY())
        self.staticButton = RadioButtonsContainer.createRadioButton(master, "Statisch", 0, getAndIncrementY(),
                                                                    self.selectedButton,
                                                                    self.STATIC, listener)
        self.breathingButton = RadioButtonsContainer.createRadioButton(master, "Atmung", 0, getAndIncrementY(),
                                                                       self.selectedButton, self.BREATHING, listener)

    def get_selected_button(self):
        return self.selectedButton.get()

    @staticmethod
    def createRadioButton(master, text, x, y, valueHolder, value, listener):
        radio = Radiobutton(master, text=text, variable=valueHolder, value=value, command=listener)
        radio.grid(column=x, row=y, sticky=N)
        return radio


y = -1


def getAndIncrementY():
    global y
    y = y + 1
    return y
