import pygame
import random
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, settings, screen):
        """Initialize the ball, and set its starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.color = settings.player_color
        self.size = settings.ball_size
        self.settings = settings

        # Set the ball's position.
        self.posx = settings.screen_width // 2
        self.posy = settings.screen_height // 2

        # Starting movement flags (0 is left/up and 1 is right/down).
        self.movex = random.randint(0, 1)
        self.movey = random.randint(0, 1)
        settings.ball_xspeed = random.randint(1, 2)
        settings.ball_yspeed = random.randint(0, 2)

    def update(self, settings):
        """Update the ball's position, based on movement flags."""
        # Update the circles speed and direction.
        if self.movey == 0 and self.posy > 0:
            self.posy -= self.settings.ball_yspeed
        if self.movey == 1 and self.posy < self.settings.screen_height - self.settings.ball_size:
            self.posy += self.settings.ball_yspeed
        if self.movex == 0 and self.posx > 0:
            self.posx -= self.settings.ball_xspeed
        if self.movex == 1 and self.posx < self.settings.screen_width - self.settings.ball_size:
            self.posx += self.settings.ball_xspeed

        # Check for out of bounds.
        if self.posy <= 25 or self.posy >= settings.screen_height - 25 or self.posx <= 25\
                or self.posx >= settings.screen_width - 25:
            if self.posx >= settings.screen_width/2:
                self.settings.ai_score += 1
                self.movex = 0
            elif self.posx < settings.screen_width/2:
                self.settings.player_score += 1
                self.movex = 1
                settings.increase_speed()
            self.reset(settings)

    def reset(self, settings):
        # Reset the ball's position and speed.
        self.posy = settings.screen_height // 2
        self.posx = settings.screen_width // 2
        self.movey = random.randint(0, 1)
        settings.ball_xspeed = random.randint(1, 2)
        settings.ball_yspeed = random.randint(0, 2)

    def draw_ball(self):
        """Draw the ball to the screen."""
        pygame.draw.circle(self.screen, self.color, [self.posx, self.posy], self.size)
