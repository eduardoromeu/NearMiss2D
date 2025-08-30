import pygame
from pygame import Surface, Rect
from pygame.font import Font
from .GameSprite import GameSprite

class UIText(GameSprite):

  def __init__(self, text: str, size: int, color: tuple | pygame.Color = (255, 255, 255), font_name="Pretendard",
               name: str = 'NewText', bg_color=None, position=(0,0), scale=(0,0), layer=2, **kwargs) -> None:

    super().__init__(name, position, scale, layer, **kwargs)
    self.text = text
    self.size = size
    self.color = color
    self.font_name = font_name
    self.bg_color = bg_color
    self.font: Font = pygame.font.SysFont(name=self.font_name, size=self.size)
    self.image: Surface = self.font.render(self.text, True, self.color, self.bg_color).convert_alpha()
    self.rect: Rect = self.image.get_rect()
    #self.update_render()

  def update_render(self):
    self.font: Font = pygame.font.SysFont(name=self.font_name, size=self.size)
    self.image: Surface = self.font.render(self.text, True, self.color, self.bg_color).convert_alpha()
    self.rect: Rect = self.image.get_rect(center=self.rect.center)

  def start(self): # Call when behaviour is instanced
    pass

  def update(self): # Call once per game loop iteration
    pass

  def late_update(self): # Call after update
    pass