#  Blink an LED with the LGPIO library
#  Uses lgpio library, compatible with kernel 5.11
#  Author: William 'jawn-smith' Wilson

import time
import lgpio
LED = 23
BTN = 24
Estatus = False

# open the gpio chip and set the LED pin as output
h = lgpio.gpiochip_open(0)
b = lgpio.gpiochip_open(1)
lgpio.gpio_claim_output(h, LED)
lgpio.gpio_set_debounce_micros(b, BTN, 80000)

try:
    while True:
        if Estatus :
            # Turn the GPIO pin on
            lgpio.gpio_write(h, LED, 1)
            time.sleep(1)

            # Turn the GPIO pin off
            lgpio.gpio_write(h, LED, 0)
            time.sleep(1)
        if lgpio.gpio_read(b,BTN):
            Estatus =  not Estatus
except KeyboardInterrupt:
    lgpio.gpio_write(h, LED, 0)
    lgpio.gpiochip_close(h)
    lgpio.gpiochip_close(b)