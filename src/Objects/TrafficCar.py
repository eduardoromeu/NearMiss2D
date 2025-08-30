import pygame
from .GameSprite import GameSprite
from ..Consts import SCREEN_HEIGHT

class TrafficCar(GameSprite, pygame.sprite.Sprite):

  def start(self):
    self.image = pygame.image.load('./assets/Sprites/Cars/NEODUOL/NeoDuol_RED.png').convert_alpha()
    self.mask_img = pygame.image.load('./assets/Sprites/Cars/NEODUOL/NeoDuol_mask.png').convert_alpha()
    if not (not hasattr(self, 'rotozoom') or not (self.rotozoom != (0, 0))):
      self.image = pygame.transform.rotozoom(self.image, self.rotozoom[0], self.rotozoom[1])
      self.mask_img = pygame.transform.rotozoom(self.mask_img, self.rotozoom[0], self.rotozoom[1])
    self.rect = self.image.get_rect(centerx=self.position[0], bottom=self.position[1])
    self.mask = pygame.mask.from_surface(self.mask_img)
    if not hasattr(self, 'speed'):
      self.speed = 3
    self.initial_speed = self.speed

  def update(self): # Call once per game loop iteration
    self.rect.centery += self.speed
    if self.rect.top > SCREEN_HEIGHT:
      self.destroy()
    # simulate player braking
    if self.scene.player_car.is_braking and hasattr(self, 'lane'):
      self.speed = self.initial_speed / 1.5
      # if self.lane.way_up:
    else:
      self.speed = self.initial_speed

  def late_update(self): # Call after update
    pass

  def on_disable(self):
    # print(f'destroying traffic car {self.name}')
    if hasattr(self, 'lane'):
      self.lane.traffic_cars.remove(self)