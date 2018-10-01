import sys
import random
import pygame


def check_keydown_events(event, player):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_UP:
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        player.moving_down = True


def check_keyup_events(event, player):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = False


def check_play_button(settings, ai, player, mouse_x, mouse_y, play_button, audio, ball):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not settings.game_active:
        # Reset the audio.
        audio.play()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        settings.ai_score = 0
        settings.player_score = 0
        settings.game_active = True

        # Reset the player, ai and ball settings.
        ai.reset(settings)
        player.reset(settings)
        ball.reset(settings)


def check_events(player, settings, ai, play_button, audio, ball):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, ai, player, mouse_x, mouse_y, play_button, audio, ball)


def updates(player, ai, ball, settings):
    """Update the player and ai"""
    ball.update(settings)
    player.update()
    ai.update(ball)


def update_screen(settings, screen, player, ball, ai, sb, play_button, audio):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(settings.black)

    # Draw the dashed center line.
    coords = 32
    while coords < settings.screen_height - 32:
        pygame.draw.line(screen, settings.color, (settings.screen_width / 2, coords),
                         (settings.screen_width / 2, coords + 10), 1)
        coords += 20

    # Draw the player, ai and ball
    check_ball_collisions(ball, player, ai, settings, audio)
    ball.draw_ball()
    player.draw_player()
    ai.draw_ai()
    sb.draw_scores()

    # Draw the play button and title if the game is inactive
    if not settings.game_active:
        play_button.draw_button()
        if settings.player_score != settings.max_score and settings.ai_score != settings.max_score:
            font = pygame.font.SysFont(None, 48)
            title_width, title_height = font.size("Pong")
            title = font.render(str("Pong"), 1, settings.color)
            instruc_width, instruc_height = font.size("AI – NO WALLS")
            instruc = font.render(str("AI – NO WALLS"), 1, settings.color)
            screen.blit(title, (settings.screen_width / 2 - title_width / 2, settings.screen_height * 1 / 4))
            screen.blit(instruc, (settings.screen_width / 2 - instruc_width / 2,
                                  settings.screen_height * 1 / 4 + instruc_height + 10))
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def check_ball_collisions(ball, player, ai, settings, audio):
    """Respond to ball collisions"""
# Change ball direction if collision occurs.
    ball.right = ball.posx + ball.size
    ball.left = ball.posx - ball.size
    ball.top = ball.posy - ball.size
    ball.bottom = ball.posy + ball.size
    if (player.rectB1.left <= ball.right <= player.rectB1.right
            or player.rectB1.left <= ball.left <= player.rectB1.right):
        if player.rectB1.top <= ball.top <= player.rectB1.bottom:
            if abs(ball.posx - player.rectB1.x) / settings.playerB_width * 10 > 5:
                settings.ball_xspeed = 3
            elif abs(ball.posx - player.rectB1.x) / settings.playerB_width * 10 > 0:
                settings.ball_xspeed = 2
            elif abs(ball.posx - player.rectB1.x) / settings.playerB_width * 10 == 0:
                settings.ball_xspeed = 1
            ball.movey = 1
            if random.randint(0, 1) == 1:
                audio.bing.play()
            else:
                audio.bong.play()
            if ball.posx < player.rectB1.centerx:
                ball.movex = 0
            elif ball.posx > player.rectB1.centerx:
                ball.movex = 1
            elif ball.posx == player.rectB1.centerx:
                ball.movex = random.randint(0, 1)
        elif player.rectB2.bottom >= ball.bottom >= player.rectB2.top:
            if abs(ball.posx - player.rectB2.x) / settings.playerB_width * 10 > 5:
                settings.ball_xspeed = 3
            elif abs(ball.posx - player.rectB2.x) / settings.playerB_width * 10 == 0:
                settings.ball_xspeed = 1
            elif abs(ball.posx - player.rectB2.x) / settings.playerB_width * 10 > 0:
                settings.ball_xspeed = 2
            ball.movey = 0
            if random.randint(0, 1) == 1:
                audio.bing.play()
            else:
                audio.bong.play()
            if ball.posx < player.rectB1.centerx:
                ball.movex = 0
            elif ball.posx > player.rectB1.centerx:
                ball.movex = 1
            elif ball.posx == player.rectB1.centrx:
                ball.movex = random.randint(0, 1)
    if (ai.rectB1.left <= ball.right <= ai.rectB1.right
            or ai.rectB1.left <= ball.left <= ai.rectB1.right):
        if ai.rectB1.top <= ai.rectB1.top <= ball.top <= ai.rectB1.bottom:
            if abs(ball.posx - ai.rectB1.x) / settings.playerB_width * 10 > 5:
                settings.ball_xspeed = 3
            elif abs(ball.posx - ai.rectB1.x) / settings.playerB_width * 10 > 0:
                settings.ball_xspeed = 2
            elif abs(ball.posx - ai.rectB1.x) / settings.playerB_width == 0:
                settings.ball_xspeed = 1
            ball.movey = 1
            if random.randint(0, 1) == 1:
                audio.bing.play()
            else:
                audio.bong.play()
            if ball.posx < ai.rectB1.centerx:
                ball.movex = 0
            elif ball.posx > ai.rectB1.centerx:
                ball.movex = 1
            elif ball.posx == ai.rectB1.centerx:
                ball.movex = random.randint(0, 1)
        elif ai.rectB2.bottom >= ball.bottom >= ai.rectB2.top:
            if abs(ball.posx - ai.rectB2.x) / settings.playerB_width * 10 > 5:
                settings.ball_xspeed = 3
            elif abs(ball.posx - ai.rectB2.x) / settings.playerB_width * 10 > 0:
                settings.ball_xspeed = 2
            elif abs(ball.posx - ai.rectB2.x) / settings.playerB_width == 0:
                settings.ball_xspeed = 1
            ball.movey = 0
            if random.randint(0, 1) == 1:
                audio.bing.play()
            else:
                audio.bong.play()
            if ball.posx < ai.rectB1.centerx:
                ball.movex = 0
            elif ball.posx > ai.rectB1.centerx:
                ball.movex = 1
            elif ball.posx == ai.rectB1.centerx:
                ball.movex = random.randint(0, 1)
    if (player.rectA.top <= ball.bottom <= player.rectA.bottom
            or player.rectA.top <= ball.top <= player.rectA.bottom):
        if player.rectA.right >= ball.right >= player.rectA.left:
            if abs(ball.posy - player.rectA.y) / settings.playerB_width * 10 > 5:
                settings.ball_yspeed = 3
            elif abs(ball.posy - player.rectA.y) / settings.playerB_width * 10 > 0:
                settings.ball_yspeed = 2
            elif abs(ball.posy - player.rectA.y) / settings.playerB_width * 10 == 0:
                settings.ball_yspeed = 1
            ball.movex = 0
            if random.randint(0, 1) == 1:
                audio.bing.play()
            else:
                audio.bong.play()
            if ball.posy > player.rectA.centery:
                ball.movey = 1
            elif ball.posy < player.rectA.centery:
                ball.movey = 0
            elif ball.posy == player.rectA.centery:
                ball.movey = random.randint(0, 1)
    if (ai.rectA.top <= ball.bottom <= ai.rectA.bottom
            or ai.rectA.top <= ball.top <= ai.rectA.bottom):
        if ai.rectA.left <= ball.left <= ai.rectA.right:
            if abs(ball.posy - ai.rectA.y) / settings.playerB_width * 10 > 5:
                settings.ball_yspeed = 3
            elif abs(ball.posy - ai.rectA.y) / settings.playerB_width * 10 > 0:
                settings.ball_yspeed = 2
            elif abs(ball.posy - ai.rectA.y) / settings.playerB_width * 10 == 0:
                settings.ball_yspeed = 1
            ball.movex = 1
            if random.randint(0, 1) == 1:
                audio.bing.play()
            else:
                audio.bong.play()
            if ball.posy > ai.rectA.centery:
                ball.movey = 1
            elif ball.posy < ai.rectA.centery:
                ball.movey = 0
            elif ball.posy == ai.rectA.centery:
                ball.movey = random.randint(0, 1)
