import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_setting, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_setting, screen, ship, aliens, bullets):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitem()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullet(ai_setting, screen, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets)

def fire_bullet(bullets, ai_setting, screen, ship):
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_setting, screen, ship, aliens):
    alien = Alien(ai_setting, screen)
    number_alien_x = get_number_alien_x(ai_setting, screen, alien)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        create_alien(ai_setting, screen, aliens, number_alien_x, row_number)


def get_number_alien_x(ai_setting, screen, alien):
    alien_width = alien.rect.width

    available_space_x = ai_setting.screen_width - alien_width * 2

    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def create_alien(ai_setting, screen, aliens, number_alien_x, row_number):
    for alien_number in range(number_alien_x):
        alien = Alien(ai_setting, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)


def get_number_rows(ai_setting, ship_height, alien_height):
    available_space_y = ai_setting.screen_height - 3 * alien_height - ship_height

    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_setting, ship, aliens):
    check_fleet_edges(ai_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        print('Ship hit!!!')

def check_fleet_edges(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def change_fleet_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_setting, screen, ship, aliens)
