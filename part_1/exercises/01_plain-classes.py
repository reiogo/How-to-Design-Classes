class Book:
    def __init__(self, author:str, title:str, price:int, pub_year:int) -> None:
        self.author = author
        self.title = title
        self.price = price # in cents
        self.pub_year = pub_year

class BookExamples:
    crusoe = Book("Daniel Defoe", "Robinson Crusoe", 1550, 1719)
    darkness = Book("Joseph Conrad", "Heart of Darkness", 1280, 1902)
    beach = Book("Pat Conroy", "Beach Music", 950, 1996)


class Image:
    def __init__(self, height: int, width: int, source: str, quality: str, gallery: str) -> None:
        self.height = height # pixels
        self.width = width # pixels
        self.source = source # file name
        self.quality = quality # informal
        self.gallery = gallery

egimage = Image(5, 10, "small.gif", "low")

class Automobile:
    def __init__ (self, model: str, price: int, mileage: float, used: bool) -> None:
        self.model = model
        self.price = price # in dollars 
        self.mileage = mileage # in miles per gallon
        self.used = used

egcar = Automobile("idkmodel", 3000, 400.0, true)


# introducing the concept of gravity
class Apple:
    RADIUS = 5
    G = 10 # meters per second square
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class AppleEg:
    a1 = Apple(4,5)
    a2 = Apple(3,4)
    a3 = Apple(2,2)



