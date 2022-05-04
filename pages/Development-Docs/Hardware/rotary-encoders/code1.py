import time

import board
import rotaryio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# ============ MAIN SETUP =====================
# HID keyboard setup
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
# Rotary encoder setup
encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB)
last_position = 0

# decide which way rotary encoder is rotating, then send keyboard event accordingly


def send_key(pos, last_pos):
    if pos > last_pos:
        keyboard_layout.write("q")
        return
    keyboard_layout.write("a")


# ============ MAIN LOOP =====================
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        send_key(position, last_position)
        last_position = position
