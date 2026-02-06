from typing import Protocol
from dataclasses import dataclass

class IShape(Protocol):
    pass

class CartPt:
    # I can also technically do this right?
    x:int
    y:int
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

class Dot:
    # implements IShape
    def __init__(self, loc: CartPt):
        self.loc = loc

class Square:
    # implements IShape
    def __init__(self,loc: CartPt, size:int):
        self.loc = loc
        self.size = size
        
class Circle:
    # implements IShape
    def __init__(self, loc: CartPt, radius:int):
        self.loc = loc
        self.radius = radius


d1 = Dot(CartPt(-3,4))
c1 = Circle(CartPt(12,5), 10)
s1 = Square(CartPt(30,-60),20)


class ISalesItem(Protocol):
    pass
@dataclass
class DeepDiscount:
    # implements ISalesItem
    originalPrice:int

@dataclass
class RegularDiscount:
    # implements ISalesItem
    originalPrice:int
    discountPercentage:int


s = DeepDiscount(9899)
t = RegularDiscount(9900,10)
# if u is defined as RegularDiscount, then it is RegularDiscount
u = RegularDiscount(9900,10)


class IZooAnimal(Protocol):
    pass

class Lion:
    meat:int
    weight:int
    name:str
    def __init__(self, name:str, weight:int, meat:int) -> None:
        self.meat = meat
        self.name = name
        self.weight = weight

class Snake:
    def __init__(self, name:str, weight:int, length:int) -> None:
        self.name = name
        self.weight = weight
        self.length = length

@dataclass
class Snake2:
    name:str
    weight:int
    length:int


class Monkey:
    def __init__(self, name:str, weight:int, food:str) -> None:
        self.name = name
        self.weight = weight
        self.food = food


leo = Lion("Leo", 300, 5)
boa = Snake("Ana", 150, 5)
george = Monkey("George", 150, "kiwi")
boa2 = Snake("Ana2", 150, 5)


class Date:
    def __init__(self, day:int, month:int, year:int) -> None:
        self.day = day
        self.month = month
        self.year = year

class IBank(Protocol):
    pass

@dataclass
class Checking:
    name:str
    id:int
    cur:int #in dollars
    min:int #in dollars

@dataclass
class Savings:
    name:str
    id:int
    cur:int #in dollars
    interest:int #in .1%

@dataclass
class CD:
    name:str
    id:int
    cur:int #in dollars
    interest:int #in .1%
    maturity_date:Date

u1 = Checking("Earl Gray", 1729, 1250,500)
date1 = Date(1,6,2005)
u2 = CD("Ima Flatt", 4104, 10123, 40, date1)
u3 = Savings("Annie Proulx", 2992, 800, 35)


class IGalleryItem(Protocol):
    pass

class Image:
    name:str
    size:int #bytes
    height:int #pixels
    width:int #pixels
    quality:str

    def __init__(self, name:str, size:int,  height:int,  width:int,  quality:str):
        self.name = name
        self.size = size
        self.height = height
        self.width = width
        self.qualtiy = quality

class Text:
    name:str
    size:int #bytes
    numLines:int
    def __init__(self, name:str, size:int, numLines:int):
        self.name = name
        self.size = size
        self.numLines = numLines


class Mp3:
    name:str
    size:int #bytes
    playing_time:int #second
    def __init__(self, name:str, size:int, playing_time:int):
        self.name = name
        self.size = size
        self.playing_time = playing_time

image1 = Image("flower.gif", 57234, 100, 50, "medium")
txt1 = Text("welcome.txt",5312, 830)
music1 = Mp3("theme.mp3", 40960, 200)


class ITaxiVehicle(Protocol):
    pass

class Cab:
    idNum:int
    passengers:int
    pricePerMile:int #dollars

    def __init__(self, idNum:int, passengers:int, pricePerMile:int):
        self.idNum = idNum
        self.passengers = passengers
        self.pricePerMile = pricePerMile

class Limo:
    minRental:int
    idNum:int
    passengers:int
    pricePerMile:int #dollars

    def __init__ (self, idNum:int, passengers:int, pricePerMile:int, minRental:int,):
        self.minRental = minRental
        self.idNum = idNum
        self.passengers = passengers
        self.pricePerMile = pricePerMile

class Van:
    access:bool
    idNum:int
    passengers:int
    pricePerMile:int #dollars

    def __init__(self, idNum:int, passengers:int, pricePerMile:int, access:bool):
        self.access = access
        self.idNum = idNum
        self.passengers = passengers
        self.pricePerMile = pricePerMile

cab1 = Cab(234,2,5)
limo1 = Limo(523,4,17,80)
van1 = Van(838, 7, 7,True)





