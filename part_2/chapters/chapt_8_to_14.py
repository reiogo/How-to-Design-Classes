from __future__ import annotations
from typing import Protocol
from dataclasses import dataclass
import math
# This contains until chapter 14 where I realized that this format isn't working too well

#CHAPTER 10, 11 ==========================================================================================
# This chapter starts the design of methods, so the test file is also quite important

class Coffee:
    kind:str
    price:int # cents per pound
    weight:int # pound
    def __init__(self, kind:str, price:int, weight:int) -> None:
        self.kind = kind
        self.price = price
        self.weight = weight

    # to compute the total cost of this coffee purchase [in cents].
    # discounts at [5000..20000) pounds: 10%, [20,000..) is 25%
    def cost(self) -> int:
        #... self.kind ... self.price ... self.weight
        if self.weight >= 20000:
            return int(self.price * self.weight * 0.75)
        elif self.weight >= 5000:
            return int(self.price * self.weight * 0.9)
        else:
            return int(self.price * self.weight)

    # to determine whether this coffee's price is more than amt
    def moreCents(self, amt:int) -> bool:
        # ... self.kind ... self.price ... self.weight
        return self.price > amt

    # to determine whether this coffee sale is lighter than that coffee sale
    def lighterThan(self, that:Coffee) ->bool:
        # ...self.kind ... that.kind #str
        # ...self.price ... that.price #int
        # ...self.weight ... that.weight #int
        return self.weight < that.weight


# collect eamples of coffee sales
class CoffeeExamples:
    kona = Coffee("Hawaiian Kona", 2095, 100)
    ethi = Coffee("Ethiopian", 800, 1000)
    colo = Coffee("Colombia Supreme", 950, 200)

# Racket version:
# (define-struct coffee (kind price weight))
# coffee (sale) is (make-coffee String Number Number)

# (cost (make-coffee "Kona" 2095 100) should produce 209500
# (cost (make-coffee "Ethi" 800 1000) should produce 800000
# (cost (make-coffee "Colo" 810 1000) should produce 810000

# cost: Coffee -> String
# computes the total cost of a coffee purchase
# (define (cost a-coffee) ...)

# becomes:
# (define (cost a-coffee) 
#  ...(coffee-kind a-coffee)
#  ...(coffee-price a-coffee)
#  ...(coffee-weight a-coffee)
#  )

# becomes 
# (define (cost a-coffee)
#   (*(coffee-price a-coffee) (coffee-weight a-coffee)))

# Conditional Computations ==========================================================================================
@dataclass
class CD:
    owner:str
    amount:int # cents

    # calculates the interest based on amount
    def interest(self) -> float:
        return (self.rate() * self.amount)/ 100

    # calculates the rate based on amount
    def rate(self) -> float:
        if 0 <= self.amount and self.amount < 500000:
            return 2.00
        elif 500000 <= self.amount and self.amount < 1000000:
            return 2.25
        else:
            return 2.50


# Star  ==========================================================================================
# represent a falling star on a 100x100 canvas
@dataclass
class Star():
    y:int
    x:int = 20
    DELTA:int = 5

    #drop this Star by DELTA pixels
    #unless it is on (or close) to the ground
    def drop(self) -> Star:
        if (self.y + self.DELTA >= 100):
            # landed star
            return Star(100)
        else:
            # fell by DELTA
            return Star(self.y + self.DELTA)

# Composing Methods ==========================================================================================

# Methods and Object Containment==========================================================================================

# a rectangle on a canvas, located at tlCorner, width pixels wide and height pixels high 
@dataclass
class Rectangle:
    tlCorner:CartPt
    width:int
    height:int

    def distance(self) -> float:
        # self.tlCorner.distance() ... self.width ... self.height
        return self.tlCorner.distance()

@dataclass
class CartPt:
    x:int
    y:int

    def distance(self) -> float:
        return math.sqrt( self.x * self.x
                    + self.y * self.y)
class Date:
    def __init__(self, day:int, month:int, year:int) -> None:
        self.day = day
        self.month = month
        self.year = year

    #def sameMonthAndYear(self, month:int, year:int) -> bool:
    #    #...self.day ...self.month...self.year
    #    return (self.year == year
    #            and self.month == month)

class TemperatureRange:
    def __init__(self, low:int, high:int) -> None:
        self.high = high
        self.low = low

    def difference(self) -> int:
        # self.high ... self.low
        return self.high - self.low
    # determines whether this is within the range of that
    def within(self, that:TemperatureRange) -> bool:
        return (that.low <= self.low and self.high <= that.high)

class WeatherRecord:
    def __init__(self, date:Date, today:TemperatureRange, normal:TemperatureRange, record:TemperatureRange, precipitation:float):
        self.date = date
        self.today = today
        self.normal = normal
        self.record = record
        self.precipitation = precipitation

    # compute the difference between today's high and low
    def differential(self) -> int:
        # ...self.date.lll() ... self.today.nnn() ... self.normal.nnn() ... self.record.nnn() ... self.precipitation
        return self.today.difference()

    # determines whether today's high and low were within the normal range
    def withinRange(self) -> bool:
        return self.today.within(self.normal)

    # determines whether the precipitation is higher than some given value
    def rainyDay(self, that:float) -> bool:
        return self.precipitation > that

    # determines whether the temperature broke either the high or the low record
    def recordDay(self) -> bool:
        return not self.today.within(self.record)

#CHAPTER 12 ==========================================================================================

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

# implements IShape
# right angle is in the lower right corner, two sides adjacent to the right angle 
# always parallel to x and y axes. loc defines the lower right point, size is the length of sides
@dataclass
class IsoTri:
    loc:CPt
    size:int

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

#CHAPTER 13 ==========================================================================================

# a representation of a room for interior design
@dataclass
class Room:
    width:int
    height:int
    a:IShape
    b:IShape
    c:IShape

    def covered(self) -> float:
        # self.a .. self.b ... self.c # all IShape
        # self.width ... self.height
        return ((self.a.area() + self.b.area() + self.c.area())
                /
                (self.width * self.height))

