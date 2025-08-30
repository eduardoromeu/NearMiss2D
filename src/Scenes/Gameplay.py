import pygame
from random import randint, random
from ..Consts import SCREEN_HEIGHT, SCREEN_WIDTH, DEV_MODE, TRAFFIC_SPAWN_EVENT
from ..Scene import Scene
from ..Objects.Highway import Highway
from ..Objects.UIText import UIText
from ..Objects.PlayerCar import PlayerCar
from ..Objects.TrafficCar import TrafficCar

class Gameplay(Scene):

  def init(self):
    self.player_score = PlayerScore("PlayerScore")
    self.add(self.player_score)

    road1 = Highway("road1", position=(0, 0), speed=9)
    road2 = Highway("road2", position=(0, -682), speed=9)
    road3 = Highway("road3", position=(0, 682), speed=9)
    self.add(road1, road2, road3)

    self.player_car = PlayerCar("PlayerCar", position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10), rotozoom=(0, 0.2))
    self.add(self.player_car)

    if DEV_MODE:
      self.debg_txt = UIText("DEV_BUILD", 28, pygame.color.THECOLORS["white"], bg_color=pygame.color.THECOLORS["black"], layer=2)
      self.debg_txt.rect.left = 0
      self.add(self.debg_txt)

    self.traffic_lanes = [
      TrafficLane(110, True, 8,  "Lane1"),
      TrafficLane(370, True, 10,  "Lane2"),
      TrafficLane(640, False, 2, "Lane3"),
      TrafficLane(910, False, 4, "Lane4")
    ]

    self.add(*self.traffic_lanes)

  def handle_event(self, event: pygame.event.Event) -> None:
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        from .MainMenu import MainMenu
        Scene.load_scene(MainMenu("MainMenu", self.window))
      if event.key == pygame.K_p:
        self.paused = False if self.paused else True

from ..Behaviour import Behaviour
class PlayerScore(Behaviour):
  def start(self):
    self.score = 0
    self.last_tick = pygame.time.get_ticks()
    if DEV_MODE:
      self.initial_tick = pygame.time.get_ticks()

  def on_enable(self):
    self.score_txt = UIText("SCORE", 24, pygame.color.THECOLORS["whitesmoke"], bg_color=pygame.color.THECOLORS["black"], layer=2)
    self.score_txt.rect.top = 10
    self.score_txt.rect.centerx = round(SCREEN_WIDTH / 2)
    self.scene.add(self.score_txt)

  def update(self):
    current_tick = pygame.time.get_ticks()
    if current_tick - self.last_tick >= 16.66: # ensure score consistency with frame variations
      self.last_tick = current_tick
      self.score += 0.36 # Car is running at 80 KM/H
      #self.scene.score_txt.text = f'SCORE {round((self.score / 1000), 3)}' # Kilometers
      self.score_txt.text = f'DISTANCE: {round(self.score)}m' # Meters
      self.score_txt.update_render()
    if DEV_MODE:
      self.scene.debg_txt.text = f'TIME {(current_tick - self.initial_tick) / 1000}s'
      self.scene.debg_txt.update_render()

class TrafficLane(Behaviour):
  def __init__(self, lanex: int, way_up: bool, cars_speed: float = 5, name: str = 'Lane', **kwargs):
    self.name = f'Lane{lanex}' if name == 'Lane' else name
    self.update_layer = 1
    self.lanex = lanex
    self.way_up = way_up
    self.cars_speed = cars_speed
    self.spawn_chance = 0.4
    self.min_spawn_rate = 2000 # Min spawn rate
    self.traffic_spawn_rate = {"min" : 2000, "max" : 10000, "set" : 3000} # Milliseconds to spawn a traffic car
    self.traffic_spawn_rate["set"] = randint(self.traffic_spawn_rate["min"], self.traffic_spawn_rate["max"]) # rnd first spawn time
    self.spawn_rate_decrement = 25 # Spawn rate decrement after each spawn
    self.start_time = pygame.time.get_ticks()
    self.time_passed = self.start_time
    for attr, value in kwargs.items():
      setattr(self, attr, value)
    self.traffic_cars = pygame.sprite.Group()

    if DEV_MODE:
      self.debg_txt = UIText("_", 28, pygame.color.THECOLORS["white"], bg_color=pygame.color.THECOLORS["black"], name=f"{self.name}_txt")
      self.debg_txt.rect.centerx = self.lanex
      self.debg_txt.rect.bottom = SCREEN_HEIGHT - 28

  def on_enable(self):
    if DEV_MODE:
      self.scene.add(self.debg_txt)

  def start(self):
    pass

  def update(self):
    self.player_hit = pygame.sprite.spritecollide(self.scene.player_car, self.traffic_cars,
                                                  False,  pygame.sprite.collide_mask)
    self.debug_text()
    self.time_passed = pygame.time.get_ticks()
    if self.time_passed - self.start_time >= self.traffic_spawn_rate["set"]:
      self.start_time = self.time_passed
      self.check_spawn()

  def check_spawn(self):
    if random() < self.spawn_chance:
      self.spawn_traffic()

  def spawn_traffic(self):
    # Update spawn rate
    if self.traffic_spawn_rate["min"] > self.min_spawn_rate:
      self.traffic_spawn_rate["min"] -= self.spawn_rate_decrement
    if self.traffic_spawn_rate["max"] > self.min_spawn_rate + self.spawn_rate_decrement:
      self.traffic_spawn_rate["max"] -= self.spawn_rate_decrement
    self.traffic_spawn_rate["set"] = randint(self.traffic_spawn_rate["min"], self.traffic_spawn_rate["max"])

    # update event timer
    # pygame.time.set_timer(TRAFFIC_SPAWN_EVENT, self.traffic_spawn_rate["set"])
    print(f'traffic spawned at {pygame.time.get_ticks()} in `{self.name}')

    # spawn!
    tr_top_pos = randint(-450, 0)
    x_offset = randint(self.lanex - 15, self.lanex + 15)
    traffic_car = TrafficCar("TrafficCar", position=(x_offset, tr_top_pos), rotozoom=(180 if self.way_up else 0, 0.2), speed=self.cars_speed, lane=self)
    traffic_car.add(self.traffic_cars) # add to sprite group
    self.scene.add(traffic_car)

  def debug_text(self):
    if DEV_MODE and hasattr(self.scene, 'debg_txt') and hasattr(self.scene, 'player_car'):
      #self.scene.debg_txt.text = f'X: {self.scene.player_car.rect.centerx} | Y: {self.scene.player_car.rect.centery}'
      # self.scene.debg_txt.text = f'min {self.traffic_spawn_rate["min"]} | max {self.traffic_spawn_rate["max"]} dec {self.spawn_rate_decrement}'
      # self.scene.debg_txt.update_render()

      self.debg_txt.text = f'TIME {self.traffic_spawn_rate["set"] - (self.time_passed - self.start_time)}'
      self.debg_txt.text = f'{self.player_hit}'
      self.debg_txt.update_render()
      self.debg_txt.rect.centerx = self.lanex
      self.debg_txt.rect.bottom = SCREEN_HEIGHT - 28
