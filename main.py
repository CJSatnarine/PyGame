#Imports.
import pygame;
import sys;

#Initialisation and set up. 
pygame.init();

#Window set-up.
windowHeight = 400;
windowWidth = 400;
window = pygame.display.set_mode((windowHeight, windowWidth));
pygame.display.set_caption('PyGame');

#Program loop.
runGame = True;
clock = pygame.time.Clock(); #Is used to control how fast the screen updates.

#Colour variables. 
black = (0, 0, 0);
white = (255, 255, 255);
green = (0, 255, 0);
red = (255, 0, 0);
blue = (0, 0, 255);
purple = (123, 50, 150);

# Player Variables. 
playerXLocation = 0;
playerYLocation = 0;
playerWidth = 20;
playerHeight = 20;
playerSpeed = 5;
player = pygame.Rect(playerXLocation, playerYLocation, playerWidth, playerHeight);

#Loop.
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False;
    
    #Key Handling. 
    keys = pygame.key.get_pressed()

    #Player Movement based on arrow keys. 
    if keys[pygame.K_w]:
        player.y -= playerSpeed;
    
    if keys[pygame.K_s]:
        player.y += playerSpeed;

    if keys[pygame.K_a]:
        player.x -= playerSpeed;
    
    if keys[pygame.K_d]:
        player.x += playerSpeed;

    #Drawing code. 
    #Clears the screen to black. 
    window.fill(black);

    #Drawing stuff. 
    pygame.draw.rect(window, purple, player);

    #Updates the screen with what is drawn. 
    pygame.display.flip();

    #Limits to 60 frames per second. 
    clock.tick(60);

#Closes the game when the program exits the loop. 
pygame.quit;