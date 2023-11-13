#!/usr/bin/env python3
#pylint: disable=missing-module-docstring, missing-function-docstring

import time
from pynput.keyboard import Controller

keyboard = Controller()
time.sleep(3)
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        keyboard.type(line)
        time.sleep(1)
