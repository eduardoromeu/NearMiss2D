import pygame
from src.Behaviour import Behaviour

class GameSprite(Behaviour, pygame.sprite.Sprite):
  def __init__(self, name: str = 'NewBehaviour', position: tuple = (0,0)) -> None:
    super().__init__(name)
    self.position = position
    self.rotation = 0

  def start(self): # Call when behaviour is instanced
    self.image = pygame.Surface((0, 0))
    self.rect = self.image.get_rect(left=self.position[0], top=self.position[1])
    pass

  def update(self): # Call once per game loop iteration
    pass

  def late_update(self): # Call after update
    pass
