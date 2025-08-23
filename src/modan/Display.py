import pygame
from .Behaviour import Behaviour

class Display(Behaviour):
  
  def start(self):
    self.screen = pygame.display.set_mode((1024, 768), vsync=True)
    self.clock = pygame.time.Clock()
    self.display_info = pygame.display.Info()

  def update(self):
    # fill the screen with a color to wipe away anything from last frame
    self.screen.fill("orange")

    # RENDER YOUR GAME HERE
    pygame.display.set_caption(f'NearMiss2d {pygame.display.get_driver()} @ {round(self.clock.get_fps())} fps ({self.display_info.current_w}, {self.display_info.current_h})')

    # flip() the display to put your work on screen
    pygame.display.flip()

    self.clock.tick(60)  # limits FPS to 60

  def late_update(self):
    return super().late_update()

  @staticmethod
  def toggle_fullscreen():
    if not pygame.display.get_init():
      return
    pygame.display.toggle_fullscreen()
    
    