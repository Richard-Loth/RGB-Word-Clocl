NUMBER_ONE = "h_1"
NUMBER_TWO = "h_2"
NUMBER_THREE = "h_3"
NUMBER_FOUR = "h_4"
NUMBER_FIVE = "h_5"
NUMBER_SIX = "h_6"
NUMBER_SEVEN = "h_7"
NUMBER_EIGHT = "h_8"
NUMBER_NINE = "h_9"
NUMBER_TEN = "h_10"
NUMBER_ELEVEN = "h_11"
NUMBER_TWELVE = "h_12"

DESCRIPTOR_AFTER = "de_after"
DESCRIPTOR_BEFORE = "de_before"
DESCRIPTOR_HALF = "de_half"

DISTANCE_FIVE = "di_five"
DISTANCE_TEN = "di_ten"
DISTANCE_QUARTER = "di_quarter"
DISTANCE_TWENTY = "di_twenty"

MINUTE_ONE = "min_one"
MINUTE_TWO = "min_two"
MINUTE_THREE = "min_three"
MINUTE_FOUR = "min_four"

class TimeConstants:

    @staticmethod
    def get_hour_constants(hour):
        return "h_" + str(hour)
