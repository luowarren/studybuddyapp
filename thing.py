from operator import inv
import pygame 

	
pygame.init()

width, height = 1500, 400
screen = pygame.display.set_mode((width, height))

bg_img = pygame.image.load('Capture.PNG')
bg_img = pygame.transform.scale(bg_img,(width,height))

inventory = []

while True:

    screen.blit(bg_img,(0,0))

    for i in range(len(inventory)//2):
        screen.blit(inventory[i], (1500/8 * i, 0))
    
    for i in range(len(inventory)//2, len(inventory)):
        screen.blit(inventory[i], (1500/8 * i, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()