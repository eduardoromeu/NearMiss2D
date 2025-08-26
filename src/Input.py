import pygame
from .Display import Display

class Input():
    pressed_keys = []

    def __init__(self):
        pass

    def update(self):
        Input.pressed_keys = pygame.key.get_pressed()
        if Input.is_key_pressed(pygame.K_F11):
            Display.toggle_fullscreen()

    @classmethod
    def is_key_pressed(cls, key) -> bool:
        return cls.pressed_keys[key]

    @classmethod
    def get_keydown_event(cls, key) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return event.key == key
        return False