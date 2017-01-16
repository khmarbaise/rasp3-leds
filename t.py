#!/usr/bin/env python

import time

from blinkt import set_clear_on_exit, set_pixel, show, set_brightness

set_clear_on_exit(False)

set_pixel(0 , 255,   0,   0, 0.1)
set_pixel(1 ,   0, 255,   0, 0.1)
set_pixel(2 ,   0,   0, 255, 0.1)
show()
time.sleep(0.1)
