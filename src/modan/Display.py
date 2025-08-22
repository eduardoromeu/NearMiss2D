import pygame

class Display:

  def __init__(self):
    pass

  @staticmethod
  def toggle_fullscreen(fullscreen: bool):
    if not pygame.display.get_init():
      return
    
    