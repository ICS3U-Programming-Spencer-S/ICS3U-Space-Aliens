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
    image_bank_background = stage.Bank.from_bmp16("dirt_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("doom_cha.bmp")

    # buttons and their state info for them
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # gets sounds ready for usage
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

     # uses the background variable and sets its size
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    
    # creates a ship variable sprite at 75x, 96y
    ship = stage.Sprite(image_bank_sprites, 4, 75, constants.SCREEN_Z - (2 * constants.SPRITE_SIZE))

    # Creates the enemy ship variable
    enemy = stage.Sprite(image_bank_sprites, 7, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)

    # sets the stage to 60 FPS
    game = stage.Stage(ugame.display, constants.Hertz)

    # creates both sprite and background layers
    game.layers = [ship] + [enemy] + [background]
    
    # renders the background
    game.render_block()

    # repeats game forever
    while True:
        # User input commands 
        keys = ugame.buttons.get_pressed()

        # For button A (Fires projection)
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # The B button
        if keys & ugame.K_O != 0:
            pass

        # The start button
        if keys & ugame.K_START != 0:
            print("Start")
        
        # The select button
        if keys & ugame.K_SELECT != 0:
            print("Select")

        # For the right button control
        if keys & ugame.K_RIGHT != 0:
            # Makes sure it's in the playable area before allowing movement
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.MOVEMENT_SPED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        # For the left button control
        if keys & ugame.K_LEFT != 0:
            # Makes sure it's in the playable area before allowing movement
            if ship.x > 0:
                ship.move((ship.x - constants.MOVEMENT_SPED), ship.y)
            else:
                ship.move(0, ship.y)

        # we want to pass on up as we don't use it
        if keys & ugame.K_UP:
            pass

        # We want to pass on down as we don't use it
        if keys & ugame.K_DOWN:
            pass

        #Update game logic.
        # this plays a sound when 'a' is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        #Redraw sprites
        game.render_sprites([ship] + [enemy])
        game.tick()

if __name__ == "__main__":
    game_scene()
