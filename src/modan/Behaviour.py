from abc import ABC, abstractmethod

class Behaviour(ABC):

  def __init__(self) -> None:
    self.Start()

  @abstractmethod
  def Start(self):
    pass