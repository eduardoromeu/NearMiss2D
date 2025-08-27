import pygame

from ..Scene import Scene
from ..Objects.Road import Road
from ..Objects.UIText import UIText

class Gameplay(Scene):

  def init(self):
    menu_bg = Road("MenuBg", position=(0, 0))
    menu_bg2 = Road("MenuBg", position=(0, -513))
    self.add(menu_bg)
    self.add(menu_bg2)

  def handle_event(self, event: pygame.event.Event) -> None:
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        from .MainMenu import MainMenu
        Scene.load_scene(MainMenu("MainMenu", self.window))
  