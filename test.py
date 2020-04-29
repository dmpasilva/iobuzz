from __future__ import print_function
from iobuzz.controllers.buzz_controller import BuzzController
import time


def on_key_down(controller, keys):
    print("-------")
    print("key down")
    print (controller)
    print (keys)



def on_key_up(controller, keys):
    print("-------")
    print("key up")
    print (controller)
    print (keys)


buzz = BuzzController()
buzz.register_on_key_down(on_key_down)
buzz.register_on_key_up(on_key_up)

print("Blink all")
buzz.blink_all()
time.sleep(3)
buzz.clear_animations()

print("Blink controllers 1 and 3")
buzz.blink_controllers([1, 3])
time.sleep(3)
buzz.clear_animations()

print("Turn on all")
buzz.turn_on_all()
time.sleep(3)
buzz.clear_animations()

print("Turn off all")
buzz.turn_off_all()
time.sleep(3)
buzz.clear_animations()

print("Turn on controllers 1 and 3")
buzz.turn_on_controllers([1, 3])
time.sleep(3)
buzz.clear_animations()

print("Turn on controllers 0 and 2")
buzz.turn_on_controllers([0, 2])
time.sleep(3)
buzz.clear_animations()

print("Turn off controllers 1 and 3")
buzz.turn_off_controllers([1, 3])
time.sleep(3)
buzz.clear_animations()

print("Turn off controllers 0 and 2")
buzz.turn_off_controllers([0, 2])
time.sleep(3)
buzz.clear_animations()

print("Do pairing animation")
buzz.do_pairing_animation()
time.sleep(3)
buzz.clear_animations()

print("Do search animation")
buzz.do_search_animation()
time.sleep(3)
buzz.clear_animations()

print("Do error animation")
buzz.do_error_animation()
time.sleep(3)
buzz.clear_animations()

