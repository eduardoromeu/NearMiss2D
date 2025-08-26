from pygame import Surface
from abc import ABC, abstractmethod
from .Behaviour import Behaviour
from src.Objects.GameSprite import GameSprite

class Scene(ABC):

  def __init__(self, name: str, window: Surface) -> None:
    print(f"Loading scene {name}")
    self.name = name
    
    # list of behaviours in this scene
    self.hierarchy: list[Behaviour] = []

    # draws a surface to be used by the scene
    self.window = window
    self.canvas = Surface(window.get_size())
    window.blit(self.canvas, self.canvas.get_rect())

  def game_loop(self):
    # Update behaviours
    for behaviour in self.hierarchy:
      behaviour.update()

      # Draw sprites
      if isinstance(behaviour, GameSprite):
        self.canvas.blit(behaviour.image, behaviour.rect)
        # print(f'Drawing {behaviour.name}')
    
    self.window.blit(self.canvas, self.canvas.get_rect())
    
    for behaviour in self.hierarchy:
      behaviour.late_update()

  def add(self, obj: Behaviour):
    self.hierarchy.append(obj)
    obj.set_scene(self)
    obj.on_enable()

  @abstractmethod
  def init(self):
    pass