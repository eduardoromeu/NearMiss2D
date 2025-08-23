# modan is my helper/boostrapper for pygame
import pygame
pygame.init()

from .Behaviour import Behaviour
from .Scene import Scene
from .Display import Display
from .Input import Input

__all__ = ['Behaviour', 'Display', 'Scene']

print("Welcome to modan!")

# Currently active scene
active_scene: Scene = Scene()

active_scene.add(Display("DisplayManager"))
active_scene.add(Input("InputManager"))

# Game loop
while active_scene is not None:
  active_scene.game_loop()