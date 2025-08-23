import pygame

class Display():
  
  def __init__(self):
    self.screen = pygame.display.set_mode((1024, 768), vsync=True)
    self.clock = pygame.time.Clock()
    self.display_info = pygame.display.Info()

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
    
    