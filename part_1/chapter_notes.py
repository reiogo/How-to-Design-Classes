from typing import Protocol
from dataclasses import dataclass
class Coffee:
    def __init__(self, kind:str, price:int, weight:int) -> None:
        self.kind = kind
        self.price = price # cents per pound
        self.weight = weight # pounds



# collect eamples of coffee sales
class CoffeeExamples:
    kona = Coffee("Hawaiian Kona", 2095, 100)
    ethi = Coffee("Ethiopian", 800, 1000)
    colo = Coffee("Colombia Supreme", 800, 1000)




class Date:
    def __init__(self, day:int, month:int, year:int) -> None:
        self.day = day
        self.month = month
        self.year = year

june5 = Date(5,6,2026)
print(june5.month)


class GPSLocation:
    def __init__(self, latitude:float, longitude:float) -> None:
        self.latitude = latitude # degrees
        self.longitude = longitude # degrees

loc1 = GPSLocation(33.5, 86.8)
loc2 = GPSLocation(40.2, 72.4)
loc3 = GPSLocation(49.0, 110.3)


# moving balls on pool table
class Ball:
    RADIUS = 5
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y





class Place:
    def __init__(self, ave:int, street:int) -> None:
        self.ave = ave
        self.street = street

class Restaurant:
    def __init__(self, name: str, kind: str, pricing:str, place: Place) -> None:
        self.name = name
        self.kind = kind
        self.pricing = pricing
        self.place =place

p1 = Place(7, 65)
p2 = Place(2, 86)
p3 = Place(10, 113)
r1 = Restaurant("La Crepe", "French", "moderate", p1)
r2 = Restaurant("Bremen Haus", "German", "moderate", p2)
r3 = Restaurant("Moon Palace", "Chinese", "inexpensive", p3)



class Routes:
    def __init__(self, origin:str, dest:str)->None:
        self.origin = origin
        self.dest = dest

class ClockTime:
    def __init__(self, hour:int, minute:int)->None:
        self.hour = hour
        self.minute = minute

class Schedules:
    def __init__(self, departure:ClockTime, arrival:ClockTime)->None:
        self.departure = departure
        self.arrival = arrival

class Train:
    def __init__(self, route:Routes,schedule:Schedules, local:bool,)->None:
        self.local = local
        self.route = route
        self.schedule = schedule

ro1 = Routes("New York", "Boston")
ro2 = Routes("Chicago", "New York")

t1 = ClockTime(23,50)
t2 = ClockTime(13,20)
t3 = ClockTime(10,34)
t4 = ClockTime(13,18)

s1 = Schedules(t1,t2)
s2 = Schedules(t3,t4)

train1 = Train(ro1,s1, True)
train2 = Train(ro2,s2, False)

# Unions, self-reference, mutual references ======================================

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

# logs where entry3 comes after entry1
l5 = ConsLog(entry3, l1)
# logs where entry3 comes after entry2
l6 = ConsLog(entry3, l2)

date4 = Date(15,6,2026)
date5 = Date(16,6,2026)
date6 = Date(23,6,2026)
date7 = Date(28,6,2026)

entry4 = Entry(date4, 15.3, 87, "Great")
entry5 = Entry(date5, 12.8, 84, "Good")
entry6 = Entry(date6, 26.2, 250, "Dead")
entry7 = Entry(date7, 26.2, 150, "Good recovery")

l5 = ConsLog(entry4, l4)
l6 = ConsLog(entry5, l5)
l7 = ConsLog(entry6, l6)
l8 = ConsLog(entry7, l7)


#interface
class ILoR(Protocol):
    pass

#implements ILoR
class EmptyListing:
    pass

#implements ILoR
@dataclass
class ConsListing:
    fst:Restaurant
    rst:ILoR

ex1 = Restaurant("Chez Nous", "French", "exp.", Place(7,56))
ex2 = Restaurant("Das Bier", "German", "cheap.", Place(2,86))
ex3 = Restaurant("Sun", "Chinese", "cheap.", Place(10,113))


lor_empty = EmptyListing()
lor1 = ConsListing(ex1, lor_empty)
lor2 = ConsListing(ex2, lor_empty)
lor3 = ConsListing(ex3, lor_empty)
lor_all = ConsListing(ex1, ConsListing(ex2, ConsListing(ex3,lor_empty)))

# Containment in Unions, part 2======================================

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

@dataclass
class SuperImp:
    bot:IShape
    top:IShape

shapeEg = SuperImp(Square(CartPt(20,40),20), Circle(CartPt(40,30),15))

cp1 = CartPt(100,200)
cp2 = CartPt(20,50)
cp3 = CartPt(0, 0)

square1 = Square(cp1, 40)
square2 = Square(cp2, 30)
circle1 = Circle(cp3, 20)

sh1 = SuperImp(circle1, square1)
sh2 = SuperImp(square2, Square(cp1, 300))
sh3 = SuperImp(square1, sh2)



@dataclass
class Mouth:
    loc:Location
    river:IRiver

@dataclass
class Location:
    x:int
    y:int
    name:str


# interface
class IRiver(Protocol):
    pass

#implements IRiver
@dataclass
class Source:
    loc:Location

#implements IRver
@dataclass
class Confluence:
    loc:Location
    left:IRiver
    right:IRiver

class RiverSystemExample:
    lm = Location(7,5,"m")
    la = Location(5,5,"a")
    lb = Location(3,3,"b")
    ls = Location(1,1,"s")
    lt = Location(1,5,"t")
    lu = Location(3,7,"u")

    s = Source(ls)
    t = Source(lt)
    u = Source(lu)

    b = Confluence(lb,s,t)
    a = Confluence(la,b,u)

    mth = Mouth(lm,a)


