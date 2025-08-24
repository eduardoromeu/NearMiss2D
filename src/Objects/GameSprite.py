import pygame
from src.Behaviour import Behaviour

class GameSprite(Behaviour, pygame.sprite.Sprite):

  def start(self): # Call when behaviour is instanced
    self.image = pygame.Surface((0, 0))
    self.rect = self.image.get_rect()
    pass

  def update(self): # Call once per game loop iteration
    pass

  def late_update(self): # Call after update
    pass