import pygame
from .Scene import Scene
from .Display import Display
from .Input import Input

class GameManager:

  # Currently active scene
  active_scene: Scene = Scene()
  running = True

  def __init__(self) -> None:
    print("Initializing game...")
    self.display_manager = Display()
    self.input_manager = Input()
    
    pygame.init()

    self.run()

  def run(self):
    # Game loop
    while GameManager.running:
      # update managers
      self.display_manager.update()
      self.input_manager.update()

      # update scene
      if GameManager.active_scene is not None:
        GameManager.active_scene.game_loop()

    pygame.quit()