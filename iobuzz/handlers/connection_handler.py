from enum import Enum
import time

from iobuzz.handlers.message_handler import MessageHandler
from iobuzz.models.buttons import Button
from iobuzz.controllers.buzz_controller import BuzzController
from iobuzz.controllers.web_socket import WebSocketConnection

class Status(Enum):
    WAITING_FOR_BUZZ = 0,
    WAITING_FOR_ROOM_ID = 1

class ConnectionHandler:
    room = ""
    buzz = None
    websocket = None
    status = None
    controller = -1

    def __init__(self, buzz: BuzzController):
        self.buzz = buzz
        message_handler = MessageHandler(buzz)
        self.websocket = WebSocketConnection(self, message_handler)
        self.on_connection_failed()

    def on_connection(self):
        self.buzz.clear_animations()
        self.buzz.turn_off_all()
        self.buzz.register_on_key_down(None)

    def on_connection_failed(self):
        self.buzz.do_error_animation()
        time.sleep(1)
        self.buzz.clear_animations()
        self.buzz.turn_off_all()
        self.buzz.register_on_key_down(self.__on_key_down)
        self.wait_for_connection()

    def wait_for_connection(self):
        print("Press the Red button in any controller to start")
        self.room = ""
        self.controller = -1
        self.status = Status.WAITING_FOR_BUZZ
        self.buzz.clear_animations()
        self.buzz.turn_off_all()
        self.buzz.do_pairing_animation()

    def connect_to_room(self, room):
        print("Connecting to " + room)
        self.buzz.do_search_animation()
        # this animation is too cool to not be shown
        time.sleep(2)
        self.websocket.connect(room)

    def __on_key_down(self, controller, keys):
        if len(keys) != 1:
            return
        self.buzz.clear_animations()
        self.buzz.turn_off_all()
        button = keys[0]
        if self.status == Status.WAITING_FOR_BUZZ:
            if button != Button.RED:
                self.wait_for_connection()
            else:
                print("Use the buzzers to type the room number")
                self.status = Status.WAITING_FOR_ROOM_ID
                self.controller = controller
                self.buzz.turn_on_controllers([controller])
        elif self.status == Status.WAITING_FOR_ROOM_ID:
            if controller != self.controller:
                return
            if button == Button.RED:
                print("Operation interrupted")
                self.wait_for_connection()
            else:
                self.room = self.room + str(int(button))
                if len(self.room) >= 4:
                    self.buzz.register_on_key_down(None)
                    self.connect_to_room(self.room[:4])
                else:
                    time.sleep(0.2)
                    self.buzz.turn_on_controllers([controller])

