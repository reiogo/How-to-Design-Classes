from dataclasses import dataclass
import pygame
from .pygame_canvas import PygameCanvas
from .ufo_game import UFOWorld, UFO, AUP, Shot, IShots, MTShots, ConsShots
from .canvas_library import Color, Posn
from . import canvas_library as canvas

@dataclass
class Player:
    def show(self, screen, c, w) -> None:
        screen.fill((255,255,255))
        w.draw(c)
        pygame.display.flip()
        pygame.time.wait(800)

    def play(self) -> bool:
        pygame.init()
        screen = pygame.display.set_mode((200,500))
        c = PygameCanvas(200,500,screen)

        a = AUP(50)
        u = UFO(Posn(41,40))
        shots1 = MTShots()
        w = UFOWorld(u,a, shots1)

        # scripted sequence
        self.show(screen, c, w)

        w = w.move()
        self.show(screen, c, w)

        w = w.shoot()
        self.show(screen, c, w)

        w = w.move()
        self.show(screen, c, w)

        w = w.move()
        w.aup = a.move("left", w)
        self.show(screen, c, w)

        w = w.move()
        w.aup = a.move("left", w)
        self.show(screen, c, w)

        w = w.move()
        w.aup = a.move("right", w)
        self.show(screen, c, w)

        w = w.shoot()
        self.show(screen, c, w)


        return True

p = Player()
p.play()
