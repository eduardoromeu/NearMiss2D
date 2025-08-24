import pygame
from .GameSprite import GameSprite

class Car(GameSprite):

  def start(self): # Call when behaviour is instanced
    self.image = pygame.image.load('./assets/Sprites/neoduol.png').convert_alpha()
    self.rect = self.image.get_rect()
    # Game.manager.display.screen.blit(newcar, newcar.get_rect(left=0, top=0))

  def update(self): # Call once per game loop iteration
    pass

  def late_update(self): # Call after update
    pass