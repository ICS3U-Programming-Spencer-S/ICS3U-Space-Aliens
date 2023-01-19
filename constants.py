#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Jan 9, 2022
# Constants folder for a pybadge


# PyBadge Screen size and sprite size
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
# max enemies and bullet 
MAX_NUM_EME = 5
MAX_NUM_BULLET = 5
# player and enemy sprite speed
PLAYER_SPEED = 1
ENEMY_SPEED = 1
# projectile speed
PROJECTILE_SPEED = 2
# out of bounds
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM = SCREEN_GRID_Y + SPRITE_SIZE
# FPS and base movement values
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
