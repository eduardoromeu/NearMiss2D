import pygame
from ..Scene import Scene
from ..Objects.Road import Road
from ..Objects.UIText import UIText

class HighScores(Scene):
    def init(self):
        bg = Road("Bg", position=(0, 0), scale=(1024, 682), speed=5)
        bg2 = Road("Bg2", position=(0, 682), scale=(1024, 682), speed=5)
        bg3 = Road("Bg2", position=(0, -682), scale=(1024, 682), speed=5)
        self.add(bg, bg2, bg3)