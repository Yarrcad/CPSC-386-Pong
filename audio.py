import pygame


class Audio:
    def __init__(self):
        # Create mixer for audio.
        pygame.mixer.init()
        self.bing = pygame.mixer.Sound("bing.wav")
        self.background = pygame.mixer.music.load("kv-leaf.mp3")
        self.bong = pygame.mixer.Sound("bong.wav")
        self.loser = pygame.mixer.Sound("loser.wav")
        pygame.mixer.Sound("congratulations.wav")

    @staticmethod
    def play():
        # Play background music.
        pygame.mixer_music.set_volume(.5)
        pygame.mixer.music.play()
