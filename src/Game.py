import pygame
from typing import Optional

from .Scene import Scene
from .Scenes.MainMenu import MainMenu
from .Display import Display
from .Input import Input

class Game:

  manager : 'Game' = None # pyright: ignore[reportAssignmentType]
  
  # Currently active scene
  running = True

  def __init__(self) -> None:
    print("Initializing game...")
    Game.manager = self
    self.display = Display()
    self.input = Input()
    pygame.init()
    self.active_scene: Scene = MainMenu("MainMenu", self.display.screen)
    self.active_scene.init()
    self.run()

  def run(self):
    # Game loop
    while Game.running:
      # update inputs
      self.display.update()

      # update scene
      if self.active_scene is not None:
        self.active_scene.game_loop()
      
      # update display
      self.input.update()

    pygame.quit()