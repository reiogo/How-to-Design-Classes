import pygame
from .pygame_canvas import PygameCanvas
from .ufo_game import UFOWorld, UFO, AUP, Shot, IShots, MTShots, ConsShots
from .canvas_library import Color, Posn
from . import canvas_library as canvas

pygame.init()
screen = pygame.display.set_mode((200,500))



c = PygameCanvas(200,500,screen)
a = AUP(50) # place aup at the bottom
u = UFO(Posn(41,40)) # place ufo at the top left corner

s1 = Shot(Posn(50,170)) # shoot shot
s2 = Shot(Posn(50,190)) # shot is lower than shot1
shots1 = ConsShots(s1, ConsShots(s2, MTShots()))

w1 = UFOWorld(u,a, shots1)
fired = False

# world = UFOWorld(ufo, aup, shots)

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not fired:
        w1 = w1.shoot()


    screen.fill(canvas.WHITE)
    w1.draw(c)

    # move world
    # world = world.move()

    # draw world
    # world.draw(canvas)

    pygame.display.flip()
    clock.tick(30)
