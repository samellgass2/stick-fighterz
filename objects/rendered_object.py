"""The classes for all of the polygons to be rendered, with the knowledge of how to update themselves"""
import pyglet as pg
from utils.utils import *


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
        if hasattr(sprite, "width"):
            self.width = sprite.width 
        if hasattr(sprite, "height"):
            self.height = sprite.height
        if hasattr(sprite, "radius"):
            self.height = sprite.radius 
            self.width = sprite.radius      # TODO: uh make this maeth work lmao
        # NOTE: WE ARE ASSUMING ALL SPRITES ARE THE SAME SIZE. or at least we use the first seen sprite to determine hit box


        # NOTE: location will be updated on the underlying sprite itself, which causes it to render where it is expected

    def __str__(self):
        return f"{self.name} with x={self.x}, y={self.y}, width={self.width}, height={self.height}"

    def update_sprite(self, onclick: "function"):
        # use game state if it makes sense to  
        #self._sprite
        pass

    def rotate(self, angle):
        self.getSprite().rotation = self.getSprite().rotation + angle

    def set_position(self, x, y):
        self.getSprite().x = x
        self.getSprite().y = y

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

    def spriteDeltaX(self, x):
        """Changes the sprite by x px"""
        self.getSprite().x = self.getSprite().x + x #to_screen_position_x(x)

    def spriteDeltaY(self, y):
        """Changes the sprite by y px"""
        self.getSprite().y = self.getSprite().y + y #to_screen_position_y(y)

    def draw(self):
        self.getSprite().draw()
    

### ~~~ Helper generator functions ~~~ ###
def Rectangle(x, y, x_end, y_end, r, g, b, name="") -> RenderedObject:
    return RenderedObject(pg.shapes.Rectangle(to_screen_position_x(x), to_screen_position_y(y), 
                                              endpoint_to_width(x, x_end), endpoint_to_height(y, y_end), 
                                              color=(r,g,b)), name)

def BorderedRectangle(x, y, x_end, y_end, r, g, b, border, name="") -> RenderedObject:
    return RenderedObject(pg.shapes.BorderedRectangle(to_screen_position_x(x), to_screen_position_y(y), 
                                              endpoint_to_width(x, x_end), endpoint_to_height(y, y_end), 
                                              color=(r,g,b), border=border), name)

def Label(x, y, x_end, y_end, text, name, font_size, r=0, g=0, b=0, z=255) -> RenderedObject:
    return RenderedObject(pg.text.Label(text=text, font_size=font_size, x = to_screen_position_x(x), y = to_screen_position_y(y), 
                                                             width=endpoint_to_width(x, x_end), height=endpoint_to_height(y, y_end), multiline=True, color=(r,g,b,z),
                                                             anchor_x='center', anchor_y='center'), name)

def Circle(x, y, rad, r, g, b, name) -> RenderedObject:
    return RenderedObject(pg.shapes.Circle(to_screen_position_x(x), to_screen_position_y(y), to_screen_position_x(rad), color=(r,g,b)), name)