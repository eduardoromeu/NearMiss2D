from .Behaviour import Behaviour

# make it abstract 
class Scene:

  def __init__(self, name: str = "Default") -> None:
    print(f"Loading scene {name}")
    self.name = name
    
    # list of behaviours in this scene
    self.hierarchy: list[Behaviour] = []

  def game_loop(self):
    for behaviour in self.hierarchy:
      behaviour.update()
    
    for behaviour in self.hierarchy:
      behaviour.late_update()

  def add(self, object: Behaviour):
    self.hierarchy.append(object)