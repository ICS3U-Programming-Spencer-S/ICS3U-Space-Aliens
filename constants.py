#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Jan 9, 2022
# Constants folder for a pybadge


# PyBadge Screen size and sprite size
SCREEN_X = 160
SCREEN_Z = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
# FPS and movement values
Hertz = 60
MOVEMENT_SPED = 1

# For the button states
button_state = {
    "button_up": "",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}

# Adds a red pallet
RED_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
