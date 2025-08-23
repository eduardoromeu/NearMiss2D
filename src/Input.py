import pygame
from .Display import Display

class Input():
  
  def __init__(self):
    pass

  def update(self):
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            from .GameManager import GameManager
            GameManager.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
              Display.toggle_fullscreen()
    