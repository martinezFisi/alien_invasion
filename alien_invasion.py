import sys
import pygame

from operator import methodcaller

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        self.ship = Ship(self)
        self.bullets = []
        self.aliens = self._create_aliens()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.fps)  # Control the frame rate

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _update_screen(self):
        self.screen.fill(self.background_color)
        self.ship.blitme()
        list(map(methodcaller('blitme'), self.bullets))
        list(map(methodcaller('blitme'), self.aliens))
        pygame.display.flip() # Update the full display surface to the screen

    def _update_bullets(self):
        list(map(methodcaller('update'), self.bullets))

    def _fire_bullet(self):
        self.bullets.append(Bullet(self))
        print(f'Numero de bullets: {len(self.bullets)}')

    def _create_aliens(self):
        aliens = []
        for i in range(0, self.number_of_aliens):
            aliens.append(Alien(self, i))
        return aliens
    
    def _update_aliens(self):
        list(map(methodcaller('update'), self.aliens))
    
    def _check_collisions(self):
        for alien in self.aliens[:]:
            for bullet in self.bullets[:]:
                if bullet.rect.colliderect(alien.rect):
                    self.aliens.remove(alien)
                    self.bullets.remove(bullet)
            
            if self.ship.rect.colliderect(alien.rect):
                self.aliens.remove(alien)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()