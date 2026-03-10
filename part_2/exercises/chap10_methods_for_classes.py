from dataclasses import dataclass
from typing import Protocol

# Image ==========================================================================================
class Image:
    def __init__(self, height: int, width: int, source: str, quality: str, gallery: str) -> None:
        self.height = height # pixels
        self.width = width # pixels
        self.source = source # file name
        self.quality = quality # informal
        self.gallery = gallery

    # determines whether the images height is larger than its width
    def isPortrait(self) -> bool:
        # ...self.width ... self.height
        return self.height > self.width

    # determines size of image in pixels
    def size(self) -> int:
        return self.height * self.width

    # determines whether this image is bigger than that image
    def isLarger(self, that:Image) -> bool:
        # ...self.width ... that.width 
        # ...self.height ... that.height
        return self.size() > that.size()

    # determines whether this image is the same as that image
    def same(self, that:Image) -> bool:
        return (
            self.height == that.height
            and self.width == that.width
            and self.source == that.source
            and self.quality == that.quality
            and self.gallery == that.gallery
        )
    # gives string description of size
    def sizeString(self) -> str:
        size = self.size()
        if size <= 10000:
            return "small"
        elif 10001 <= size  <= 1000000:
            return "medium"
        else:
            return "large"

# House ==========================================================================================

class Addr:
    def __init__(self, street_num:int, street_name:str, city:str) -> None:
        self.street_num = street_num
        self.street_name = street_name
        self.city = city


class House:
    def __init__(self, kind:str, room_num:int, address:Addr, asking_price:int) -> None:
        self.kind = kind
        self.room_num = room_num
        self.address = address
        self.asking_price = asking_price # in usd

    # determines whether this house has more rooms than that house
    def isBigger(self, that:House) -> bool:
        # self.room ... that.room
        return self.room_num > that.room_num

    # checks whether this house is in the given city
    def thisCity(self, city:str) -> bool:
        return self.address.city == city

    # determines whether this house is in the same city as that house
    def sameCity(self, this:House) -> bool:
        return self.address.city == this.address.city


a1 = Addr(23, "Maple Street", "Brookline")
a2 = Addr(5, "Joye Road", "Newton")
a3 = Addr(83, "Winslow Road", "Waltham")

h1 = House("Ranch", 7, a1, 375000)
h2 = House("Colonial", 9, a2, 450000)
h3 = House("Cape", 6, a3, 235000)

# runner's log ==========================================================================================

# interface
class ILog(Protocol):
    pass

# implements ILog
class MTLog:
    pass

# implements ILog
@dataclass
class ConsLog:
    fst:Entry
    rst:ILog

class Entry:
    def __init__(self, d: Date, distance: float, duration: int, comment: str) -> None:
        self.d = d
        self.distance = distance
        self.duration = duration
        self.comment = comment

    # compute how fast the runner ran in minutes per mile
    def pace(self) -> float:
        return self.distance / self.duration

class Date:
    def __init__(self, day:int, month:int, year:int) -> None:
        self.day = day
        self.month = month
        self.year = year

    # determines whether this date is earlier than that date
    def earlierThan(self, that:Date) -> bool:
        if self.year < that.year:
            return True
        elif (self.year == that.year
              and self.month < that.month):
            return True
        elif (self.year == that.year
              and self.month == that.month
              and self.day < that.day):
            return True
        else:
            return False


date1 = Date(5,6,2026)
date2 = Date(6,6,2026)
date3 = Date(23,6,2026)

entry1 = Entry(date1, 5.3, 27, "Good")
entry2 = Entry(date2, 2.8, 24, "Tired")
entry3 = Entry(date3, 26.2, 150, "Exhausted")

l1 = MTLog()
l2 = ConsLog(entry1, l1)
l3 = ConsLog(entry2, l2)
l4 = ConsLog(entry3, l3)

# represents a bouncing ball on a 10x100 canvas
@dataclass
class BouncingBall:
    y:int
    down:bool = True
    x:int = 5
    DELTA:int = 4

    # simulates the movement of the ball
    # drops downwards, then bounces upwards
    def move(self) -> BouncingBall:
        # self.y ... self.down ... self.x ... self.DELTA
        if self.down and (self.y + self.DELTA) <= 100:
            return BouncingBall(self.y + self.DELTA)
        elif self.down and (self.y + self.DELTA) > 100:
            return BouncingBall(100, False)
        elif not self.down and (self.y - self.DELTA) >= 0:
            return BouncingBall(self.y - self.DELTA, False)
        elif not self.down and (self.y - self.DELTA) < 0:
            return BouncingBall(0)
        else:
            return BouncingBall(0)

# Composing Methods  ==========================================================================================

@dataclass
class Precipitation:
    day1:int
    day2:int
    day3:int

    def cumulative(self) -> int:
        return self.day1 + self.day2 + self.day3

    # determine the average of the 3 days
    def average(self) -> float:
        return self.cumulative() / 3

@dataclass
class JetFuel:
    amount:int # gallons
    quality:str
    base_price:int # cents per gallon

    # computes the cost of the sale
    def totalCost(self) -> int:
        if self.amount > 100000:
            return self.discountPrice()
        else:
            return self.amount * self.base_price

    # computes the discounted price
    def discountPrice(self) -> int:
        return (int)(self.amount * self.base_price * .9)

# Object Containment  ==========================================================================================

class Author:
    def __init__(self, name:str, year_of_birth:int) -> None:
        self.name = name
        self.year_of_birth = year_of_birth

    def equal(self, that:Author) -> bool:
        # self.name ... self.year_of_birth
        return self.name == that.name and self.year_of_birth == that.year_of_birth

class Book:
    def __init__(self, author:Author, title:str, price:int, pub_year:int) -> None:
        self.author = author
        self.title = title
        self.price = price # in cents
        self.pub_year = pub_year

    # checks whether the book appeared during a given year
    def currentBook(self, thatYear) -> bool:
        # self.author.mmm() ... self.title ... self.price ... self.pub_year
        return self.pub_year == thatYear

    # determines whether a book is written by that Author
    def thisAuthor(self, thatAuthor:Author) -> bool:
        # self.author.mmm() ... self.title ... self.price ... self.pub_year
        return self.author.equal(thatAuthor)

    # determines whether a book is written by the same author as a that book
    def sameAuthor(self, that:Book) -> bool:
        # self.author.mmm() ... self.title ... self.price ... self.pub_year
        return self.author.equal(that.author)

