from dataclasses import dataclass
from typing import Protocol

# Real Estate List =========================================================
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


a1 = Addr(23, "Maple Street", "Brookline")
a2 = Addr(5, "Joye Road", "Newton")
a3 = Addr(83, "Winslow Road", "Waltham")

h1 = House("Ranch", 7, a1, 375000)
h2 = House("Colonial", 9, a2, 450000)
h3 = House("Cape", 6, a3, 235000)


#interface 
class ILoH(Protocol):
    pass

class EmptyLoH:
    pass

@dataclass
class ConsLoH:
    fst:House
    rst:ILoH

emptyloh = EmptyLoH()
loh1 = ConsLoH(h1, emptyloh)
loh2 = ConsLoH(h2, loh1)
loh3 = ConsLoH(h3, loh2)


# Librarian List =========================================================

class Author:
    def __init__(self, name:str, year_of_birth:int) -> None:
        self.name = name
        self.year_of_birth = year_of_birth

class Book:
    def __init__(self, author:Author, title:str, price:int, pub_year:int) -> None:
        self.author = author
        self.title = title
        self.price = price # in cents
        self.pub_year = pub_year

au1 = Author("Daniel Defoe", 1660)
au2 = Author("Joseph Conrad", 1857)
au3 = Author("Pat Conroy", 1945)

crusoe = Book(au1, "Robinson Crusoe", 1550, 1719)
darkness = Book(au2, "Heart of Darkness", 1280, 1902)
beach = Book(au3, "Beach Music", 950, 1996)

#interface
class ILoB(Protocol):
    pass
class EmptyLoB:
    pass
@dataclass
class ConsLoB:
    fst:Book
    rst:ILoB

au4 = Author("Ray Bradbury", 1920)
fahr = Book(au4, "Fahrenheit 451", 750, 1953)
lob1 = ConsLoB(crusoe, ConsLoB(darkness, ConsLoB(beach, EmptyLoB())))
lob2 = ConsLoB(beach, ConsLoB(fahr, EmptyLoB()))

# Weather Record List =========================================================

class Date:
    def __init__(self, day:int, month:int, year:int) -> None:
        self.day = day
        self.month = month
        self.year = year

class TemperatureRange:
    def __init__(self, high:int, low:int) -> None:
        self.high = high
        self.low = low

class WeatherRecord:
    def __init__(self, date:Date, today:TemperatureRange, normal:TemperatureRange, record:TemperatureRange):
        self.date = date
        self.today = today
        self.normal = normal
        self.record = record

#interface
class IWR(Protocol):
    pass

#implements IWR
class EmptyWR:
    pass
#implements IWR
@dataclass
class ConsWR:
    fst:WeatherRecord
    rst:IWR

date1 = Date(31,1,2026)
t1 = TemperatureRange(0,5)
t2 = TemperatureRange(2,7)
t3 = TemperatureRange(-3,0)

t4 = TemperatureRange(0,5)
t5 = TemperatureRange(2,7)
t6 = TemperatureRange(-3,0)

w1 = WeatherRecord(date1,t1,t2,t3)
w2 = WeatherRecord(date1,t4,t5,t6)

wr1 = ConsWR(w1, ConsWR(w2, EmptyWR()))


# Containment in Unions, not lists =========================================================

#interface 
class IAncestor(Protocol):
    pass

#implements IAncestor
@dataclass
class Person:
    name:str
    bd:int
    mom:IAncestor
    dad:IAncestor

class Unknown:
    pass

sampletree = Person("Peter", 1980,
                    Person("Janet", 1958,
                           Person("Angela", 1936, Unknown(), Unknown()),
                           Person("Robert", 1935, Unknown(), Unknown())),
                    Person("Paul", 1956,
                           Person("Annie", 1938,
                                  Unknown(),
                                  Person("Bob", 1917, Unknown(), Unknown())),
                           Unknown()))


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
    name:str

#implements IRver
@dataclass
class Confluence:
    loc:Location
    name:str
    left:IRiver
    right:IRiver

mouth = loc(0,0,"mouth")
rhinexmaas = loc(3,5,"rhine")
france = loc(5,60,"france")
germany = loc(30,45,"germany")
maas = Mouth(mouth,
             Confluence(rhinexmaas, "rhinexmaas",
                        Source(france, "maas"),
                        Source(germany, "rhine")))

@dataclass
class Coach:
    team:IPT

@dataclass
class Player:
    name:str
    phone:int

#interface:
class IPT(Protocol):
    pass

class EmptyTeam:
    pass

@dataclass
class PhoneTree:
    call1:IPT
    call2:IPT
    p:Player


