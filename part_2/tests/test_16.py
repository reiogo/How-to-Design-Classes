from chapters.chapter16_UFO.ufo_game import *
import pytest

# test UFOWorld ==========================================================================================
# def test_UFOWorld_move()->None:

#     # first world ======================================
#     a1 = AUP(50)
#     u1 = UFO(Posn(40,40))

#     s1 = Shot(Posn(50,170))
#     s2 = Shot(Posn(50,190))
#     shots1 = ConsShots(s1, ConsShots(s2, MTShots()))

#     # second world ======================================
#     u2 = UFO(Posn(40,40))

#     s3 = Shot(Posn(50,170))
#     s4 = Shot(Posn(50,190))
#     shots2 = ConsShots(s3, ConsShots(s4, MTShots()))

#     # world  definition ======================================
#     initial_world = UFOWorld(u1, a1, shots1)
#     expected_world = UFOWorld(u2, a1, shots2)
#     moved_world = initial_world.move()

#     assert moved_world == expected_world

def test_UFO_move()->None:
    # world  definition ======================================
    a1 = AUP(50)
    u1 = UFO(Posn(40,40))

    s1 = Shot(Posn(50,170))
    s2 = Shot(Posn(50,190))
    shots1 = ConsShots(s1, ConsShots(s2, MTShots()))

    w1 = UFOWorld(u1, a1, shots1)
    # end world  definition ======================================

    u1 = UFO(Posn(88,11))

    moved_ufo = u1.move()
    expect_ufo = UFO(Posn(88,14))

    assert moved_ufo == expect_ufo
    assert UFO(Posn(88,14)).move() == UFO(Posn(88,17))
    assert UFO(Posn(88,17)).move() == UFO(Posn(88,20))

def test_UFO_landed()->None:
    # world  definition ======================================
    a1 = AUP(50)
    u1 = UFO(Posn(40,40))

    s1 = Shot(Posn(50,170))
    s2 = Shot(Posn(50,190))
    shots1 = ConsShots(s1, ConsShots(s2, MTShots()))

    w1 = UFOWorld(u1, a1, shots1)
    # end world  definition ======================================

    u1 = UFO(Posn(88,11))
    u2 = UFO(Posn(88,500))

    assert u1.landed() == False
    assert u2.landed() == True

def test_UFO_closeToGround()->None:
    a1 = AUP(50)
    u1 = UFO(Posn(40,40))

    s1 = Shot(Posn(50,170))
    s2 = Shot(Posn(50,190))
    shots1 = ConsShots(s1, ConsShots(s2, MTShots()))

    w1 = UFOWorld(u1, a1, shots1)

    u1 = UFO(Posn(88,11))
    u2 = UFO(Posn(88,500))

    assert u1.closeToGround() == False
    assert u2.closeToGround() == True

def test_shot_move()->None:
    assert Shot(Posn(88,17)).move() == Shot(Posn(88,14))
    assert Shot(Posn(88,14)).move() == Shot(Posn(88,11))
    assert Shot(Posn(88,11)).move() == Shot(Posn(88,8))

def test_multiple_shots_move() -> None:

    s1 = Shot(Posn(50,-1))
    s2 = Shot(Posn(50,190))
    s3 = Shot(Posn(50,170))
    shots1 = ConsShots(s1,
                ConsShots(s2,
                    ConsShots(s3,
                       MTShots())))
    s4 = Shot(Posn(50,187))
    s5 = Shot(Posn(50,167))

    shots2 = ConsShots(s4,
                ConsShots(s5,
                   MTShots()))

    assert shots1.move() == shots2

def test_UFOWorld_shoot() -> None:
    AUP_LOCATION = 90
    SHOT_START_X = 106
    SHOT_START_Y = 480

    a = AUP(AUP_LOCATION)
    u = UFO(Posn(100,5))
    s = Shot(Posn(112,480))
    le = MTShots()
    ls = ConsShots(s, MTShots())
    w1 = UFOWorld(u,a,le)
    w2 = UFOWorld(u,a,ls)

    shots1 = ConsShots(Shot(Posn(SHOT_START_X, SHOT_START_Y)),
                        MTShots())
    shots2 = ConsShots(Shot(Posn(SHOT_START_X, SHOT_START_Y)),
                  ConsShots(Shot(Posn(112, 480)),
                            MTShots()))

    assert w1.shoot() == UFOWorld(u,a, shots1)

    assert w2.shoot() == UFOWorld(u,a, shots2)


def test_AUP_fireShot() -> None:
    AUP_LOCATION = 90
    SHOT_START_X = 106
    SHOT_START_Y = 480

    a = AUP(AUP_LOCATION)
    u = UFO(Posn(100,5))
    le = MTShots()
    w1 = UFOWorld(u,a,le)

    assert a.fireShot(w1) == Shot(Posn(SHOT_START_X,SHOT_START_Y))


