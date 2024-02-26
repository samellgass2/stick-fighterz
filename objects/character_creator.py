from objects.rendered_object import *
from math import atan2, degrees
import pyglet as pg
from utils.constants import *

def rotate_rendered_object(sprite, angle, point):
    """
    Rotate a sprite around a given point.
    
    Args:
    - sprite (pyglet.sprite.Sprite): The sprite to rotate.
    - angle (float): The angle in degrees to rotate the sprite.
    - point (tuple): The (x, y) point around which to rotate the sprite.
    """
    sprite.rotate(angle)
    # Adjust sprite position based on the rotation around the point
    #sprite.set_position(point[0] - sprite.width / 2, point[1] - sprite.height / 2)

def connect_sprites(base_sprite, attached_sprite, connection_point, offset_angle=0):
    """
    Position one sprite at a specific connection point on another sprite, with an optional rotation offset.
    
    Args:
    - base_sprite (pyglet.sprite.Sprite): The sprite to connect to.
    - attached_sprite (pyglet.sprite.Sprite): The sprite being connected.
    - connection_point (tuple): The (x, y) point on the base sprite to connect the attached sprite to.
    - offset_angle (float): Additional rotation angle for the attached sprite, relative to the base sprite's orientation.
    """
    # Calculate the angle between the sprites
    dx = connection_point[0] - base_sprite.x
    dy = connection_point[1] - base_sprite.y
    angle = atan2(dy, dx)
    degrees_angle = degrees(angle) + offset_angle
    
    # Set the position and rotation of the attached sprite
    attached_sprite.rotation = degrees_angle
    attached_sprite.set_position(connection_point[0], connection_point[1])

class DynamicObject(RenderedObject):
    """A rendered object of multiple sprites that move in tandem"""
    def __init__(self, sprites: "list[pg.sprite.Sprite]", name: str):
        self._sprites = sprites 
        self._dx = 5 
        self._dy = 5

    def getSprites(self) -> "list[pg.sprite.Sprite]":
        return self._sprites
    
    def getPosition(self):
        """On the base DynamicObject, the first _sprite's position is used for position"""
        return self._sprites[0].position()
    
    def draw(self):
        for sprite in self.getSprites():
            sprite.draw()

    def deltaX(self, allObjects, keyMapper):
        # TODO: for now all dynamic things except characters have no update rules
        return 0
        

    def deltaY(self, allObjects, keyMapper):
        # TODO: if on top of an object, no gravity. Else, gravity
        return 0


    def update_position(self, allObjects: "list[RenderedObject]", keyMapper: "dict[str, bool]"):
        deltaX = self.deltaX(allObjects, keyMapper)
        deltaY = self.deltaY(allObjects, keyMapper)
        for sprite in self.getSprites():
            sprite.update(x=sprite.x() + deltaX, y=sprite.y() + deltaY)


class BaseCharacter(DynamicObject):
    """A base character with scalable arms, legs, and head, with physics response ability"""
    def __init__(self, left_arm_len, right_arm_len, left_leg_len, right_leg_len, head_size, torso_len, speed=5):
        self._la_len = left_arm_len
        self._ra_len = right_arm_len
        self._ll_len = left_leg_len
        self._rl_len = right_leg_len 
        self._head_size = head_size 
        self._t_len = torso_len

        self._spritemap = self.base_sprites()
        self.moveSprite(NUM_COLUMNS // 2, NUM_ROWS // 2)

        # Leg animation starting moving opposite
        self.left_leg_dir = 1 
        self.right_leg_dir = -1

        # Position is defined as the middle of the ground beneath the character's feet, which starts at 0,0
        # TODO: these will be for internal record keeping later (x,y that is)
        self.x = 0 
        self.y = 0

        self._dx = speed
        self._dy = speed

    def getSprites(self):
        return self._spritemap.values()
    
    def getBottom(self):
        """Returns the rectangle hit box of the character's entire footing"""
        # TODO: calculate dynamically based on the legs' actual angle - for now just approximate with 90% leg len lmao

    def getPosition(self):
        # TODO: make this more accurate. For now, I am testing membership of middle of torso
        torso = self.getSprite("torso")
        return torso.getSprite().position
    
    def animate(self, keyMapper):
        if keyMapper["A"] or keyMapper["D"]:
            self.walkingAnimation()


    def getSprite(self, sprite=None) -> RenderedObject:
        if not sprite:
            return super().getSprite()
        else:
            return self._spritemap.get(sprite, None)

    def base_sprites(self):
        right_arm = Rectangle(0, 0, self._ra_len, ARM_WIDTH, 0, 0, 0, "left arm")
        rotate_rendered_object(right_arm, 60, [0,0])
        left_arm = Rectangle(0,0, self._la_len, ARM_WIDTH, 0, 0, 0, "right arm")
        rotate_rendered_object(left_arm, 120, [0,0])
        right_leg = Rectangle(0, 0, self._rl_len, LEG_WIDTH, 0, 0, 0, "left leg")
        rotate_rendered_object(right_leg, 80, [0,0])
        left_leg = Rectangle(0, 0, self._ll_len, LEG_WIDTH, 0, 0, 0, "right leg")
        rotate_rendered_object(left_leg, 100, [0,0])
        torso = Rectangle(-TORSO_WIDTH//2, 0, TORSO_WIDTH//2, self._t_len, 0, 0, 0, "torso")
        head = Circle(0, 0, self._head_size, 0, 0, 0, "head")

        # Torso atop legs
        torso.spriteDeltaX(to_screen_position_x(TORSO_WIDTH))
        torso.spriteDeltaY(-to_screen_position_y(2 * TORSO_WIDTH))

        # Head atop torso
        head.spriteDeltaY(to_screen_position_y(self._t_len))
        head.spriteDeltaX(-to_screen_position_x(TORSO_WIDTH -self._head_size // 2))

        # Arms halfway up torso
        left_arm.spriteDeltaY(to_screen_position_y(5 * self._t_len / 8))
        right_arm.spriteDeltaY(to_screen_position_y(5 * self._t_len / 8))
        return {"left arm": left_arm, "right arm": right_arm, "left leg": left_leg, 
                "right leg": right_leg, "torso": torso, "head": head}

    def moveSprite(self, deltaX, deltaY):
        for sprite in self.getSprites():
            sprite.spriteDeltaX(deltaX)
            sprite.spriteDeltaY(deltaY)

    def walkingAnimation(self, deltaTheta=5):
        left_leg = self.getSprite("left leg")
        left_leg_angle = left_leg.getSprite().rotation 
        right_leg = self.getSprite("right leg")
        right_leg_angle = right_leg.getSprite().rotation 

        new_left_angle = left_leg_angle + deltaTheta * self.left_leg_dir
        if new_left_angle >= LEG_MAX_ANGLE or new_left_angle <= LEG_MIN_ANGLE:
            self.left_leg_dir = -1 * self.left_leg_dir 
        left_leg.rotate(deltaTheta * self.left_leg_dir)

        new_right_angle = right_leg_angle + deltaTheta * self.right_leg_dir
        if new_right_angle >= LEG_MAX_ANGLE or new_right_angle <= LEG_MIN_ANGLE:
            self.right_leg_dir = -1 * self.right_leg_dir
        right_leg.rotate(deltaTheta * self.right_leg_dir)

    def render(self):
        for sprite in self.getSprites():
            sprite.draw()

    def deltaX(self, keyMapper, allObjects):
        # TODO: if key press and unobstructed left or right, go left or right
        # Will take STEP of +delta
        dx = 0 
        if keyMapper["A"]:
            dx = self._dx * -1
        elif keyMapper["D"]:
            dx = self._dx 

        if dx:
            new_position = self.getPosition()[0] + dx 
            for otherobj in allObjects:
                print("x={}, y={}, is inside = {}".format(new_position, self.getPosition()[1], otherobj.is_inside_box(new_position, self.getPosition()[1])))
                if otherobj.is_inside_box(new_position, self.getPosition()[1]):
                    return 0
                
            # If it is possible to make dx change without collision:
            return dx 
        
        return 0
    
    def deltaY(self, keyMapper, allObjects):
        # TODO: handle jumping & falling
        return 0
    
    def update_position(self, allObjects: "list[RenderedObject]", keyMapper: "dict[str, bool]"):
        deltaX = self.deltaX(keyMapper, allObjects)
        deltaY = self.deltaY(keyMapper, allObjects)
        for sprite in self.getSprites():
            sprite.spriteDeltaX(deltaX)
            sprite.spriteDeltaY(deltaY)





