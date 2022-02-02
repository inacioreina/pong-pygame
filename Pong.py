from tkinter import Variable
import pygame, sys

def ball_behaviour():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top >= screen_height or ball.bottom <= 0:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(player2):
        ball_speed_x *= -1

def player_input():
    global player_speed, player2_speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            #DEBUG
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player2_speed += 7
            if event.key == pygame.K_UP:
                player2_speed -= 7
            if event.key == pygame.K_s:
                player_speed += 7
            if event.key == pygame.K_w:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player2_speed -= 7
            if event.key == pygame.K_UP:
                player2_speed += 7
            if event.key == pygame.K_s:
                player_speed -= 7
            if event.key == pygame.K_w:
                player_speed += 7

                
        
                


#Setup
#Initiates pygame modules
pygame.init()
clock = pygame.time.Clock()

#Setup window size
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

#Window caption
pygame.display.set_caption('Pong')

#Setup play game actors
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
ball_speed_x = 7
ball_speed_y = 7

player_speed = 0
player2_speed = 0

player = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
player2 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

while True:
    #Handle input
    player_input()
    ball_behaviour()

    player.y += player_speed
    player2.y += player2_speed

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
 

    pygame.display.flip()
    clock.tick(60) #frames per second