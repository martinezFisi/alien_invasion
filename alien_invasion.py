import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        
        pygame.init()

        self.settings = Settings()
        dimensions = (self.settings.screen_width, self.settings.screen_height)
        title = self.settings.title
        screen = pygame.display.set_mode(dimensions)
        background_color = self.settings.bg_color
        clock = pygame.time.Clock()
        ship_velocity = self.settings.ship_velocity

        self._set_title(title)
        self.screen = screen
        self.background_color = background_color
        self.clock = clock
        self.ship_velocity = ship_velocity

        self.ship = Ship(self)

    def run_game(self):
        while True:

            self._check_events()
            self.ship.update()
            self._update_screen()

            self.clock.tick(self.settings.fps)  # Control the frame rate

    def _set_title(self, title):
        pygame.display.set_caption(title)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.background_color)
        self.ship.blitme()
        pygame.display.flip() # Update the full display surface to the screen

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()