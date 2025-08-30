import pygame

from ..Consts import SCREEN_WIDTH, SCREEN_HEIGHT
from ..Scene import Scene
from ..Objects.Road import Road
from ..Objects.Highway import Highway
from ..Objects.UIText import UIText

class GammeOver(Scene):
    def init(self):
        bg = Highway("Bg", position=(0, 0), scale=(1024, 682), speed=0)
        bg2 = Highway("Bg2", position=(0, 682), scale=(1024, 682), speed=0)
        bg3 = Highway("Bg2", position=(0, -682), scale=(1024, 682), speed=0)
        self.add(bg, bg2, bg3)

        ilust = GameOverSprite("GameOverSprite", position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.add(ilust)

        go_text = UIText("GAME OVER!", 64, color=pygame.Color('orange1'), name=f"go-text", layer=3, bg_color=pygame.Color('black'))
        go_text.rect.center = (round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 4))
        self.add(go_text)

        if hasattr(self, "player_score"):
            score_text = UIText(f"SCORE: {round(self.player_score.score)}", 64, color=pygame.Color('whitesmoke'), name=f"score-text", bg_color=pygame.Color('black'))
            score_text.rect.center = (round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 4) * 3)
            self.add(score_text)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from .MainMenu import MainMenu
                Scene.load_scene(MainMenu("MainMenu", self.window))

from ..Objects.GameSprite import GameSprite
class GameOverSprite(GameSprite):

  def start(self):
    self.image = pygame.image.load("./assets/Sprites/game_over_img.png").convert_alpha()
    self.rect = self.image.get_rect(center=self.position)