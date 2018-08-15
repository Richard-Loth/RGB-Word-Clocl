import time


class ColorCalculator:

    BREATHFREQUENCY = 1000

    def __init__(self, background):
        self.background = background

    def calculateColor(self, mode, red, green, blue):
        if mode == 1:
            return red, green, blue
        elif mode == 2:
            return self._calculateBreathing(red, green, blue)

    def _calculateBreathing(self, red, green, blue):
        current_time_ms = (time.time() * 1000)
        current_value = current_time_ms % ColorCalculator.BREATHFREQUENCY
        factor = current_value / ColorCalculator.BREATHFREQUENCY
        factor = self._inverseFactorIfOddRound(factor, current_time_ms)

        new_red = self._calc_new_color(red, self.background[0], factor)
        new_green = self._calc_new_color(green, self.background[1], factor)
        new_blue = self._calc_new_color(blue, self.background[2], factor)

        return new_red, new_green, new_blue

    def _inverseFactorIfOddRound(self, factor, current_time):
        odd_round = current_time % (ColorCalculator.BREATHFREQUENCY * 2) > ColorCalculator.BREATHFREQUENCY
        return 1 - factor if odd_round else factor

    def _calc_new_color(self, old_color, background, factor):
        distance = background - old_color
        return int(old_color + (distance * factor))
