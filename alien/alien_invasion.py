import pygame
from setting import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats

from button import Button

def run_game():
    pygame.init()

    ai_setting = Setting()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_setting, screen, 'Play')
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_setting)
    gf.create_fleet(ai_setting, screen, ship, aliens)
    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        gf.update_screen(ai_setting, screen, stats, ship,
                         aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)
            gf.update_bullet(ai_setting, screen, ship, aliens, bullets)



run_game()
