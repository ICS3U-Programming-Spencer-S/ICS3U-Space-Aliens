#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Jan 9, 2022
# A basic game called "Horde"

import stage
import ugame
import constants

def game_scene():

    # access image bank for PyBadge
    # uses the background variable and sets its size
    image_bank_background = stage.Bank.from_bmp16("peter_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

     # uses the background variable and sets its size
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    
    # creates a ship variable sprite at 75x, 66y
    ship = stage.Sprite(image_bank_sprites, 4, 75, constants.SCREEN_Z - (2 * constants.SPRITE_SIZE))

    # sets the stage to 60 FPS
    game = stage.Stage(ugame.display, constants.Hertz)

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
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        #Update game logic.

        #Redraw sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
