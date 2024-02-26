from objects.rendered_object import *
import pyglet as pg 
from utils.utils import *
from utils.constants import *
from objects.character_creator import *
from objects.screen import Screen, Textures, MainMenu, BattleStage
from objects.event_trackers import MainMenuEventHandler

### ~~~ ### ~~~~~~ DEFINING OBJECT STATE CONSTANTS ~~~~~~ ### ~~~ ###

# ~~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~ #

MENU_BGRND = Rectangle(0, 0, 100, 100, 255, 255, 255, "menu background")
BOTTOM_HALF_OF_SCREEN = Rectangle(0, 0, 100, 50, 0,0,0)
CHARACTER_SELECT_BUTTON = Rectangle(5, 20, 45, 80, 255, 0, 0, "char select button")

CHARACTER_SELECT_BUTTON_LABEL = Label(15, 45, 25, 65, CHARACTER_SELECT_TEXT, "char select text", 38)
START_BUTTON = Rectangle(55, 20, 95, 80, 0, 255, 0, "start button")
START_BUTTON_LABEL = Label(75, 45, 85, 65, START_GAME_TEXT, "start game label", 38)


MAIN_MENU_TEXTURE_MAP = {
    0: [MENU_BGRND, BOTTOM_HALF_OF_SCREEN], # TODO: add a background
    1: [CHARACTER_SELECT_BUTTON, START_BUTTON], # TODO: put rest of menu buttons at this layer
    2: [CHARACTER_SELECT_BUTTON_LABEL, START_BUTTON_LABEL]
}

    
MAIN_MENU_TEXTURES = Textures(MAIN_MENU_TEXTURE_MAP)
MAIN_MENU_SCREEN = MainMenu(MAIN_MENU_TEXTURES)

# ~~~~~~~~~~~~~ START MENU ~~~~~~~~~~ #

START_MENU_BGRND = Rectangle(0,0,100,100, 0,0,0, "start background")
START_MENU_BOTTOM_HALF_OF_SCREEN = Rectangle(0, 0, 100, 50, 255, 255, 255, "start menu bottom half")
ONE_PLAYER_BUTTON = Rectangle(10, 50, 50, 80, 255, 0, 0, "one player button")
ONE_PLAYER_BUTTON_LABEL = Label(20, 70, 40, 80, SINGLE_PLAYER_TEXT, "one player text", 20)
TWO_PLAYER_BUTTON = Rectangle(10, 10, 50, 40, 100, 100, 100, "two player button")
TWO_PLAYER_BUTTON_LABEL = Label(20, 20, 40, 40, TWO_PLAYER_TEXT, "two player text", 20)
BACK_BUTTON = Rectangle(65, 15, 80, 30, 255, 0, 0, "back button")
BACK_BUTTON_LABEL = Label(75, 20, 80, 25, BACK_TEXT, "back button label", 15)

START_MENU_TEXTURE_MAP = {
    0: [START_MENU_BGRND, START_MENU_BOTTOM_HALF_OF_SCREEN], # TODO: add a background
    1: [ONE_PLAYER_BUTTON, TWO_PLAYER_BUTTON, BACK_BUTTON], # TODO: put rest of menu buttons at this layer
    2: [ONE_PLAYER_BUTTON_LABEL, TWO_PLAYER_BUTTON_LABEL, BACK_BUTTON_LABEL]
}

START_MENU_TEXTURES = Textures(START_MENU_TEXTURE_MAP)
START_MENU_SCREEN = MainMenu(START_MENU_TEXTURES)

# ~~~~~~~~~~~~~ STAGE SELECTION MENU ~~~~~~~~~~ #
# The stage selection screen will be a grid of stages 
NUM_STAGE_ROWS = 5
NUM_STAGE_COLS = 5
DIVIDER_SPACE = 5 # percent

def stage_grid_to_coords(row, col):
    # The top bar is 4 dividers tall
    """
    D                       N * width + (N * D)             ==> 100 = NUM_COLS * width + (NUM_COLS+1) * D ==> width = (100 - (D * (NUM_COLS+1))) / NUM_COLS

    NUM_ROWS            

    D

    ...                     . <-- N x M             M * height + (M * D) ==> height = (100 - (D * (NUM_ROWS+1))) / NUM_ROWS
    2

    D

    1

    0   D   1   D   2   D   ... D   NUM_COLS    D  
    """
    box_width = (100 - (DIVIDER_SPACE * (NUM_STAGE_COLS + 1))) / NUM_STAGE_COLS
    box_height = (100 - (DIVIDER_SPACE * (NUM_STAGE_ROWS + 1))) / NUM_STAGE_ROWS
    x = col * box_width + (col+1) * (DIVIDER_SPACE)
    y = row * box_height + (row+1) * (DIVIDER_SPACE)
    return [x, y, x + box_width, y + box_height]

s1_cords = stage_grid_to_coords(4, 0)
LABEL_PAD = 1.35 * DIVIDER_SPACE
STAGE_ONE_BOX = Rectangle(s1_cords[0], s1_cords[1], s1_cords[2], s1_cords[3], 255, 0, 0, "stage one")
STAGE_ONE_LABEL = Label(s1_cords[0] + LABEL_PAD, s1_cords[1] + LABEL_PAD, s1_cords[2] + LABEL_PAD, s1_cords[3] + LABEL_PAD, "STAGE ONE", "stage one text", 20)

s2_cords = stage_grid_to_coords(4, 1)
STAGE_TWO_BOX = Rectangle(s2_cords[0], s2_cords[1], s2_cords[2], s2_cords[3], 0, 255, 0, "stage one")
STAGE_TWO_LABEL = Label(s2_cords[0] + LABEL_PAD, s2_cords[1] + LABEL_PAD, s2_cords[2] + LABEL_PAD, s2_cords[3] + LABEL_PAD, "STAGE TWO", "stage two text", 20)

s3_cords = stage_grid_to_coords(4, 2)
STAGE_THREE_BOX = Rectangle(s3_cords[0], s3_cords[1], s3_cords[2], s3_cords[3], 0, 0, 255, "stage one")
STAGE_THREE_LABEL = Label(s3_cords[0] + LABEL_PAD, s3_cords[1] + LABEL_PAD, s3_cords[2] + LABEL_PAD, s3_cords[3] + LABEL_PAD, "STAGE THREE", "stage three text", 20)

s4_cords = stage_grid_to_coords(4, 3)
STAGE_FOUR_BOX = Rectangle(s4_cords[0], s4_cords[1], s4_cords[2], s4_cords[3], 100, 0, 100, "stage one")
STAGE_FOUR_LABEL = Label(s4_cords[0] + LABEL_PAD, s4_cords[1] + LABEL_PAD, s4_cords[2] + LABEL_PAD, s4_cords[3] + LABEL_PAD, "STAGE FOUR", "stage four text", 20)

s5_cords = stage_grid_to_coords(4, 4)
STAGE_FIVE_BOX = Rectangle(s5_cords[0], s5_cords[1], s5_cords[2], s5_cords[3], 0, 150, 100, "stage one")
STAGE_FIVE_LABEL = Label(s5_cords[0] + LABEL_PAD, s5_cords[1] + LABEL_PAD, s5_cords[2] + LABEL_PAD, s5_cords[3] + LABEL_PAD, "STAGE FIVE", "stage five text", 20)

s6_cords = stage_grid_to_coords(3, 0)
STAGE_SIX_BOX = Rectangle(s6_cords[0], s6_cords[1], s6_cords[2], s6_cords[3], 150, 100, 0, "stage one")
STAGE_SIX_LABEL = Label(s6_cords[0] + LABEL_PAD, s6_cords[1] + LABEL_PAD, s6_cords[2] + LABEL_PAD, s6_cords[3] + LABEL_PAD, "STAGE SIX", "stage six text", 20)

STAGE_SELECT_BGRND = Rectangle(0,0,100,100, 255,255,255, "stage select background")

STAGE_SELECT_TEXTURE_MAP = {
    0: [STAGE_SELECT_BGRND], # TODO: add a background
    1: [STAGE_ONE_BOX, STAGE_TWO_BOX, STAGE_THREE_BOX, STAGE_FOUR_BOX, STAGE_FIVE_BOX, STAGE_SIX_BOX], # TODO: put rest of menu buttons at this layer
    2: [STAGE_ONE_LABEL, STAGE_TWO_LABEL, STAGE_THREE_LABEL, STAGE_FOUR_LABEL, STAGE_FIVE_LABEL, STAGE_SIX_LABEL]
}

TEST_CHARACTER = BaseCharacter(3.5, 3.5, 5, 5, 2, 7)
STAGE_SELECT_TEXTURE_MAP[3] = TEST_CHARACTER.getSprites()

STAGE_SELECT_MENU_TEXTURES = Textures(STAGE_SELECT_TEXTURE_MAP)
STAGE_SELECT_SCREEN = MainMenu(STAGE_SELECT_MENU_TEXTURES)


### ~~~ ### ~~~~~~ DEFINING STAGE CONSTANTS ~~~~~~ ### ~~~ ###


# ~~~~~~~~~~~~~ STAGE ONE: MIDDLE LAND OVER TWO HOLES OF DEATH ON THE SIDES ~~~~~~~~~~ #

STAGE_ONE_BGRND = Rectangle(0,0,100,100, 255,255,255, "stage one background")
STAGE_ONE_MAINSTAGE = BorderedRectangle(15,0,85,45,100,255,100, 20, "stage one main stage")
TEST_CHARACTER_2 = BaseCharacter(3.5, 3.5, 5, 5, 2, 7)

#HELL_DEMON = BaseCharacter(15, 12, 20, 19, 12, 9, 20)


STAGE_ONE_TEXTURE_MAP = {
    0: [STAGE_ONE_BGRND],
    1: [STAGE_ONE_MAINSTAGE]
}

STAGE_ONE_DYNAMIC_OBJECTS = [TEST_CHARACTER_2]
STAGE_ONE_TEXTURES = Textures(STAGE_ONE_TEXTURE_MAP)
STAGE_ONE_SCREEN = BattleStage(STAGE_ONE_TEXTURES)