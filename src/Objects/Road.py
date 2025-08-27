import pygame
from .GameSprite import GameSprite
from .. import Consts


class Road(GameSprite):

  def start(self): # Call when behaviour is instanced
    self.image = pygame.image.load('./assets/Sprites/Roads/road1.png').convert()
    self.rect = self.image.get_rect(left=self.position[0], top=self.position[1])
    self.original_position = self.position
    # Game.manager.display.screen.blit(newcar, newcar.get_rect(left=0, top=0))

  def update(self): # Call once per game loop iteration
    # self.rect.centery += 5
    if self.rect.top >= Consts.SCREEN_HEIGHT:
      self.rect.top = self.original_position[1]

  def late_update(self): # Call after update
    pass