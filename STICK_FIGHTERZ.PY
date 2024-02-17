""" EXECUTABLE GAME FILE """

import pyglet as pg
from utils.constants import *
from utils.utils import *
from objects.rendered_object import * 
from objects.event_handlers import * 
from objects.event_trackers import *
from objects.screen import *
from objects.game_state import GameState
from utils.object_constants import *

# ALL EVENT HANDLERS

MAIN_MENU_HANDLER = MainMenuEventHandler(MAIN_MENU_TEXTURE_MAP, MAIN_MENU_EVENT_HANDLERS)


START_MENU_HANDLER = MainMenuEventHandler(START_MENU_TEXTURE_MAP, START_MENU_EVENT_HANDLERS)

all_handlers = [MAIN_MENU_HANDLER, START_MENU_HANDLER]
str_to_handler = {
    "MAIN" : MAIN_MENU_HANDLER, 
    "START" : START_MENU_HANDLER
}

### ~~~ ### ~~~~~~ SETUP ~~~~~~ ### ~~~ ###

window = pg.window.Window(width=NUM_COLUMNS*TILE_SIZE, height=NUM_ROWS*TILE_SIZE, caption="STICK FIGHTERZ")

# Game state begins with Main menu screen and main menu handler
GAME_STATE = GameState(MAIN_MENU_SCREEN, MAIN_MENU_HANDLER, str_to_handler)

print(BOOT_MESSAGE)


### ~~~ ### ~~~~~~ EVENT HANDLERS ~~~~~~ ### ~~~ ###
@window.event 
def on_draw():
    """Main Render loop - dispatches """
    window.clear()


    GAME_STATE.renderScreen()

@window.event
def on_key_press(symbol: pg.window.key, modifiers):
    # TODO: use "press" to set player heading for continuous motion in update loop
    GAME_STATE.handleKeyboardEvent(symbol, False)

@window.event 
def on_key_release(symbol: pg.window.key, modifiers):
    # TODO: use "release" to stop player heading for continuous motion in update loop, AND to handle key clicks
    GAME_STATE.handleKeyboardEvent(symbol, True)

@window.event
def on_mouse_release(x, y, button, modifiers):
    GAME_STATE.handleMouseClickEvent(x, y)


# ACTUAL RENDER LOOP
pg.clock.schedule_interval(GAME_STATE.UPDATE_STATE, 1/REFRESH_RATE_HERTZ)
pg.app.run()