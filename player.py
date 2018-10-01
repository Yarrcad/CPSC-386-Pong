import pygame
from pygame.sprite import Sprite


class Player(Sprite):

    def __init__(self, settings, screen):
        """Initialize the player, and set its starting position."""
        super(Player, self).__init__()
        self.screen = screen
        self.color = settings.player_color
        self.settings = settings

        # Get the player's rect.
        self.rectA = pygame.Rect(settings.screen_width * (9/10),
                                 settings.screen_height/2 - settings.playerA_height/2, settings.playerA_width,
                                 settings.playerA_height)
        self.rectB1 = pygame.Rect(settings.screen_width * (3 / 4) - settings.playerB_width/2, 25,
                                  settings.playerB_width, settings.playerB_height)
        self.rectB2 = pygame.Rect(settings.screen_width * (3 / 4) - settings.playerB_width/2,
                                  settings.screen_height - 35, settings.playerB_width, settings.playerB_height)
        self.screen_rect = screen.get_rect()

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def reset(self, settings):
        # Reset the player's position.
        self.rectA.x = settings.screen_width * (9 / 10)
        self.rectA.y = settings.screen_height / 2 - settings.playerA_height / 2
        self.rectB1.x = settings.screen_width * (3 / 4) - settings.playerB_width / 2
        self.rectB1.y = 25
        self.rectB2.x = settings.screen_width * (3 / 4) - settings.playerB_width / 2
        self.rectB2.y = settings.screen_height - 35

    def update(self):
        """Update the player's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_up and self.rectA.top > self.rectB1.bottom:
            self.rectA.y -= self.settings.mov_pspeed
        if self.moving_down and self.rectA.bottom < self.rectB2.top:
            self.rectA.y += self.settings.mov_pspeed
        if self.moving_left and self.rectB1.x > self.settings.screen_width/2:
            self.rectB1.x -= self.settings.mov_pspeed
            self.rectB2.x -= self.settings.mov_pspeed
        if self.moving_right and self.rectB1.right < self.rectA.left:
            self.rectB1.x += self.settings.mov_pspeed
            self.rectB2.x += self.settings.mov_pspeed

    def draw_player(self):
        """Draw the player to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rectA)
        pygame.draw.rect(self.screen, self.color, self.rectB1)
        pygame.draw.rect(self.screen, self.color, self.rectB2)
