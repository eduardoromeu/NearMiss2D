import pygame
from dataclasses import dataclass

@dataclass
class Car:
    name: str
    image_path: str
    accel: float
    max_speed: float
    weight: float
