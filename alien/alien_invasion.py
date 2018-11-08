import pygame
from setting import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group

def run_game():
  pygame.init()

  ai_setting = Setting()
  screen = pygame.display.set_mode(
      (ai_setting.screen_width, ai_setting.screen_height))
  pygame.display.set_caption('Alien Invasion')
  ship = Ship(ai_setting, screen)

  bullets = Group()

  while True:
    gf.check_events(ai_setting, screen, ship, bullets)
    ship.update()
    bullets.update()
    for bullet in bullets.copy():
      if bullet.rect.bottom <= 0:
        bullets.remove(bullet)
      print(len(bullets))
    gf.update_screen(ai_setting, screen, ship, bullets)

run_game()
