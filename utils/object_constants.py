from objects.rendered_object import RenderedObject
import pyglet as pg 
from utils.utils import *
from utils.constants import *
from objects.screen import Screen, Textures, MainMenu
from objects.event_trackers import MainMenuEventHandler

### ~~~ ### ~~~~~~ DEFINING OBJECT STATE CONSTANTS ~~~~~~ ### ~~~ ###


# ~~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~ #
MENU_BGRND = RenderedObject(pg.shapes.Rectangle(0,0, width=NUM_COLUMNS*TILE_SIZE, height=NUM_ROWS*TILE_SIZE, color=(255,255,255)), "menu background") #bgrnd size = size of da window
BOTTOM_HALF_OF_SREEN = RenderedObject(pg.shapes.Rectangle(0,0, width=NUM_COLUMNS*TILE_SIZE/2, height=NUM_ROWS*TILE_SIZE/2, color=(0,0,0)), "test box") # TEST OBJECT 4 RENDER
CHARACTER_SELECT_BUTTON = RenderedObject(pg.shapes.Rectangle(to_screen_position_x(5), to_screen_position_y(20), endpoint_to_width(5, 45), endpoint_to_height(20, 80), color=(255,0,0)), "char select button")
CHARACTER_SELECT_BUTTON_LABEL = RenderedObject(pg.text.Label(text=CHARACTER_SELECT_TEXT, font_size=38, x = to_screen_position_x(15), y = to_screen_position_y(45), 
                                                             width=endpoint_to_width(15, 25), height=endpoint_to_height(45, 65), multiline=True, color=(0,0,0,255),
                                                             anchor_x='center', anchor_y='center'), "char select label")
START_BUTTON = RenderedObject(pg.shapes.Rectangle(to_screen_position_x(55), to_screen_position_y(20), endpoint_to_width(55, 95), endpoint_to_height(20, 80), color=(0,255,0)), "game start button")
START_BUTTON_LABEL = RenderedObject(pg.text.Label(text=START_GAME_TEXT, font_size=38, x = to_screen_position_x(75), y = to_screen_position_y(45), 
                                                             width=endpoint_to_width(75, 85), height=endpoint_to_height(45, 65), multiline=True, color=(0,0,0,255),
                                                             anchor_x='center', anchor_y='center'), "char select label")


MAIN_MENU_TEXTURE_MAP = {
    0: [MENU_BGRND, BOTTOM_HALF_OF_SREEN], # TODO: add a background
    1: [CHARACTER_SELECT_BUTTON, START_BUTTON], # TODO: put rest of menu buttons at this layer
    2: [CHARACTER_SELECT_BUTTON_LABEL, START_BUTTON_LABEL]
}

    
MAIN_MENU_TEXTURES = Textures(MAIN_MENU_TEXTURE_MAP)
MAIN_MENU_SCREEN = MainMenu(MAIN_MENU_TEXTURES)

# ~~~~~~~~~~~~~ START MENU ~~~~~~~~~~ #

START_MENU_BGRND = RenderedObject(pg.shapes.Rectangle(0,0, width=NUM_COLUMNS*TILE_SIZE, height=NUM_ROWS*TILE_SIZE, color=(0,0,0)), "start menu background") #bgrnd size = size of da window
START_MENU_BOTTOM_HALF_OF_SREEN = RenderedObject(pg.shapes.Rectangle(0,0, width=NUM_COLUMNS*TILE_SIZE/2, height=NUM_ROWS*TILE_SIZE/2, color=(0,0,0)), "test box") # TEST OBJECT 4 RENDER
ONE_PLAYER_BUTTON = RenderedObject(pg.shapes.BorderedRectangle(to_screen_position_x(10), to_screen_position_y(50), endpoint_to_width(10, 50), endpoint_to_height(50, 80), color=(255,0,0)), "one player button")
ONE_PLAYER_BUTTON_LABEL = RenderedObject(pg.text.Label(text=SINGLE_PLAYER_TEXT, font_size=20, x = to_screen_position_x(20), y = to_screen_position_y(70), 
                                                             width=endpoint_to_width(20, 40), height=endpoint_to_height(60, 80), multiline=True, color=(0,0,0,255),
                                                             anchor_x='center', anchor_y='center'), "single player label")
TWO_PLAYER_BUTTON = RenderedObject(pg.shapes.BorderedRectangle(to_screen_position_x(10), to_screen_position_y(10), endpoint_to_width(10, 50), endpoint_to_height(10, 40), color=(100,100,100)), "two player button")
TWO_PLAYER_BUTTON_LABEL = RenderedObject(pg.text.Label(text=TWO_PLAYER_TEXT, font_size=20, x = to_screen_position_x(20), y = to_screen_position_y(20), 
                                                             width=endpoint_to_width(20, 40), height=endpoint_to_height(20, 40), multiline=True, color=(0,0,0,255),
                                                             anchor_x='center', anchor_y='center'), "two player label")
BACK_BUTTON = RenderedObject(pg.shapes.BorderedRectangle(to_screen_position_x(65), to_screen_position_y(15), endpoint_to_width(60, 80), endpoint_to_height(15, 30), color=(255,0,0)), "back button")
BACK_BUTTON_LABEL = RenderedObject(pg.text.Label(text=BACK_TEXT, font_size=15, x = to_screen_position_x(75), y = to_screen_position_y(20), 
                                                             width=endpoint_to_width(70, 80), height=endpoint_to_height(20, 25), multiline=True, color=(0,0,0,255),
                                                             anchor_x='center', anchor_y='center'), "back button label")

START_MENU_TEXTURE_MAP = {
    0: [START_MENU_BGRND, START_MENU_BOTTOM_HALF_OF_SREEN], # TODO: add a background
    1: [ONE_PLAYER_BUTTON, TWO_PLAYER_BUTTON, BACK_BUTTON], # TODO: put rest of menu buttons at this layer
    2: [ONE_PLAYER_BUTTON_LABEL, TWO_PLAYER_BUTTON_LABEL, BACK_BUTTON_LABEL]
}
    
START_MENU_TEXTURES = Textures(START_MENU_TEXTURE_MAP)
START_MENU_SCREEN = MainMenu(START_MENU_TEXTURES)