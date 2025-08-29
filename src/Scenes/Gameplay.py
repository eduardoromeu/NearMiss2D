import pygame
from random import randint
from ..Consts import SCREEN_HEIGHT, SCREEN_WIDTH, DEV_MODE, TRAFFIC_SPAWN_EVENT
from ..Scene import Scene
from ..Objects.Road import Road
from ..Objects.Highway import Highway
from ..Objects.UIText import UIText
from ..Objects.PlayerCar import PlayerCar
from ..Objects.TrafficCar import TrafficCar

class Gameplay(Scene):

  def init(self):
    road1 = Highway("road1", position=(0, 0), speed=10)
    road2 = Highway("road2", position=(0, -682), speed=10)
    road3 = Highway("road3", position=(0, 682), speed=10)
    self.add(road1, road2, road3)

    self.player_car = PlayerCar("PlayerCar", position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10), rotozoom=(0, 0.25))
    self.add(self.player_car)

    self.debg_txt = UIText("score", 28, pygame.color.THECOLORS["white"], bg_color=pygame.color.THECOLORS["black"])
    self.debg_txt.rect.bottom = SCREEN_HEIGHT - 2
    self.add(self.debg_txt)

    self.gameplay_manager = GameplayManager("GameplayManager")
    self.add(self.gameplay_manager)

  def handle_event(self, event: pygame.event.Event) -> None:
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        from .MainMenu import MainMenu
        Scene.load_scene(MainMenu("MainMenu", self.window))
    if event.type == TRAFFIC_SPAWN_EVENT:
      self.gameplay_manager.spawn_traffic()

from ..Behaviour import Behaviour
class GameplayManager(Behaviour):
  def start(self):
    self.road_lanes = {
      "up": [640, 910],
      "down": [110, 370]
    }

    self.min_spawn_rate = 3000 # Min spawn rate
    self.traffic_spawn_rate = {"min" : 8000, "max" : 10000, "set" : 9000} # Milliseconds to spawn a traffic car
    self.spawn_rate_decrement = 250 # Spawn rate decrement after each spawn

    pygame.time.set_timer(TRAFFIC_SPAWN_EVENT, self.traffic_spawn_rate["set"])

  def update(self):
    if DEV_MODE and hasattr(self.scene, 'debg_txt') and hasattr(self.scene, 'player_car'):
      #self.scene.debg_txt.text = f'X: {self.scene.player_car.rect.centerx} | Y: {self.scene.player_car.rect.centery}'
      self.scene.debg_txt.text = f'min {self.traffic_spawn_rate["min"]} | max {self.traffic_spawn_rate["max"]} | set {self.traffic_spawn_rate["set"]} | dec {self.spawn_rate_decrement}'
      self.scene.debg_txt.update_render()

  def spawn_traffic(self):
    # Update spawn rate
    if self.traffic_spawn_rate["min"] > self.min_spawn_rate:
      self.traffic_spawn_rate["min"] -= self.spawn_rate_decrement
    if self.traffic_spawn_rate["max"] > self.min_spawn_rate + self.spawn_rate_decrement:
      self.traffic_spawn_rate["max"] -= self.spawn_rate_decrement
    self.traffic_spawn_rate["set"] = randint(self.traffic_spawn_rate["min"], self.traffic_spawn_rate["max"])

    # update event timer
    pygame.time.set_timer(TRAFFIC_SPAWN_EVENT, self.traffic_spawn_rate["set"])
    print(f'traffic spawned at {pygame.time.get_ticks()}')

    # spawn!
    tr_top_pos = randint(-100, 0)
    traffic_car = TrafficCar("TrafficCar", position=(370, tr_top_pos), rotozoom=(180, 0.25))
    self.scene.add(traffic_car)