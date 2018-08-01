from storage import *
from time_constants import *


class Factory:
    @staticmethod
    def get_word_dictionary():
        word_list = {}
        word_list.update(Factory._get_distances())
        word_list.update(Factory._get_descriptors())
        word_list.update(Factory._get_numbers())
        return word_list

    @staticmethod
    def _get_distances():
        distances = {}
        distances[DISTANCE_FIVE] = Singleword("fünf", 0, 0, 4)
        distances[DISTANCE_TEN] = Singleword("zehn", 4, 0, 4)
        distances[DISTANCE_QUARTER] = Singleword("viertel", 0, 1, 6)
        distances[DISTANCE_TWENTY] = Singleword("zwanzig", 8, 0, 7)
        return distances

    @staticmethod
    def _get_descriptors():
        descriptors = {}
        descriptors[DESCRIPTOR_AFTER] = Singleword("nach", 7, 1, 4)
        descriptors[DESCRIPTOR_BEFORE] = Singleword("vor", 11, 1, 3)
        descriptors[DESCRIPTOR_HALF] = Singleword("halb", 14, 1, 4)
        return descriptors

    @staticmethod
    def _get_numbers():
        numbers = {}
        numbers[NUMBER_ONE] = Singleword("eins", 0, 2, 4)
        numbers[NUMBER_TWO] = Singleword("zwei", 4, 2, 4)
        numbers[NUMBER_THREE] = Singleword("drei", 8, 2, 4)
        numbers[NUMBER_FOUR] = Singleword("vier", 12, 2, 4)
        numbers[NUMBER_FIVE] = Singleword("fünf", 0, 3, 4)
        numbers[NUMBER_SIX] = Singleword("sechs", 4, 3, 5)
        numbers[NUMBER_SEVEN] = Singleword("sieben", 9, 3, 6)
        numbers[NUMBER_EIGHT] = Singleword("acht", 15, 3, 4)
        numbers[NUMBER_NINE] = Singleword("neun", 0, 4, 4)
        numbers[NUMBER_TEN] = Singleword("zehn", 4, 4, 4)
        numbers[NUMBER_ELEVEN] = Singleword("elf", 8, 4, 3)
        numbers[NUMBER_TWELVE] = Singleword("zwölf", 11, 4, 5)
        return numbers
