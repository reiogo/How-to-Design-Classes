from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol
from typing import Union
from dataclasses import dataclass
from typing import List
import math

@dataclass
class Posn:
    x:int
    y:int

@dataclass
class Canvas:
    width: int
    height: int

    def __post_init__(self) -> None:
        self.log: List[str] = []

    def show(self) -> bool:
        print(f"Canvas {self.width}x{self.height}")
        for cmd in self.log:
            print(cmd)
        return True

    def close(self) -> bool:
        self.log.clear()
        return True

    def drawCircle(self, p:Posn, r:int, c:IColor) -> bool:
        self.log.append(f"drawCircle at {p} r={r} color={c}")
        return True

    def drawDisk(self, p:Posn, r:int, c:IColor) -> bool:
        self.log.append(f"drawDisk at {p} r={r} color={c}")
        return True

    def drawRect(self, p:Posn, width:int, height:int, c:IColor) -> bool:
        self.log.append(
            f"drawRect at {p} w={width} h={height} color={c}"
        )
        return True

    def drawLine(self, p:Posn, dx:int, dy:int, c:IColor) -> bool:
        self.log.append(
            f"drawLine from {p} dx={dx} dy={dy} color={c}"
        )
        return True

    def drawString(self, p:Posn, s:str) -> bool:
        self.log.append(f'drawString "{s}" at {p}')
        return True


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

class Black(IColor):
    def __repr__(self) -> str:
        return "Black"


# Box and circle car ================================================
c = Canvas(100, 100)
c.drawRect(Posn(45,45), 10, 5, Red())
c.drawCircle(Posn(45,50), 3, Red())
c.drawCircle(Posn(55,50), 3, Red())
c.show()
c.close()

# match-stick man================================================
c.drawLine(Posn(45,45), 0, 3, Blue())
c.drawLine(Posn(45,48), 1, 4, Blue())
c.drawLine(Posn(45,48), -1, 4, Blue())
c.drawLine(Posn(43,46), 4, 0, Blue())
c.drawCircle(Posn(45,44), 1, Blue())
c.show()
c.close()

# house ================================================
c.drawLine(Posn(40,40), 5, 3, Blue())
c.drawLine(Posn(40,40), -5, 3, Blue())
c.drawRect(Posn(37,43), 6, 7, Blue())
c.show()
c.close()


# HouseDrawing class  ================================================

class HouseDrawing:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.c = Canvas(width, height)
        self.roofColor =Red()
        self.houseColor = Blue()
        self.doorColor = Yellow()

    #draw a house on the canvas
    def draw(self) -> None:
        roofHeight = 3
        roofLength = int(math.sqrt(
                        (self.width / 2) * (self.width / 2)
                        +
                        roofHeight * roofHeight))
        posx = 30
        posy = 30
        self.c.drawLine(Posn(posx,posy),
                        roofLength, roofHeight,
                        self.roofColor)
        self.c.drawLine(Posn(posx,posy),
                        -roofLength, roofHeight,
                        self.roofColor)
        self.c.drawRect(Posn(posx - roofLength, posy + roofHeight),
                        self.width, self.height - roofHeight,
                        self.houseColor)
        self.c.show()
        return

h = HouseDrawing(10, 11)
h.draw()

# Room ================================================

class IShape(Protocol):
    # to compute the area of this shape
    def area(self) -> float:
        ...

    # to compute the distance from this shape to the origin
    def distTo0(self) -> float:
        ...

    # is the given point within the bounds of this shape
    def within(self, p:CPt) -> bool:
        ...

    # compute the bounding box for this shape
    def bb(self) -> Square:
        ...

    # compute the perimeter of this shape
    def perimeter(self) -> float:
        ...

    # draw this shape into canvas
    def draw(self, c:Canvas) ->bool:
        ...

#interface cartesian point already defined above so changed name
@dataclass
class CPt:
    x:int
    y:int

    # this is the same as that coordinate
    def same(self, p:CPt) -> bool:
        return self.x == p.x and self.y == p.y

    # to compute the distance of this point to the origin
    def distTo0(self) -> float:
        #self.x ... self.y
       return math.sqrt(self.x * self.x
                        + self.y * self.y)

   # compute the distance from this point to that point
    def distTo(self, p:CPt) -> float:
        # self.x ... p.x ... self.y ... p.y 
        width = self.x - p.x
        height = self.y - p.y
        dist = math.sqrt(width * width + height * height)
        return dist
    # create a point that is delta pixels (up, left) from this
    def translate(self, delta:int) -> CPt:
        return CPt(self.x + delta, self.y + delta)

    # Translate CPt to Posn
    def toPosn(self) -> Posn:
        return Posn(self.x, self.y)

# implements IShape
@dataclass
class Dot:
    loc:CPt

    def area(self) ->float:
            # self.loc.nnn()
            return 0.0

    def distTo0(self) -> float:
        return self.loc.distTo0()

    def within(self, p:CPt) -> bool:
        # self.loc.nnn() ...
        return self.loc.same(p)

    def bb(self) -> Square:
        return Square(self.loc, 1)

    def perimeter(self) -> float:
        return 0.0

    def draw(self, c:Canvas)-> bool:
        #...self.loc.nnn()
        return c.drawDisk(self.loc.toPosn(), 1, Green())

# implements IShape
@dataclass
class Square:
    loc:CPt
    size:int

    def area(self) -> float:
        # self.loc.nnn() ... self.size
        return self.size * self.size

    def distTo0(self) -> float:
        return self.loc.distTo0()

    # is x in the interval [lft, lft + wdth]
    def between(self, lft:int, x:int, wdth:int) -> bool:
        return lft <= x and x <= lft + wdth

    def within(self, p:CPt) -> bool:
        #... self.loc.nnn() ...self.size
        return (self.between(self.loc.x, p.x, self.size)
                and self.between(self.loc.y, p.y, self.size))

    def bb(self) -> Square:
        return self

    def perimeter(self) -> float:
        return self.size * 4

    def draw(self, c:Canvas)-> bool:
        #...self.loc.nnn() ...self.size
        return c.drawRect(self.loc.toPosn(),
                          self.size,
                          self.size,
                          Blue())

# implements IShape
@dataclass
class Circle:
    loc:CPt
    radius:int
    def area(self) -> float:
        # self.loc.nnn() ... self.radius
        return self.radius * self.radius * math.pi

    def distTo0(self) -> float:
        return self.loc.distTo0() - self.radius

    def within(self, p:CPt) -> bool:
        #self.loc.nnn() ... self.radius
        return self.loc.distTo(p) < self.radius

    def bb(self) -> Square:
        # ... self.loc.nnn() ... self.radius
        return Square(self.loc.translate( -self.radius), 2 * self.radius)

    def perimeter(self) -> float:
        return self.radius * 2 * math.pi

    def draw(self, c:Canvas)-> bool:
        #...self.loc.nnn() ...self.radius
        return c.drawCircle(self.loc.toPosn(),
                            self.radius,
                            Red())

# implements IShape
# right angle is in the lower right corner, two sides adjacent to the right angle 
# always parallel to x and y axes. loc defines the lower right point, size is the length of sides
class IsoTri:
    def __init__(self, loc:CPt, size:int):
        self.loc = loc
        self.size = size
        self.hypotenuseLength = math.sqrt(2 *(self.size * self.size))

    def area(self) -> float:
        # self.loc.nnn() ... self.size
        return (self.size * self.size) / 2

    # distance from lower right point to 0
    def distTo0(self) -> float:
        # self.loc.nnn() ... self.size
        return self.loc.distTo0()

    # is x in the interval [rght - wdth, rght]
    def between(self, rght:int, x:int, wdth:int) -> bool:
        return rght - wdth <= x and x <= rght

    # is CPt under the slope
    def underSlope(self, topRight:CPt, bottomLeft:CPt, p:CPt) -> bool:
        slope = abs((topRight.y - bottomLeft.y) / (topRight.x - bottomLeft.x))
        yintercept = slope * bottomLeft.x + bottomLeft.y
        return -(slope * p.x) + yintercept >= p.y


    def within(self, p:CPt) -> bool:
        # self.loc.nnn() ... self.size
        return (self.between(self.loc.x, p.x, self.size)
            and self.between(self.loc.y, p.y, self.size)
            and self.underSlope(
                        CPt(self.loc.x, self.loc.y - self.size),
                        CPt(self.loc.x - self.size, self.loc.y),
                        p))

    def bb(self) -> Square:
        # self.loc.nnn() ... self.size
        return Square(self.loc.translate(-self.size), self.size)

    def perimeter(self) -> float:
        return self.size * 2 + math.sqrt(self.size * self.size * 2)

    # get the Posn of the top right corner
    def topRightPosn(self):
        # self.loc.nnn() ... self.size
        return Posn(self.loc.x, self.loc.y - self.size)

    def draw(self, c:Canvas) -> bool:
        #self.loc.nnn() ... self.size
        return (c.drawLine(self.loc.toPosn(), -self.size, 0, Red())
                and c.drawLine(self.loc.toPosn(), 0, -self.size, Red())
                and c.drawLine(self.topRightPosn(),
                           -self.size,
                           self.size,
                           Red()))



# a representation of a room for interior design
class Room:
    def __init__(self, width:int, height:int, x:IShape, y:IShape, z:IShape):
        self.width = width
        self.height = height
        self.c = Canvas(width, height)
        self.x = x
        self.y = y
        self.z = z

    # draw a margin of given weight
    def drawMargin(self, weight:int)->bool:
        #self.width ... self.height... self.c.nnn()
        return (self.c.drawRect(Posn(0,0), weight, self.height, Black())
                and self.c.drawRect(Posn(self.width-weight, 0), weight, self.height, Black())
                and self.c.drawRect(Posn(weight, 0), self.width - (2 * weight), weight, Black())
                and self.c.drawRect(Posn(weight, self.height - weight), self.width - (2 * weight), weight, Black()))


    # show the world(the room) with its furniture
    def show(self):
        return (self.x.draw(self.c)
                and self.y.draw(self.c)
                and self.z.draw(self.c)
                and self.drawMargin(20)
                and self.c.show())

    def covered(self) -> float:
        # self.a .. self.b ... self.c # all IShape
        # self.width ... self.height
        return ((self.x.area() + self.x.area() + self.z.area())
                /
                (self.width * self.height))


r1 = Room(100, 100, Square(CPt(20,20), 5), IsoTri(CPt(70,70), 4), Dot(CPt(50,50)))
r1.show()
