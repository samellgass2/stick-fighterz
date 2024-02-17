from utils.object_constants import MAIN_MENU_SCREEN, START_MENU_SCREEN

def MainMenuToCharacterSelectHandler(**kwargs):
    GAME_STATE = kwargs.get("GAME_STATE")
    # TODO: make this change to character select

def MainMenuToStartMenuSelectHandler(**kwargs):
    return {
        "state reacHed": "start menu", 
        "screen" : START_MENU_SCREEN,
        "eventtracker": "START"
        }

def SelectMenuToMainMenuSelectHandler(**kwargs):
    return {
        "state reached": "main menu",
        "screen" : MAIN_MENU_SCREEN, 
        "eventtracker": "MAIN"
    }

def BasicPrintStateHandler(**kwargs):
    GAME_STATE = kwargs.get("GAME_STATE") 
    return {"state reached": "the basic print state handler"}

START_MENU_EVENT_HANDLERS = [
    SelectMenuToMainMenuSelectHandler, 
    SelectMenuToMainMenuSelectHandler,
    SelectMenuToMainMenuSelectHandler, 
    SelectMenuToMainMenuSelectHandler,
    SelectMenuToMainMenuSelectHandler,
    SelectMenuToMainMenuSelectHandler,
    SelectMenuToMainMenuSelectHandler,
    SelectMenuToMainMenuSelectHandler
]

MAIN_MENU_EVENT_HANDLERS = [
    MainMenuToStartMenuSelectHandler, 
    MainMenuToStartMenuSelectHandler,
    MainMenuToStartMenuSelectHandler, 
    MainMenuToStartMenuSelectHandler,
    MainMenuToStartMenuSelectHandler,
    MainMenuToStartMenuSelectHandler 
]