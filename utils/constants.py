import pyglet as pg

### ~~~ ### ~~~~~~ TEXTURE / RENDER CONSTANTS ~~~~~~ ### ~~~ ###
# Refresh rate
REFRESH_RATE_HERTZ = 60

# Define the game world as an N x M grid of tiles of size S
TILE_SIZE = 1 
NUM_COLUMNS = 1000
NUM_ROWS = 750

BOOT_MODE = "test"

BOOT_MESSAGE = """


============================================================


                BEGINNING STICK_FIGHTERZ BOOT...

                REFRESH RATE = {} FPS

                SIZE OF SCREEN = {} X {}

                MODE = {}


============================================================


""".format(REFRESH_RATE_HERTZ, NUM_COLUMNS * TILE_SIZE, NUM_ROWS * TILE_SIZE, BOOT_MODE)



# ~~~~~~~~~~~~~ TEXT CONSTANTS ~~~~~~~~~~ #
CHARACTER_SELECT_TEXT = "CHARACTER SELECT"
START_GAME_TEXT = "START GAME"
SINGLE_PLAYER_TEXT = "SINGLE PLAYER"
TWO_PLAYER_TEXT = "TWO PLAYER"
BACK_TEXT = "BACK"




### ~~~ ### ~~~~~~ GAMEPLAY / EVENT HANDLER CONSTANTS ~~~~~~ ### ~~~ ###
PLAYER_MOVEMENT_KEYS = set([pg.window.key.W, pg.window.key.S, pg.window.key.A, pg.window.key.D, pg.window.key.LEFT, pg.window.key.RIGHT, pg.window.key.UP, pg.window.key.DOWN])
