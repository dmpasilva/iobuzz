from iobuzz.io.buzz_io import io
import time, _thread

class InputReader():
    on_key_down = None
    on_key_up = None
    #on_key_long_pressed = None

    previous_controller = -1
    previous_keys = []

    def __init__(self):
        io.turn_on_all()
        io.write()
        _thread.start_new_thread(self.__wait_for_input, ())

    def register_on_key_down(self, callback):
        self.on_key_down = callback

    def register_on_key_up(self, callback):
        self.on_key_up = callback

    #def register_on_key_long_pressed(self, duration, callback):
    #    self.on_key_long_pressed = callback

    def __on_button_press(self, controller, keys):
        if (self.previous_controller == -1 and controller > -1) or self.previous_controller != controller:
            self.previous_controller = controller
            self.previous_keys = keys
            if self.on_key_down is not None:
                self.on_key_down(controller, keys)
        elif self.previous_controller > -1 and controller == -1:
            if self.on_key_up is not None:
                self.on_key_up(self.previous_controller, self.previous_keys)
            self.previous_controller = controller
            self.previous_keys = keys

    def __wait_for_input(self):
        controllers = [0, 1, 2, 3]
        while True:
            buttons = io.read()
            found = -1
            keys = []
            for controller in controllers:
                for button, pressed in buttons[controller].items():
                    if button is not None and pressed:
                        found = controller
                        keys.append(button)
                if found > -1 and len(keys) > 0:
                    break

            if found > -1 and len(keys) > 0:
                self.__on_button_press(found, keys)
                time.sleep(0.2)
            else:
                self.__on_button_press(found, keys)

            #if found is not False and len(keys) > 0:

            #else:
            #    self.__on_button_press(None, [])