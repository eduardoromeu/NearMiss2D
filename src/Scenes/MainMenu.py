import pygame
from ..Scene import Scene

class MainMenu(Scene):

  def init(self):
    from ..Game import Game
    newcar = pygame.image.load('./assets/Sprites/NeoDuol_ESCADA.png')
    Game.manager.display.screen.blit(newcar, newcar.get_rect())
    pass

  