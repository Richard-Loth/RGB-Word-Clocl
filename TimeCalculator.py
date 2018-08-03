import datetime
from time_constants import *


class TimeCalculator:

    def __init__(self, storage):
        self.storage = storage
        self.minute_to_expression = {}
        self._fill_minute_to_expression_dictionary()

    def _fill_minute_to_expression_dictionary(self):
        time_expressions = TimeExpressions()
        for i in range(0, 4):
            self.minute_to_expression[i] = time_expressions.simple_hour_expression
        for i in range(5, 14):
            self.minute_to_expression[i] = time_expressions.simple_after_hour_expression
        for i in range(15, 19):
            self.minute_to_expression[i] = time_expressions.quarter_hour_expression
        for i in range(20, 24):
            self.minute_to_expression[i] = time_expressions.simple_after_hour_expression
        for i in range(25, 29):
            self.minute_to_expression[i] = time_expressions.five_before_half_expression
        for i in range(30, 34):
            self.minute_to_expression[i] = time_expressions.half_hour_expression
        for i in range(35, 39):
            self.minute_to_expression[i] = time_expressions.after_half_hour_expression
        for i in range(40, 44):
            self.minute_to_expression[i] = time_expressions.after_half_hour_expression
        for i in range(45, 49):
            self.minute_to_expression[i] = time_expressions.quarter_before_expression
        for i in range(50, 54):
            self.minute_to_expression[i] = time_expressions.before_hour_expression
        for i in range(55, 59):
            self.minute_to_expression[i] = time_expressions.before_hour_expression

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
        for i in range(35, 39):
            self.minute_to_distance[i] = DISTANCE_FIVE
        for i in range(40, 44):
            self.minute_to_distance[i] = DISTANCE_TEN
        for i in range(50, 54):
            self.minute_to_distance[i] = DISTANCE_TEN
        for i in range(55, 59):
            self.minute_to_distance[i] = DISTANCE_FIVE

    def simple_hour_expression(self, now):
        return TimeConstants.get_hour_constants(now.hour % 12)

    def simple_after_hour_expression(self, now):
        hour_identifier = TimeConstants.get_hour_constants(now.hour % 12)
        distance_identifier = self.minute_to_distance[now.minute]
        return distance_identifier, DESCRIPTOR_AFTER, hour_identifier

    def quarter_hour_expression(self, now):
        hour_identifier = TimeConstants.get_hour_constants((now.hour + 1) % 12)
        return DISTANCE_QUARTER, hour_identifier

    def five_before_half_expression(self, now):
        hour_identifier = TimeConstants.get_hour_constants((now.hour + 1) % 12)
        return DISTANCE_FIVE, DESCRIPTOR_BEFORE, DESCRIPTOR_HALF, hour_identifier

    def half_hour_expression(self, now):
        hour_identifier = TimeConstants.get_hour_constants((now.hour + 1) % 12)
        return DESCRIPTOR_HALF, hour_identifier

    def after_half_hour_expression(self, now):
        hour_identifier = TimeConstants.get_hour_constants((now.hour + 1) % 12)
        distance_identifier = self.minute_to_distance[now.minute]
        return distance_identifier, DESCRIPTOR_AFTER, DESCRIPTOR_HALF, hour_identifier

    def quarter_before_expression(self, now):
        hour_identifier = TimeConstants.get_hour_constants((now.hour + 1) % 12)
        return DISTANCE_QUARTER, DESCRIPTOR_BEFORE, hour_identifier

    def before_hour_expression(self, now):
        hour_identifier = TimeConstants.get_hour_constants((now.hour + 1) % 12)
        distance_identifier = self.minute_to_distance[now.minute]
        return distance_identifier, DESCRIPTOR_BEFORE, hour_identifier
