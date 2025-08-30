import pygame
from random import randint, random
from ..Consts import SCREEN_HEIGHT, SCREEN_WIDTH, DEV_MODE, TRAFFIC_SPAWN_EVENT
from ..Scene import Scene
from ..Objects.Road import Road
from ..Objects.Highway import Highway
from ..Objects.UIText import UIText
from ..Objects.PlayerCar import PlayerCar
from ..Objects.TrafficCar import TrafficCar
from ..Input import Input

class Gameplay(Scene):

  def init(self):
    road1 = Highway("road1", position=(0, 0), speed=10)
    road2 = Highway("road2", position=(0, -682), speed=10)
    road3 = Highway("road3", position=(0, 682), speed=10)
    self.add(road1, road2, road3)

    self.player_car = PlayerCar("PlayerCar", position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10), rotozoom=(0, 0.25))
    self.add(self.player_car)

    if DEV_MODE:
      self.debg_txt = UIText("score", 28, pygame.color.THECOLORS["white"], bg_color=pygame.color.THECOLORS["black"])
      self.debg_txt.rect.bottom = SCREEN_HEIGHT - 2
      self.add(self.debg_txt)

    # self.gameplay_manager = SpawnManager()
    self.traffic_lanes = [
      TrafficLane(110, True, 8,  "Lane1"),
      TrafficLane(370, True, 10,  "Lane2"),
      TrafficLane(640, False, 4, "Lane3"),
      TrafficLane(910, False, 2, "Lane4")
    ]

    self.add(*self.traffic_lanes)

  def handle_event(self, event: pygame.event.Event) -> None:
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        from .MainMenu import MainMenu
        Scene.load_scene(MainMenu("MainMenu", self.window))
      if event.key == pygame.K_p:
        self.paused = False if self.paused else True
    # if event.type == TRAFFIC_SPAWN_EVENT:
    #   self.gameplay_manager.spawn_traffic()

from ..Behaviour import Behaviour
class TrafficLane(Behaviour):
  def __init__(self, lanex: int, way_up: bool, cars_speed = 5, name: str = 'Lane', **kwargs):
    self.name = f'Lane{lanex}' if name == 'Lane' else name
    self.lanex = lanex
    self.way_up = way_up
    self.cars_speed = cars_speed
    self.spawn_chance = 0.4
    self.min_spawn_rate = 2000 # Min spawn rate
    self.traffic_spawn_rate = {"min" : 5000, "max" : 6000, "set" : 5000} # Milliseconds to spawn a traffic car
    self.spawn_rate_decrement = 250 # Spawn rate decrement after each spawn
    self.start_time = pygame.time.get_ticks()
    self.time_passed = self.start_time
    for attr, value in kwargs.items():
      setattr(self, attr, value)
    # pygame.time.set_timer(TRAFFIC_SPAWN_EVENT, self.traffic_spawn_rate["set"])
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
    traffic_car = TrafficCar("TrafficCar", position=(self.lanex, tr_top_pos), rotozoom=(180 if self.way_up else 0, 0.25), speed=self.cars_speed, lane=self)
    self.scene.add(traffic_car)

  def debug_text(self):
    if DEV_MODE and hasattr(self.scene, 'debg_txt') and hasattr(self.scene, 'player_car'):
      #self.scene.debg_txt.text = f'X: {self.scene.player_car.rect.centerx} | Y: {self.scene.player_car.rect.centery}'
      # self.scene.debg_txt.text = f'min {self.traffic_spawn_rate["min"]} | max {self.traffic_spawn_rate["max"]} dec {self.spawn_rate_decrement}'
      # self.scene.debg_txt.update_render()

      self.debg_txt.text = f'TIME {self.traffic_spawn_rate["set"] - (self.time_passed - self.start_time)}'
      self.debg_txt.update_render()
      self.debg_txt.rect.centerx = self.lanex
      self.debg_txt.rect.bottom = SCREEN_HEIGHT - 28
