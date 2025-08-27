import pygame
from ..Scene import Scene

class Gameplay(Scene):

  def init(self):
    print('started gameplay scene')

  def handle_event(self, event: pygame.event.Event) -> None:
    pass
  