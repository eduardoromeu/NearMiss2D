import pygame
from pygame import FULLSCREEN

from .Consts import SCREEN_WIDTH, SCREEN_HEIGHT

class Display():

  manager : "Display, None" = None
  screen_height: int = SCREEN_HEIGHT
  screen_width: int = SCREEN_WIDTH

  def __init__(self):
    self.display_info = pygame.display.Info()
    Display.screen_width = self.display_info.current_w # monitor width
    Display.screen_height = self.display_info.current_h # monitor height
    Display.manager = self
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync=True)
    self.clock = pygame.time.Clock()
    self.display_info = pygame.display.Info()
    icon = pygame.image.load('./assets/logo-pixel.png').convert_alpha()
    pygame.display.set_icon(icon)

  def update(self):
    self.clock.tick(60)  # limits FPS to 60
   
    # display window info
    pygame.display.set_caption(f'NearMiss2d {pygame.display.get_driver()} @ {round(self.clock.get_fps())} fps ({self.display_info.current_w}, {self.display_info.current_h})')

    # update screen
    pygame.display.flip()

  @staticmethod
  def toggle_fullscreen():
    if not pygame.display.get_init():
      return
    # pygame.display.toggle_fullscreen()
    if Display.manager is not None:
      if pygame.display.is_fullscreen():
        Display.manager.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync=True)
      else:
        Display.manager.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=FULLSCREEN, vsync=True)
        # For allowing full height
        # Display.manager.screen = pygame.display.set_mode((SCREEN_WIDTH, Display.screen_height), flags=FULLSCREEN, vsync=True)

    
    