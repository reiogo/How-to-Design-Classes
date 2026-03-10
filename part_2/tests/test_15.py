from chapters.chapt_15 import *
import pytest

# Runner's Log ==========================================================================================

def test_runners_miles()->None:
    d1 = Date(5,5,2023)
    d2 = Date(6,6,2023)
    d3 = Date(23,6,2023)

    e1 = Entry(d1, 5.0,25,"Good")
    e2 = Entry(d2, 3.0,24,"Tired")
    e3 = Entry(d3, 26.0,156,"Great")

    l1:ILog = MTLog()
    l2:ILog = ConsLog(e1,l1)
    l3:ILog = ConsLog(e2,l2)
    l4:ILog = ConsLog(e3,l3)

    assert l1.miles() == pytest.approx(0.0,abs=.1)
    assert l2.miles() == pytest.approx(5.0,abs=.1)
    assert l3.miles() == pytest.approx(8.0,abs=.1)
    assert l4.miles() == pytest.approx(34.0,abs=.1)

def test_runners_oneMonth()->None:
    d1 = Date(5,5,2023)
    d2 = Date(6,6,2023)
    d3 = Date(23,6,2023)

    e1 = Entry(d1, 5.0,25,"Good")
    e2 = Entry(d2, 3.0,24,"Tired")
    e3 = Entry(d3, 26.0,156,"Great")

    l1:ILog = MTLog()
    l2:ILog = ConsLog(e1,l1)
    l3:ILog = ConsLog(e2,l2)
    l4:ILog = ConsLog(e3,l3)

    assert l1.oneMonth(6,2023) == MTLog()
    assert l3.oneMonth(6, 2023) == ConsLog(e2, MTLog())
    assert l4.oneMonth(6, 2023) == ConsLog(e3, ConsLog(e2, MTLog()))

def test_runners_milesInMonth()->None:
    d1 = Date(5,5,2023)
    d2 = Date(6,6,2023)
    d3 = Date(23,6,2023)

    e1 = Entry(d1, 5.0,25,"Good")
    e2 = Entry(d2, 3.0,24,"Tired")
    e3 = Entry(d3, 26.0,156,"Great")

    l1:ILog = MTLog()
    l2:ILog = ConsLog(e1,l1)
    l3:ILog = ConsLog(e2,l2)
    l4:ILog = ConsLog(e3,l3)

    assert l1.milesInMonth(6,2023) == 0
    assert l3.milesInMonth(6, 2023) == 3.0
    assert l4.milesInMonth(6, 2023) == 29.0

def test_runners_longestRun()->None:
    d1 = Date(5,5,2023)
    d2 = Date(6,6,2023)
    d3 = Date(23,6,2023)

    e1 = Entry(d1, 5.0,25,"Good")
    e2 = Entry(d2, 3.0,24,"Tired")
    e3 = Entry(d3, 26.0,156,"Great")

    l1:ILog = MTLog()
    l2:ILog = ConsLog(e1,l1)
    l3:ILog = ConsLog(e2,l2)
    l4:ILog = ConsLog(e3,l3)

    assert l1.longestRun() == 0
    assert l3.longestRun() == 5.0
    assert l4.longestRun() == 26.0

def test_date_sameMonthAndYear()->None:
    d1 = Date(5,5,2023)
    assert d1.sameMonthAndYear(5,2023) is True
    assert d1.sameMonthAndYear(4,2023) is False
    assert d1.sameMonthAndYear(5,2022) is False


def test_runners_sortByDist()->None:
    d1 = Date(5,5,2023)
    d2 = Date(6,6,2023)
    d3 = Date(23,6,2023)

    e1 = Entry(d1, 5.0,25,"Good")
    e2 = Entry(d2, 3.0,24,"Tired")
    e3 = Entry(d3, 26.0,156,"Great")

    l1:ILog = MTLog()
    l2:ILog = ConsLog(e1,l1)
    l3:ILog = ConsLog(e2,l2)
    l4:ILog = ConsLog(e3,l3)

    assert l1.sortByDist() == l1
    assert l2.sortByDist() == l2
    assert l4.sortByDist() == ConsLog(e3,
                                          ConsLog(e1,
                                                  ConsLog(e2, MTLog())))

def test_runners_insertDist()->None:
    # A sorted log
    l5:ILog = ConsLog(Entry(Date(1,1,2023), 5.1, 26, "good"),
                      ConsLog(Entry(Date(1,2,2023), 4.9,25, "okay"),
                              MTLog()))

    # case where log is in the middle
    assert (l5.insertDist(Entry(Date(1,3,2023), 5.0, 27, "great"))
                == ConsLog(Entry(Date(1,1,2023), 5.1, 26, "good"),
                           ConsLog(Entry(Date(1,3,2023), 5.0, 27, "great"),
                                  ConsLog(Entry(Date(1,2,2023), 4.9,25, "okay"),
                                          MTLog()))))
    # case where log is in the front
    assert (l5.insertDist(Entry(Date(1,3,2023), 5.3, 27, "great"))
            == ConsLog(Entry(Date(1,3,2023), 5.3, 27,"great"),
                    ConsLog(Entry(Date(1,1,2023),5.1,26, "good"),
                            ConsLog(Entry(Date(1,2,2023),4.9,25,"okay"),
                                    MTLog()))))
    # case where log is in the end
    assert (l5.insertDist(Entry(Date(1,3,2023), 4.8, 27, "great")) ==
            ConsLog(Entry(Date(1,1,2023),5.1,26, "good"),
                    ConsLog(Entry(Date(1,2,2023),4.9,25,"okay"),
                            ConsLog(Entry(Date(1,3,2023), 4.8, 27,"great"),
                                    MTLog()))))

def test_runners_sortByPace()->None:
    d1 = Date(5,5,2023)
    d2 = Date(6,6,2023)
    d3 = Date(23,6,2023)

    e1 = Entry(d1, 5.0,25,"Good") # 5 mins/mile
    e2 = Entry(d2, 3.0,24,"Tired") # 8 mins/mile
    e3 = Entry(d3, 26.0,156,"Great") # 6 mins/mile

    l1:ILog = MTLog()
    l2:ILog = ConsLog(e1,l1)
    l3:ILog = ConsLog(e2,l2)
    l4:ILog = ConsLog(e3,l3)

    assert l1.sortByPace() == l1
    assert l2.sortByPace() == l2
    assert l4.sortByPace() == ConsLog(e1,
                                          ConsLog(e3,
                                                  ConsLog(e2, MTLog())))

def test_runners_insertDistByPace()->None:
    # A sorted log
    l6:ILog = ConsLog(Entry(Date(1,1,2023), 5, 25, "good"), # 5m/m
                      ConsLog(Entry(Date(1,2,2023), 5, 35, "okay"), #7m/m
                              MTLog()))

    # case where log is in the middle
    assert (l6.insertDistByPace(Entry(Date(1,3,2023), 5.0, 30, "great"))
                == ConsLog(Entry(Date(1,1,2023), 5, 25, "good"),
                           ConsLog(Entry(Date(1,3,2023), 5.0, 30, "great"),
                                  ConsLog(Entry(Date(1,2,2023), 5,35, "okay"),
                                          MTLog()))))
    # case where log is in the front
    assert (l6.insertDistByPace(Entry(Date(1,3,2023), 5, 20, "great")) ==
            ConsLog(Entry(Date(1,3,2023), 5, 20,"great"),
                    ConsLog(Entry(Date(1,1,2023),5,25, "good"),
                            ConsLog(Entry(Date(1,2,2023),5,35,"okay"),
                                    MTLog()))))
    # case where log is in the end
    assert (l6.insertDistByPace(Entry(Date(1,3,2023), 5, 40, "great")) ==
            ConsLog(Entry(Date(1,1,2023),5,25, "good"),
                    ConsLog(Entry(Date(1,2,2023),5,35,"okay"),
                            ConsLog(Entry(Date(1,3,2023), 5, 40,"great"),
                                    MTLog()))))

def test_entry_pace()->None:
    assert Entry(Date(1,3,2023), 5,20, "great").pace() == 4
    assert Entry(Date(1,3,2023), 4.1 ,21, "great").pace() == pytest.approx(5.12, abs=0.01)



# Test Composite ========================================================
def test_shape_distTo0():
    s1:IComposite = Square(CartPt(40,30),40)
    s2:IComposite = Square(CartPt(120,50),50)
    c1:IComposite = Circle(CartPt(50,120),20)
    c2:IComposite = Circle(CartPt(30,40),20)
    u1:IComposite = SuperImp(s1,s2)
    u2:IComposite = SuperImp(s1,c2)
    u3:IComposite = SuperImp(c1,u1)
    u4:IComposite = SuperImp(u3,u2)

    assert s1.distTo0() == pytest.approx(50, abs=.1)
    assert s2.distTo0() == pytest.approx(130, abs=.1)
    assert c1.distTo0() == pytest.approx(110, abs=.1)
    assert c2.distTo0() == pytest.approx(30, abs=.1)

    assert u1.distTo0() == pytest.approx(50, abs=.1)
    assert u2.distTo0() == pytest.approx(30, abs=.1)
    assert u3.distTo0() == pytest.approx(50, abs=.1)
    assert u4.distTo0() == pytest.approx(30, abs=.1)

def test_shape_within():
    s1:IComposite = Square(CartPt(40,30),40)
    s2:IComposite = Square(CartPt(120,50),50)
    c1:IComposite = Circle(CartPt(50,120),20)
    c2:IComposite = Circle(CartPt(30,40),20)
    u1:IComposite = SuperImp(s1,s2)
    u2:IComposite = SuperImp(s1,c2)
    u3:IComposite = SuperImp(c1,u1)
    u4:IComposite = SuperImp(u3,u2)

    assert u1.within(CartPt(42,42)) is True
    assert u2.within(CartPt(45,40)) is True
    assert u2.within(CartPt(20,5)) is False


#def test_shape_bb_boundingBox():
#    s1:IComposite = Square(CartPt(40,30),40)
#    s2:IComposite = Square(CartPt(120,50),50)
#    c1:IComposite = Circle(CartPt(50,120),20)
#    c2:IComposite = Circle(CartPt(30,40),20)
#    u1:IComposite = SuperImp(s1,s2)
#    u2:IComposite = SuperImp(s1,c2)
#    u3:IComposite = SuperImp(c1,u1)
#    u4:IComposite = SuperImp(u3,u2)

#    #s1.bb() should produce a 40 by 40 rectangle at (40,80)
#    assert s1.bb() == BoundingBox(40,80,30,70)
#    #s2.bb() should produce a 50 by 50 rectangle at (120,50)
#    assert s2.bb() == BoundingBox(120,170,50,100)
#    #c1.bb() should produce a 40 by 40 rectangle at (30,100)
#    assert c1.bb() == BoundingBox(30,70,100,140)
#    #c2.bb() should produce a 40 by 40 rectangle at (10,20)
#    assert c2.bb() == BoundingBox(10,50,20,60)

#    #u1.bb() should produce 110 by 80 rectangle at (40,30)
#    assert u1.bb() == BoundingBox(40,170,30,100)
#    #u2.bb() should produce 70 by 50 rectangle at (10,20)
#    assert u2.bb() == BoundingBox(10,80,20,70)
#    #u3.bb() should produce 70 by 120 rectangle at (10,20)
#    assert u3.bb() == BoundingBox(30,170,30,140)
#    #u4.bb() should produce 70 by 120 rectangle at (10,20)
#    assert u4.bb() == BoundingBox(10,170,20,140)

def test_shape_bb_rectangle():
    s1:IComposite = Square(CartPt(40,30),40)
    s2:IComposite = Square(CartPt(120,50),50)
    c1:IComposite = Circle(CartPt(50,120),20)
    c2:IComposite = Circle(CartPt(30,40),20)
    u1:IComposite = SuperImp(s1,s2)
    u2:IComposite = SuperImp(s1,c2)
    u3:IComposite = SuperImp(c1,u1)
    u4:IComposite = SuperImp(u3,u2)

    #s1.bb() should produce a 40 by 40 rectangle at (40,80)
    assert s1.bb() == Rectangle(CartPt(40,30), 40, 40)
    #s2.bb() should produce a 50 by 50 rectangle at (120,50)
    assert s2.bb() == Rectangle(CartPt(120,50),50,50)
    #c1.bb() should produce a 40 by 40 rectangle at (30,100)
    assert c1.bb() == Rectangle(CartPt(30,100),40,40)
    #c2.bb() should produce a 40 by 40 rectangle at (10,20)
    assert c2.bb() == Rectangle(CartPt(10,20),40,40)

    #u1.bb() should produce 110 by 80 rectangle at (40,30)
    assert u1.bb() == Rectangle(CartPt(40,30),130,70)
    #u2.bb() should produce 70 by 50 rectangle at (10,20)
    assert u2.bb() == Rectangle(CartPt(10,20),70,50)
    #u3.bb() should produce 70 by 120 rectangle at (10,20)
    assert u3.bb() == Rectangle(CartPt(30,30),140,110)
    #u4.bb() should produce 70 by 120 rectangle at (10,20)
    assert u4.bb() == Rectangle(CartPt(10,20),160,120)

# River Systems=======================================================================
# def test_river_sources():
#     lm = Location(7,5,"m")
#     la = Location(5,5,"a")
#     lb = Location(3,3,"b")
#     ls = Location(1,1,"s")
#     lt = Location(1,5,"t")
#     lu = Location(3,7,"u")

#     s = Source(ls)
#     t = Source(lt)
#     u = Source(lu)

#     b = Confluence(lb,s,t)
#     a = Confluence(la,b,u)

#     m = Mouth(lm,a)


#     assert s.sources() == 1
#     assert a.sources() == 3
#     assert b.sources() == 2
#     assert m.sources() == 3

# def test_river_onRiver():
#     lm = Location(7,5,"m")
#     la = Location(5,5,"a")
#     lb = Location(3,3,"b")
#     ls = Location(1,1,"s")
#     lt = Location(1,5,"t")
#     lu = Location(3,7,"u")

#     s = Source(ls)
#     t = Source(lt)
#     u = Source(lu)

#     b = Confluence(lb,s,t)
#     a = Confluence(la,b,u)

#     m = Mouth(lm,a)

#     assert m.onRiver(Location(7,5)) is True
#     assert m.onRiver(Location(1,5)) is True

def test_river_length() -> None:
    lm = Location(7,5,"m")
    la = Location(5,5,"a")
    lb = Location(3,3,"b")
    ls = Location(1,1,"s")
    lt = Location(1,5,"t")
    lu = Location(3,7,"u")

    s = Source(3,ls)
    t = Source(2,lt)
    u = Source(1,lu)

    b = Confluence(3,lb,s,t)
    a = Confluence(4,la,b,u)

    m = Mouth(lm,a)

    assert s.length() == 3
    assert t.length() == 2
    assert u.length() == 1
    assert b.length() == 8
    assert a.length() == 13
    assert m.length() == 13

def test_location_dist() -> None:
    assert Location(0,0).dist(Location(3,4)) == 5
    assert Location(0,0).dist(Location(0,4)) == 4
    assert Location(14,4).dist(Location(10,1)) == 5

def test_river_onRiver() -> None:
    lm = Location(7,5,"m")
    la = Location(5,5,"a")
    lb = Location(3,3,"b")
    ls = Location(1,1,"s")
    lt = Location(1,5,"t")
    lu = Location(3,7,"u")

    s = Source(3,ls)
    t = Source(2,lt)
    u = Source(1,lu)

    b = Confluence(3,lb,s,t)
    a = Confluence(4,la,b,u)

    m = Mouth(lm,a)

    assert m.onRiver(Location(7,5), 4) is True
    assert m.onRiver(Location(2,5), 3) is True
    assert m.onRiver(Location(6,11), 3) is False
    assert m.onRiver(Location(6,11), 5) is True

def test_river_maxLength() -> None:
    lm = Location(7,5,"m")
    la = Location(5,5,"a")
    lb = Location(3,3,"b")
    ls = Location(1,1,"s")
    lt = Location(1,5,"t")
    lu = Location(3,7,"u")

    s = Source(3,ls)
    t = Source(2,lt)
    u = Source(1,lu)

    b = Confluence(3,lb,s,t)
    a = Confluence(4,la,b,u)

    m = Mouth(lm,a)

    assert m.maxLength() == 10

def test_river_confluences() -> None:
    lm = Location(7,5,"m")
    la = Location(5,5,"a")
    lb = Location(3,3,"b")
    ls = Location(1,1,"s")
    lt = Location(1,5,"t")
    lu = Location(3,7,"u")

    s = Source(3,ls)
    t = Source(2,lt)
    u = Source(1,lu)

    b = Confluence(3,lb,s,t)
    a = Confluence(4,la,b,u)

    m = Mouth(lm,a)

    assert m.confluences() == 2

def test_confluence_combine() -> None:
    lm = Location(7,5,"m")
    la = Location(5,5,"a")
    lb = Location(3,3,"b")
    ls = Location(1,1,"s")
    lt = Location(1,5,"t")
    lu = Location(3,7,"u")

    s = Source(3,ls)
    t = Source(2,lt)
    u = Source(1,lu)

    b = Confluence(3,lb,s,t)
    a = Confluence(4,la,b,u)

    m = Mouth(lm,a)

    l1 = ConsLoLocations(lm,
             ConsLoLocations(la,
                 MTLoLocations()))

    l2 = ConsLoLocations(lb,
             ConsLoLocations(ls,
                 MTLoLocations()))

    l3 = ConsLoLocations(lm,
             ConsLoLocations(la,
                 ConsLoLocations(lb,
                     ConsLoLocations(ls,
                         MTLoLocations()))))
    assert b.combine(l1,l2) == l3


def test_river_confluences() -> None:
    lm = Location(7,5,"m")
    la = Location(5,5,"a")
    lb = Location(3,3,"b")
    ls = Location(1,1,"s")
    lt = Location(1,5,"t")
    lu = Location(3,7,"u")

    s = Source(3,ls)
    t = Source(2,lt)
    u = Source(1,lu)

    b = Confluence(3,lb,s,t)
    a = Confluence(4,la,b,u)

    m = Mouth(lm,a)

    assert (m.locations()
    == ConsLoLocations(lm,
        ConsLoLocations(la,
          ConsLoLocations(lb,
            ConsLoLocations(ls,
              ConsLoLocations(lt,
                ConsLoLocations(lu,
                  MTLoLocations())))))))


# Grocery Items ==================================================================

def test_grocery_howmany() -> None:
    i1 = IceCream("Orangino", 40, 100, "orange")
    c1 = Coffee("Coffee", 120, 250, True)
    j1 = Juice("Melon Soda", 100, 200, "melon", "bottled")


    g1 = ConsShoppingList(i1,
                        MTShoppingList())
    g2 = ConsShoppingList(c1, g1)
    g3 = ConsShoppingList(j1, g2)
    assert g1.howMany() == 1
    assert g2.howMany() == 2
    assert g3.howMany() == 3

def test_grocery_brandList() -> None:
    i1 = IceCream("Orangino", 40, 100, "orange")
    c1 = Coffee("Coffee", 120, 250, True)
    j1 = Juice("Melon Soda", 100, 200, "melon", "bottled")


    g1 = ConsShoppingList(i1,
                        MTShoppingList())
    g2 = ConsShoppingList(c1, g1)
    g3 = ConsShoppingList(j1, g2)
    assert g3.brandList() == ConsBrandList("Melon Soda",
                                           ConsBrandList("Coffee",
                                                         ConsBrandList("Orangino",
                                                                       MTBrandList())))
def test_grocery_highestPrice() -> None:
    i1 = IceCream("Orangino", 40, 100, "orange")
    c1 = Coffee("Coffee", 120, 250, True)
    j1 = Juice("Melon Soda", 100, 200, "melon", "bottled")


    g1 = ConsShoppingList(i1,
                        MTShoppingList())
    g2 = ConsShoppingList(c1, g1)
    g3 = ConsShoppingList(j1, g2)

    g4 = ConsShoppingList(j1,
            ConsShoppingList(c1,
                        MTShoppingList()))

    assert g3.highestPrice() == i1
    assert g4.highestPrice() == c1

# Books ==================================================================

def test_book_thisAuthor()->None:
    a1 = Author("a", Date(19,12,1926))
    a2 = Author("b", Date(18,12,1926))
    a3 = Author("c", Date(17,12,1926))

    la2 = ConsLoAuthors(a2,
                ConsLoAuthors(a3,
                      MTLoAuthors()))
    la1 = ConsLoAuthors(a1,
             ConsLoAuthors(a2,
                ConsLoAuthors(a3,
                   MTLoAuthors())))

    b1 = Book(la1, "afirst", 2000, 1997)
    b2 = Book(la2, "second", 2100, 1998)
    b3 = Book(la2, "third", 2200, 1999)
    b4 = Book(la1, "asecond", 2000, 1999)

    l1 = ConsLoBooks(b1, MTLoBooks())
    l2 = ConsLoBooks(b2,l1)
    l3 = ConsLoBooks(b3,l2)
    l4 = ConsLoBooks(b4,l3)
    assert l4.thisAuthor(a1) == ConsLoBooks(b4,
                                ConsLoBooks(b1,
                                    MTLoBooks()))
def test_iloauthors_contains()->None:
    a1 = Author("a", Date(19,12,1926))
    a2 = Author("b", Date(18,12,1926))
    a3 = Author("c", Date(17,12,1926))
    a4 = Author("d", Date(17,12,1926))

    la1 = ConsLoAuthors(a1,
            ConsLoAuthors(a2,
                ConsLoAuthors(a3,
                      MTLoAuthors())))
    assert la1.contains(a3) is True
    assert la1.contains(a4) is False


