#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Jan 9, 2022
# A basic game called "Horde"

import stage
import ugame


def game_scene():

    # access image bank for PyBadge
    # uses the background variable and sets its size
    image_bank_background = stage.Bank.from_bmp16("peter_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

     # uses the background variable and sets its size
    background = stage.Grid(image_bank_background, 10, 8)
    
    # creates a ship variable sprite at 75x, 66y
    ship = stage.Sprite(image_bank_sprites, 4, 75, 66)

    # sets the stage to 60 FPS
    game = stage.Stage(ugame.display, 60)

    # creates both sprite and background layers
    game.layers = [ship] + [background]
    
    # renders the background
    game.render_block()
    # Place Holder
    while True:
        # User input commands 
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)

        #Update game logic.

        #Redraw sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
