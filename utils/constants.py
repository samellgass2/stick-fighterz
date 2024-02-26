import pyglet as pg

### ~~~ ### ~~~~~~ TEXTURE / RENDER CONSTANTS ~~~~~~ ### ~~~ ###
# Refresh rate
REFRESH_RATE_HERTZ = 60

# Define the game world as an N x M grid of tiles of size S
TILE_SIZE = 1 
NUM_COLUMNS = 1400
NUM_ROWS = 1000

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


# ~~~~~~~~~~~~~ CHARACTER CONSTANTS ~~~~~~~~~ #
ARM_WIDTH = 1 #8 * TILE_SIZE
LEG_WIDTH = 1 #8 * TILE_SIZE
TORSO_WIDTH = 1 #15 * TILE_SIZE

LEG_MAX_ANGLE = 135
LEG_MIN_ANGLE = 45


### ~~~ ### ~~~~~~ GAMEPLAY / EVENT HANDLER CONSTANTS ~~~~~~ ### ~~~ ###
PLAYER_MOVEMENT_KEYS = set([pg.window.key.W, pg.window.key.S, pg.window.key.A, pg.window.key.D, pg.window.key.LEFT, pg.window.key.RIGHT, pg.window.key.UP, pg.window.key.DOWN])
