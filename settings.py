
class Settings:
    
    def __init__(self):
        self.title = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.fps = 60
        self.ship_velocity = 5
        self.bullet_velocity = 5
        self.alien_vertical_velocity = 0
        self.bullet_color = (255, 0, 0)#red
        self.alien_init_pos = (120, 80)
        self.horizontal_distance_between_aliens = 120
        self.vertical_distance_between_aliens = 80
        self.number_of_aliens = 24
        self.number_of_aliens_per_row = 8
        self.player_lifes = 5

    # Tabla de cocientes y restos para números del 0 al 23 divididos entre 8:
    # Número | Cociente (//) | Resto (%)
    # ----------------------------------
    #   0    |      0        |    0
    #   1    |      0        |    1
    #   2    |      0        |    2
    #   3    |      0        |    3
    #   4    |      0        |    4
    #   5    |      0        |    5
    #   6    |      0        |    6
    #   7    |      0        |    7
    #   8    |      1        |    0
    #   9    |      1        |    1
    #  10    |      1        |    2
    #  11    |      1        |    3
    #  12    |      1        |    4
    #  13    |      1        |    5
    #  14    |      1        |    6
    #  15    |      1        |    7
    #  16    |      2        |    0
    #  17    |      2        |    1
    #  18    |      2        |    2
    #  19    |      2        |    3
    #  20    |      2        |    4
    #  21    |      2        |    5
    #  22    |      2        |    6
    #  23    |      2        |    7
    #
    # Los cocientes vienen a el numero de fila en la que debe aparecer un alien
    # El residuo es la posicion horizontal del alien en la fila