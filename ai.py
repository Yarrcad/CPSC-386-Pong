import pygame
from pygame.sprite import Sprite


class Ai(Sprite):

    def __init__(self, settings, screen):
        """Initialize the ai, and set its starting position."""
        super(Ai, self).__init__()
        self.screen = screen
        self.color = settings.player_color
        self.settings = settings

        # Get the ai's rect.
        self.rectA = pygame.Rect(settings.screen_width * (1/10), settings.screen_height/2 - settings.playerA_height/2,
                                 settings.playerA_width, settings.playerA_height)
        self.rectB1 = pygame.Rect(settings.screen_width * (1 / 4) - settings.playerB_width/2, 25,
                                  settings.playerB_width, settings.playerB_height)
        self.rectB2 = pygame.Rect(settings.screen_width * (1 / 4) - settings.playerB_width/2,
                                  settings.screen_height - 35, settings.playerB_width, settings.playerB_height)
        self.screen_rect = screen.get_rect()

    def reset(self, settings):
        # Reset the ai's position.
        self.rectA.x = settings.screen_width * (1 / 10)
        self.rectA.y = settings.screen_height / 2 - settings.playerA_height / 2
        self.rectB1.x = settings.screen_width * (1 / 4) - settings.playerB_width / 2
        self.rectB1.y = 25
        self.rectB2.x = settings.screen_width * (1 / 4) - settings.playerB_width / 2
        self.rectB2.y = settings.screen_height - 35

    def update(self, ball):
        """Update the ai's position based on the ball's position."""
        # Update the ai's location.
        if self.rectA.centery < ball.posy and self.rectA.bottom < self.rectB2.top:
            self.rectA.y += self.settings.mov_aispeed
        elif self.rectA.centery > ball.posy and self.rectA.top > self.rectB1.bottom:
            self.rectA.y -= self.settings.mov_aispeed
        if self.rectB1.centerx < ball.posx and \
                self.rectB1.x < self.settings.screen_width/2 - self.settings.playerB_width:
            self.rectB1.x += self.settings.mov_aispeed
            self.rectB2.x += self.settings.mov_aispeed
        elif self.rectB1.centerx > ball.posx and self.rectB1.left > self.rectA.right:
            self.rectB1.x -= self.settings.mov_aispeed
            self.rectB2.x -= self.settings.mov_aispeed

    def draw_ai(self):
        """Draw the ai to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rectA)
        pygame.draw.rect(self.screen, self.color, self.rectB1)
        pygame.draw.rect(self.screen, self.color, self.rectB2)
