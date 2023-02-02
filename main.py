#Imports.
import pygame;

#Initialisation and set up. 
pygame.init();

#Window variables
windowHeight = 400;
windowWidth = 400;

#Window set-up.
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
playerWidth = 10;
playerHeight = 10;
player = pygame.Rect(playerXLocation, playerYLocation, playerWidth, playerHeight);

#Loop.
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False;

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