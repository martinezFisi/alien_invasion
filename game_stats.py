
import pygame

class GameStats:
    """ Track statistics for Alien Invasion. """

    def __init__(self, game):
        self.game = game
        self.game_screen = game.screen

        self.lifes = game.player_lifes
        self.best_history_score = 0
        self.score = 0

        self.life_image = pygame.transform.scale(pygame.image.load('images/ship.bmp'), (30,24))
        self.life_image_rect = self.life_image.get_rect()
        self.life_image_rect.x = 10
        self.life_image_rect.y = 10

        self.font = pygame.font.SysFont(None, 30)

    def blitme(self):
        """ Draw stats to the screen."""
        self._blit_lifes()
        self._blit_scores()

    def _blit_lifes(self):
        for i in range(0, self.lifes):
            rect = self.life_image_rect.copy()
            rect.x = self.life_image_rect.x + 40*i
            self.game_screen.blit(self.life_image, rect)

    def _blit_scores(self):
        img = self.font.render(f'{self.score}', True, (255,0,0))
        self.game_screen.blit(img, (self.game.settings.screen_width/2 - 40, 15))

        img2 = self.font.render(f'{self.best_history_score}', True, (255,0,0))
        self.game_screen.blit(img2, (self.game.settings.screen_width - 80, 15))
    
    def reset_stats(self):
        self.best_history_score = max(self.best_history_score, self.score)
        self.lifes = self.game.player_lifes
        self.score = 0