from dataclasses import dataclass
from typing import Protocol

@dataclass
class Package:
    recipient:IPerson
    sender:IPerson
    size:str
    weight:int #kilogram
    URL:str

class Addr:
    def __init__(self, street_num:int, street_name:str, city:str) -> None:
        self.street_num = street_num
        self.street_name = street_name
        self.city = city

#interface
class IPerson(Protocol):
    pass

#implements Person
@dataclass
class Sender:
    name:str
    address:Addr

#implements Person
@dataclass
class Recipient:
    name:str
    address:Addr

a1 = Addr(23, "Maple Street", "Brookline")
a2 = Addr(5, "Joye Road", "Newton")

p1 = Package(Sender("John", a1), Recipient("Hank", a2), "big", 30, "www.hi.com")

class Place:
    def __init__(self, ave:int, street:int) -> None:
        self.ave = ave
        self.street = street

@dataclass
class Hours:
    opening:int
    closing:int

#interface
class Business(Protocol):
    pass

#implements Business
@dataclass
class Museum:
    name:str
    price:int # cents
    hours:Hours
    place:Place

#implements Business
@dataclass
class Shop:
    name:str
    kind:str
    hours:Hours
    place:Place


#implements Business
class Restaurant:
    def __init__(self, name: str, kind: str, pricing:str, place: Place) -> None:
        self.name = name
        self.kind = kind
        self.pricing = pricing
        self.place =place

place1 = Place(7, 65)
place2 = Place(2, 86)
place3 = Place(10, 113)

museu1 = Museum("natural history museum", 2340, Hours(9,19), place1)
rest2 = Restaurant("Bremen Haus", "German", "moderate", place2)
shop1 = Shop("corner", "convenience", Hours(7,11), place3)

@dataclass
class Time:
    hour: int
    mins: int

#interface
class IRoute(Protocol):
    pass

#implements IRoute
class EmptyRoute:
    pass

#implements IRoute
@dataclass
class Stop:
    name:str
    arrival:Time
    departure:Time
    rest:IRoute

route1 = Stop("paddington",
                 Time(10,30),
                 Time(10,32),
                 Stop("picadilly",
                         Time(10,34),
                         Time(10,35),
                         EmptyRoute()))

#interface
class IEstate(Protocol):
    pass


#implements IEstate
@dataclass
class FamilyHouse:
    address:Addr
    living_area:int
    asking_price:int #dollars
    land_area:int
    rooms:int

#implements IEstate
@dataclass
class TownHouse:
    address:Addr
    living_area:int
    asking_price:int #dollars
    garden_area:int

#implements IEstate
@dataclass
class Condo:
    address:Addr
    living_area:int
    asking_price:int #dollars
    num_rooms:int
    wheelchair_accessible:bool

# GRAPHICAL USER INTERFACE ====================================================

#interface
class IGUI(Protocol):
    pass

#implements IGUI
@dataclass
class BoolView:
    label:str
    data:str

#implements IGUI
@dataclass
class TextFieldView:
    label:str
    data:str

#implements IGUI
@dataclass
class OptionsView:
    label:str
    data:str

#implements IGUI
@dataclass
class ColorView:
    label:str
    data:str


#implements IGUI
@dataclass
class Table:
    rows:ILoRow

#interface
class ILoGUI(Protocol):
    pass

class EmptyLoGUI:
    pass

@dataclass
class ConsLoGUI:
    fst: IGUI
    rst:ILoGUI


class ILoRow(Protocol):
    pass

class EmptyLoRow:
    pass
@dataclass
class ConsLoRow:
    fst:ILoGUI
    rst:ILoRow

# Libary Checkout =============================================================================================

#interface 
class ICheckout(Protocol):
    pass

#implements ICheckout
@dataclass
class Book:
    title:str
    cat_id:int
    author:str
    pub_year:int

#implements ICheckout
@dataclass
class CD:
    title:str
    cat_id:int
    artist:str
    track_num:int


#implements ICheckout
@dataclass
class DVD:
    title:str
    cat_id:int
    kind:str
    length:int #mins

# COMPANY STRUCTURE ==========================================================================================

@dataclass
class Employee:
    id:int
    name:str
    title:str
    team:ILoEmployees

#interface
class ILoEmployees(Protocol):
    pass

#implements ILoEmployees
class EmptyLoEmployees:
    pass

@dataclass
class ConsLoEmployees:
    fst:Employee
    rst:ILoEmployees

john = Employee(2, "john", "support", EmptyLoEmployees())
katy = Employee(3, "katy", "cto", EmptyLoEmployees())

hank_team = ConsLoEmployees(john,
                            ConsLoEmployees(katy,EmptyLoEmployees()))
hank = Employee(1,"hank","ceo", hank_team)

# CARD GAME ==========================================================================================

@dataclass
class Pebble:
    color:str

#interface
class IWallet(Protocol):
    pass

#implements IWallet
class EmptyWallet:
    pass

#implements IWallet
@dataclass
class ConsWallet:
    fst:Pebble
    rst:IWallet

@dataclass
class Card:
    p:Pebble
    designation:str

#interface
class IDeck(Protocol):
    pass

#implements IDeck
class EmptyDeck:
    pass

#implements IDeck
@dataclass
class ConsDeck:
    fst:Card
    rst:IDeck

red_p = Pebble("red")

my_wallet = ConsWallet(red_p, EmptyWallet())

red_card = Card(red_p, "super")

deck = ConsDeck(red_card, EmptyDeck())

# PUZZLE ==========================================================================================

@dataclass
class State:
    start:ILoP
    destination:ILoP
    light_time:int # remmaining battery time
    light_loc:str # start or destination

#interface
class ILoP(Protocol):
    pass

#implements ILoP
class EmptyILoP:
    pass

#implements ILoP
@dataclass
class ConsILoP:
    fst:Person
    rst:ILoP

@dataclass
class Person:
    name:str
    time:int
