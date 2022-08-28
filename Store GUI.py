from glob import glob
import pygame
from Store_logic import *
SCREEN_HEIGHT = 475
SCREEN_WIDTH = 600
SCALE = 4

BALANCE = 100

a = 1
b = 3

sl = store_logic(a, BALANCE, b)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Storefront')

# load images for buttons
icon = pygame.image.load('baricon.png').convert_alpha()

apple = pygame.Surface((32, 32)).convert_alpha()
apple.blit(icon, (0, 0), (192, 544, 244, 576))
                        # L1  H1   L2   H2
                        # 6   17   7    18
apple = pygame.transform.scale(apple, (32*SCALE, 32*SCALE))

carrot = pygame.Surface((32, 32)).convert_alpha()
carrot.blit(icon, (0, 0), (10*32, 18*32, 11*32, 19*32))
carrot = pygame.transform.scale(carrot, (32*3.5, 32*3.5))

pizza = pygame.Surface((32, 32)).convert_alpha()
pizza.blit(icon, (0, 0), (3*32, 15*32, 11*32, 4*32))
pizza = pygame.transform.scale(pizza, (32*SCALE, 32*SCALE))

iceblock = pygame.Surface((32, 32)).convert_alpha()
iceblock.blit(icon, (0, 0), (8*32, 13*32, 9*32, 14*32))
iceblock = pygame.transform.scale(iceblock, (32*SCALE, 32*SCALE))

coffee = pygame.Surface((32, 32)).convert_alpha()
coffee.blit(icon, (0, 0), (10*32, 14*32, 11*32, 15*32))
coffee = pygame.transform.scale(coffee, (32*3.5, 32*3.5))

fries = pygame.Surface((32, 32)).convert_alpha()
fries.blit(icon, (0, 0), (5*32, 15*32, 6*32, 16*32))
fries = pygame.transform.scale(fries, (32*SCALE, 32*SCALE))

sushi = pygame.Surface((32, 32)).convert_alpha()
sushi.blit(icon, (0, 0), (10*32, 16*32, 11*32, 17*32))
sushi = pygame.transform.scale(sushi, (32*SCALE, 32*SCALE))

burger = pygame.Surface((32, 32)).convert_alpha()
burger.blit(icon, (0, 0), (2*32, 15*32, 11*32, 3*32))
burger = pygame.transform.scale(burger, (32*3.5, 32*3.5))


class Label():
    def __init__(self, x, y, price):
        self.x = x
        self.y = y
        self.price = price

    def pricelabel(self):
        font = pygame.font.Font('Pixel.ttf', 20)
        label = font.render(self.price, True, (0, 0, 0), (254, 220, 86))
        screen.blit(label, (self.x, self.y))

    def label(self):
        font = pygame.font.Font('Pixel.ttf', 40)
        label = font.render(self.price, True, (0, 0, 0))
        screen.blit(label, (self.x, self.y))

    def balance(self):
        font = pygame.font.Font('Pixel.ttf', 30)
        label = font.render(self.price, True, (255, 255, 255), (180, 0, 0))
        screen.blit(label, (self.x, self.y))

class Button():
    def __init__(self, x, y, image, price):
        self.image = image
        self.price = price
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        # get mouse pos
        pos = pygame.mouse.get_pos()

        # is the cursor colliding w button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print(self.price)
                self.update()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        global BALANCE 
        BALANCE = sl.food_purchase(self.price)
        
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
		        return True

apple_label = Label(77, 195, ' $10 ')
apple_button = Button(50, 75, apple, 10)
                    # C    R
carrot_label = Label(205, 195, ' $10 ')
carrot_button = Button(175, 75, carrot, 10)
fries_label = Label(340, 195, ' $10 ')
fries_button = Button(300, 70, fries, 10)
iceblock_label = Label(469, 195, ' $10 ')
iceblock_button = Button(425, 65, iceblock, 10)

pizza_label = Label(69, 400, ' $20 ')
pizza_button = Button(35, 275, pizza, 20)
coffee_label = Label(205, 400, ' $20 ')
coffee_button = Button(190, 275, coffee, 20)
sushi_label = Label(340, 400, ' $30 ')
sushi_button = Button(310, 275, sushi, 30)
burger_label = Label(467, 400, ' $30 ')
burger_button = Button(440, 275, burger, 30)

food_label = Label(25, 15, 'Food')

run = True
while run:
    
    screen.fill((245, 242, 208))
    balance = Label(470, 25, ' $' + str(BALANCE) + ' ')
    balance.balance()
    food_label.label()
    apple_label.pricelabel()
    apple_button.draw()
    carrot_label.pricelabel()
    carrot_button.draw()
    fries_label.pricelabel()
    fries_button.draw()
    iceblock_label.pricelabel()
    iceblock_button.draw()

    pizza_label.pricelabel()
    pizza_button.draw()
    coffee_label.pricelabel()
    coffee_button.draw()
    burger_label.pricelabel()
    sushi_label.pricelabel()
    sushi_button.draw()
    burger_label.pricelabel()
    burger_button.draw()

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
