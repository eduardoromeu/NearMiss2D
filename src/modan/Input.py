import pygame
from .Behaviour import Behaviour
from .Display import Display

class Input(Behaviour):
  
  def start(self):
    pass

  def update(self):
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
              Display.toggle_fullscreen()

  def late_update(self):
    return super().late_update()
    