
import pygame

class GameStats:

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

    def blitme(self):
        for i in range(0, self.lifes):
            rect = self.life_image_rect.copy()
            rect.x = self.life_image_rect.x + 40*i
            self.game_screen.blit(self.life_image, rect)