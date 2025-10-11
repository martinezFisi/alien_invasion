
import pygame

class Ship:
    
    def __init__(self, game):
        self.game = game
        self.game_screen = game.screen
        self.game_screen_rect = game.screen.get_rect()

        #rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #init position
        self.rect.midbottom = self.game_screen_rect.midbottom

        #velocity
        self.velocity = game.ship_velocity

    def blitme(self):
        self.game_screen.blit(self.image, self.rect)

    def update(self):
        
        keys = pygame.key.get_pressed() # return a tuple with all keys

        if keys[pygame.K_RIGHT] and (self.rect.x + self.rect.width < self.game_screen_rect.width):
            self.rect.x += self.velocity
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocity