from chapters.chapt_8_to_14 import *
import pytest

def test_coffee_cost():
    kona = Coffee("Hawaiian Kona", 2095, 100)
    ethi = Coffee("Ethiopian", 800, 1000)
    colo = Coffee("Colombia Supreme", 950, 200)
    discount1 = Coffee("Colombia Supreme", 950, 5000)
    discount2 = Coffee("Colombia Supreme", 950, 5001)
    discount3 = Coffee("Colombia Supreme", 950, 20000)
    discount4 = Coffee("Colombia Supreme", 950, 20001)

    assert(kona.cost() == 209500)
    assert(ethi.cost() == 800000)
    assert(colo.cost() == 190000)
    assert(discount1.cost() == 4275000)
    assert(discount2.cost() == 4275855)
    assert(discount3.cost() == 14250000)
    assert(discount4.cost() == 14250712)

def test_coffee_moreCents():
    assert(Coffee("Hawaiian Kona", 2095, 100).moreCents(1200) is True)
    assert(Coffee("Ethiopian", 800, 1000).moreCents(799) is True)
    assert(Coffee("Colombia Supreme", 950, 200).moreCents(1000) is False )

def test_coffee_lighterThan():
    assert(Coffee("Hawaiian Kona", 2095, 100)
           .lighterThan(Coffee("Ethiopian", 800, 1000)) is True)
    assert(Coffee("Ethiopian", 800, 1000)
           .lighterThan(Coffee("Colombia Supreme", 950, 200)) is False)


# Bank  ==========================================================================================
def test_CD_interest():
    assert(CD("ray", 100).interest() == 2)
    assert(CD("ray", 250000).interest() == 5000)
    assert(CD("ray", 500000).interest() == 11250)
    assert(CD("ray", 510000).interest() == 11475)
    assert(CD("ray", 1000000).interest() == 25000)
    assert(CD("ray", 1100000).interest() == 27500)

# Star  ==========================================================================================
class Test_Star:
    s = Star(10)
    t = Star(100)

    def test_start_drop(self):
        assert(self.s.drop() == Star(15))
        assert(self.t.drop() == Star(100))
        assert(Star(98).drop() == Star(100))
        assert(Star(94).drop() != Star(100))

# Rectangle  ==========================================================================================

class Test_Rect:
    p = CartPt(3,4)
    q = CartPt(5,12)

    r = Rectangle(p, 5, 17)
    s = Rectangle(q, 10, 10)

    def test_distance(self):
        assert(self.p.distance() == 5)
        assert(self.q.distance() == 13)

        assert(self.r.distance() == 5)
        assert(self.s.distance() == 13)

# WeatherRecord ==========================================================================================

class Test_WeatherRecord:
    d1 = Date(2,9,1959)
    d2 = Date(8,8,2004)
    d3 = Date(12,12,1999)

    tr1 = TemperatureRange(66, 88)
    tr2 = TemperatureRange(70,99)
    tr3 = TemperatureRange(28,31)
    tr4 = TemperatureRange(65, 89)

    r1 = WeatherRecord(d1, tr1, tr4, tr3, 0)
    r2 = WeatherRecord(d2, tr2, tr3, tr1, 10)
    r3 = WeatherRecord(d3, tr3, tr1, tr2, 0)

    def test_differential(self):
        assert(self.r1.differential() == 22)

    def test_withinRange(self):
        assert(self.r1.withinRange() is True)
        assert(self.r2.withinRange() is False)

    def test_rainyDay(self):
        assert(self.r1.rainyDay(1) is False)
        assert(self.r2.rainyDay(1) is True)

    def test_recordDay(self):
        assert(self.r1.recordDay() is True)

# Shape ==========================================================================================

class TestShapes:
    dot:IShape = Dot(CPt(4,3))
    squ:IShape = Square(CPt(4,3), 3)
    cir:IShape = Circle(CPt(12,5), 2)
    tri:IShape = IsoTri(CPt(4,3), 2)

    def testarea(self):
        # d = Dot(CPt(10,22))
        # with pytest.raises(NotImplementedError):
        #     d.area()
        assert(self.dot.area() == pytest.approx(0.0, abs=0.1))
        assert(self.squ.area() == pytest.approx(9.0, abs=0.1))
        assert(self.cir.area() == pytest.approx(12.56, abs=0.01))

    def testsame(self) -> None:
        assert CPt(4,3).same(CPt(4,3)) is True
        assert CPt(3,3).same(CPt(4,3)) is False

    def testcptdistTos0(self):
        assert CPt(4,3).distTo0() == 5.0
        assert CPt(12,5).distTo0() == 13.0

    def testdistTo0(self):
        assert self.dot.distTo0() == 5.0
        assert self.squ.distTo0() == 5.0
        assert self.cir.distTo0() == 11.0

    def testdistTo(self) -> None:
        assert CPt(10, 4).distTo(CPt(14,7)) == 5.0

    def testwithin(self) -> None:
        d1:IShape = Dot(CPt(100, 200))
        assert d1.within(CPt(100,200)) is True
        assert d1.within(CPt(90,220)) is False

        s1:IShape = Square(CPt(100,200), 40)
        assert s1.within(CPt(120, 220)) is True
        assert s1.within(CPt(80, 220)) is False

        c1:IShape = Circle(CPt(0,0),20)
        assert c1.within(CPt(4,3)) is True
        assert c1.within(CPt(20,5)) is False

    def testtranslate(self) -> None:
        assert CPt(10, 11).translate(4) == CPt(14, 15)
        assert CPt(10, 11).translate(-4) == CPt(6, 7)

    def testbb(self) -> None:
        assert Dot(CPt(100,200)).bb() == Square(CPt(100,200),1)
        assert self.squ.bb() == self.squ
        assert self.cir.bb() == Square(CPt(10,3), 4)

    def testIsoTri(self) -> None:
        t1 = IsoTri(CPt(4,3), 2)
        assert t1.area() == 2.0
        assert t1.distTo0() == 5.0
        assert t1.within(CPt(3,2)) is True
        assert t1.within(CPt(5,2)) is False
        # assert t1.bb() == Square(CPt(2,1), 2)

        # helper methods
        assert t1.between(4, 3, 2) is True
        assert t1.between(4, 5, 2) is False
        assert t1.between(4, 1, 2) is False

    def testperimeter(self) -> None:
        assert self.dot.perimeter() == 0.0
        assert self.squ.perimeter() == 12
        assert self.cir.perimeter() == pytest.approx(4 * 3.14, abs=0.1)
        assert self.tri.perimeter() == pytest.approx(6.82, abs=0.1)


# Shape ==========================================================================================
def testroomcovered():
    r1 = Room(10, 10, Square(CPt(1,2), 5), Square(CPt(9,9), 5), Dot(CPt(3,3)))
    assert r1.covered() == 0.5

