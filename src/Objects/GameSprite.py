import pygame
from src.Behaviour import Behaviour

class GameSprite(Behaviour, pygame.sprite.Sprite):
  def __init__(self, name: str = 'NewBehaviour', position: tuple = (0,0),
               scale: tuple = (0,0), update_layer: int = 0, **kwargs) -> None:
    self.name = name
    self.position = position
    self.rotation = 0
    self.scale = scale
    self.update_layer = update_layer

    for attr, value in kwargs.items():
      setattr(self, attr, value)
    self.start()

  def start(self): # Call when behaviour is instanced
    self.image = pygame.Surface((0, 0))
    if self.scale != (0, 0):
      self.image = pygame.transform.smoothscale(self.image, self.scale)
    self.rect = self.image.get_rect(center=self.position)
    pass

  def update(self): # Call once per game loop iteration
    pass

  def late_update(self): # Call after update
    pass
