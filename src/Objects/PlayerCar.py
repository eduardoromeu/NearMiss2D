import pygame
from .GameSprite import GameSprite
from ..Input import Input

class PlayerCar(GameSprite):

  def start(self): # Call when behaviour is instanced
    self.image = pygame.image.load('./assets/Sprites/Cars/NEODUOL/NeoDuol_RED.png').convert_alpha()
    if self.scale != (0, 0):
      self.image = pygame.transform.smoothscale(self.image, self.scale)
    self.rect = self.image.get_rect(center=self.position)
    # Game.manager.display.screen.blit(newcar, newcar.get_rect(left=0, top=0))

  def update(self): # Call once per game loop iteration
    if Input.is_key_pressed(pygame.K_RIGHT):
      self.rect.centerx += 5
    if Input.is_key_pressed(pygame.K_LEFT):
      self.rect.centerx -= 5
    if Input.is_key_pressed(pygame.K_UP):
      self.rect.centery -= 5
    if Input.is_key_pressed(pygame.K_DOWN):
      self.rect.centery += 5

  def late_update(self): # Call after update
    pass