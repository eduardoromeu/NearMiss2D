import pygame

from ..Consts import SCREEN_HEIGHT, SCREEN_WIDTH
from ..Scene import Scene
from ..Objects.Road import Road
from ..Objects.Highway import Highway
from ..Objects.UIText import UIText
from ..Objects.PlayerCar import PlayerCar

class Gameplay(Scene):

  def init(self):
    road1 = Highway("road1", position=(0, 0), scale=(1024, 682), speed=10)
    road2 = Highway("road2", position=(0, -682), scale=(1024, 682), speed=10)
    road3 = Highway("road3", position=(0, 682), scale=(1024, 682), speed=10)
    self.add(road1, road2, road3)

    newcar = PlayerCar("PlayerCar", position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10), rotozoom=(0, 0.25))
    self.add(newcar)

  def handle_event(self, event: pygame.event.Event) -> None:
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        from .MainMenu import MainMenu
        Scene.load_scene(MainMenu("MainMenu", self.window))
  