from typing import Protocol
from dataclasses import dataclass
import pygame
from .canvas_library import Posn, ICanvas, Color
# PYGAMES ==========================================================================================
class PygameCanvas(ICanvas):

    def __init__(self, width, height, screen):
        super().__init__(width, height)
        self.height = height
        self.width = width
        self.screen = screen


    def drawDisk(self, p: Posn, r: int, c: Color) -> bool:
        pygame.draw.circle(self.screen, c, (p.x, p.y), r)
        return True

    def drawRect(self, p: Posn, width: int, height: int, c: Color) -> bool:
        pygame.draw.rect(self.screen, c,
                         pygame.Rect(p.x, p.y, width, height))
        return True

