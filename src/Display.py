import pygame
from .Consts import SCREEN_WIDTH, SCREEN_HEIGHT

class Display():

  def __init__(self):
    self.display_info = pygame.display.Info()
    Display.screen_width = self.display_info.current_w # monitor width
    Display.screen_height = self.display_info.current_h # monitor height

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
    pygame.display.toggle_fullscreen()
    
    