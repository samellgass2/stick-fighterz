"""A Screen object renders all of the present objects to the screen""" 
import pyglet as pg 
from objects.rendered_object import RenderedObject

class Textures:
    """An object to hold all of the current environment's RenderedObjects, by level, with attributes"""
    def __init__(self, texturesByLevel: "dict[int, list[RenderedObject]]"):
        self._textureMap = texturesByLevel 
        if texturesByLevel: 
            self._levels = len(texturesByLevel)
        else:
            self._levels = 1 # TODO: does this default even make sense lmao
        self._batchesByLevel = {level: pg.graphics.Batch() for level in range(self._levels)}

    def get_textures_by_level(self, level: int) -> "list[RenderedObject]":
        """Gets all the RenderedObjects for level n of the texture map, or returns an empty list if no such level exists"""
        return self._textureMap.get(level, [])
    
    def getBatches(self, level=None) -> "list[pg.graphics.Batch]":
        if level:
            return self._batchesByLevel.get(level, {})
        else:
            return list(self._batchesByLevel.values())
    
    
    def render(self, levels:int=None):
        # Allow for only rendering a subset of levels
        if not levels:
            levels = self._levels 
        
        # Assign textures to correct batch (TODO: see if we always need to do this or if it should be in an UPDATE before RENDER step)
        for level in range(levels):
            for rendered_object in self.get_textures_by_level(level):
                rendered_object.draw()
                #rendered_object.setBatch(self.getBatches(level)) TODO: if it gets much more demanding,
                # do batching and fix the garbage collector
                
        # Render everything
        #for batch in self.getBatches():
            #batch.draw()
                
    


class Screen: 
    """The rendering and logic for the current menu / encounter"""
    def __init__(self, textures: Textures):
        self._textures = textures 

    def setTextures(self, textures: Textures):
        self._textures = textures 

    def getTextures(self) -> Textures:
        return self._textures

    def render(self, dynamicElements: "list[RenderedObject]"):
        self.getTextures().render() 
        for element in dynamicElements:
            element.render()



class MainMenu(Screen): 
    """The main menu screen"""
    # TODO: save data gets passed in here - maybe by the gamestate though
    def __init__(self, menuTextures: Textures):
        super().__init__(menuTextures)

    def render(self, dynamicElements=None):
        # TODO: put any main menu specific render rules here, e.g. a beginning animation
        self.getTextures().render()


class BattleStage(Screen):
    """Generic battle screen"""
    def __init__(self, allTextures):
        super().__init__(allTextures)

    def render(self, dynamicElements):
        # TODO: handle dynamic effects here
        self.getTextures().render()
        for element in dynamicElements:
            element.render()

