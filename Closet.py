import pygame
SCREEN_HEIGHT = 475
SCREEN_WIDTH = 600
SCALE = 5

BALANCE = 100

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Closet')

# load images for buttons
clownmaskpic = pygame.image.load('clownmask.png').convert_alpha()
cowboypic = pygame.image.load('cowboy.png').convert_alpha()
dresspic = pygame.image.load('dress.png').convert_alpha()
overallspic = pygame.image.load('overalls.png').convert_alpha()
pantssuitpic = pygame.image.load('pantssuit.png').convert_alpha()
pumpkinpic = pygame.image.load('pumpkin.png').convert_alpha()
sailorpic = pygame.image.load('sailor.png').convert_alpha()
suitpic = pygame.image.load('suit.png').convert_alpha()

sailor = pygame.Surface((32, 32)).convert_alpha()
sailor.blit(sailorpic, (0, 0), (73*32, 0*32, 74*32, 1*32))
                        # L1  H1   L2   H2
                        # 6   17   7    18
sailor = pygame.transform.scale(sailor, (32*6, 32*6))

clownmask = pygame.Surface((32, 32)).convert_alpha()
clownmask.blit(clownmaskpic, (0, 0), (0*32, 0*32, 1*32, 1*32))
clownmask = pygame.transform.scale(clownmask, (32*4, 32*4))

pantssuit = pygame.Surface((32, 32)).convert_alpha()
pantssuit.blit(pantssuitpic, (0, 0), (8*32, 0*32, 9*32, 1*32))
pantssuit = pygame.transform.scale(pantssuit, (32*6, 32*12))

cowboy = pygame.Surface((32, 32)).convert_alpha()
cowboy.blit(cowboypic, (0, 0), (0*32, 0*32, 1*32, 1*32))
cowboy = pygame.transform.scale(cowboy, (32*SCALE, 32*SCALE))

overalls = pygame.Surface((32, 32)).convert_alpha()
overalls.blit(overallspic, (0, 0), (20*32, 8*32, 21*32, 9*32))
overalls = pygame.transform.scale(overalls, (32*SCALE, 32*SCALE))

pumpkin = pygame.Surface((32, 32)).convert_alpha()
pumpkin.blit(pumpkinpic, (0, 0), (0*32, 0*32, 1*32, 1*32))
pumpkin = pygame.transform.scale(pumpkin, (32*SCALE, 32*SCALE))

dress = pygame.Surface((32, 32)).convert_alpha()
dress.blit(dresspic, (0, 0), (48*32, 0*32, 49*32, 1*32))
dress = pygame.transform.scale(dress, (32*SCALE, 32*SCALE))

suit = pygame.Surface((32, 32)).convert_alpha()
suit.blit(suitpic, (0, 0), (0*32, 0*32, 1*32, 1*32))
suit = pygame.transform.scale(suit, (32*SCALE, 32*SCALE))


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
        global BALANCE, balance
        if BALANCE - self.price > 0:
            BALANCE -= self.price

sailor_label = Label(77, 195, ' $30 ')
sailor_button = Button(5, 1, sailor, 30)
                    # C    R
clownmask_label = Label(205, 195, ' $30 ')
clownmask_button = Button(170, 75, clownmask, 30)
pumpkin_label = Label(340, 195, ' $40 ')
pumpkin_button = Button(290, 70, pumpkin, 40)
cowboy_label = Label(469, 195, ' $40 ')
cowboy_button = Button(415, 65, cowboy, 40)

pantssuit_label = Label(69, 400, ' $40 ')
pantssuit_button = Button(1, 5, pantssuit, 40)
overalls_label = Label(205, 400, ' $50 ')
overalls_button = Button(153, 240, overalls, 50)
dress_label = Label(347, 400, ' $50 ')
dress_button = Button(295, 225, dress, 50)
suit_label = Label(467, 400, ' $50 ')
suit_button = Button(415, 232, suit, 50)

clothes_label = Label(25, 15, 'Clothes')

run = True
while run:
    
    screen.fill((209, 237, 242))
    balance = Label(470, 25, ' $' + str(BALANCE) + ' ')
    balance.balance()
    clothes_label.label()
    sailor_label.pricelabel()
    sailor_button.draw()
    clownmask_label.pricelabel()
    clownmask_button.draw()
    pumpkin_label.pricelabel()
    pumpkin_button.draw()
    cowboy_label.pricelabel()
    cowboy_button.draw()

    pantssuit_label.pricelabel()
    pantssuit_button.draw()
    overalls_label.pricelabel()
    overalls_button.draw()
    suit_label.pricelabel()
    dress_label.pricelabel()
    dress_button.draw()
    suit_label.pricelabel()
    suit_button.draw()

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()