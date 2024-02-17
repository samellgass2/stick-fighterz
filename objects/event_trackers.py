"""Situation event trackers and utilities: """
import pyglet as pg

class MouseLocation:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def position(self) -> "tuple[int, int]":
        return self.x, self.y
    
class SpriteClickHandler:
    def __init__(self, x, y, width, height, onClick: "function"):
        self._x = x 
        self._y = y 
        self.width = width 
        self.height = height 
        self._onClickFunction = onClick

    def is_inside_box(self, x, y) -> bool:
        return (self._x <= x <= self._x+self.width and self._y <= y <= self._y + self.height)
    
    def onClick(self, **kwargs):
        return self._onClickFunction(**kwargs)


class EventTracker:
    """A class to keep track of window events and maintain player state"""
    def __init__(self):
        self._keyMapper = {sym : False for sym in pg.window.key._key_names}
        self._lastKeyMapper = {}
        self._mouseClickQueue = []
    
    def updateKeyMap(self, symbol: pg.window.key, newvalue: bool):
        if symbol in self._keyMapper: 
            self._keyMapper[symbol] = newvalue 

    def getCurrentKeyMap(self) -> "dict[str, bool]":
        return self._keyMapper 
    
    def getMouseClickQueue(self) -> MouseLocation: 
        oldQueue = self._mouseClickQueue
        #self._mouseClickQueue = []
        return oldQueue
    
    def clearMouseClickQueue(self):
        self._mouseClickQueue = []

    def updateMouseClickQueue(self, mouseLoc: MouseLocation):
        self._mouseClickQueue.append(mouseLoc)
    
    def HandleKeyPress(self, symbol: pg.window.key):
        self.updateKeyMap(symbol, True) 

    def HandleKeyRelease(self, symbol: pg.window.key):
        self.updateKeyMap(symbol, False)
        

    def HandleMouseClick(self, mouse_x: int, mouse_y: int):
        # TODO: plan as of now is to process as a FIFO queue, with all stacked locations being popped off from the beginning (but should be small so
        # handling as a list LOL)
        self.updateMouseClickQueue(MouseLocation(mouse_x, mouse_y))


class MainMenuEventHandler(EventTracker):
    """The Event TRACKER - keeps track of what is happening with user input and """
    def __init__(self, textureMap: "dict[int, pg.sprite.Sprite]", eventHandlers: "list[function]"):
        super().__init__() 
        self._clickableTextures = self.processTextureMap(textureMap, eventHandlers)

    def processTextureMap(self, textureMap: "dict[int, pg.sprite.Sprite]", eventHandlers: "list[function]") -> "list[SpriteClickHandler]":
        all_boxes = []
        all_textures = []
        [all_textures.extend(textureMap.get(level)) for level in textureMap.keys()]
        if len(all_textures) != len(eventHandlers):
            print("ERROR: LEN(TEXTURE MAP) {} != LEN(EVENT HANDLERS){} IN MAIN MENU HANDLER".format(len(all_textures), len(eventHandlers)))
            return []
        for sprite, handler in zip(all_textures, eventHandlers): 
            all_boxes.append(SpriteClickHandler(sprite.x, sprite.y, sprite.width, sprite.height, handler))

        return all_boxes
    
    def updateMouseClick(self, mouseLocation: MouseLocation, GAME_STATE: "GameState") -> "dict":
        for loc in self._clickableTextures: 
            x,y = mouseLocation.position()
            if loc.is_inside_box(x,y):
                results_dict = loc.onClick(GAME_STATE = GAME_STATE)
                results_dict["response"] = True 
                return results_dict 
        return {}



