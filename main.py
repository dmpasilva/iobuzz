from iobuzz.controllers.buzz_controller import BuzzController
from iobuzz.handlers.connection_handler import ConnectionHandler
import time


if __name__ == "__main__":
    buzz = BuzzController()
    controller = ConnectionHandler(buzz)
    while True:
        time.sleep(0.1)