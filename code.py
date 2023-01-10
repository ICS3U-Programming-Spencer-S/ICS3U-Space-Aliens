#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Jan 9, 2022
# A basic game called "Horde"

import ugame
import stage

# function for main scene
def game_scene():

    # access image bank for PyBadge
    image_bank_background = stage.Bank.from_bmp16("peter_background.bmp")
    # uses the background variable and sets its size
    background = stage.Grid(image_bank_background, 10, 8)
    # sets the stage to 60 FPS
    game = stage.Stage(ugame.display, 60)
    # creates the layer for sprites
    game.layers = [background]
    # renders the images
    game.render_block()

    # place holder for later???
    while True:
        pass


if __name__ == "__main__":
    game_scene()
