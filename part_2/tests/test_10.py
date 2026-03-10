from exercises.chap10_methods_for_classes import *

# Image ==========================================================================================
def test_image_isPortrait():
    assert(Image(5, 10, "small.gif", "low", "place").isPortrait() is False)

def test_image_size():
    assert(Image(5, 10, "small.gif", "low", "place").size() == 50)

def test_image_sizeString():
    assert(Image(5, 10, "small.gif", "low", "place").sizeString() == "small")
    assert(Image(5, 2000, "small.gif", "low", "place").sizeString() == "small")
    assert(Image(6, 2000, "small.gif", "low", "place").sizeString() == "medium")
    assert(Image(6, 200000, "small.gif", "low", "place").sizeString() == "large")

def test_image_isLarger():
    assert(Image(5, 10, "small.gif", "low", "place")
           .isLarger(Image(4, 10, "small.gif", "low", "place"))
           is True)
    assert(Image(5, 10, "small.gif", "low", "place")
           .isLarger(Image(6, 10, "small.gif", "low", "place"))
           is False)

def test_image_same():
    assert(Image(5, 10, "small.gif", "low", "place")
           .same(Image(4, 10, "small.gif", "low", "place"))
           is False)
    assert(Image(5, 10, "small.gif", "low", "place")
           .same(Image(5, 10, "small.gif", "low", "place"))
           is True)


# House  ==========================================================================================

class Test_house:

    a1 = Addr(23, "Maple Street", "Brookline")
    a2 = Addr(5, "Joye Road", "Newton")
    a3 = Addr(83, "Winslow Road", "Waltham")

    h1 = House("Ranch", 7, a1, 375000)
    h2 = House("Colonial", 9, a2, 450000)
    h3 = House("Cape", 6, a3, 235000)

    def test_house_isBigger(self):
        assert(self.h1.isBigger(self.h2) is False)

    def test_house_thisCity(self):
        assert(self.h1.thisCity("New York") is False)
        assert(self.h1.thisCity("Brookline") is True)

    def test_house_sameCity(self):
        assert(self.h1.sameCity(self.h2) is False)
        assert(self.h1.sameCity(self.h1) is True)


def test_runnerLog_pace():
    assert(Entry(Date(5,6,2026), 5.3, 27, "Good").pace() == (5.3/ 27))

def test_date_earlierThan():
    assert(Date(5,6,2026).earlierThan(Date(4,6,2026)) is False)
    assert(Date(5,6,2026).earlierThan(Date(6,6,2026)) is True)



# BouncingBall  ==========================================================================================
def test_ball_move():
    assert(BouncingBall(0).move() == BouncingBall(4))
    assert(BouncingBall(99).move() == BouncingBall(100, False))
    assert(BouncingBall(96, False).move() == BouncingBall(92, False))
    assert(BouncingBall(3, False).move() == BouncingBall(0))

# Precipitation  ==========================================================================================

def test_precipitation_average():
    assert(Precipitation(3,4,5).average() == 4)

# JetFuel  ==========================================================================================
def test_jetfuel_totalCost():
    assert(JetFuel(1, "high", 14).totalCost() == 14)
    assert(JetFuel(100000, "high", 14).totalCost() == 1400000)
    assert(JetFuel(100001, "high", 14).totalCost() == (int)(100001 * 14 * .9))

# JetFuel  ==========================================================================================
class Test_Book:
    au1 = Author("Daniel Defoe", 1660)
    au2 = Author("Joseph Conrad", 1857)
    au3 = Author("Pat Conroy", 1945)

    crusoe = Book(au1, "Robinson Crusoe", 1550, 1719)
    darkness = Book(au2, "Heart of Darkness", 1280, 1902)
    beach = Book(au3, "Beach Music", 950, 1996)

    def test_currentBook(self):
        assert(self.crusoe.currentBook(1719) is True)
        assert(self.crusoe.currentBook(1990) is False)
    def test_thisAuthor(self):
        assert(self.crusoe.thisAuthor(self.au1) is True)
        assert(self.crusoe.thisAuthor(self.au2) is False)
    def test_sameAuthor(self):
        assert(self.crusoe.sameAuthor(self.darkness) is False)

