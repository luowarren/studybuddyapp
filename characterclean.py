import pygame

# Configuration
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []

#Button class
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

#character class

class Character():
    #all character stats
    #happiness, happiness correlates to multiplyer on coins earned? increased through studying
    #hunger and thrist is increased by food and water
    #every time energy is low, the person goes to take a break (irl break)

    def __init__(self, happiness = 50, hunger = 0, energy = 100, name = 'timmy', outfit = 'naked', coins = 0):
        self.happiness = happiness
        self.hunger = hunger
        self.energy = energy
        self.name = name
        self.coins = coins        
        self.inventory = []

        self.outfit = {
            'hat' : 'basic hat',
            'shirt' : 'basic shirt',
            'pants' : 'basic pants'
        }

    def reset_character(self):
        self.happiness = 50
        self.hunger = 0
        self.thirst = 0
        self.energy = 100

    #coins
    def get_coins(self):
        return str(self.coins)

    def add_coins(self, coins):
        self.coins += coins

    def use_coins(self, coins):
        if self.coins - coins < 0:
            pass
        self.coins -= coins

    #outfit methods
    def get_outfit(self):
        #use this to index into the dictionary
        return self.outfit
    
    def change_hat(self, hat):
        #or whatever inventory
        if hat not in self.inventory:
            print("You do not own this item")
        else:
            self.outfit['hat'] = hat

    def change_shirt(self, shirt):
        #or whatever inventory
        if shirt not in self.inventory:
            print("You do not own this item")
        else:
            self.outfit['shirt'] = shirt

    def change_pants(self, pants):
        #or whatever inventory
        if pants not in self.inventory:
            print("You do not own this item")
        else:
            self.outfit['pants'] = pants

    #happiness methods

    def get_happiness(self):  

        #for warren, 0-5 from no happines to top happiness
        if self.happiness < 100/6:
            return 5
        elif self.happiness >= 100/6 and self.happiness < 200/6:
            return 4
        elif self.happiness >= 200/6 and self.happiness < 300/6:
            return 3
        elif self.happiness >= 300/6 and self.happiness < 400/6:
            return 2
        elif self.happiness >= 400/6 and self.happiness < 500/6:
            return 1
        else:
            return 0

    def str_happiness(self):
        return str(self.happiness)

    def reset_happiness(self):
        self.happiness = 50

    def increase_happiness(self, value=5):
        if self.happiness + value >= 100:
            self.happiness = 100
        else:
            self.happiness += value

    def decrease_happiness(self, value=5):
        if self.happiness - value < 0:
            self.happiness = 0
        else:
            self.happiness -= value
    
    #hunger methods
    def get_hunger(self):
        return str(self.hunger)

    def reset_hunger(self):
        self.hunger = 0

    def check_hunger(self):
        if self.hunger <= 0:
            print("not hungry")
        elif self.hunger > 0 and self.hunger < 25:
            print("little bit hungry")
        elif self.hunger >= 25 and self.hunger < 50:
            print("hungry")
        elif self.hunger >= 50 and self.hunger < 75:
            print("very hungry")
        elif self.hunger >= 75 and self.hunger < 100:
            print("starving")
        else:
            print("dead")

    def increase_hunger(self, value= 10):
        if self.hunger + value > 100:
            self.hunger = 100
        else: 
            self.hunger += value

    def decrease_hunger(self, value= 10):
        if self.hunger - value < 0:
            self.hunger = 0
        else:
            self.hunger -= value

    def use_food(self, food):
        #check if the inventory of food is > 1 
        self.decrease_hunger(self.food[food])

    #energy functions
    def get_energy(self):
        return str(self.energy)

    def reset_energy(self):
        self.energy = 100

    def decrease_energy(self, value=5):
        if self.energy - value < 0:
            self.energy = 0
            print('Break time')
        else:
             self.energy -= value

while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for object in objects:
        object.process()

    pygame.display.flip()

    