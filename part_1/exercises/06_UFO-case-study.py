from dataclasses import dataclass
from typing import Protocol
from typing import Union

# LIBRARY CODE ==========================================================================================
# asked ai to help me build the framework

@dataclass
class Posn:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x},{self.y})"

def tick(world: World) -> World:
    return world.move().handle_collisions()


def run(world: World, steps: int) -> None:
    for i in range(steps):
        print(f"tick {i}: {world}")
        world = tick(world)



# interface (marker)
class IColor:
    pass

# variants
class Red(IColor):
    def __repr__(self) -> str:
        return "Red"

class Green(IColor):
    def __repr__(self) -> str:
        return "Green"

class Yellow(IColor):
    def __repr__(self) -> str:
        return "Yellow"

class Blue(IColor):
    def __repr__(self) -> str:
        return "Blue"

Color = Union[Red, Green, Yellow, Blue]



# CODE ==========================================================================================

@dataclass
class UFOWorld:
    ufo:UFO
    aup:AUP
    shots:IShots

    HEIGHT:int = 500
    WIDTH:int = 200
    BACKG:Color = Blue()

@dataclass
class UFO:
    location:Posn

    colorUFO:Color = Green()

@dataclass
class AUP:
    location:Posn

    aupColor:Color = Red()

#interface
class IShots(Protocol):
    pass

#implements IShots
class EmptyShots:
    pass

#implements IShots
@dataclass
class ConsShots:
    fst:Shot
    rst:IShots

@dataclass
class Shot:
    location:Posn

    shotClr:Color = Yellow()

class WoWExamples:
    aup = AUP(Posn(495, 100)) # place aup at teh bottom
    ufo = UFO(Posn(0,0)) # place ufo at the top left corner

    shot1 = Shot(Posn(300,90)) # shoot shot
    shot2 = Shot(Posn(350,90)) # shot is lower than shot1
    shots = ConsShots(shot1, ConsShots(shot2, EmptyShots()))

    world = UFOWorld(ufo, aup, shots) # a complete world with two shots
