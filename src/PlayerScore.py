from json import JSONDecodeError

import pygame
import json
from .Consts import DEV_MODE, SCREEN_WIDTH
from .Objects.UIText import UIText
from .Behaviour import Behaviour

class PlayerScore(Behaviour):
  def start(self):
    self.score = 0
    self.score_list: list[int] = []
    self.last_tick = pygame.time.get_ticks()
    self.extra_score_txt = ""
    self.extra_score_time = self.last_tick
    self.running = True
    if DEV_MODE:
      self.initial_tick = pygame.time.get_ticks()

  def on_enable(self):
    self.score_txt = UIText("SCORE", 32, pygame.color.THECOLORS["whitesmoke"], bg_color=pygame.color.THECOLORS["black"], layer=2)
    self.score_txt.rect.top = 10
    self.score_txt.rect.centerx = round(SCREEN_WIDTH / 2)
    self.scene.add(self.score_txt)

  def update(self):
    if not self.running:
      return
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

  def load_scores(self):
    try:
      with open("scores.json", "r") as file:
        saved_scores = file.read()
        scores_list = json.loads(saved_scores) # json
        scores_list["scores"].append(self.score)
        scores_list["scores"].sort(reverse=True)
        del scores_list["scores"][5:] # only 5 better scores
        self.score_list = scores_list["scores"]
        if self.score_list[0] == 0:
          return None
        return self.score_list
    except Exception as e:
      self.create_save_file()
      return None

  def save_score(self):
    self.score = round(self.score)

    try:
      with open("scores.json", "r+") as file:
        saved_scores = file.read()
        scores_list = json.loads(saved_scores) # json
        file.seek(0)

        scores_list["scores"].append(self.score)
        scores_list["scores"].sort(reverse=True)
        del scores_list["scores"][5:] # only 5 better scores
        self.score_list = scores_list["scores"]

        json.dump(scores_list, file)

    except FileNotFoundError:
      self.create_save_file()
    except JSONDecodeError:
      self.create_save_file()
    except Exception as e:
      self.create_save_file()

  def create_save_file(self):
    print("File not found or corrupt. Creating a new file.")
    with open("scores.json", "w") as file:
      self.score_list.append(self.score)
      scores = {"scores": self.score_list}
      json.dump(scores, file)
