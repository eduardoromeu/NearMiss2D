import pygame
from .Scene import Scene
from .Display import Display
from .Input import Input

class GameManager:

  # Currently active scene
  active_scene: Scene = Scene()

  def __init__(self) -> None:
    GameManager.active_scene.add(Display("DisplayManager"))
    GameManager.active_scene.add(Input("InputManager"))
    self.run()
  
  def run(self):
    # Game loop
    while GameManager.active_scene is not None:
      GameManager.active_scene.game_loop()

    pygame.Quit()