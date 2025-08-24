from abc import ABC, abstractmethod

class Behaviour(ABC):

  isActive: bool = False

  def __init__(self, name: str = 'NewBehaviour') -> None:
    self.start()

  @abstractmethod
  def start(self): # Call when behaviour is instanced
    pass

  @abstractmethod
  def update(self): # Call once per game loop iteration
    pass

  @abstractmethod
  def late_update(self): # Call after update
    pass