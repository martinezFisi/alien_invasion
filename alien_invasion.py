import sys
import pygame

from operator import methodcaller

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class AlienInvasion:
    def __init__(self):
        
        pygame.init()

        self.settings = Settings()
        pygame.display.set_caption(self.settings.title)
        dimensions = (self.settings.screen_width, self.settings.screen_height)

        self.screen = pygame.display.set_mode(dimensions)
        self.background_color = self.settings.bg_color
        self.clock = pygame.time.Clock()
        self.ship_velocity = self.settings.ship_velocity
        self.alien_vertical_velocity = self.settings.alien_vertical_velocity
        self.bullet_velocity = self.settings.bullet_velocity
        self.bullet_color = self.settings.bullet_color
        self.alien_init_pos = self.settings.alien_init_pos
        self.horizontal_distance_between_aliens = self.settings.horizontal_distance_between_aliens
        self.vertical_distance_between_aliens = self.settings.vertical_distance_between_aliens
        self.number_of_aliens = self.settings.number_of_aliens
        self.number_of_aliens_per_row = self.settings.number_of_aliens_per_row
        self.player_lifes = self.settings.player_lifes
        self.player_number_of_special_bullets = self.settings.player_number_of_special_bullets
        self.special_bullet_width = self.settings.special_bullet_width

        self.ship = Ship(self)
        self.bullets = []
        self.aliens = []
        self.game_stats = GameStats(self)

        self.game_is_active = False  # False means the game is inactive
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()
            
            if self.game_is_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._check_collisions()
                self._check_ship_lifes() 
                self._check_aliens_lifes()

            self._update_screen()
            self.clock.tick(self.settings.fps)  # Control the frame rate


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.game_is_active:
                self._fire_bullet()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT and self.game_is_active and self.game_stats.player_number_of_special_bullets > 0:
                self._fire_bullet(True)
                self.game_stats.player_number_of_special_bullets -= 1


            # Mouse click to start the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.rect.collidepoint(mouse_pos) and not self.game_is_active:
                    print("Botón Play presionado")
                    self._start_game()

    def _update_screen(self):
        self.screen.fill(self.background_color)
        self.game_stats.blitme()
        self.ship.blitme()
        list(map(methodcaller('blitme'), self.bullets))
        list(map(methodcaller('blitme'), self.aliens))

        if self.game_is_active == False: 
            self.play_button.draw_button()

        pygame.display.flip() # Update the full display surface to the screen

    def _update_bullets(self):
        list(map(methodcaller('update'), self.bullets))

    def _fire_bullet(self, isSpecial=False):
        self.bullets.append(Bullet(self, isSpecial))
        print(f'Numero de bullets: {len(self.bullets)}')

    def _create_aliens(self):
        aliens = []
        for i in range(0, self.number_of_aliens):
            aliens.append(Alien(self, i))
        return aliens
    
    def _update_aliens(self):
        list(map(methodcaller('update'), self.aliens))
    
    def _check_collisions(self):

        specialBullet = None

        for alien in self.aliens[:]:
            
            # Check collision with ship
            if self.ship.rect.colliderect(alien.rect):
                self.aliens.remove(alien)
                self.game_stats.lifes -= 1
                continue  # Move to the next alien after handling collision

            # Check if alien reached bottom of screen
            if alien.rect.y + alien.rect.height >= self.screen.get_rect().height:
                self.aliens.remove(alien)
                self.game_stats.lifes -= 1
                continue

            # Check collision with bullets
            for bullet in self.bullets[:]:
                if bullet.rect.colliderect(alien.rect):
                    self.aliens.remove(alien)

                    if bullet.isSpecial:
                        specialBullet = bullet
                    else:
                        self.bullets.remove(bullet)

                    self.game_stats.score += 10
                    break  # Exit the inner loop to avoid checking other bullets for this alien

        if specialBullet:
            self.bullets.remove(specialBullet)
            

    def _check_ship_lifes(self):
        if self.game_stats.lifes <= 0:
            self.game_is_active = False

    def _check_aliens_lifes(self):
        if len(self.aliens) == 0:
            self._load_next_level()
    

    def _start_game(self):
        self.game_is_active = True
        self.game_stats.reset_stats()
        self.aliens = self._create_aliens()
        self.bullets.clear()
        self.ship.rect.midbottom = self.screen.get_rect().midbottom
        self.alien_vertical_velocity = self.settings.alien_vertical_velocity

    def _load_next_level(self):
        self.ship.rect.midbottom = self.screen.get_rect().midbottom
        self.bullets.clear()
        self.aliens = self._create_aliens()
        self.game_stats.player_number_of_special_bullets = self.settings.player_number_of_special_bullets
        self.alien_vertical_velocity += 1
        pygame.time.delay(500)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()