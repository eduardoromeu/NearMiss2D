# modan is my helper/boostrapper for pygame
import pygame
pygame.init()

from .Behaviour import Behaviour
from .Scene import Scene
from .Display import Display
from .Input import Input
from .GameManager import GameManager

__all__ = ['Behaviour', 'Display', 'Scene', 'Display', 'Input', 'GameManager']

print("Welcome to modan!")

game_manager = GameManager()