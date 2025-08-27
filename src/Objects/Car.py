import pygame

class Car:
  def __init__(self, name: str, image_path: str, accel: int, max_speed: int, weight: int):
    self.name = name
    self.image_path = image_path
    self.accel = accel
    self.max_speed = max_speed
    self.weight = weight
