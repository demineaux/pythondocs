#Import libraries
import pygame
import math
import colors
#Initialize the game engine
pygame.init()


#Defining Pi
PI = 3.141592653
#Setting window variables and size
display_width = 800
display_height = 600
size = (display_width, display_height)
screen = pygame.display.set_mode(size)
#Window Title
pygame.display.set_caption("animated square")
# --- Font definitions
font = pygame.font.SysFont('Calibri', 25, True, False)


#--- Game Object Definitions
def draw_tree(screen, x, y):
    pygame.draw.rect(screen, colors.BROWN, [60+x, 170+y, 30, 45])
    pygame.draw.polygon(screen, colors.GREEN, [[150+x,170+y],[75+x,20+y], [x,170+y]])
    pygame.draw.polygon(screen, colors.GREEN, [[140+x,120+y], [75+x,y], [10+x,120+y]])
    
def player1(screen, x, y):
    pygame.draw.rect(screen, colors.BLUE, [display_width/2 + x, display_height/2 + y, 30, 30])
    
def player2(screen, x, y):
    pygame.draw.polygon(screen, colors.PINK, [[350+x, 350+y], [337+x,325+y], [325+x,350+y]])
    

    


# Loop until the user clicks the close button.
done = False
 # Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Program Variables
background_image = pygame.image.load("bgspace1.jpg").convert()
background_position = [0, 0]
fuckImg = pygame.image.load('fuck.png')
p1_img = pygame.image.load("destructor.png")

x_speed = 0
y_speed = 0
x_coord = 10
y_coord = 10

x_speed2 = 0
y_speed2 = 0
x_coord2 = 40
y_coord2 = 10


p1pos = pygame.mouse.get_pos()

x = p1pos[0]
y = p1pos[1]

rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5

mouse1click_sound = pygame.mixer.Sound("laser5.ogg")
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    #Keyboard Event Loop
        #Moving player depending on key pressed and speed control
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            elif event.key == pygame.K_a:
                x_speed2 = -3
            elif event.key == pygame.K_d:
                x_speed2 = 3
            elif event.key == pygame.K_w:
                y_speed2 = -3
            elif event.key == pygame.K_s:
                y_speed2 = 3
        
        #Resetting movement to 0 upon key release        
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed2 = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
            elif  event.key == pygame.K_w or event.key == pygame.K_s:
                y_speed2 = 0
       
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse1click_sound.play()
        
        
        
    #Movement variables
    x_coord += x_speed
    y_coord += y_speed
    
    x_coord2 += x_speed2
    y_coord2 += y_speed2
    
                
    #Screen clear
    screen.fill(colors.BLACK)    
 
    # --- Drawing code should go here
    screen.blit(background_image, background_position)

    player1(screen, x_coord, y_coord)
    player2(screen, x_coord2, y_coord2)
    
    screen.blit(fuckImg, [rect_x, rect_y])
    
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    if rect_x > (display_width - 50) or rect_x < 0:
        rect_change_x = rect_change_x * -1
    if rect_y > (display_height - 50) or rect_y < 0:
        rect_change_y = rect_change_y * -1   
        
    screen.blit(p1_img, [x, y])
    p1_img.set_colorkey(colors.BLACK)
        

    
    
    # --- Screen draw update
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
    

#Program shutdown
pygame.quit()
