import hid

from iobuzz.config import VENDOR_ID, DEVICE_ID
from iobuzz.models.buttons import Button


class __BuzzIO:
    buffer = []
    light_array = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    buttonState = [
        {Button.RED: False, Button.BLUE: False, Button.ORANGE: False, Button.GREEN: False, Button.YELLOW: False},
        {Button.RED: False, Button.BLUE: False, Button.ORANGE: False, Button.GREEN: False, Button.YELLOW: False},
        {Button.RED: False, Button.BLUE: False, Button.ORANGE: False, Button.GREEN: False, Button.YELLOW: False},
        {Button.RED: False, Button.BLUE: False, Button.ORANGE: False, Button.GREEN: False, Button.YELLOW: False}
    ]

    def __init__(self):
        self.hid = hid.device()

        # Open up the device
        self.hid.open(VENDOR_ID, DEVICE_ID)

        # Set the non blocking mode
        self.hid.set_nonblocking(1)

        # Clear the Buzz Controller LEDs
        self.write()

    def read(self):
        data = self.hid.read(5)
        if data:
            self.buttonState[0][Button.RED] = ((data[2] & 0x01) != 0)  # red
            self.buttonState[0][Button.YELLOW] = ((data[2] & 0x02) != 0)  # yellow
            self.buttonState[0][Button.GREEN] = ((data[2] & 0x04) != 0)  # green
            self.buttonState[0][Button.ORANGE] = ((data[2] & 0x08) != 0)  # orange
            self.buttonState[0][Button.BLUE] = ((data[2] & 0x10) != 0)  # blue

            self.buttonState[1][Button.RED] = ((data[2] & 0x20) != 0)  # red
            self.buttonState[1][Button.YELLOW] = ((data[2] & 0x40) != 0)  # yellow
            self.buttonState[1][Button.GREEN] = ((data[2] & 0x80) != 0)  # green
            self.buttonState[1][Button.ORANGE] = ((data[3] & 0x01) != 0)  # orange
            self.buttonState[1][Button.BLUE] = ((data[3] & 0x02) != 0)  # blue

            self.buttonState[2][Button.RED] = ((data[3] & 0x04) != 0)  # red
            self.buttonState[2][Button.YELLOW] = ((data[3] & 0x08) != 0)  # yellow
            self.buttonState[2][Button.GREEN] = ((data[3] & 0x10) != 0)  # green
            self.buttonState[2][Button.ORANGE] = ((data[3] & 0x20) != 0)  # orange
            self.buttonState[2][Button.BLUE] = ((data[3] & 0x40) != 0)  # blue

            self.buttonState[3][Button.RED] = ((data[3] & 0x80) != 0)  # red
            self.buttonState[3][Button.YELLOW] = ((data[4] & 0x01) != 0)  # yellow
            self.buttonState[3][Button.GREEN] = ((data[4] & 0x02) != 0)  # green
            self.buttonState[3][Button.ORANGE] = ((data[4] & 0x04) != 0)  # orange
            self.buttonState[3][Button.BLUE] = ((data[4] & 0x08) != 0)  # blue
        return self.buttonState

    def write(self):
        self.hid.write(self.light_array)

    def turn_on_single(self, controller):
        self.light_array[controller + 2] = 0xFF

    def turn_off_single(self, controller):
        self.light_array[controller + 2] = 0x00

    def turn_on_all(self):
        self.light_array = [0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00]

    def turn_off_all(self):
        self.light_array = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]


io = __BuzzIO()