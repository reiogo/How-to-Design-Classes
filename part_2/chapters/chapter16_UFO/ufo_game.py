from typing import Protocol
from dataclasses import dataclass
import math
from .canvas_library import Color, Posn, ICanvas
from . import canvas_library as canvas

#CHAPTER 16  Designing Methods =============================================================================
# Library defined in canvas_library to help with graphical interpretation
# I decided to upgrade to pygame
@dataclass
class UFOWorld:
    ufo:UFO
    aup:AUP
    shots:IShots

    HEIGHT:int = 500
    WIDTH:int = 200
    BACKG:Color = canvas.BLUE

    def __repr__(self):
        return f"[UFO: {self.ufo}\nShots: {self.shots}\nAUP: {self.aup}]"

    # draw this world
    def draw(self, c:ICanvas) -> bool:
        # ... self.BACKG .. self.HEIGHT ... self.WIDTH
        # self.ufo.draw(...) ... self.aup.draw(...) ... self.shots.draw(...)
        return (c.drawRect(Posn(0,0), self.WIDTH, self.HEIGHT, self.BACKG)
                    and self.ufo.draw(c)
                    and self.aup.draw(c, self.HEIGHT)
                    and self.shots.draw(c))

    # move the objects in this world
    def move(self) -> UFOWorld:
        # self.BACKG ... self.HEIGHT .. self.WIDTH 
        #... self.ufo.move(...) ... self.aup.move(...) ... self.shots.move(...)
        return UFOWorld(self.ufo.move(), self.aup, self.shots.move())

    # fire a shot in this world
    def shoot(self) -> UFOWorld:
        #... self.ufo.shoot(...) ... self.aup.shoot(...) ... self.shots.shoot(...)
        return UFOWorld(self.ufo,
                        self.aup,
                        ConsShots(self.aup.fireShot(self), self.shots))

# a UFO: its center is at location
@dataclass
class UFO:
    location:Posn
    colorUFO:Color = canvas.GREEN

    GROUND:int = 500
    UFO_UNIT:int = 14
    UFO_WIDTH:int = UFO_UNIT * 3
    UFO_BAR_HEIGHT:int = UFO_UNIT * 1

    def __repr__(self):
        return f"[UFO: {self.location}]"

    # draw this UFO
    def draw(self, c:ICanvas) -> bool:
        return(
            c.drawDisk(self.location, self.UFO_UNIT, self.colorUFO)
            and c.drawRect(Posn(self.location.x - (self.UFO_WIDTH//2),
                                self.location.y - (self.UFO_BAR_HEIGHT//2)),
                           self.UFO_WIDTH, self.UFO_BAR_HEIGHT,
                           self.colorUFO)
        )
    # has this UFO landed yet?
    def landed(self) -> bool:
        if self.location.y == self.GROUND:
            return True
        else:
            return False

    # is this UFO about to land?
    def closeToGround(self) -> bool:
        # ... self.location ... self.GROUND
        if self.location.y + 3 >= self.GROUND:
            return True
        else:
            return False

    # drop this UFO
    def move(self) -> UFO:
        #...w... self.location ... self.colorUFO
        if self.landed():
            return self
        else:
            if self.closeToGround():
                return UFO(Posn(self.location.x, self.GROUND), self.colorUFO)
            else:
                return UFO(Posn(self.location.x, self.location.y + 3), self.colorUFO)



# an anti-UFO platform: its left corner is location pixels from the left
# at the bottom of the world
@dataclass
class AUP:
    location:int
    aupColor:Color = canvas.RED

    AUP_UNIT = 1
    AUP_HEIGHT = AUP_UNIT * 10
    AUP_WIDTH = AUP_UNIT * 40
    AUP_CANNON_HEIGHT = AUP_UNIT * 10
    AUP_CANNON_WIDTH = AUP_UNIT * 8

    def __repr__(self):
        return f"[AUP: {self.location}]"

    # draw this AUP
    def draw(self, c:ICanvas, height:int) -> bool:
        return(
            c.drawRect(Posn(self.location,
                            height - self.AUP_HEIGHT),
                       self.AUP_WIDTH, self.AUP_HEIGHT, canvas.BLACK)
            and
            c.drawRect(Posn((self.location
                            +(self.AUP_WIDTH//2)
                            - (self.AUP_CANNON_WIDTH//2)),
                            (height
                             - self.AUP_HEIGHT
                             - self.AUP_CANNON_HEIGHT)),
                       self.AUP_CANNON_WIDTH,
                       self.AUP_CANNON_HEIGHT,
                       canvas.BLACK)
        )
    # create a shot at the middle of this platform
    def fireShot(self, w:UFOWorld) ->Shot:
        # ... self.location
        return Shot(
                Posn(self.location
                     + ((self.AUP_WIDTH//2) - (self.AUP_CANNON_WIDTH//4)),
                    w.HEIGHT - (self.AUP_HEIGHT
                                +(2 * self.AUP_CANNON_HEIGHT))))

# a shot in flight, whose upper left corner is located at location
@dataclass
class Shot:
    location:Posn
    shotClr:Color = canvas.YELLOW

    SHOT_WIDTH = 4
    SHOT_HEIGHT = 2*SHOT_WIDTH

    def __repr__(self):
        return f"[Shot: {self.location}]"

    # draw this shot
    def draw(self, c:ICanvas) -> bool:
        return (c.drawRect(self.location, self.SHOT_WIDTH, self.SHOT_HEIGHT, self.shotClr))

    # move this shot by 3 pixels upwards
    def move(self) -> Shot:
        return Shot(Posn(self.location.x, self.location.y - 3), self.shotClr)

#interface
@dataclass
class IShots(Protocol):
    # draw this list of shots
    def draw(self, c:ICanvas) -> bool:
        ...

    # move this list of shots
    def move(self) -> IShots:
        ...

#implements IShots
@dataclass
class MTShots(IShots):
    def __repr__(self):
        return f"[Empty Shot]"

    def draw(self, c:ICanvas) -> bool:
        return True

    def move(self) -> IShots:
        return self

#implements IShots
@dataclass
class ConsShots(IShots):
    fst:Shot
    rst:IShots

    def __repr__(self):
        return f"[{self.fst} | {self.rst}]"

    def draw(self, c:ICanvas) -> bool:
        #self.fst.draw() ... self.rst.draw()
        return(self.fst.draw(c) and self.rst.draw(c))

    def move(self) -> IShots:
        # if the shot is off screen remove from list
        if self.fst.location.y < 0:
            return self.rst.move()
        else:
            return  ConsShots(self.fst.move(), self.rst.move())


# RUN ========================================================================================== 

# Example1  =========================================================
# aup = AUP(50) # place aup at the bottom
# ufo = UFO(Posn(0,0)) # place ufo at the top left corner

# shot1 = Shot(Posn(300,90)) # shoot shot
# shot2 = Shot(Posn(350,90)) # shot is lower than shot1
# shots = ConsShots(shot1, ConsShots(shot2, MTShots()))
# c = LogCanvas(200,500)
# shots.draw(c)
# aup.draw(c)
# ufo.draw(c)
# c.show()

