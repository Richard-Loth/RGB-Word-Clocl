import datetime
from time_constants import *


class TimeCalculator:

    def __init__(self, storage):
        self.storage = storage
        self.minute_to_expression = {}
        self._fill_minute_to_expression_dic()

    def _fill_minute_to_expression_dic(self):
        time_expressions = TimeExpressions()
        for i in range(0, 4):
            self.minute_to_expression[i] = time_expressions.simple_hour_expression
        for i in range(5, 14):
            self.minute_to_expression[i] = time_expressions.simple_after_hour_expression
        for i in range(15, 19):
            pass
        for i in range(20, 24):
            self.minute_to_expression[i] = time_expressions.simple_after_hour_expression
        for i in range(25, 29):
            pass
        for i in range(30, 34):
            pass
        for i in range(35, 39):
            pass
        for i in range(40, 44):
            pass
        for i in range(45, 49):
            pass
        for i in range(50, 54):
            pass
        for i in range(55, 59):
            pass

    def set_visibility_of_all_words(self):
        self.turn_off_all_words()
        now = datetime.datetime.now()
        expression_mode = self.minute_to_expression[now.minute]
        for word_identifier in expression_mode(now):
            self.storage.words[word_identifier].is_active = True

    def turn_off_all_words(self):
        for key, word in self.storage.words.items():
            word.is_active = False


class TimeExpressions:

    def __init__(self):
        self.minute_to_distance = {}
        self.fill_minute_to_distance_dic()

    def fill_minute_to_distance_dic(self):
        for i in range(5, 9):
            self.minute_to_distance[i] = DISTANCE_FIVE
        for i in range(10, 14):
            self.minute_to_distance[i] = DISTANCE_TEN
        for i in range(20, 24):
            self.minute_to_distance[i] = DISTANCE_TWENTY

    def simple_hour_expression(self, now):
        return TimeConstants.get_hour_constants(now.hour % 12)

    def simple_after_hour_expression(self, now):
        hour_identifier = TimeConstants.get_hour_constants(now.hour % 12)
        distance_identifier = self.minute_to_distance[now.minute]
        return distance_identifier, DESCRIPTOR_AFTER, hour_identifier
