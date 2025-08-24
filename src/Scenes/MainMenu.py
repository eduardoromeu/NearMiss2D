import pygame

from src.Objects.GameSprite import GameSprite
from ..Scene import Scene
from ..Objects.Car import Car

class MainMenu(Scene):

  def init(self):
    newCar = Car()
    self.add(newCar)
    pass

  def game_loop(self):
    for behaviour in self.hierarchy:
      behaviour.update()
      if(isinstance(behaviour, Car)):
        self.canvas.blit(behaviour.image, behaviour.image.get_rect())
    
    for behaviour in self.hierarchy:
      behaviour.late_update()

  