import pygame
from pygame import Surface
from abc import ABC, abstractmethod
from .Behaviour import Behaviour
from src.Objects.GameSprite import GameSprite

class Scene(ABC):
    active_scene: 'Scene, None' = None

    @staticmethod
    def load_scene(scene: 'Scene'):
        Scene.active_scene = scene
        Scene.active_scene.init()

    def __init__(self, name: str, window: Surface) -> None:
        print(f"Loading scene {name}")
        self.name = name

        # list of behaviours in this scene
        self.hierarchy: list[Behaviour] = []

        # draws a surface to be used by the scene
        self.window = window
        self.canvas = Surface(window.get_size())
        window.blit(self.canvas, self.canvas.get_rect())

    # idea: use to subscribe to a game scene list
    def __init_subclass__(cls) -> None:
        print(f"Creating scene {cls.__name__}")

    def game_loop(self):
        # print('game loop start')
        # Update behaviours
        for behaviour in self.hierarchy:
            behaviour.update()
            # print(f'Updating {behaviour.name}')

            # Draw sprites
            if isinstance(behaviour, GameSprite):
                self.canvas.blit(behaviour.image, behaviour.rect)
                # print(f'Drawing {behaviour.name}')

        self.window.blit(self.canvas, self.canvas.get_rect())

        for behaviour in self.hierarchy:
            behaviour.late_update()

        # print('game loop end')

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def add(self, *objs: Behaviour):
        for obj in objs:
            self.hierarchy.append(obj)
            obj.set_scene(self) # Set object current scene
            obj.on_enable()

    def remove(self, *objs: Behaviour):
        for obj in objs:
            self.hierarchy.remove(obj)
            obj.on_disable()

    def get_object(self, name: str) -> Behaviour | None:
        for behaviour in self.hierarchy:
            if behaviour.name == name:
                return behaviour
        return None

    @abstractmethod
    def init(self):
        pass
