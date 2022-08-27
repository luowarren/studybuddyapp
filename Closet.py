from glob import glob
import pygame
from Store_logic import *
SCREEN_HEIGHT = 475
SCREEN_WIDTH = 600
SCALE = 4

inventory = Inventory()
coins = 100
stores = Store()
sll = store_logic(inventory, 100, stores)
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Storefront')


class Button():
    def __init__(self, x, y, image, price, name):
        self.name = name
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
        sll.attempt_buy(self.name)
        #global BALANCE 
        #BALANCE = sl.food_purchase(self.price)  

class print_item():

    def __init__(self, sll):
        self.available_item = {}
        self.item_price = {}

        self.item_button = {}
    
    def get_store(self):
        for item, Value in sll.list_item().items():
            G = item
            icon = pygame.image.load(Value[0]).convert_alpha()
            G = pygame.Surface((32,32)).convert_alpha()
            G.blit(icon, (0,0), (1*32, 1*32, 2*32, 2*32))
            G = pygame.transform.scale(G,(32*3.5, 32*3.5))
            
            
            self.available_item[item] = G
            self.item_price[item] = Value[1]
    
    def set_button(self):
        for counter, item in enumerate(self.available_item.items()):
            if counter < 4:
                self.item_button[item] = Button(50 + counter*125, 75, item[1], 10, item[0])
            else:
                self.item_button[item] = Button(35 + (counter - 4)*125, 275, item[1], 10, item[0])
    
    def reset_item(self):
        self.available_item = {}
        self.item_price = {}

        self.item_button = {}
        
    def draw_store(self):
        self.get_store()
        self.set_button()

        for button in self.item_button.values():
            button.draw()
        
        self.reset_item()
        
store_gui = print_item(sll)

run = True
while run: 
    screen.fill((245, 242, 208))
    store_gui.draw_store()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
