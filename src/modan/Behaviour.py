from abc import ABC, abstractmethod

class Behaviour(ABC):

  isActive: bool = False

  def __init__(self) -> None:
    self.Start()


  @abstractmethod
  def Start(self):
    pass

  @abstractmethod
  def Update(self):
    pass