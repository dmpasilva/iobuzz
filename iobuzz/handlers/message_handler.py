from iobuzz.controllers.buzz_controller import BuzzController


class MessageHandler:
    buzz = None
    websocket = None
    controllers = []
    buttons = []

    def __init__(self, buzz: BuzzController):
        self.buzz = buzz

    def on_stop_read(self):
        print("Stop reading data from controllers")
        self.buzz.register_on_key_down(None)

    def on_read(self, data, messenger):
        print("Read data from controllers")
        print(data)
        self.websocket = messenger
        self.buttons = data['buttons']
        self.controllers = data['controllers']
        self.buzz.register_on_key_down(self.__on_key_down)

    def on_write(self, data):
        print("Write data to controllers")
        print(data)
        self.buzz.clear_animations()
        self.buzz.turn_off_all()

        turn_on = []
        turn_off = []
        blink = []

        for idx, status in enumerate(data):
            if status == 0:
                turn_off.append(idx)
            elif status == 1:
                turn_on.append(idx)
            elif status == 2:
                blink.append(idx)

        if len(turn_on):
            self.buzz.turn_on_controllers(turn_on)
        if len(turn_off):
            self.buzz.turn_off_controllers(turn_off)
        if len(blink):
            self.buzz.blink_controllers(blink)

    def __on_key_down(self, controller, buttons):
        if controller in self.controllers and set(buttons).issubset(set(self.buttons)):
            if self.websocket:
                self.websocket.send_buttons(controller, buttons)