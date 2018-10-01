import pygame
from settings import Settings
from player import Player
from ai import Ai
from ball import Ball
from scoreboard import Scorebord
from button import Button
from audio import Audio
import functions as func


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Pong")

    play_button = Button(settings, screen, "Play")
    player = Player(settings, screen)
    ball = Ball(settings, screen)
    ai = Ai(settings, screen)
    audio = Audio()
    sb = Scorebord(settings, screen, audio)

    # Start the main loop for the game.
    while True:
        func.check_events(player, settings, ai, play_button, audio, ball)
        if settings.game_active:
            func.updates(player, ai, ball, settings)
        func.update_screen(settings, screen, player, ball, ai, sb, play_button, audio)
        pygame.time.Clock().tick(settings.game_speed)


run_game()
