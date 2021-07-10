

import os
import arcade


PIPES = ["assets" + os.sep + "sprites" + os.sep + "pipe-brown.png"]

BASE = "assets" + os.sep + "sprites" + os.sep + "base.png"

PLAY_BUTTON = "assets" + os.sep + "sprites" + os.sep + "play.png"
BACKGROUNDS = ["assets" + os.sep + "sprites" + os.sep + "background-day.png"]

BIRDS = {'red': ["assets" + os.sep + "sprites" + os.sep + "Wing_down.png", "assets" + os.sep + "sprites" + os.sep + "wing_stationary.png",
                    "assets" + os.sep + "sprites" + os.sep + "wing_up.png"]}

GET_READY_MESSAGE = "assets" + os.sep + "sprites" + os.sep + "message.png"

GAME_OVER = "assets" + os.sep + "sprites" + os.sep + "gameover.png"

SOUNDS = {'wing': arcade.load_sound("assets" + os.sep + "audio" + os.sep + "wing.mp3"),
          'die': arcade.load_sound("assets" + os.sep + "audio" + os.sep + "die.wav"),
          'point': arcade.load_sound("assets" + os.sep + "audio" + os.sep + "point.wav")}
          

MIN_HEIGHT = 50


GAP_SIZE = 120


JUMP_DY = 60

JUMP_STEP = 4
DY = 2

GRAVITY = 2

ANGLEP = 15
ANGLEM = -1.5


SCORE = {
    '0': 'assets' + os.sep + 'sprites' + os.sep + '0.png',
    '1': 'assets' + os.sep + 'sprites' + os.sep + '1.png',
    '2': 'assets' + os.sep + 'sprites' + os.sep + '2.png',
    '3': 'assets' + os.sep + 'sprites' + os.sep + '3.png',
    '4': 'assets' + os.sep + 'sprites' + os.sep + '4.png',
    '5': 'assets' + os.sep + 'sprites' + os.sep + '5.png',
    '6': 'assets' + os.sep + 'sprites' + os.sep + '6.png',
    '7': 'assets' + os.sep + 'sprites' + os.sep + '7.png',
    '8': 'assets' + os.sep + 'sprites' + os.sep + '8.png',
    '9': 'assets' + os.sep + 'sprites' + os.sep + '9.png',
}
