from collections.abc import Callable

import pygame

from .Gameplay import Gameplay
from .HighScores import HighScores
from ..Consts import SCREEN_WIDTH, SCREEN_HEIGHT
from ..Scene import Scene
# from ..Objects.PlayerCar import Car
from ..Objects.Road import Road
from ..Objects.UIText import UIText

class MainMenu(Scene):

  def init(self):
    # Draw menu bg
    menu_bg = Road("MenuBg", position=(0, 0), scale=(1024, 682), speed=2)
    menu_bg2 = Road("MenuBg2", position=(0, 682), scale=(1024, 682), speed=2)
    menu_bg3 = Road("MenuBg2", position=(0, -682), scale=(1024, 682), speed=2)
    self.add(menu_bg, menu_bg2, menu_bg3)

    # Game logo
    game_logo = GameLogo("GameLogo", position=(512, 150))
    self.add(game_logo)

    # Menu Behaviour
    menu_behaviour = MainMenuBehaviour("MainMenuBehaviour")
    self.add(menu_behaviour)

    # Controls
    ctrls_txt = UIText("CONTROLS", 52, color=pygame.Color('darkorange2'), name=f"ctrls_txt", bg_color=pygame.Color('black'))
    ctrls_txt.rect.center = (round(SCREEN_WIDTH / 2), round((SCREEN_HEIGHT / 12) * 8))
    txt_move = UIText("MOVE: WASD / ARROW KEYS", 42, color=pygame.Color('whitesmoke'), name=f"txt-move", bg_color=pygame.Color('black'))
    txt_move.rect.center = (round(SCREEN_WIDTH / 2), round((SCREEN_HEIGHT / 12) * 9))
    txt_pause = UIText("PAUSE: P", 42, color=pygame.Color('whitesmoke'), name=f"txt-pause", bg_color=pygame.Color('black'))
    txt_pause.rect.center = (round(SCREEN_WIDTH / 2), round((SCREEN_HEIGHT / 12) * 10))
    txt_exit = UIText("EXIT: ESC", 42, color=pygame.Color('whitesmoke'), name=f"txt-exit", bg_color=pygame.Color('black'))
    txt_exit.rect.center = (round(SCREEN_WIDTH / 2), round((SCREEN_HEIGHT / 12) * 11))

    self.add(ctrls_txt, txt_move, txt_pause, txt_exit)

  def handle_event(self, event: pygame.event.Event) -> None:
    if event.type == pygame.KEYDOWN:
      menu_behaviour = self.get_object("MainMenuBehaviour")
      if isinstance(menu_behaviour, MainMenuBehaviour):
        if event.key == pygame.K_UP:
          menu_behaviour.prev_option()
        if event.key == pygame.K_DOWN:
          menu_behaviour.next_option()
        # Enter selected option
        if event.key == pygame.K_RETURN:
          menu_behaviour.select_active_option()

# Class for a menu option
class MenuOption:
  def __init__(self, text: str, callback: Callable) -> None:
    self.text = text
    self.callback = callback
    self.uitext: UIText|None = None

from ..Behaviour import Behaviour
class MainMenuBehaviour(Behaviour):

  def start(self):
    self.selection = 0
    self.options = [
      MenuOption('Start Game', self.start_game),
      MenuOption('High Scores', self.high_scores),
      MenuOption('Exit Game', self.quit_game)
    ]

  def on_enable(self): # Call when behaviour is instanced
    # Menu Text
    for option in self.options:
      option_index = self.options.index(option)
      col = pygame.Color('orange') if option_index == self.selection else pygame.Color('whitesmoke')
      option.uitext = UIText(option.text, 56, color=col, name=f"option-text-{option_index}")
      option.uitext.rect.centerx = 512
      option.uitext.rect.centery = 384 + (option_index * 64)
      self.scene.add(option.uitext)
    pass

  def update(self):
    pass

  def next_option(self):
    self.selection = (self.selection + 1) % len(self.options)
    self.update_options()

  def prev_option(self):
    self.selection = (self.selection - 1) % len(self.options)
    self.update_options()

  def select_active_option(self):
    self.options[self.selection].callback()

  def update_options(self):
    for option in self.options:
      option_index = self.options.index(option)
      option.uitext.color = pygame.Color('orange') if option_index == self.selection else pygame.Color('whitesmoke')
      option.uitext.update_render()
      option.uitext.rect.centerx = 512
      option.uitext.rect.centery = 384 + (option_index * 64)

  def start_game(self):
    Scene.load_scene(Gameplay("Gameplay", self.scene.window))

  def high_scores(self):
    Scene.load_scene(HighScores("HighScores", self.scene.window))

  def quit_game(self):
    pygame.event.post(pygame.event.Event(pygame.QUIT))

from ..Input import Input
from ..Objects.GameSprite import GameSprite
class GameLogo(GameSprite):

  def start(self):
    logo_img = pygame.image.load('./assets/logo-pixel.png').convert_alpha()
    self.image = pygame.transform.scale(logo_img, (300, 300))
    self.original_image = self.image
    self.rect = self.image.get_rect(center=self.position)
    # self.rect.centerx = 512
    # self.rect.centery = 150
    self.angle = 0

  def update(self):
    if Input.is_key_pressed(pygame.K_RIGHT):
      self.angle -= .05
    if Input.is_key_pressed(pygame.K_LEFT):
      self.angle += .05

    self.image = pygame.transform.rotate(self.original_image, self.angle)
    # keep image location
    old_center = self.rect.center
    self.rect = self.image.get_rect()
    self.rect.center = old_center