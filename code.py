#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Jan 9, 2022
# A basic game called "Horde"

import stage
import ugame
import supervisor
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
    image_bank_background = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")

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
        # waits for 2 seconds
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    # function for the main menu scene

    # access image bank for PyBadge
    # uses the background variable and sets its size
    image_bank_background = stage.Bank.from_bmp16("WORLD_BACKGROUND.bmp")

    # Text for main menu scene
    # Displays MT Game Studies at the top
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MT Game Studies")
    text.append(text1)

    # Press start prompt
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text2.move(3, 110)
    text2.text("PRESS START TO PLAY")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text3.move(20, 40)
    text3.text("PRESS SELECT FOR")
    text.append(text3)

    text4 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text4.move(40, 50)
    text4.text("GAME INFO")
    text.append(text4)

    text5 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text5.move(30, 80)
    text5.text(" PRESS A FOR")
    text.append(text5)

    text6 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text6.move(50, 90)
    text6.text("CONTROLS")
    text.append(text6)

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

        if keys & ugame.K_SELECT != 0:
            how_to_scene()

        if keys & ugame.K_X != 0:
            controls_scene()


def controls_scene():
    # this is a function controls info

    # image bank for background
    image_bank_background = stage.Bank.from_bmp16("how_to.bmp")

    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text1.move(2, 20)
    text1.text(
        "A = Fire Bullet\nLeft D-pad =\nMove left\nRight D-pad =\nMove right\n\n"
    )
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text2.move(2, 90)
    text2.text("Press START to the\nstart game or B to\nreturn to the main\nmenu!")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text3.move(26, 10)
    text3.text("!!!CONTROLS!!!")
    text.append(text3)

    # set the backgorund image to 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.Hertz)

    # set the layers of all sprites, items show up in order
    game.layers = text + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # call game scene
        if keys & ugame.K_O != 0:
            menu_scene()
        if keys & ugame.K_START != 0:
            game_scene()

        # redraw Sprites
        game.tick()


def how_to_scene():
    # this function is the game info scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("how_to.bmp")

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text1.move(2, 10)
    text1.text("Welcome to my game\nHorde!")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text2.move(2, 30)
    text2.text(
        "In this game you are\na person that \nhas mission to\ndestory as many\ndemons before they\noverwelm you \nand kill you\n"
    )
    text.append(text2)

    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text3.move(2, 90)
    text3.text("Press START to the\nstart game or B to\nreturn to the main\nmenu!")
    text.append(text3)

    # set the backgorund image to 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.Hertz)

    # set the layers of all sprites, items show up in order
    game.layers = text + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # call game scene
        if keys & ugame.K_O != 0:
            menu_scene()
        if keys & ugame.K_START != 0:
            game_scene()

        # redraw Sprites
        game.tick()


def game_scene():
    # function for the game scene

    def display_enemies():
        # function that takes aliens that are off the screen but moves it to the screen when needed
        for enemies_num in range(len(enemies)):
            if enemies[enemies_num].x < 0:
                enemies[enemies_num].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    # for score keeping
    score = 0

    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

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
    shot_sound = open("Gun.wav", "rb")
    boom_sound = open("boom.wav", "rb")
    crash_sound = open("crash.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # sound_state_glo = sound.mute(False)

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
        image_bank_sprites, 4, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # creates the enemies list
    enemies = []
    for enemies_num in range(constants.MAX_NUM_EME):
        a_single_enemy = stage.Sprite(
            image_bank_sprites, 7, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        enemies.append(a_single_enemy)

    # places one enemy on the screen
    display_enemies()

    # list for the bullets(lasers) for the player
    bullets = []
    for bullets_num in range(constants.MAX_NUM_BULLET):
        one_bullet = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        bullets.append(one_bullet)

    # sets the stage to 60 FPS
    game = stage.Stage(ugame.display, constants.Hertz)

    # creates both sprite and background layers
    game.layers = [score_text] + enemies + bullets + [player] + [background]

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
            if player.x <= (constants.SCREEN_X - constants.SPRITE_SIZE):
                player.move(player.x + 1, player.y)
            else:
                player.move(0, player.y)

        # for the left button control
        if keys & ugame.K_LEFT != 0:
            # Makes sure it's in the playable area before allowing movement
            if player.x >= 0:
                player.move(player.x - 1, player.y)
            else:
                player.move(constants.SCREEN_X - constants.SPRITE_SIZE, player.y)

        # this is for the up button, it's unused so we pass
        if keys & ugame.K_UP:
            pass

        # this is for the down button, it's unused so we pass
        if keys & ugame.K_DOWN:
            pass

        # updates game logic
        # fires a button with sound when 'a' is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            for bullets_num in range(len(bullets)):
                if bullets[bullets_num].x < 0:
                    bullets[bullets_num].move(player.x + 3, player.y)
                    # if sound_state_glo == False:
                    sound.play(shot_sound)
                    break

        # move the bullet each frame
        for bullets_num in range(len(bullets)):
            if bullets[bullets_num].x > 0:
                bullets[bullets_num].move(
                    bullets[bullets_num].x,
                    bullets[bullets_num].y - constants.PROJECTILE_SPEED,
                )

                if bullets[bullets_num].y < constants.OFF_TOP_SCREEN:
                    bullets[bullets_num].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # moves the enemies down each frame
        for enemies_num in range(len(enemies)):
            if enemies[enemies_num].x > 0:
                enemies[enemies_num].move(
                    enemies[enemies_num].x,
                    enemies[enemies_num].y + constants.ENEMY_SPEED,
                )
                if enemies[enemies_num].y > constants.SCREEN_Y:
                    enemies[enemies_num].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    display_enemies()
                    # keeps track of the score
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        # checks each frame to see if any bullets have hit an enemy
        for bullets_num in range(len(bullets)):
            if bullets[bullets_num].x > 0:
                for enemies_num in range(len(enemies)):
                    if enemies[enemies_num].x > 0:
                        if stage.collide(
                            bullets[bullets_num].x + 6,
                            bullets[bullets_num].y + 2,
                            bullets[bullets_num].x + 11,
                            bullets[bullets_num].y + 12,
                            enemies[enemies_num].x + 1,
                            enemies[enemies_num].y,
                            enemies[enemies_num].x + 15,
                            enemies[enemies_num].y + 15,
                        ):
                            # hit detection
                            enemies[enemies_num].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            bullets[bullets_num].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            sound.stop()
                            sound.play(boom_sound)
                            display_enemies()
                            display_enemies()
                            # ups the score
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))

        # checks each frame to see if a enemy touches the player and end the game
        for enemies_num in range(len(enemies)):
            if enemies[enemies_num].x > 0:
                if stage.collide(
                    enemies[enemies_num].x + 1,
                    enemies[enemies_num].y,
                    enemies[enemies_num].x + 15,
                    enemies[enemies_num].y + 15,
                    player.x,
                    player.y,
                    player.x + 15,
                    player.y + 15,
                ):
                    # crash sound
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(3.0)
                    game_over_scene(score)

        # redraws sprites
        game.render_sprites(enemies + bullets + [player])
        # game tick waits until refresh is over
        game.tick()


def game_over_scene(final_score):
    # a function for the game over scene

    # to turn off sound from the last scene
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    lose_sound = open("losing.wav", "rb")
    # plays a sound when you lose
    sound.play(lose_sound)

    # image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # open and sets the background for image 0
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # text for the screen
    text = []
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text2.move(43, 40)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text3.move(32, 60)
    text3.text("PRESS SELECT")
    text.append(text3)

    text4 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text4.move(20, 80)
    text4.text("TO RETURN TO MENU")
    text.append(text4)

    text5 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text5.move(38, 100)
    text5.text("PRESS START")
    text.append(text5)

    text6 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text6.move(16, 115)
    text6.text("TO RESTART LEVEL")
    text.append(text6)

    # stage for the background to show with 60 hertz
    game = stage.Stage(ugame.display, constants.Hertz)
    # sets layers up for objects to display correctly
    game.layers = text + [background]
    # renders the background and the initial location of the sprite list
    game.render_block()

    # game loop, repeats forever
    while True:

        # user input
        keys = ugame.buttons.get_pressed()

        # start button selection
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        if keys & ugame.K_START != 0:
            game_scene()

        # updates game logic
        # waits until refresh rate is done
        game.tick()


if __name__ == "__main__":
    splash_scene()
