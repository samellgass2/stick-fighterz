"""GameState aims to encapsulate the event handlers, screen render, and save-level logic"""
from objects.screen import Screen
from utils.constants import *
from objects.event_trackers import EventTracker

class GameState:
    """Game Manager: Determines current screen, current controls, and current textures"""

    def __init__(self, screen: Screen, eventTracker: EventTracker, eventTrackerMapper: "dict[str,EventTracker]"):
        self._screen = screen 
        self._keyboardLocked = False 
        self._mouseClickLocked = False 
        self._eventTracker = eventTracker
        self._allEventTrackers = eventTrackerMapper

    # ~~~~~~~~~~~~~ MAIN UPDATE LOOP ~~~~~~~~~~ #
    def UPDATE_STATE(self, dt):
        # TODO: this is the big, main logical piece of the project
        # 1. Must account for any player movements that have occurred 

        # TODO: handle keys
        current_pressed_keys = self.getEventTracker().getCurrentKeyMap()

        # TODO: handle mice 
        for mouseLocation in self.getEventTracker().getMouseClickQueue():
            settingsChanges = self.getEventTracker().updateMouseClick(mouseLocation, self)
            if settingsChanges.get("response",""):
                print(settingsChanges)
                self.handleSettingsChange(settingsChanges)

        self.getEventTracker().clearMouseClickQueue()


        # TODO: handle animations 

        # TODO: handle state changes (?) how will we switch menus? maybe leave a "Transformer" object to tell you where to go next
        


    # ~~~~~~~~~~~~~ MAIN UPDATE LOOP ~~~~~~~~~~ #

    def handleSettingsChange(self, settingsChange: "dict"):
        if settingsChange.get("screen", None):
            self.setScreen(settingsChange["screen"])
        if settingsChange.get("eventtracker", None):
            # NOTE: must go through a layer of indirection here to get to event trackers sent by event tracker
            tracker = self._allEventTrackers.get(settingsChange["eventtracker"])
            self.setEventTracker(tracker)

    def setScreen(self, new_screen: Screen):
        self._screen = new_screen 

    def getScreen(self) -> Screen:
        return self._screen
    
    def getEventTracker(self) -> EventTracker:
        return self._eventTracker
    
    def setEventTracker(self, eventTracker: EventTracker):
        self._eventTracker = eventTracker

    def renderScreen(self):
        return self.getScreen().render()
    
    def isKeyboardLocked(self) -> bool:
        return self._keyboardLocked 
    
    def setKeyboardLock(self, state: bool) -> bool:
        self._keyboardLocked = state 

    def isMouseClickLocked(self) -> bool:
        return self._mouseClickLocked

    def setMouseClickLock(self, state: bool):
        self._mouseClickLocked = state 
    
    def handleKeyboardEvent(self, symbol: pg.window.key, key_released: bool):
        if not self.isKeyboardLocked():
            # TODO: for both this and the mouse - decide at THIS LEVEL whether to dispatch through screen or through a standalone "event handler"
            self.getEventTracker().HandleKeyPress(symbol, key_released) 
        
    def handleMouseClickEvent(self, mouse_x: int, mouse_y: int):
        if not self.isMouseClickLocked():
            self.getEventTracker().HandleMouseClick(mouse_x, mouse_y)