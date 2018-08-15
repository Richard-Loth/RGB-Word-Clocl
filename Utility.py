class Utility:

    @staticmethod
    def decimalToHex(decimal):
        result = str(hex(decimal)[2:])
        return result if len(result) > 1 else "0" + result

    @staticmethod
    def rgb_to_fill_color(red,green,blue):
        return "#" + Utility.decimalToHex(red) + Utility.decimalToHex(green) + Utility.decimalToHex(blue)

    @staticmethod
    def fps_to_millis(fps):
        return 1/fps
