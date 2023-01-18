#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Jan 9, 2022
# A basic game called "Horde"

import stage
import ugame
import constants
import time
import random


def splash_scene():
    # this function is the splash scene

    # gets sound ready for use
    coin_flip = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_flip)

    # image bank for the mt game studio
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # background that selects image one from the bank
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # used this program to split the image into tile:
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white

    # sets the stage to 60 FPS
    game = stage.Stage(ugame.display, constants.Hertz)

    # layers
    game.layers = [background]

    # renders the background
    game.render_block()

    # repeats forever, game loop
    while True:
        # waits for 5 seconds
        time.sleep(5.0)
        menu_scene()


def menu_scene():
    # function for the main menu scene

    # access image bank for PyBadge
    # uses the background variable and sets its size
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Text for main menu scene
    # Displays MT Game Studies at the top
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MT Game Studies")
    text.append(text1)

    # Press start prompt
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # uses the background variable and sets its size
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # sets the stage to 60 FPS
    game = stage.Stage(ugame.display, constants.Hertz)

    # creates both text and background layers
    game.layers = text + [background]

    # renders the background
    game.render_block()

    # repeats game forever
    while True:
        # User input commands
        keys = ugame.buttons.get_pressed()

        # The start button
        if keys & ugame.K_START != 0:
            game_scene()


def game_scene():
    # function for the game scene

    # access image bank for PyBadge
    # uses the background variable and sets its size
    image_bank_background = stage.Bank.from_bmp16("dirt_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("doom_cha.bmp")

    # buttons and their start state info for them
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # gets sounds ready for usage
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound_state_glo = sound.mute(False)

    # uses the background variable and sets its size
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 2)
            background.tile(x_location, y_location, tile_picked)

    # creates a player variable sprite at 75x, 96y
    player = stage.Sprite(
        image_bank_sprites, 4, 75, constants.SCREEN_Z - (2 * constants.SPRITE_SIZE)
    )

    # creates the enemy player variable
    enemy = stage.Sprite(
        image_bank_sprites,
        7,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # sets the stage to 60 FPS
    game = stage.Stage(ugame.display, constants.Hertz)

    # creates both sprite and background layers
    game.layers = [player] + [enemy] + [background]

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

        # The B button (For mute button)
        if keys & ugame.K_O != 0:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        # the start button
        if keys & ugame.K_START != 0:
            print("Start")

        # the select button
        if keys & ugame.K_SELECT != 0:
            print("Select")

        # for the right button control
        if keys & ugame.K_RIGHT != 0:
            # Makes sure it's in the playable area before allowing movement
            if player.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                player.move((player.x + constants.MOVEMENT_SPED), player.y)
            else:
                player.move((constants.SCREEN_X - constants.SPRITE_SIZE), player.y)

        # for the left button control
        if keys & ugame.K_LEFT != 0:
            # Makes sure it's in the playable area before allowing movement
            if player.x > 0:
                player.move((player.x - constants.MOVEMENT_SPED), player.y)
            else:
                player.move(0, player.y)

        # this is for the up button, it's unused so we pass
        if keys & ugame.K_UP:
            pass

        # this is for the down button, it's unused so we pass
        if keys & ugame.K_DOWN:
            pass

        # updates game logic
        # this is a mute button which changes the state
        if b_button == constants.button_state["button_just_pressed"]:
            if sound_state_glo == True:
                sound_state_glo = False
                print("Unmuted")
            else:
                sound_state_glo = True
                print("muted")

        # this plays a sound when 'a' is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            if sound_state_glo == False:
                sound.play(pew_sound)
                print("sound")
            else:
                print("No sound")

        # redraws sprites
        game.render_sprites([player] + [enemy])
        game.tick()


if __name__ == "__main__":
    splash_scene()
