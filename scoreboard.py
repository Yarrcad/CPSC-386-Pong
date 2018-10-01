import pygame.font


class Scorebord:
    """A class to report scoring information"""

    def __init__(self, settings, screen, audio):
        """Initialize scorekeeping attributes"""
        self.settings = settings
        self.screen = screen
        self.audio = audio

        # Font settings for scoring information.
        self.font = pygame.font.SysFont(None, 48)
        self.font2 = pygame.font.SysFont(None, 24)

    def draw_scores(self):
        """Turn the player's score into a rendered image and ends the game"""

        if self.settings.ai_score != self.settings.max_score and self.settings.player_score != self.settings.max_score:
            # Create Score image
            score_pimage = self.font.render(str(self.settings.player_score), 1, self.settings.color)
            score_aiimage = self.font.render(str(self.settings.ai_score), 1, self.settings.color)
            score_maximage = self.font2.render("Max Score: " + str(self.settings.max_score), 1, self.settings.color)

            # Draw Scores
            self.screen.blit(score_pimage, (self.settings.screen_width/2 + self.settings.screen_width/10,
                                            self.settings.screen_height * 1 / 20))
            self.screen.blit(score_aiimage,
                             (self.settings.screen_width/2 - self.settings.screen_width/10,
                              self.settings.screen_height * 1 / 20))
            self.screen.blit(score_maximage,
                             (self.settings.screen_width / 40,
                              self.settings.screen_height / 40))

        else:
            # Show the winner.

            if self.settings.player_score == self.settings.max_score:
                if self.settings.game_active:
                    self.audio.congratulations.play()
                winner = self.font.render(str("PLAYER WINS!!!"), 1, self.settings.color)
                text_width, text_height = self.font.size("PLAYER WINS!!!")
                self.screen.blit(winner, [self.settings.screen_width / 2 - text_width / 2,
                                          self.settings.screen_height * 1 / 4])
            elif self.settings.ai_score == self.settings.max_score:
                if self.settings.game_active:
                    self.audio.loser.play()
                winner = self.font.render(str("AI WINS :'("), 1, self.settings.color)
                text_width, text_height = self.font.size("AI WINS :'(")
                self.screen.blit(winner, [self.settings.screen_width / 2 - text_width / 2,
                                          self.settings.screen_height * 1 / 4])

            # Show the mouse cursor.
            pygame.mouse.set_visible(True)

            # Stop the game.
            self.settings.game_active = False
