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

d1 = Date(31,1,2026)
t1 = TemperatureRange(0,5)
t2 = TemperatureRange(2,7)
t3 = TemperatureRange(-3,0)

w1 = WeatherRecord(d1,t1,t2,t3)


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

class BookExamples:
    a1 = Author("Daniel Defoe", 1660)
    a2 = Author("Joseph Conrad", 1857)
    a3 = Author("Pat Conroy", 1945)

    crusoe = Book(a1, "Robinson Crusoe", 1550, 1719)
    darkness = Book(a2, "Heart of Darkness", 1280, 1902)
    beach = Book(a3, "Beach Music", 950, 1996)



