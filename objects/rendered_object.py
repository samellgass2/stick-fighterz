"""The classes for all of the polygons to be rendered, with the knowledge of how to update themselves"""
import pyglet as pg


class RenderedObject:
    """A Rendered Object is an "object" that knows its position, update behavior, and sprite"""
    def __init__(self, sprite: pg.sprite.Sprite, name: str="renderedObject"):
        # TODO: for now, we are assuming all sprites are square, so let us abstract away for now the idea of collision 
        # Every sprite instead will just have a method "IS INSIDE" and "NEAREST EDGE" that will allow us to handle collision
        # e.g. fighting cleanly
        self._sprite = sprite 
        self.name = name
        self.x = sprite.x 
        self.y = sprite.y  
        self.width = sprite.width 
        self.height = sprite.height
        # NOTE: WE ARE ASSUMING ALL SPRITES ARE THE SAME SIZE. or at least we use the first seen sprite to determine hit box


        # NOTE: location will be updated on the underlying sprite itself, which causes it to render where it is expected

    def __str__(self):
        return f"{self.name} with x={self.x}, y={self.y}, width={self.width}, height={self.height}"

    def update_sprite(self, onclick: "function"):
        # use game state if it makes sense to  
        #self._sprite
        pass

    def getSprite(self) -> pg.sprite.Sprite:
        return self._sprite

    def is_inside_sprite(self, screen_x: int, screen_y: int):
        """Returns true if the provided point is inside of the sprite, or touching its edges (>=)"""
        spriteX, spriteY = self.getSprite().position
        spriteMaxX = self.getSprite().width + spriteX 
        spriteMaxY = self.getSprite().height + spriteY
        return not (spriteX <= screen_x and screen_x <= spriteMaxX and spriteY <= screen_y and screen_y <= spriteMaxY)
    
    def setBatch(self, batch: pg.graphics.Batch):
        self.getSprite().batch = batch
    

