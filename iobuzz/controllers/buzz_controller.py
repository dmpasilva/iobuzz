from iobuzz.io.input_reader import InputReader
from iobuzz.io.output_writer import OutputWriter


class BuzzController:
    def __init__(self):
        self.input = InputReader()
        self.output = OutputWriter()

    def register_on_key_down(self, callback):
        self.input.register_on_key_down(callback)

    def register_on_key_up(self, callback):
        self.input.register_on_key_up(callback)

    def clear_all(self):
        self.output.clear_all()

    def clear_animations(self, timeout=0.5):
        self.output.clear_animations(timeout)

    def blink_all(self, period=0.5):
        self.output.blink_all(period)

    def blink_controllers(self, controllers, period=0.5):
        self.output.blink_controllers(controllers, period)

    def turn_on_all(self):
        self.output.turn_on_all()

    def turn_on_controllers(self, controllers):
        self.output.turn_on_controllers(controllers)

    def turn_off_all(self):
        self.output.turn_off_all()

    def turn_off_controllers(self, controllers):
        self.output.turn_off_controllers(controllers)

    def do_pairing_animation(self):
        self.output.do_pairing_animation()

    def do_error_animation(self):
        self.output.do_error_animation()

    def do_search_animation(self):
        self.output.do_search_animation()
