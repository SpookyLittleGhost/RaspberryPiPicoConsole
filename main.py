import lib

import time
import board
import neopixel

import busio
from adafruit_ssd1306 import SSD1306_I2C

import pwmio

import digitalio
import rotaryio


def rotary_encoder_do_something():
    while True:
        position = encoder.position
        if last_position is None or position != last_position:
            print(f"Rotary: {position}")
        last_position = position

        if switch_state != switch.value:
            switch_state = switch.value
            print('Switch is ' + ('ON' if switch.value else 'OFF'))


def display_do_something(str):
    display.fill(0)

    display_text(str, 0)
    display_text_black(str, 1)

    display.show()


def buzzer_do_something():
    buzzer.frequency = TONE_ON
    time.sleep(Buffer)
    buzzer.frequency = TONE_OFF


def LED_do_something():
    pixels[0] = LED_ON
    time.sleep(Buffer)
    pixels[0] = LED_OFF


# The main method

# Parameters
LED_OFF = (0, 0, 0)
LED_ON = (0, 20, 30)
Buffer = 3.1
TONE_OFF = 30000
TONE_ON = 600

#RGB LED Setup
pixels = neopixel.NeoPixel(board.GP22, 1)

# Display Setup
i2c0 = busio.I2C(scl=board.GP17, sda=board.GP16)
display = SSD1306_I2C(128, 64, i2c0)


def display_text(str, line):
    display.text(str, 0, (line % 8) * 8, 1, font_name="/lib/font5x8.bin")


def display_text_black(str, line):
    display.text(str, 0, (line % 8) * 8, 0, font_name="/lib/font5x8.bin")


# Buzzer Setup
buzzer = pwmio.PWMOut(board.GP27, variable_frequency=True)

buzzer.frequency = TONE_OFF
buzzer.duty_cycle = 32768

# Rotary Encoder Setup
encoder = rotaryio.IncrementalEncoder(board.GP7, board.GP6)

switch = digitalio.DigitalInOut(board.GP26)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

last_position = encoder.position
switch_state = switch.value

# Code
while True:
    choice = input("weiter1?")
    display.fill(0)

    display.show()
    choice = input("weiter2?")
    display.fill(1)

    display.show()
    choice = input("weiter3?")

    display.fill(0)

    display.show()
    choice = input("weiter4?")

    display_text(f"moin",0)

    display.show()
    choice = input("weiter5?")

    display_text(f"servus",1)
    display_text(f"gruezi",2)

    display.show()
    choice = input("weiter6?")