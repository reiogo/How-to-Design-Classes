from typing import Protocol
from dataclasses import dataclass
import math

#CHAPTER 15  Methods and Classes with Mutual References=========================================

# Runner's Log =======================================================================
@dataclass
class Date:
    day:int
    month:int
    year:int

    def __repr__(self):
        return f"[{self.day}, {self.month}, {self.year}]"

    def sameMonthAndYear(self, month:int, year:int) -> bool:
        #...self.day ...self.month...self.year
        return (self.year == year
                and self.month == month)


# interface
class ILog(Protocol):
    # to compute the total number of miles recorded in this log
    def miles(self) -> float:
        ...

    # to extract those entries in this log for the given month and year
    def oneMonth(self, month:int, year:int) -> ILog:
        ...

    # to compute the total number of miles recorded in a given month and year
    def milesInMonth(self, month:int, year:int) -> float:
        ...

    # to compute the length of the lonngest run recorded in this log
    def longestRun(self) -> float:
        ...

    # to create a sorted version of this log, with entries sorted by distance
    def sortByDist(self) -> ILog:
        ...

    # insert the given entry into this (sorted) log
    def insertDist(self, e:Entry) ->ILog:
        ...

    # insert the given entry into this (sorted) log according to pace
    def insertDistByPace(self, e:Entry) ->ILog:
        ...

    # to create a sorted version of this log, with entries sorted
    # by pace(minutes per mile)
    def sortByPace(self) -> ILog:
        ...

# implements ILog
@dataclass
class MTLog(ILog):

    def miles(self) -> float:
        return 0.0

    def oneMonth(self, month:int, year:int) -> ILog:
        return MTLog()

    def milesInMonth(self, month:int, year:int) -> float:
        return 0.0

    def longestRun(self) -> float:
        return 0.0

    def sortByDist(self) -> ILog:
        return self

    def insertDist(self, e:Entry) ->ILog:
        return ConsLog(e, MTLog())

    def sortByPace(self) -> ILog:
        return self

    def insertDistByPace(self, e:Entry) ->ILog:
        return ConsLog(e, MTLog())

# implements ILog
@dataclass
class ConsLog(ILog):
    fst:Entry
    rst:ILog

    def miles(self) -> float:
        # self.fst.mmm() ... self.rst.nnn()
        return self.fst.distance + self.rst.miles()

    def oneMonth(self, m:int, y:int) -> ILog:
        # self.fst.mmm() ... self.rst.nnn()
        if self.fst.sameMonthAndYear(m, y):
            return ConsLog(self.fst, self.rst.oneMonth(m,y))
        else:
            return self.rst.oneMonth(m,y)

    def milesInMonth(self, month:int, year:int) -> float:
        # self.fst.nnn() ... self.rst.mmm()
        return self.oneMonth(month, year).miles()

    def longestRun(self) -> float:
        # self.fst.nnn() ... self.rst.mmm()
        previousBest = self.rst.longestRun()
        if self.fst.distance > previousBest:
            return self.fst.distance
        else:
            return previousBest

    def insertDist(self, e:Entry) ->ILog:
        #self.fst.nnn()...self.rst.mmm()
        if e.distance > self.fst.distance:
            return ConsLog(e, self)
        else:
            return  ConsLog(self.fst, self.rst.insertDist(e))

    def sortByDist(self) -> ILog:
        #self.fst.nnn()... self.rst.sortByDist()
        return self.rst.sortByDist().insertDist(self.fst)

    def insertDistByPace(self, e:Entry) ->ILog:
        if e.pace() < self.fst.pace():
            return ConsLog(e, self)
        else:
            return ConsLog(self.fst, self.rst.insertDistByPace(e))

    def sortByPace(self) -> ILog:
        #self.fst.nnn()...self.rst.sortByPace()
        return self.rst.sortByPace().insertDistByPace(self.fst)

@dataclass
class Entry:
    d:Date
    distance:float
    duration:int # in minutes
    comment:str

    # was this entry made in the given month and year?
    def sameMonthAndYear(self, month:int, year:int) -> bool:
        #...self.d.lll()...self.distance...self.duration...self.comment
        return self.d.sameMonthAndYear(month, year)

    # to compute the pace (mins/mile) recorded in this entry
    def pace(self) -> float:
        #...self.d.lll()...self.distance...self.duration...self.comment
        return self.duration/self.distance



# Overlapping Shapes =======================================================================

class IShape(Protocol):
    # to compute the area of this shape
    def area(self) -> float:
        ...

    # to compute the distance from this shape to the origin
    def distTo0(self) -> float:
        ...

    # is the given point within the bounds of this shape
    def within(self, p:CartPt) -> bool:
        ...

    # compute the bounding box for this shape
    def bb(self) -> Rectangle:
        ...

    # compute the perimeter of this shape
    def perimeter(self) -> float:
        ...

#interface cartesian point already defined above so changed name
@dataclass
class CartPt:
    x:int
    y:int

    # this is the same as that coordinate
    def same(self, p:CartPt) -> bool:
        return self.x == p.x and self.y == p.y

    # to compute the distance of this point to the origin
    def distTo0(self) -> float:
        #self.x ... self.y
       return math.sqrt(self.x * self.x
                        + self.y * self.y)

   # compute the distance from this point to that point
    def distTo(self, p:CartPt) -> float:
        # self.x ... p.x ... self.y ... p.y 
        width = self.x - p.x
        height = self.y - p.y
        dist = math.sqrt(width * width + height * height)
        return dist

    # create a point that is delta pixels (up, left) from this
    def translate(self, delta:int) -> CartPt:
        return CartPt(self.x + delta, self.y + delta)


# implements IShape
@dataclass
class Square(IShape):
    loc:CartPt
    size:int

    def area(self) -> float:
        # self.loc.nnn() ... self.size
        return self.size * self.size

    def distTo0(self) -> float:
        return self.loc.distTo0()

    # is x in the interval [lft, lft + wdth]
    def between(self, lft:int, x:int, wdth:int) -> bool:
        return lft <= x and x <= lft + wdth

    def within(self, p:CartPt) -> bool:
        #... self.loc.nnn() ...self.size
        return (self.between(self.loc.x, p.x, self.size)
                and self.between(self.loc.y, p.y, self.size))

    def bb(self) -> Rectangle:
        # self.loc.nnn()...self.size
        return Rectangle(self.loc, self.size, self.size)

    # def bb(self) -> BoundingBox:
    #     # self.loc.nnn()...self.size
    #     return BoundingBox(self.loc.x,
    #                        self.loc.x + self.size,
    #                        self.loc.y,
    #                        self.loc.y + self.size
    #                        )

    def perimeter(self) -> float:
        return self.size * 4

# implements IShape
@dataclass
class Circle(IShape):
    loc:CartPt
    radius:int
    def area(self) -> float:
        # self.loc.nnn() ... self.radius
        return self.radius * self.radius * math.pi

    def distTo0(self) -> float:
        return self.loc.distTo0() - self.radius

    def within(self, p:CartPt) -> bool:
        #self.loc.nnn() ... self.radius
        return self.loc.distTo(p) < self.radius

    def bb(self) -> Rectangle:
        # self.loc.nnn()...self.size
        return Rectangle(
                CartPt(self.loc.x - self.radius, self.loc.y - self.radius),
                self.radius * 2,
                self.radius * 2)



    # def bb(self) -> BoundingBox:
    #     # ... self.loc.nnn() ... self.radius
    #     return BoundingBox(self.loc.x - self.radius,
    #                        self.loc.x + self.radius,
    #                        self.loc.y - self.radius,
    #                        self.loc.y + self.radius)

    def perimeter(self) -> float:
        return self.radius * 2 * math.pi



# implements IShape
@dataclass
class SuperImp(IShape):
    bot:IShape
    top:IShape

    def distTo0(self) -> float:
        #self.bot.nnn() ... self.top.nnn()
        return min(self.bot.distTo0(), self.top.distTo0())

    def within(self, p:CartPt) -> bool:
        #self.bot.within() ... self.top.within()
        return self.bot.within(p) or self.top.within(p)

    def bb(self) -> Rectangle:
        # self.loc.nnn()...self.size
        # self.bot.bb() + self.top.bb()
        return self.bot.bb().combine(self.top.bb())

    #def bb(self) ->BoundingBox:
    #    # compute the bounding box for top
    #    #... self.top.bb()
    #    # compute the bounding box for bot
    #    #... self.bot.bb() 
    #    return self.top.bb().combine(self.bot.bb())

# reprsenting a rectangle
# implements IShape
@dataclass
class Rectangle(IShape):
    loc:CartPt
    width:int
    height:int

    def combine(self, that:Rectangle):
        # self.loc ... self.width... self.height
        # that.loc ... that.width .. that.height
        c = CartPt(min(self.loc.x, that.loc.x), min(self.loc.y, that.loc.y))

        return Rectangle(c,
                  max(self.loc.x + self.width, that.loc.x + that.width) - c.x,
                  max(self.loc.y + self.height, that.loc.y + that.height) - c.y)


    def bb(self) -> Rectangle:
        # self.loc.nnn()...self.size
        return self

# reprsenting bounding boxes in general
@dataclass
class BoundingBox:
    lft:int
    rgt:int
    top:int
    bot:int
    # combine this bounding box with that one
    def combine(self, that:BoundingBox) -> BoundingBox:
        return BoundingBox(min(self.lft, that.lft),
                           max(self.rgt, that.rgt),
                           min(self.top, that.top),
                           max(self.bot, that.bot))


# River Systems=======================================================================

# the end of a river
@dataclass
class Mouth:
    loc:Location
    river:IRiver

    # count the number of sources
    # that feed this Mouth
    def sources(self) -> int:
        #self.loc.mmm() ... self.river.nnn()
        return self.river.sources()

    # does aloc occur along this river system?
    # using same
    #def onRiver(self, aloc:Location) -> bool:
    #    #self.loc.same(aloc) ... self.river.onRiver(aloc)
    #    return self.loc.same(aloc) or self.river.onRiver(aloc)

    # does aloc occur along this river system?
    # using withinRadius
    def onRiver(self, aloc:Location, radius:int) -> bool:
        return (self.loc.withinRadius(aloc, radius)
                or self.river.onRiver(aloc, radius))

    # the total length of the river system
    def length(self) -> int:
        #self.loc.mmm() ... self.river.nnn()
        return self.river.length()

    # compute the length of the longest path through the river system
    def maxLength(self) -> int:
        #self.loc.mmm() .self.river.nnn()
        return self.river.maxLength()

    # counts the number of confluence in the river system
    def confluences(self) -> int:
        #self.loc.mmm()... self.river.nnn()
        return self.river.confluences()

    def locations(self) -> ILoLocations:
        #self.loc ... self.river.nnn()
        return ConsLoLocations(self.loc, self.river.locations())


# a location on a river
@dataclass
class Location:
    x:int
    y:int
    name:str = ""

    def __repr__(self):
        return f"[{self.name}]"

    def same(self, aloc:Location) -> bool:
        # self.x ... self.y ... self.name
        # aloc.x ... aloc.y ...
        return (self.x == aloc.x and self.y == aloc.y)

    # calculates distance from this location to that location
    def dist(self, aloc:Location) -> float:
        x = aloc.x - self.x
        y = aloc.y - self.y
        return math.sqrt(x * x + y * y)

    # whether that location is within a given radius of this location
    def withinRadius(self, aloc:Location, radius:int) -> bool:
        # self.x ... self.y 
        # aloc.x ... aloc.y
        return self.dist(aloc) <= radius

# interface for a river system
@dataclass
class IRiver(Protocol):
    # count the number of sources
    # for this river system
    def sources(self) -> int:
        ...

    # does aloc occur
    # along this river system?
    def onRiver(self, aloc:Location, radius:int) -> bool:
        ...

    # compute the total length of the waterways that flow into this point
    def length(self) -> int:
        ...

    # compute the length of the longest path through the river system
    def maxLength(self) -> int:
        ...

    # counts the number of confluence in the river system
    def confluences(self) -> int:
        ...

    def locations(self) -> ILoLocations:
        ...

# the source of a river
#implements IRiver
@dataclass
class Source(IRiver):
    miles:int
    loc:Location

    def __repr__(self):
        return f"[{self.loc}]"

    def sources(self)->int:
        #self.loc.mmm()
        return 1

    # using same
    # def onRiver(self, aloc:Location) -> bool:
    #     # ...self.loc.same(aloc)
    #     return self.loc.same(aloc)

    # using withinRadius
    def onRiver(self, aloc:Location, radius:int) -> bool:
        return self.loc.withinRadius(aloc, radius)

    def length(self)->int:
        #self.miles ... self.loc.mmm()
        return self.miles

    def maxLength(self) -> int:
        #self.miles
        return self.miles

    def confluences(self) -> int:
        # self.miles... self.loc.nnn()...
        return 0

    def locations(self) -> ILoLocations:
        #self.miles ... self.loc
        return ConsLoLocations(self.loc, MTLoLocations())


# a confluence of two rivers
# implements IRiver
@dataclass
class Confluence(IRiver):
    miles:int
    loc:Location
    left:IRiver
    right:IRiver

    def __repr__(self):
        return f"[{self.loc} | {self.left} | {self.right}]"

    def sources(self) -> int:
        #loc.mmm() ... left.nnn()... right.nnn()
        return self.left.sources() + self.right.sources()

    # def onRiver(self, aloc:Location) -> bool:
    #     # ... self.loc.same(aloc) ... self.left.onRiver(aloc) ... self.right.onRiver(aloc)
    #     return (self.loc.same(aloc)
    #             or self.left.onRiver(aloc)
    #             or self.right.onRiver(aloc))

    def onRiver(self, aloc:Location, radius:int) -> bool:
        # self.loc.withinRadius(aloc, radius) ... self.left.onRiver(aloc,radius) ... self.right.onRiver(aloc)
        return (
            self.loc.withinRadius(aloc, radius)
            or self.left.onRiver(aloc, radius)
            or self.right.onRiver(aloc, radius))

    def length(self)->int:
        # self.miles ... self.loc.mmm() ... 
        # self.left.nnn() ... self.right.nnn() ...
        return self.miles + self.left.length() + self.right.length()

    def maxLength(self) -> int:
        # self.miles ... self.loc.mmm() ... 
        # self.left.nnn() ... self.right.nnn() ...
        return self.miles + max(self.left.maxLength(), self.right.maxLength())

    def confluences(self) -> int:
        # self.left.nnn() ...self.right.nnn()
        return 1 + self.left.confluences() + self.right.confluences()

    def combine(self, left: ILoLocations, right: ILoLocations) -> ILoLocations:
        assert isinstance(left, ConsLoLocations)
        if isinstance(left.rst, MTLoLocations):
            return ConsLoLocations(left.fst, right)
        else:
            return ConsLoLocations(left.fst, self.combine(left.rst, right))


    def locations(self) -> ILoLocations:
        # self.loc ...self.left.nnn() ... self.right.nnn()
        return ConsLoLocations(
                    self.loc,
                    self.combine(self.left.locations(), self.right.locations()))


# interface for List of Locations 
@dataclass
class ILoLocations(Protocol):
    ...

# implements ILoLocations
# An empty list of locations
@dataclass
class MTLoLocations(ILoLocations):
    def __repr__(self):
        return f"[EmptyList]"

# implements ILoLocations
# A cons of location onto a list of locations
@dataclass
class ConsLoLocations(ILoLocations):
    fst:Location
    rst:ILoLocations

    def __repr__(self):
        return f"[{self.fst} | {self.rst}]"

# Finger Exercises =================================================================

# an interface for grocery items
class GroceryItem(Protocol):
    # computes unit price (cents per gram)
    def unitPrice(self) -> float:
        ...

    #determines whether unit price is lower than a given amount
    def lowerUnitPrice(self, that:GroceryItem) -> bool:
        ...

    # determines whether a grocery items's unit price is less than
    # that item's unit price
    def cheaperThan(self, that:GroceryItem) -> bool:
        ...

# implements, a null grocery item
@dataclass
class NullItem(GroceryItem):
    name:str = "Null"
    weight:int = 0
    price:int = 0

    # computes unit price (cents per gram)
    def unitPrice(self) -> float:
        return 0

    #determines whether unit price is lower than a given amount
    def lowerUnitPrice(self, that:GroceryItem) -> bool:
        return False

    # determines whether a grocery items's unit price is less than
    # that item's unit price
    def cheaperThan(self, that:GroceryItem) -> bool:
        return True

# implements GroceryItem
@dataclass
class IceCream(GroceryItem):
    name:str
    weight:int #grams
    price:int #cents
    flavor:str

    def __repr__(self):
        return f"[{self.name}]"

    # computes unit price (cents per gram)
    def unitPrice(self) -> float:
        return self.price / self.weight

    #determines whether unit price is lower than a given amount
    def lowerUnitPrice(self, thatPrice) -> bool:
        return self.unitPrice() < thatPrice

    # determines whether a grocery items's unit price is less than
    # that item's unit price
    def cheaperThan(self, that:GroceryItem) -> bool:
        return self.unitPrice() < that.unitPrice()

# implements GroceryItem
@dataclass
class Coffee(GroceryItem):
    name:str
    weight:int #grams
    price:int #cents
    decaf:bool

    def __repr__(self):
        return f"[{self.name}]"

    # computes unit price (cents per gram)
    def unitPrice(self) -> float:
        return self.price / self.weight

    #determines whether unit price is lower than a given amount
    def lowerUnitPrice(self, thatPrice) -> bool:
        return self.unitPrice() < thatPrice

    # determines whether a grocery items's unit price is less than
    # that item's unit price
    def cheaperThan(self, that:GroceryItem) -> bool:
        return self.unitPrice() < that.unitPrice()

# implements GroceryItem
@dataclass
class Juice(GroceryItem):
    name:str
    weight:int #grams
    price:int #cents
    flavor:str
    package:str #frozen,fresh,bottled,canned

    def __repr__(self):
        return f"[{self.name}]"

    # computes unit price (cents per gram)
    def unitPrice(self) -> float:
        return self.price / self.weight

    #determines whether unit price is lower than a given amount
    def lowerUnitPrice(self, thatPrice) -> bool:
        return self.unitPrice() < thatPrice

    # determines whether a grocery items's unit price is less than
    # that item's unit price
    def cheaperThan(self, that:GroceryItem) -> bool:
        return self.unitPrice() < that.unitPrice()

#interface for ShoppingList
@dataclass
class IShoppingList(Protocol):
    # calculates number of items in the list
    def howMany(self) -> int:
        ...
    # creates list of all of the brand names in the list
    def brandList(self) -> IBrandList:
        ...
    # determines the highest unit price among all items
    def highestPrice(self) -> GroceryItem:
        ...

#implements IShoppingList, empty list
@dataclass
class MTShoppingList(IShoppingList):

    def __repr__(self):
        return f"[Empty]"

    def howMany(self) -> int:
        return 0

    def brandList(self) -> IBrandList:
        return MTBrandList()

    def highestPrice(self) -> GroceryItem:
        return NullItem()

#implements IShoppingList, cons list
@dataclass
class ConsShoppingList(IShoppingList):
    fst:GroceryItem
    rst:IShoppingList

    def __repr__(self):
        return f"[{self.fst} | {self.rst}]"

    def howMany(self) -> int:
        # self.fst.nnn() ... self.rst.mmm()
        return 1 + self.rst.howMany()

    def brandList(self) -> IBrandList:
        # self.fst.nnn() ... self.rst.mmm()
        return ConsBrandList(self.fst.name, self.rst.brandList())

    def highestPrice(self) -> GroceryItem:
        # self.fst.nnn() ...self.rst.mmm()
        bestsofar = self.rst.highestPrice()
        if self.fst.cheaperThan(bestsofar):
            return bestsofar
        else:
            return self.fst

# interface for brand list
@dataclass
class IBrandList(Protocol):
    ...

# implements, empty brand list
@dataclass
class MTBrandList(IBrandList):
    def __repr__(self):
        return f"[Empty]"

# implements, cons brand list
@dataclass
class ConsBrandList(IBrandList):
    fst:str
    rst:IBrandList

    def __repr__(self):
        return f"[{self.fst} | {self.rst}]"

@dataclass
class Author:
    name:str
    birth:Date
    def __repr__(self):
        return f"[{self.name}]"

@dataclass
class Book:
    loauthors: ILoAuthors
    title:str
    price:int
    pub_year:int

    def __repr__(self):
        return f"[{self.title}]"

# interface for list of books
@dataclass
class ILoBooks(Protocol):
    # produces a list of books with a given author
    def thisAuthor(self, author:Author) -> ILoBooks:
        ...

# implementation, empty list of books
@dataclass
class MTLoBooks(ILoBooks):
    def __repr__(self):
        return f"[Empty]"

    def thisAuthor(self, author:Author) -> ILoBooks:
        return MTLoBooks()

# implementation, cons list of books
@dataclass
class ConsLoBooks(ILoBooks):
    fst:Book
    rst:ILoBooks
    def __repr__(self):
        return f"{self.fst} | {self.rst}"

    def thisAuthor(self, author:Author) -> ILoBooks:
        #self.fst.nnn() ... self.rst.mmm()
        if self.fst.loauthors.contains(author):
            return ConsLoBooks(self.fst, self.rst.thisAuthor(author))
        else:
            return self.rst.thisAuthor(author)

# interface for list of authors
@dataclass
class ILoAuthors(Protocol):
    def contains(self, givenAuthor) -> bool:
        ...

# implementation, empty list of authors
@dataclass
class MTLoAuthors(ILoAuthors):
    def __repr__(self):
        return f"[Empty]"

    def contains(self, givenAuthor) -> bool:
        return False

# implementation, cons list of authors
@dataclass
class ConsLoAuthors(ILoAuthors):
    fst:Author
    rst:IloAuthors

    def __repr__(self):
        return f"[{self.fst} | {self.rst}"

    def contains(self, givenAuthor) -> bool:
        # self.fst.nnn() ... self.rst.mmm()
        if self.fst == givenAuthor:
            return True
        else:
            return self.rst.contains(givenAuthor)

