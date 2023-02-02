#Imports.
import pygame;
import random;

#Initialisation and set up. 
pygame.init();

#Window set-up.
windowHeight = 400;
windowWidth = 400;
window = pygame.display.set_mode((windowHeight, windowWidth));
pygame.display.set_caption('PyGame');
windowBorder = window.get_rect();

#Program loop.
runGame = True;
clock = pygame.time.Clock(); #Is used to control how fast the screen updates.

#Colour variables. 
black = (0, 0, 0);
white = (255, 255, 255);
red = (255, 0, 0);
blue = (0, 0, 255);
yellow = (255, 255, 0);
green = (0, 255, 0);
orange = (255, 102, 0);
purple = (123, 50, 150);

# Player Variables. 
playerWidth = 20;
playerHeight = 20;
playerXLocation = (windowHeight / 2) - playerHeight;
playerYLocation = (windowWidth / 2) - playerWidth;
playerSpeed = 5;
player = pygame.Rect(playerXLocation, playerYLocation, playerWidth, playerHeight);

#Colour-rects variables.
rectWidth = 40;
rectHeight = 40;

leftRectXLocation = 40;
leftRectYLocation = 40;

rightRectXLocation = 320;
rightRectYLocation = leftRectYLocation;

#Colour-rects
blueRect = pygame.Rect(leftRectXLocation, leftRectYLocation, rectWidth, rectHeight);
purpleRect = pygame.Rect(leftRectXLocation, leftRectYLocation + 120, rectWidth, rectHeight);
redRect = pygame.Rect(leftRectXLocation, leftRectYLocation + 240, rectWidth, rectHeight);
greenRect = pygame.Rect(rightRectXLocation, rightRectYLocation, rectWidth, rectHeight);
yellowRect = pygame.Rect(rightRectXLocation, rightRectYLocation + 120, rectWidth, rectHeight);
orangeRect = pygame.Rect(rightRectXLocation, rightRectYLocation + 240, rectWidth, rectHeight);

#Loop.
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False;
    
    #Key Handling. 
    keys = pygame.key.get_pressed()

    #Player Movement based on WASD movement seen in most games. 
    if keys[pygame.K_w]:
        player.y -= playerSpeed;
    
    if keys[pygame.K_s]:
        player.y += playerSpeed;

    if keys[pygame.K_a]:
        player.x -= playerSpeed;
    
    if keys[pygame.K_d]:
        player.x += playerSpeed;

    #Keeps the player within the screen. 
    player.clamp_ip(windowBorder);

    #Clears the screen to black. 
    window.fill(black);

    #Drawing stuff. 
    pygame.draw.rect(window, red, redRect);
    pygame.draw.rect(window, blue, blueRect);
    pygame.draw.rect(window, yellow, yellowRect);
    pygame.draw.rect(window, purple, purpleRect);
    pygame.draw.rect(window, orange, orangeRect);
    pygame.draw.rect(window, green, greenRect);

    #Default player sprite. 
    pygame.draw.rect(window, white, player);

    #Updating the player colour if it overlaps a coloured rectangle. 
    if player.colliderect(blueRect):
        pygame.draw.rect(window, blue, player);

    if player.colliderect(purpleRect):
        pygame.draw.rect(window, purple, player);

    if player.colliderect(redRect):
        pygame.draw.rect(window, red, player);

    if player.colliderect(greenRect):
        pygame.draw.rect(window, green, player);

    if player.colliderect(yellowRect):
        pygame.draw.rect(window, yellow, player);

    if player.colliderect(orangeRect):
        pygame.draw.rect(window, orange, player);

    #Updates the screen with what is drawn. 
    pygame.display.flip();

    #Limits to 60 frames per second. 
    clock.tick(60);

#Closes the game when the program exits the loop. 
pygame.quit;