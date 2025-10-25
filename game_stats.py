
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

        self.player_number_of_special_bullets = game.player_number_of_special_bullets
        self.special_bullet_rect = pygame.Rect( 10, game.screen.get_size()[1] - 20, 20, 5)

    def blitme(self):
        """ Draw stats to the screen."""
        self._blit_lifes()
        self._blit_scores()
        self._blit_special_bullets()

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
    
    def _blit_special_bullets(self):
        for i in range(0, self.player_number_of_special_bullets):
            rect = self.special_bullet_rect.copy()
            rect.x = self.special_bullet_rect.x + 30*i
            pygame.draw.rect(self.game_screen, (255, 0, 0), rect)

    def reset_stats(self):
        self.best_history_score = max(self.best_history_score, self.score)
        self.lifes = self.game.player_lifes
        self.score = 0
        self.player_number_of_special_bullets = self.game.player_number_of_special_bullets