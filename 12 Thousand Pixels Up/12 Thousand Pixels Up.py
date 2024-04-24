# Game made by Jed Krause
import sys
import os
import pygame
from pygame import mixer
from PlayerYes import player
from GroundYes import ground
from EnemyYes import enemy
from BirdYes import bird
from LavaYes import lava
from BackgroundYes import background
from VictoryYes import victory

"""
SETUP section - preparing everything before the main loop runs
"""

pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
text1 = pygame.font.SysFont("Arial", 35)
text2 = pygame.font.SysFont("Inconsolata", 35)
text3 = pygame.font.SysFont("Times New Roman", 45)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Game Variables
music = mixer.Sound(os.path.join(os.path.dirname(__file__), "Shiny_Tech.ogg")) # Game Music
death_sound = mixer.Sound(os.path.join(os.path.dirname(__file__), "AH.ogg"))
victory_sound = mixer.Sound(os.path.join(os.path.dirname(__file__), "WOOO.ogg"))
playDeath_sound = True
playVictory_sound = True
playMusic = True
platform_rightness = 0
Lava = []
lava_index = 0
scroll_threshold = 400
scroll = 0
collision_offset = 25
birdslist = []
bird_height = 200
bird_direction = 6
enemieslist = []
gameOver = False
won = False
enemy_platform_offset = 50 # This variable prevents the goomba-like enemies from walking on air
enemy_sprite_offset = 38 # This variable moves the enemies up a bit so they are actually stadning on the ground
platform_index = 0
canIncrease = True
distance_from_top = 12000 # This variable will tell the player how far they needed to travel to win if they die
gameStart = False

# Create sprites and sprite group
Player1 = player()
for i in range(20):
    Lava.append(lava(platform_rightness, 750, 50, 250))
    platform_rightness += 50

# Set up PLatform creator function so I can call it
# Easy platforms
Ground1 = ground(250, 500, 250, 50)
Ground2 = ground(500, 300, 250, 50)
Ground3 = ground(900, 100, 250, 50)
Ground4 = ground(500, -100, 250, 50)
Ground5 = ground(400, -300, 250, 50)
Ground6 = ground(300, -500, 250, 50)
Ground7 = ground(600, -700, 250, 50)
Ground8 = ground(200, -900, 250, 50)
Ground9 = ground(500, -1100, 250, 50)
Ground10 = ground(400, -1300, 250, 50)
Ground11 = ground(650, -1500, 250, 50)
Ground12 = ground(400, -1700, 250, 50)
Ground13 = ground(400, -1900, 250, 50)
Ground14 = ground(530, -2100, 250, 50)
Ground15 = ground(300, -2300, 250, 50)
Ground16 = ground(600, -2500, 250, 50)
Ground17 = ground(249, -2700, 250, 50)
Ground18 = ground(500, -2900, 250, 50)
Ground19 = ground(750, -3100, 250, 50)
Ground20 = ground(360, -3300, 250, 50)

# Medium platforms
Ground21 = ground(250, -3500, 125, 50)
Ground22 = ground(500, -3700, 125, 50)
Ground23 = ground(700, -3900, 125, 50)
Ground24 = ground(500, -4100, 125, 50)
Ground25 = ground(400, -4300, 125, 50)
Ground26 = ground(300, -4500, 125, 50)
Ground27 = ground(600, -4700, 125, 50)
Ground28 = ground(300, -4900, 125, 50)
Ground29 = ground(500, -5100, 125, 50)
Ground30 = ground(400, -5300, 125, 50)
Ground31 = ground(650, -5500, 125, 50)
Ground32 = ground(400, -5700, 125, 50)
Ground33 = ground(400, -5900, 125, 50)
Ground34 = ground(530, -6100, 125, 50)
Ground35 = ground(300, -6300, 125, 50)
Ground36 = ground(600, -6500, 125, 50)
Ground37 = ground(300, -6700, 125, 50)
Ground38 = ground(500, -6900, 125, 50)
Ground39 = ground(750, -7100, 125, 50)
Ground40 = ground(500, -7300, 125, 50)

# Difficult platforms
Ground41 = ground(250, -7500, 75, 50)
Ground42 = ground(500, -7700, 75, 50)
Ground43 = ground(700, -7900, 75, 50)
Ground44 = ground(500, -8100, 75, 50)
Ground45 = ground(400, -8300, 75, 50)
Ground46 = ground(300, -8500, 75, 50)
Ground47 = ground(600, -8700, 75, 50)
Ground48 = ground(400, -8900, 75, 50)
Ground49 = ground(500, -9100, 75, 50)
Ground50 = ground(400, -9300, 75, 50)
Ground51 = ground(650, -9500, 75, 50)
Ground52 = ground(400, -9700, 75, 50)
Ground53 = ground(400, -9900, 75, 50)
Ground54 = ground(530, -10100, 75, 50)
Ground55 = ground(300, -10300, 75, 50)
Ground56 = ground(600, -10500, 75, 50)
Ground57 = ground(400, -10700, 75, 50)
Ground58 = ground(500, -10900, 75, 50)
Ground59 = ground(750, -11100, 75, 50)
Ground60 = ground(500, -11300, 75, 50)

platformslist = [Ground1, Ground2, Ground3, Ground4, Ground5,
Ground6, Ground7, Ground8, Ground9, Ground10,
Ground11, Ground12, Ground13, Ground14, Ground15, 
Ground16, Ground17, Ground18, Ground19, Ground20, 
Ground21, Ground22, Ground23, Ground24, Ground25,
Ground26, Ground27, Ground28, Ground29, Ground30,
Ground31, Ground32, Ground33, Ground34, Ground35,
Ground36, Ground37, Ground38, Ground39, Ground40,
Ground41, Ground42, Ground43, Ground44, Ground45,
Ground46, Ground47, Ground48, Ground49, Ground50,
Ground51, Ground52, Ground53, Ground54, Ground55,
Ground56, Ground57, Ground58, Ground59, Ground60]

#Function to create text
def Write(text, font, colour, x, y):
    writing = font.render(text, True, colour)
    screen.blit(writing, (x, y))

# Create game objects like enemies and the victory zone
for i in range(8):
    enemieslist.append(enemy(platformslist[platform_index].rect.x, platformslist[platform_index].rect.y - enemy_sprite_offset, platform_index))
    platform_index += 5
for i in range(59):
    birdslist.append(bird(500, bird_height, 50, 50, bird_direction))
    bird_height -= 200
    bird_direction *= -1

Background = background(SCREEN_WIDTH, SCREEN_HEIGHT)
Victory = victory(250, -12000, 500, 500)

# Sprite groups
playersprites = pygame.sprite.Group(Player1)
lavasprites = pygame.sprite.Group(Lava)
groundsprites = pygame.sprite.Group(platformslist)
enemysprites = pygame.sprite.Group(enemieslist, birdslist)
backgroundsprites = pygame.sprite.Group(Background)
victorysprites = pygame.sprite.Group(Victory)

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                gameStart = True

    if gameStart == True:
        
        if playMusic == True:
            music.play()
            playMusic = False
        
        # Keyboard events
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            Player1.Move(-1)
        if keys_pressed[pygame.K_RIGHT]:
            Player1.Move(1)
        if keys_pressed[pygame.K_SPACE]:
                Player1.Jump()
        if keys_pressed[pygame.K_x] and gameOver == True or keys_pressed[pygame.K_x] and won == True: # If the player is dead or won and they restart
            # Reset the game when they restart
            gameOver = False
            won = False
            scroll = 0
            Player1 = player()
            playersprites = pygame.sprite.Group(Player1)
            playersprites.draw(screen)
            music.play()
            for lava in Lava:
                lava.rect.y = 750
            playDeath_sound = True
            playVictory_sound = True
            Player1.canJump = False  
            platform_index = 0  
            distance_from_top = 12000 
            for platform in groundsprites:
                platform.rect.y -= platform.total_scroll
                platform.total_scroll = 0
            for foe in enemieslist:
                foe.rect.y -= foe.total_scroll
                foe.rect.x = foe.x + 1
                foe.total_scroll = 0
            for foe in birdslist:
                foe.rect.y -= foe.total_scroll
                foe.rect.x = 500
                foe.total_scroll = 0
            Victory.rect.y -= Victory.total_scroll
            Victory.total_scroll = 0
        if keys_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        """
        UPDATE section - manipulate everything on the screen
        """   

        # Check for collision
        for sprite in groundsprites:
            if Player1.rect.colliderect(sprite):
                if abs(sprite.rect.right - Player1.rect.left) < collision_offset: #Check collision with right
                    Player1.rect.left = sprite.rect.right
                    Player1.rect.y += 1
                if abs(sprite.rect.left - Player1.rect.right) < collision_offset: #Check collision with left
                    Player1.rect.right = sprite.rect.left
                    Player1.rect.y += 1
                if abs(sprite.rect.top - Player1.rect.bottom) < collision_offset: #Check collision with top
                    Player1.rect.bottom = sprite.rect.top
                if abs(sprite.rect.bottom - Player1.rect.top) < collision_offset: #Check collision with bottom
                    Player1.rect.top = sprite.rect.bottom
                if Player1.y_velocity > 0:
                    Player1.y_velocity = 0
                    Player1.canJump = True
        
        for sprite in enemysprites:
            if pygame.sprite.collide_rect(Player1, sprite):
                Player1.kill()
                Player1.canJump = False
                if playDeath_sound == True:
                    death_sound.play()
                    playDeath_sound = False
                gameOver = True
        
        for sprite in lavasprites:
            if pygame.sprite.collide_rect(Player1, sprite):
                Player1.kill()
                Player1.canJump = False
                if playDeath_sound == True:
                    death_sound.play()
                    playDeath_sound = False
                gameOver = True
        
        # Check if player falls off screen and kill them so they don't stay alive if they are too far down
        if Player1.rect.y > SCREEN_HEIGHT:
            Player1.kill()
            Player1.canJump = False
            if playDeath_sound == True:
                    death_sound.play()
                    playDeath_sound = False
            gameOver = True
        
        # Check if player won by reaching the top
        if pygame.sprite.collide_rect(Player1, Victory):
            Player1.kill()
            Player1.canJump = False
            playDeath_sound = False
            if playVictory_sound == True:
                victory_sound.play()
                playVictory_sound = False
            won = True

        # Move things down when players moves up if they are jumping to simulate scrolling and moving
        if Player1.rect.top <= scroll_threshold:
            if Player1.y_velocity < 0:
                scroll = -Player1.y_velocity
                Player1.Scroll(scroll)
                for sprite in groundsprites:
                    sprite.Scroll(scroll)
                for sprite in enemysprites:
                    sprite.Scroll(scroll)
                for sprite in lavasprites:
                    sprite.Scroll(scroll)
                Victory.Scroll(scroll)
                distance_from_top -= scroll
            
        Player1.Update()
        Player1.ApplyGravity()
        for i in range(20):
            Lava[lava_index].update()
            lava_index += 1
            if lava_index > 19:
                lava_index = 0
        for enemy in enemieslist:
            enemy.Update(platformslist[enemy.native_index].rect.right - enemy_platform_offset, platformslist[enemy.native_index].rect.left)
        for bird in birdslist:
            bird.Update()

        """
        DRAW section - make everything show up on screen
        """

        screen.fill(BLACK)  # Fill the screen with one colour
        backgroundsprites.draw(screen)
        victorysprites.draw(screen)
        playersprites.draw(screen)
        groundsprites.draw(screen)
        enemysprites.draw(screen)
        lavasprites.draw(screen)
        if gameOver == True:
            screen.fill(BLACK) 
            Write("YOU FAILED, PRESS X TO TRY AGAIN", text1, WHITE, 240, 300)
            Write("PIXELS TRAVELLED: " + str(Ground1.total_scroll), text2, WHITE, 350, 400)
            Write("DISTANCE FROM TOP: " + str(distance_from_top), text2, WHITE, 350, 500)
            music.stop()
        if won == True:
            screen.fill(WHITE) 
            Write("YOU WON, PRESS X TO PLAY AGAIN", text1, BLACK, 250, 400)
            music.stop()

        pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
        clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
    
    else:
        screen.fill(BLACK)
        Write("12 THOUSAND PIXELS UP", text3, WHITE, 250, 300)
        Write("PRESS Z TO BEGIN, ESC TO QUIT", text1, WHITE, 275, 400)
        Write("CONTROLS:", text1, WHITE, 275, 500)
        Write("LEFT ARROW = MOVE LEFT", text1, WHITE, 275, 550)
        Write("RIGHT ARROW = MOVE RIGHT", text1, WHITE, 275, 600)
        Write("SPACE = JUMP", text1, WHITE, 275, 650)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
        clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
