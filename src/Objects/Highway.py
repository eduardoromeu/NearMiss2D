import pygame
from .GameSprite import GameSprite
from .. import Consts


class Highway(GameSprite):

  def start(self): # Call when behaviour is instanced
    self.image = pygame.image.load('./assets/Sprites/Roads/highway.jpg').convert()
    if self.scale != (0, 0):
      self.image = pygame.transform.smoothscale(self.image, self.scale)
    self.rect = self.image.get_rect(left=self.position[0], top=self.position[1])
    self.original_position = self.position
    if not hasattr(self, 'speed'):
      self.speed = 5

  def update(self): # Call once per game loop iteration
    self.rect.centery += self.speed
    if self.rect.top >= self.original_position[1] + self.rect.height:
      self.rect.top = self.original_position[1]

  def late_update(self): # Call after update
    pass