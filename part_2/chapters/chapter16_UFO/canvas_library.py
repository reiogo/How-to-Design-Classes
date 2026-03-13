from typing import Protocol
from dataclasses import dataclass
import math

# LIBRARY ==========================================================================================
# AI helped a lot with setting up this library

# Define Colors ====================================================================================

Color = tuple[int, int, int]

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,225,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# # interface (Color) 
# class IColor:
#     pass

# class Red(IColor):
#     def __repr__(self) -> str:
#         return "Red"

# class Green(IColor):
#     def __repr__(self) -> str:
#         return "Green"

# class Yellow(IColor):
#     def __repr__(self) -> str:
#         return "Yellow"

# class Blue(IColor):
#     def __repr__(self) -> str:
#         return "Blue"

# class Black(IColor):
#     def __repr__(self) -> str:
#         return "Black"

# POSN ===================================================================================

@dataclass
class Posn:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x},{self.y})"

def tick(world):
    return world.move()


def run(world, steps: int) -> None:
    for i in range(steps):
        print(f"tick {i}: {world}")
        world = tick(world)

# CANVAS  ===================================================================================

@dataclass
class ICanvas(Protocol):
    width:int
    height:int

    def drawCircle(self, p: Posn, r: int, c: Color) -> bool: ...
    def drawDisk(self, p: Posn, r: int, c: Color) -> bool: ...
    def drawRect(self, p: Posn, width: int, height: int, c: Color) -> bool: ...
    def drawLine(self, p: Posn, dx: int, dy: int, c: Color) -> bool: ...
    def drawString(self, p: Posn, s: str) -> bool: ...

# Define the Canvas =========================
COLOR_NAMES: dict[Color, str] = {
        RED: "Red",
        GREEN: "Green",
        BLUE: "Blue",
        YELLOW: "Yellow",
        BLACK: "Black",
}
def color_to_string(c: Color) -> str:
        return COLOR_NAMES.get(c, f"UnknownColor{c}")
@dataclass
class LogCanvas:
    width: int
    height: int

    def __post_init__(self) -> None:
        self.log:list[str] = []

    def show(self) -> bool:
        print(f"\nCanvas {self.width}x{self.height}")
        for cmd in self.log:
            print(cmd)
        print("\n")
        return True

    def close(self) -> bool:
        self.log.clear()
        return True

    def drawCircle(self, p:Posn, r:int, c:Color) -> bool:
        self.log.append( f"Circle: at {p} r={r} color={color_to_string(c)}")
        return True

    def drawDisk(self, p:Posn, r:int, c:Color) -> bool:
        self.log.append( f"Disk: at {p} r={r} color={color_to_string(c)}")
        return True

    def drawRect(self, p:Posn, width:int, height:int, c:Color) -> bool:
        self.log.append( f"Rectangle: at {p} w={width} h={height} color={color_to_string(c)}")
        return True

    def drawLine(self, p:Posn, dx:int, dy:int, c:Color) -> bool:
        self.log.append( f"Line: from {p} dx={dx} dy={dy} color={color_to_string(c)}")
        return True

    def drawString(self, p:Posn, s:str) -> bool:
        self.log.append( f'String "{s}" at {p}')
        return True

