import pygame, sys, random
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
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

PLAYER_SPEED = 0
PLAYER2_SPEED = 0
AI_PLAYER_SPEED = 7

ai_player = True

player = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
player2 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

def ball_behaviour():
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    if ball.centerx >= screen_width or ball.centerx <= 0:
        ball_reset()

    if ball.top >= screen_height or ball.bottom <= 0:
        BALL_SPEED_Y *= -1

    if ball.colliderect(player) or ball.colliderect(player2):
        BALL_SPEED_X *= -1

def ball_reset():
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.center = (screen_width/2, screen_height/2)
    BALL_SPEED_X *= random.choice((1, -1))
    BALL_SPEED_Y *= random.choice((1, -1))

def player_input(bool: ai_player):
    global PLAYER_SPEED, PLAYER2_SPEED
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            #DEBUG
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        #Find a better way of doing this
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                PLAYER_SPEED += 7
            if event.key == pygame.K_w:
                PLAYER_SPEED -= 7
            if not ai_player:
                if event.key == pygame.K_DOWN:
                    PLAYER2_SPEED += 7
                if event.key == pygame.K_UP:
                    PLAYER2_SPEED -= 7
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                PLAYER_SPEED -= 7
            if event.key == pygame.K_w:
                PLAYER_SPEED += 7
            if not ai_player:
                if event.key == pygame.K_DOWN:
                    PLAYER2_SPEED -= 7
                if event.key == pygame.K_UP:
                    PLAYER2_SPEED += 7

    player.y += PLAYER_SPEED
    player2.y += PLAYER2_SPEED
    
    if player.top <= 0:
        player.top = 0
    if player. bottom >= screen_height:
        player.bottom = screen_height
    if player2.top <= 0:
        player2.top = 0
    if player2. bottom >= screen_height:
        player2.bottom = screen_height

def ai_player_behaviour():
    global AI_PLAYER_SPEED
    if ball.y > player2.top:
        player2.top += AI_PLAYER_SPEED
    if ball.y < player2.bottom:
        player2.bottom -= AI_PLAYER_SPEED


while True:
    #Handle input
    player_input(ai_player)
    ball_behaviour()
    if(ai_player):
        ai_player_behaviour()



    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
 

    pygame.display.flip()
    clock.tick(60) #frames per second