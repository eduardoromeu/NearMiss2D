import pygame

from ..Scene import Scene
from ..Objects.PlayerCar import Car
from ..Objects.Road import Road

class MainMenu(Scene):

  def init(self):
    menuBg = Road("MenuBg")
    scaled_bg = pygame.transform.scale(menuBg.image, (1024, 768))
    menuBg.image = scaled_bg
    self.add(menuBg)
    pass

  