import pygame
from src.Behaviour import Behaviour

class GameSprite(pygame.sprite.Sprite, Behaviour):

  def start(self): # Call when behaviour is instanced
    pass

  def update(self): # Call once per game loop iteration
    pass

  def late_update(self): # Call after update
    pass