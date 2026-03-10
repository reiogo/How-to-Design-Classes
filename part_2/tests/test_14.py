from exercises.chap14_methods_and_unions import *

# IGallery =============================================================
# image1 = Image("flower.gif", 57234, 100, 50, "medium")
# txt1 = Text("welcome.txt",5312, 830)
# music1 = Mp3("theme.mp3", 40960, 200)

def test_image_timetodownload():
    image1 = Image("flower.gif", 57234, 100, 50, "medium")
    assert image1.timeToDownload(200) ==  57234 // 200

def test_image_smallerThan():
    image1 = Image("flower.gif", 57234, 100, 50, "medium")
    assert image1.smallerThan(200) is False
    assert image1.smallerThan(200000) is True

def test_image_sameName():
    image1 = Image("flower.gif", 57234, 100, 50, "medium")
    assert image1.sameName("boyo.gif") is False
    assert image1.sameName("flower.gif") is True

def test_text_timetodownload():
    txt1 = Text("welcome.txt",5312, 830)
    assert txt1.timeToDownload(200) == 5312 // 200

def test_text_smallerThan():
    txt1 = Text("welcome.txt",5312, 830)
    assert txt1.smallerThan(200) is False
    assert txt1.smallerThan(200000) is True

def test_text_sameName():
    txt1 = Text("welcome.txt",5312, 830)
    assert txt1.sameName("boyo.gif") is False
    assert txt1.sameName("welcome.txt") is True

def test_mp3_timetodownload():
    music1 = Mp3("theme.mp3", 40960, 200)
    assert music1.timeToDownload(200) == 40960 // 200

def test_mp3_smallerThan():
    music1 = Mp3("theme.mp3", 40960, 200)
    assert music1.smallerThan(200) is False
    assert music1.smallerThan(200000) is True

def test_mp3_sameName():
    music1 = Mp3("theme.mp3", 40960, 200)
    assert music1.sameName("boyo.gif") is False
    assert music1.sameName("theme.mp3") is True


def test_icecream_unitPrice():
    ice1 = IceCream("B&J", 100, 200, "Vanilla")
    assert ice1.unitPrice() == 2

def test_icecream_lowerUnitPrice():
    ice1 = IceCream("B&J", 100, 200, "Vanilla")
    assert ice1.lowerUnitPrice(3) is True

def test_icecream_lowerUnitPrice():
    ice1 = IceCream("B&J", 100, 200, "Vanilla")
    ice2 = IceCream("B&J", 100, 300, "Chocolate")
    assert ice1.cheaperThan(ice2) is True

def test_coffee_unitPrice():
    coffee1 = Coffee("Good", 100, 200, True)
    assert coffee1.unitPrice() == 2

def test_coffee_lowerUnitPrice():
    coffee1 = Coffee("Good", 100, 200, True)
    assert coffee1.lowerUnitPrice(3) is True

def test_coffee_lowerUnitPrice():
    coffee1 = Coffee("Good", 100, 200, True)
    coffee2 = Coffee("Good caf", 100, 300, False)
    assert coffee1.cheaperThan(coffee2) is True

def test_juice_unitPrice():
    juice1 = Juice("Sun", 100, 200, "juice", "Frozen")
    assert juice1.unitPrice() == 2

def test_juice_lowerUnitPrice():
    juice1 = Juice("Sun", 100, 200, "juice", "Frozen")
    assert juice1.lowerUnitPrice(3) is True

def test_juice_lowerUnitPrice():
    juice1 = Juice("Sun", 100, 200, "juice", "Frozen")
    juice2 = Juice("Sun", 100, 300, "juice", "Fresh")
    assert juice1.cheaperThan(juice2) is True
