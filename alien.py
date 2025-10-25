
import pygame

class Alien:

    count = 0

    def __init__(self, game, order):
        Alien.count += 1
        self.id = Alien.count
        self.game = game
        self.game_screen = game.screen
        self.game_screen_rect = game.screen.get_rect()
        self.init_pos = game.alien_init_pos
        self.horizontal_distance = game.horizontal_distance_between_aliens
        self.vertical_distance = game.vertical_distance_between_aliens
        self.order = order

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.topleft = self.init_pos
        # Calculate init position based on order in the fleet using division and module operations
        self.rect.x = self.rect.x + self.horizontal_distance*(self.order%self.game.number_of_aliens_per_row)
        self.rect.y = self.rect.y + self.vertical_distance*(self.order//self.game.number_of_aliens_per_row)

    def blitme(self):
        self.game_screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.game.alien_vertical_velocity

        if(self.rect.y + self.rect.height > self.game_screen_rect.height):#check if alien reached bottom of screen
            self.game.aliens.remove(self)

    def __eq__(self, other):
        if isinstance(other, Alien):
            return self.id == other.id
        return False 