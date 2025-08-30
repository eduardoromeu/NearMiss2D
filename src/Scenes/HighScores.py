import pygame

from ..Consts import SCREEN_WIDTH, SCREEN_HEIGHT
from ..PlayerScore import PlayerScore
from ..Scene import Scene
from ..Objects.Road import Road
from ..Objects.UIText import UIText

class HighScores(Scene):
    def init(self):
        bg = Road("Bg", position=(0, 0), scale=(1024, 682), speed=5)
        bg2 = Road("Bg2", position=(0, 682), scale=(1024, 682), speed=5)
        bg3 = Road("Bg2", position=(0, -682), scale=(1024, 682), speed=5)
        self.add(bg, bg2, bg3)

        self.player_score = PlayerScore()
        self.scores = self.player_score.load_scores()
        print(self.scores)

        scores_txt = UIText("HIGH SCORES", 64, color=pygame.Color('orange1'), name=f"hs-text", layer=3, bg_color=pygame.Color('black'))
        scores_txt.rect.center = (round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 10))
        self.add(scores_txt)

        if self.scores is not None:
            scores_texts:list[UIText] = []

            for i, score in enumerate(self.scores):
                scr_txt = UIText(f'{score}', 52, color=pygame.Color('orange1'), name=f"hs-text", layer=3,
                       bg_color=pygame.Color('black'))
                scr_txt.rect.center = (round(SCREEN_WIDTH / 2), round((SCREEN_HEIGHT / 10) * (i + 3)))
                scores_texts.append(scr_txt)

            self.add(*scores_texts)
        else:
            no_scores_txt = UIText("NO SAVED SCORES", 64, color=pygame.Color('orange1'), name=f"hs-text", layer=3,
                                bg_color=pygame.Color('black'))
            no_scores_txt.rect.center = (round(SCREEN_WIDTH / 2), round((SCREEN_HEIGHT / 10) * 5))
            self.add(no_scores_txt)

        exit_txt = UIText("PRESS ANY KEY TO EXIT", 64, color=pygame.Color('whitesmoke'), name=f"hs-text", layer=3, bg_color=pygame.Color('black'))
        exit_txt.rect.center = (round(SCREEN_WIDTH / 2), round((SCREEN_HEIGHT / 10) * 9))
        self.add(exit_txt)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
                from .MainMenu import MainMenu
                Scene.load_scene(MainMenu("MainMenu", self.window))