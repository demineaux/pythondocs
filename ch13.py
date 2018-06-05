import pygame
import random
import math

pygame.init()

BLACK   = (  0,   0,   0)   
WHITE   = (255, 255, 255)
GREEN   = (  0, 255,   0)
RED     = (255,   0,   0)
BLUE    = (  0,   0, 255)
BROWN   = (165,  42,  42)
PINK    = (255, 182, 193)

pygame.display.set_caption("blocking blocks")


display_width = 800
display_height = 600
screen = pygame.display.set_mode([display_width, display_height])


class Block(pygame.sprite.Sprite):
    
    
    def __init__(self, color, width, height):
        super().__init__()
    
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
    
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
    
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > display_height:
            self.rect.y = random.randrange(-100, -10)
            self.rect.x = random.randrange(0, display_width)
            
        if self.rect.y > (display_height + 10):
            self.reset_pos()
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, display_width)

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15)
    block.rect.x = random.randrange(display_width)
    block.rect.y = random.randrange(display_height)
    block_list.add(block)
    all_sprites_list.add(block)
    
    
player = Block(RED, 20, 15)
all_sprites_list.add(player)



done = False
clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(WHITE)
    
    #--- Draw
    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in blocks_hit_list:
        score += 1
        print(score)
        block.reset_pos()
    
    all_sprites_list.draw(screen)
    block_list.update()
    
    #--- End Draw
    
    
    pygame.display.flip()

    clock.tick(60)
    
    
    
pygame.quit()