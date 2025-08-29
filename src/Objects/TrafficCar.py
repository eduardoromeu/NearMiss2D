import pygame
from .GameSprite import GameSprite

class TrafficCar(GameSprite):

  def start(self):
    self.image = pygame.image.load('./assets/Sprites/Cars/BLASTER/Blaster_CARAMELO.png').convert_alpha()
    if not (not hasattr(self, 'rotozoom') or not (self.rotozoom != (0, 0))):
      self.image = pygame.transform.rotozoom(self.image, self.rotozoom[0], self.rotozoom[1])
    self.rect = self.image.get_rect(centerx=self.position[0], bottom=self.position[1])
    if not hasattr(self, 'speed'):
      self.speed = 3

  def update(self): # Call once per game loop iteration
    self.rect.centery += self.speed

  def late_update(self): # Call after update
    pass