import pygame
from typing import Optional

from .Scene import Scene
from .Scenes.MainMenu import MainMenu
from .Scenes.Gameplay import Gameplay
from .Scenes.HighScores import HighScores
from .Display import Display
from .Input import Input

class Game:

    manager: 'Game, None' = None

    # Currently active scene
    running = True

    def __init__(self) -> None:
        print("Initializing game...")
        pygame.init()
        Game.manager = self
        self.display = Display()
        self.input = Input()
        Scene.load_scene(MainMenu("MainMenu", self.display.screen))
        self.run()

    def run(self):
        # Game loop
        while Game.running:
            # update events
            for event in pygame.event.get():
                # pass events to scene
                if Scene.active_scene is not None:
                    Scene.active_scene.handle_event(event)
                if event.type == pygame.QUIT:
                    Game.running = False

            # update inputs
            self.input.update()

            # update scene
            if Scene.active_scene is not None:
                Scene.active_scene.game_loop()

            # update display
            self.display.update()

        # exit game
        pygame.quit()
