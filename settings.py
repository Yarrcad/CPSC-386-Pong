class Settings:
    """A class to store all settings for Pong."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.black = (0, 0, 0)
        self.color = (255, 255, 255)

        # Player settings.
        self.playerA_width = 5
        self.playerA_height = 50
        self.playerB_width = 50
        self.playerB_height = 5
        self.player_color = self.color

        # Game settings.
        self.max_score = 15

        # Ball settings.
        self.ball_size = 5

        # How quickly the game speeds up.
        self.speedup_scale = 1

        """Initialize settings that change throughout the game"""
        # Set game speed.
        self.game_speed = 200
        self.ball_xspeed = 1
        self.ball_yspeed = 1
        self.mov_pspeed = 8
        self.mov_aispeed = 1

        # Scoring
        self.ai_score = 0
        self.player_score = 0

        self.game_active = False

    def increase_speed(self):
        """Increase ai speed."""
        if self.mov_aispeed < 2 and self.player_score >= 5:
            self.mov_aispeed += self.speedup_scale
