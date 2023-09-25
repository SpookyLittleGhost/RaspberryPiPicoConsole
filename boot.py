import board
from database import set_up_storage
import digitalio

# Rotary Encoder Setup
switch = digitalio.DigitalInOut(board.GP26)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

switch_state = switch.value

if switch_state:
    print("Writing enabled")
else:
    print("Writing disabled")

set_up_storage(not switch_state)
