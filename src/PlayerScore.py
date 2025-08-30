import pygame
from .Consts import DEV_MODE, SCREEN_WIDTH
from .Objects.UIText import UIText
from .Behaviour import Behaviour

class PlayerScore(Behaviour):
  def start(self):
    self.score = 0
    self.last_tick = pygame.time.get_ticks()
    self.extra_score_txt = ""
    self.extra_score_time = self.last_tick
    if DEV_MODE:
      self.initial_tick = pygame.time.get_ticks()

  def on_enable(self):
    self.score_txt = UIText("SCORE", 32, pygame.color.THECOLORS["whitesmoke"], bg_color=pygame.color.THECOLORS["black"], layer=2)
    self.score_txt.rect.top = 10
    self.score_txt.rect.centerx = round(SCREEN_WIDTH / 2)
    self.scene.add(self.score_txt)

  def update(self):
    current_tick = pygame.time.get_ticks()
    if current_tick - self.last_tick >= 16.66: # ensure score consistency with frame variations
      self.last_tick = current_tick
      self.score += 0.36 # Car is running at 80 KM/H
      #self.scene.score_txt.text = f'SCORE {round((self.score / 1000), 3)}' # Kilometers
      self.score_txt.text = f' SCORE: {round(self.score)} {self.extra_score_txt}' # Meters
      self.score_txt.update_render()
    if DEV_MODE:
      self.scene.debg_txt.text = f'TIME {(current_tick - self.initial_tick) / 1000}s'
      self.scene.debg_txt.update_render()