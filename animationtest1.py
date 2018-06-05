#Import libraries
import pygame
import math
#Initialize the game engine
pygame.init()

BLACK   = (  0,   0,   0)   
WHITE   = (255, 255, 255)
GREEN   = (  0, 255,   0)
RED     = (255,   0,   0)
BLUE    = (  0,   0, 255)
BROWN   = (165,  42,  42)
PINK    = (255, 182, 193)

#Defining Pi
PI = 3.141592653
#Setting window variables and size
display_width = 800
display_height = 600
size = (display_width, display_height)
screen = pygame.display.set_mode(size)
#Setting window title
pygame.display.set_caption("a fucking screensaver")
# --- Font definitions
font = pygame.font.SysFont('Calibri', 25, True, False)


#--- Game Object Definitions
def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, [60+x, 170+y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150+x,170+y],[75+x,20+y], [x,170+y]])
    pygame.draw.polygon(screen, GREEN, [[140+x,120+y], [75+x,y], [10+x,120+y]])


# Loop until the user clicks the close button.
done = False
 # Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Program Variables
rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5

fuckImg = pygame.image.load('fuck.png')

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
    screen.fill(BLACK)    
 
    # --- Drawing code should go here

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    
   
    screen.blit(fuckImg, [(rect_x * 2), (rect_y * 2)])
   
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    if rect_x > (display_width - 50) or rect_x < 0:
        rect_change_x = rect_change_x * -1
    if rect_y > (display_height - 50) or rect_y < 0:
        rect_change_y = rect_change_y * -1    

    # --- Screen draw update
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    

#Program shutdown
pygame.quit()
