"""Situation event trackers and utilities: """
import pyglet as pg

class MouseLocation:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def position(self) -> "tuple[int, int]":
        return self.x, self.y
    
class SpriteClickHandler:
    def __init__(self, x, y, width, height, onClick: "function", is_solid=True):
        self._x = x 
        self._y = y 
        self.width = width 
        self.height = height 
        self._onClickFunction = onClick
        self.is_solid = is_solid

    def is_inside_box(self, x, y) -> bool:
        return (self._x <= x <= self._x+self.width and self._y <= y <= self._y + self.height) and self.is_solid
    
    def onClick(self, **kwargs):
        return self._onClickFunction(**kwargs)


class EventTracker:
    """A class to keep track of window events and maintain player state"""
    def __init__(self):
        self._keyMapper = {sym : False for sym in ["W", "A", "S", "D"]} # TODO: codify this more seriously and concretely in the constants
        self._lastKeyMapper = {}
        self._mouseClickQueue = []
    
    def updateKeyMap(self, symbol: pg.window.key, newvalue: bool):
        if symbol == pg.window.key.S:
            self._keyMapper["S"] = newvalue
        elif symbol == pg.window.key.D:
            self._keyMapper["D"] = newvalue
        elif symbol == pg.window.key.A:
            self._keyMapper["A"] = newvalue 
        elif symbol == pg.window.key.W:
            self._keyMapper["W"] = newvalue

    def processTextureMap(self, textureMap: "dict[int, pg.sprite.Sprite]", eventHandlers: "list[function]") -> "list[SpriteClickHandler]":
        all_boxes = []
        all_textures = []
        [all_textures.extend(textureMap.get(level)) for level in textureMap.keys()]
        if len(all_textures) != len(eventHandlers):
            print("ERROR: LEN(TEXTURE MAP) {} != LEN(EVENT HANDLERS){} IN MAIN MENU HANDLER".format(len(all_textures), len(eventHandlers)))
            return []
        
        # Make level 0 textures NON-solid
        bgrnd_textures = len(textureMap.get(0, 0))
        ind = 0
        for sprite, handler in zip(all_textures, eventHandlers): 
            is_solid = ind >= bgrnd_textures
            all_boxes.append(SpriteClickHandler(sprite.x, sprite.y, sprite.width, sprite.height, handler, is_solid))
            ind += 1


        # LOGIC NOTE: since we have appended the textures from bottom level up, we want to reverse this list, 
        # since click priority etc should go to top layer textures
        return list(reversed(all_boxes))

    def processKeyMap(self):
        """Dummy method for menus"""
        return

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
    
    def HandleKeyPress(self, symbol: pg.window.key, key_released):
        self.updateKeyMap(symbol, key_released) 
        

    def HandleMouseClick(self, mouse_x: int, mouse_y: int):
        # TODO: plan as of now is to process as a FIFO queue, with all stacked locations being popped off from the beginning (but should be small so
        # handling as a list LOL)
        self.updateMouseClickQueue(MouseLocation(mouse_x, mouse_y))

    def UpdateDynamicElements(self):
        pass

    def getDynamicElements(self):
        return []


class MainMenuEventHandler(EventTracker):
    """The Event handler inherits from event tracker - keeps track of what is happening with user input and responds"""
    def __init__(self, textureMap: "dict[int, pg.sprite.Sprite]", eventHandlers: "list[function]"):
        super().__init__() 
        self._clickableTextures = self.processTextureMap(textureMap, eventHandlers)

    def updateMouseClick(self, mouseLocation: MouseLocation, GAME_STATE: "GameState") -> "dict":
        for loc in self._clickableTextures: 
            x,y = mouseLocation.position()
            if loc.is_inside_box(x,y):
                results_dict = loc.onClick(GAME_STATE = GAME_STATE)
                results_dict["response"] = True 
                return results_dict 
        return {}
    

class SinglePlayerBattleStageEventHandler(EventTracker):
    """The battle stage handler inherits the event tracker, and also processes player interaction
        as well as eventually an AI agent response. THIS OBJECT is responsible for the stateful version of dynamic elements.
    """

    # A battle stage handler takes in dynamic textures: player models
    def __init__(self, textureMap: "dict[int, pg.sprite.Sprite]", eventHandlers: "list[function]", dynamicObjects: "list[RenderedObject]"):
        super().__init__() 
        self._clickableTextures = self.processTextureMap(textureMap, eventHandlers)
        self._dynamicElements = dynamicObjects

    def getDynamicElements(self) -> "list[RenderedObject]":
        return self._dynamicElements
    
    def processKeyMap(self):
        keyMap = self.getCurrentKeyMap()
        for obj in self.getDynamicElements():
            obj.update_position(self._clickableTextures, keyMap)



    
    

