from iobuzz.io.buzz_io import io
from enum import Enum
import time
import _thread

class Status(Enum):
    STOPPED = 0,
    RUNNING = 1,
    BLINKING_ALL = 2,
    BLINKING_SPECIFIC = 3,
    SEARCHING = 4

class OutputWriter():
    def __init__(self):
        self.current_status = Status.STOPPED

    def clear_all(self):
        self.clear_animations()
        self.turn_off_all()

    def clear_animations(self, timeout=0.5):
        self.current_status = Status.STOPPED
        time.sleep(timeout)

    def blink_all(self, period=0.5):
        if self.current_status != Status.STOPPED:
            self.clear_animations()

        self.current_status = Status.BLINKING_ALL
        _thread.start_new_thread(self.__blink_all, (period,))

    def blink_controllers(self, controllers, period=0.5):
        if self.current_status != Status.STOPPED:
            self.clear_animations()

        self.current_status = Status.BLINKING_SPECIFIC
        _thread.start_new_thread(self.__blink_controllers, (controllers, period))

    def turn_on_all(self):
        io.turn_on_all()
        io.write()

    def turn_on_controllers(self, controllers):
        for controller in controllers:
            io.turn_on_single(controller)
        io.write()

    def turn_off_all(self):
        io.turn_off_all()
        io.write()

    def turn_off_controllers(self, controllers):
        for controller in controllers:
            io.turn_off_single(controller)
        io.write()

    def do_pairing_animation(self):
        if self.current_status != Status.STOPPED:
            self.clear_animations()
        self.blink_all(0.2)

    def do_error_animation(self):
        if self.current_status != Status.STOPPED:
            self.clear_animations()

        self.current_status = Status.RUNNING
        for i in range(0, 3):
            self.turn_on_all()
            time.sleep(0.2)
            self.turn_off_all()
            time.sleep(0.2)
        time.sleep(1)
        self.current_status = Status.STOPPED

    def do_search_animation(self):
        if self.current_status != Status.STOPPED:
            self.clear_animations()

        self.current_status = Status.SEARCHING
        _thread.start_new_thread(self.__do_search_animation, ())

    def __blink_controllers(self, controllers, period=0.5):
        while self.current_status == Status.BLINKING_SPECIFIC:
            self.turn_on_controllers(controllers)
            time.sleep(period)
            self.turn_off_controllers(controllers)
            time.sleep(period)

    def __blink_all(self, period=0.5):
        while self.current_status == Status.BLINKING_ALL:
            io.turn_on_all()
            io.write()
            time.sleep(period)
            io.turn_off_all()
            io.write()
            time.sleep(period)

    def __do_search_animation(self):
        controller = 0
        while self.current_status == Status.SEARCHING:
            self.turn_on_controllers([controller])
            time.sleep(0.2)
            self.turn_off_controllers([controller])
            controller = controller + 1
            if controller == 4:
                controller = 0
