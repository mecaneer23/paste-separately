#!/usr/bin/env python3
"""After 3 seconds, paste lines from `file.txt` one at a time"""
# pylint: disable=missing-function-docstring

import time
from pathlib import Path

from pynput.keyboard import Controller

keyboard = Controller()
time.sleep(3)
with Path(__file__).parent.joinpath("file.txt").open("r", encoding="utf-8") as f:
    for line in f.readlines():
        keyboard.type(line)
        time.sleep(1)
