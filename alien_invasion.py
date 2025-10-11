import sys
import pygame

from operator import methodcaller

from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.bullet_velocity = self.settings.bullet_velocity
        self.bullet_color = self.settings.bullet_color

        self.ship = Ship(self)
        self.bullets = []

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
        pygame.display.flip() # Update the full display surface to the screen

    def _update_bullets(self):
        list(map(methodcaller('update'), self.bullets))

    def _fire_bullet(self):
        self.bullets.append(Bullet(self))
        print(f'Numero de bullets: {len(self.bullets)}')


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()