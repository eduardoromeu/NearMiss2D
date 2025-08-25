import pygame
from pygame import Surface, Rect
from pygame.font import Font
from .GameSprite import GameSprite

class UIText(GameSprite):

  def __init__(self, text: str, size: int, color: tuple = (255, 255, 255), font_name = "Arial", name: str = 'NewText',) -> None:
    super().__init__(name)
    self.text = text
    self.size = size
    self.color = color
    self.font_name = font_name
    self._update_text()

  def _update_text(self):
    self.font: Font = pygame.font.SysFont(name=self.font_name, size=self.size)
    self.image: Surface = self.font.render(self.text, True, self.color).convert_alpha()
    self.rect: Rect = self.image.get_rect()

  def start(self): # Call when behaviour is instanced
    pass

  def update(self): # Call once per game loop iteration
    pass

  def late_update(self): # Call after update
    pass