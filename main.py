from wordfactory import *
from storage import *
from ui import *
from backgroundtask import *
from TimeCalculator import *

storage = Storage()
storage.set_words(Factory.get_word_dictionary())
time_calculator = TimeCalculator(storage)

ui = UI(storage)
redraw_task = BackgroundTask(30, ui.redraw)
calculate_time_task = BackgroundTask(1, time_calculator.set_visibility_of_all_words)
ui.start_ui()
