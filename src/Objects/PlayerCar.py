import pygame
from .GameSprite import GameSprite
from .. import Consts
from ..Input import Input

class PlayerCar(GameSprite):

  def __init__(self, name: str = 'NewBehaviour', position: tuple = (0, 0), scale: tuple = (0, 0), **kwargs) -> None:
    self.is_braking = False
    super().__init__(name, position, scale, **kwargs)

  def start(self): # Call when behaviour is instanced
    self.image = pygame.image.load('./assets/Sprites/Cars/NEODUOL/NeoDuol_BLUE.png').convert_alpha()
    if not (not hasattr(self, 'rotozoom') or not (self.rotozoom != (0, 0))):
      self.image = pygame.transform.rotozoom(self.image, self.rotozoom[0], self.rotozoom[1])
    self.rect = self.image.get_rect(centerx=self.position[0], bottom=self.position[1])

  def update(self): # Call once per game loop iteration
    if Input.is_key_pressed(pygame.K_UP, pygame.K_w) and self.rect.top > 0:
      self.rect.centery -= 5
    if Input.is_key_pressed(pygame.K_DOWN, pygame.K_s):
      self.is_braking = True
      if self.rect.bottom < Consts.SCREEN_HEIGHT:
        self.rect.centery += 8
    else:
      self.is_braking = False
    if Input.is_key_pressed(pygame.K_RIGHT, pygame.K_d) and self.rect.right < Consts.SCREEN_WIDTH:
      self.rect.centerx += 5
    if Input.is_key_pressed(pygame.K_LEFT, pygame.K_a) and self.rect.left > 0:
      self.rect.centerx -= 5

  def late_update(self): # Call after update
    pass