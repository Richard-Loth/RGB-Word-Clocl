import time


class ColorCalculator:
    BREATHFREQUENCY = 1200
    BACKGROUND = 240, 240, 240

    @staticmethod
    def calculateColor(mode, red, green, blue):
        if mode == 1:
            return red, green, blue
        elif mode == 2:
            return ColorCalculator._calculateBreathing(red, green, blue)

    @staticmethod
    def _calculateBreathing(red, green, blue):
        current_time_ms = (time.time() * 1000)
        current_value = current_time_ms % ColorCalculator.BREATHFREQUENCY
        factor = current_value / ColorCalculator.BREATHFREQUENCY
        factor = ColorCalculator._inverseFactorIfOddRound(factor, current_time_ms)

        new_red = ColorCalculator._calc_new_color(red, ColorCalculator.BACKGROUND[0], factor)
        new_green = ColorCalculator._calc_new_color(green, ColorCalculator.BACKGROUND[1], factor)
        new_blue = ColorCalculator._calc_new_color(blue, ColorCalculator.BACKGROUND[2], factor)

        return new_red, new_green, new_blue

    @staticmethod
    def _inverseFactorIfOddRound(factor, current_time):
        odd_round = current_time % (ColorCalculator.BREATHFREQUENCY * 2) > ColorCalculator.BREATHFREQUENCY
        return 1 - factor if odd_round else factor

    @staticmethod
    def _calc_new_color(old_color, background, factor):
        distance = background - old_color
        return int(old_color + (distance * factor))
