from entities import player
from entities import ball
from services import gameFont
import pygame

pygame.init()

clock = pygame.time.Clock()

screen_width, screen_height = 1280, 720

fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

in_game = True

game_fonts = gameFont.GameFont(screen, font_path='./game/assets/fonts/game_font.otf', font_size=64, font_color=(255, 255, 255))
p1 = player.Player(screen, x=0, y=screen_height/2, width=25, height=100, color=(0, 0, 255), speed=10)
p2 = player.Player(screen, x=screen_width-25, y=screen_height/2, width=25, height=100, color=(255, 0, 0), speed=10)
ball = ball.Ball(screen, x=screen_width/2-25, y=screen_height/2-25, width=25, height=25, color=(255,255,255), speed=10)

line_start = (screen_width // 2, 0)
line_end = (screen_width // 2, screen_height)
line_color = color=(255,255,255)
line_thickness = 5

score_p1 = 0
score_p2 = 0

ball_out_of_screen = False
last_reset_time = pygame.time.get_ticks()

while in_game:
    screen.fill((0, 0, 0))
    ball.move()

    for event in pygame.event.get():
        key = pygame.key.get_pressed()

        # Pour quitter le jeu
        if (event.type == pygame.QUIT):
            in_game = False

        # Mouvement du joueur 1
        if (key[pygame.K_z]):
            p1.move_up()
        if (key[pygame.K_s]):
            p1.move_down()

        # Mouvement du joueur 2
        if (key[pygame.K_KP_8]):
            p2.move_up()
        if (key[pygame.K_KP_2]):
            p2.move_down()

    game_fonts.display(score_p2,(screen_width/2+25,0))
    game_fonts.display(score_p1,(screen_width/2-50,0))
    pygame.draw.line(screen, line_color,line_start, line_end, line_thickness)
    p1.show()
    p2.show()
    ball.show()
    ball.collision(p1,p2)

    if ball.rect.right < 0:
        score_p2 += 1
        if not ball_out_of_screen:
            ball.change_position(x=screen_width/2-25, y=screen_height/2-25, width=25, height=25)
            ball.speed = 0
            ball.reset_movement()
            ball_out_of_screen = True
    elif ball.rect.left > screen_width:
        score_p1 += 1
        if not ball_out_of_screen:
            ball.change_position(x=screen_width/2-25, y=screen_height/2-25, width=25, height=25)
            ball.speed = 0
            ball.reset_movement()
            ball_out_of_screen = True
    else:
        ball_out_of_screen = False

    pygame.display.flip()

    clock.tick(fps)