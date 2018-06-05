#Import libraries
import pygame
import math
#Initialize the game engine
pygame.init()
#Defining colors
BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
GREEN   = (  0, 255,   0)
RED     = (255,   0,   0)
BLUE    = (  0,   0, 255)
#Defining Pi
PI = 3.141592653
#Setting window variables and size
display_width = 800
display_height = 600
size = (display_width, display_height)
screen = pygame.display.set_mode(size)
#Setting window title
pygame.display.set_caption("test_game")
# --- Font definitions
font = pygame.font.SysFont('Calibri', 25, True, False)



# Loop until the user clicks the close button.
done = False
 # Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    #Program event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")   
            
    #Screen clear
    screen.fill(WHITE)    
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 5)
    pygame.draw.polygon(screen, BLACK, [[100, 100], [40, 200], [200, 200]], 5)
    
    text1 = font.render("Hello everyone, I am here!", True, BLACK)
    screen.blit(text1, [250, 250])
    screen.blit(text1, [500, 225])
    
    #--score = input("pick a score lol ")
    #--toptext = font.render("score: " +str(score), True, RED)
    #--screen.blit(toptext, [100, 400])

    name = font.render(input("Enter your name:"), True, BLACK)
    screen.blit(name, [400, 300])
 
 
    # --- Screen draw update
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    

#Program shutdown
pygame.quit()
