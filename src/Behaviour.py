from abc import ABC, abstractmethod

class Behaviour(ABC):

  isActive: bool = False

  def __init__(self, name: str = 'NewBehaviour', **kwargs) -> None:
    self.name = name
    for attr, value in kwargs.items():
      setattr(self, attr, value)
    self.start()

  # use to subscribe events?
  def __init_subclass__(cls) -> None:
    return super().__init_subclass__()

  def set_scene(self, scene):
    self.scene = scene

  @abstractmethod
  def start(self): # Call when behaviour is instanced
    pass

  def on_enable(self): # Call when behaviour is added to scene
    pass

  @abstractmethod
  def update(self): # Call once per game loop iteration
    pass

  # @abstractmethod
  def late_update(self): # Call after update
    pass