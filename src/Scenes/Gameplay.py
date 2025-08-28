import pygame

from ..Scene import Scene
from ..Objects.Road import Road
from ..Objects.UIText import UIText
from ..Objects.PlayerCar import PlayerCar

class Gameplay(Scene):

  def init(self):
    road1 = Road("road1", position=(0, 0), scale=(1024, 682))
    road2 = Road("road2", position=(0, -682), scale=(1024, 682))
    road3 = Road("road3", position=(0, 682), scale=(1024, 682))
    self.add(road1, road2, road3)

    newcar = PlayerCar("PlayerCar", position=(350, 400), scale=(247, 508))
    self.add(newcar)

  def handle_event(self, event: pygame.event.Event) -> None:
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        from .MainMenu import MainMenu
        Scene.load_scene(MainMenu("MainMenu", self.window))
  