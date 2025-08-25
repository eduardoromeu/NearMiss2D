import pygame

from ..Scene import Scene
from ..Objects.PlayerCar import Car
from ..Objects.Road import Road
from ..Objects.UIText import UIText

class MainMenu(Scene):

  def init(self):
    # Draw menu bg
    menuBg = Road("MenuBg")
    scaled_bg = pygame.transform.scale(menuBg.image, (1024, 768))
    menuBg.image = scaled_bg
    self.add(menuBg)

    # Game logo
    game_logo = GameLogo("GameLogo")
    self.add(game_logo)

    # Menu Behaviour
    menuBhv = MainMenuBehaviour()
    self.add(menuBhv)


from ..Behaviour import Behaviour
class MainMenuBehaviour(Behaviour):
  
  def start(self):
    self.selection = 0

  def on_enable(self): # Call when behaviour is instanced
    # Menu Text
    start_text = UIText("Start Game", 56, font_name="Pretendard", name="start-text")
    start_text.rect.centerx = 512
    start_text.rect.centery = 400
    self.scene.add(start_text)
    
    pass

  def update(self): # Call once per game loop iteration
    pass

from ..Objects.GameSprite import GameSprite
class GameLogo(GameSprite):
  def start(self):
    logo_img = pygame.image.load('./assets/logo-pixel.png').convert_alpha()
    
    self.image = pygame.transform.scale(logo_img, (300, 300))
    self.rect = self.image.get_rect()
    self.rect.centerx = 512

  def update(self):
    self.rect.centerx = 512
    # print('Updating game logo!')