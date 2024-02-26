from utils.object_constants import MAIN_MENU_SCREEN, START_MENU_SCREEN, STAGE_SELECT_SCREEN, STAGE_ONE_SCREEN

def ToStartHandler(**kwargs):
    return {
        "state reached": "start menu", 
        "screen" : START_MENU_SCREEN,
        "eventtracker": "START"
        }

def ToMainHandler(**kwargs):
    return {
        "state reached": "main menu",
        "screen" : MAIN_MENU_SCREEN, 
        "eventtracker": "MAIN"
    }

def ToStageSelectHandler(**kwargs):
    return {
        "state reached": "stage select",
        "screen" : STAGE_SELECT_SCREEN,
        "eventtracker": "STAGE SELECT" # TODO make sure this works here
    }

def ToStageOneHandler(**kwargs):
    return {
        "state reached": "stage one",
        "screen" : STAGE_ONE_SCREEN,
        "eventtracker": "STAGE ONE"
    }

def BasicPrintStateHandler(**kwargs):
    GAME_STATE = kwargs.get("GAME_STATE") 
    return {"state reached": "the basic print state handler"}

START_MENU_EVENT_HANDLERS = [
    BasicPrintStateHandler, 
    BasicPrintStateHandler,
    ToStageSelectHandler, 
    ToStageSelectHandler,
    ToMainHandler,
    ToStageSelectHandler,
    ToStageSelectHandler,
    ToMainHandler
]

MAIN_MENU_EVENT_HANDLERS = [
    BasicPrintStateHandler, 
    BasicPrintStateHandler,
    BasicPrintStateHandler, 
    ToStartHandler,
    BasicPrintStateHandler,
    ToStartHandler 
]

STAGE_SELECT_EVENT_HANDLERS = [BasicPrintStateHandler for i in range(19)]
STAGE_SELECT_EVENT_HANDLERS[1] = ToStageOneHandler

STAGE_ONE_EVENT_HANDLERS = [BasicPrintStateHandler for i in range(2)]