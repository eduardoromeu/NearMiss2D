import pygame
from typing import Optional

from .Scenes.MainMenu import MainMenu
from .Scene import Scene
from .Display import Display
from .Input import Input

class Game:
  manager : 'Game' = None # pyright: ignore[reportAssignmentType]
  
  # Currently active scene
  active_scene: Scene = MainMenu("MainMenu")
  running = True

  def __init__(self) -> None:
    print("Initializing game...")
    manager = self
    self.display = Display()
    self.input = Input()
    pygame.init()
    Game.active_scene.init()
    self.run()

  def run(self):
    # Game loop
    while Game.running:
      # update inputs
      self.display.update()

      # update scene
      if Game.active_scene is not None:
        Game.active_scene.game_loop()
      
      # update display
      self.input.update()

    pygame.quit()