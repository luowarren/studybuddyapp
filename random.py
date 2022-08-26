# Simple pygame program

# Import and initialize the pygame library
import button
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

font = pygame.font.SysFont('Arial', 40)

objects = []

# Run until the user asks to quit
running = True

class Character():
    #all character stats
    #happiness, happiness correlates to multiplyer on coins earned? increased through studying
    #hunger and thrist is increased by food and water
    #every time energy is low, the person goes to take a break (irl break)

    def __init__(self, happiness = 50, hunger = 0, thirst = 0, energy = 100):
        self.happiness = happiness
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.food = {
            'steak' : 30,
            'sushi' : 20,
            'potato' : 10,
        }
        self.drinks = {
            'water' : 30,
            'gatorade' : 20,
            'redbull' : 10
        }

        self.clothes = {}

    def reset_character(self):
        self.happiness = 50
        self.hunger = 0
        self.thirst = 0
        self.energy = 100

    #happiness methods
    def get_happiness(self):
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
    
    #depending on how happy the buddy is, can mutiply the coins earnt by this amount
    def happiness_multiplyer(self):
        if self.happiness <= 33:
            return 1
        elif self.happiness <= 67:
            return 1.5
        else:
            return 2
    
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

    #thirst functions
    def get_thirst(self):
        return str(self.thirst)

    def reset_thirst(self):
        self.thirst = 0

    def check_thirst(self):
        if self.thirst <= 0:
            print("not thirsty")
        elif self.thirst > 0 and self.thirst < 25:
            print("little bit thirsty")
        elif self.thirst >= 25 and self.thirst < 50:
            print("thirsty")
        elif self.thirst >= 50 and self.thirst < 75:
            print("very thirsty")
        elif self.thirst >= 75 and self.thirst < 100:
            print("dehydrated")
        else:
            print("dead")

    def increase_thirst(self, value= 10):
        if self.thirst + value > 100:
            self.thirst = 100
        else: 
            self.thirst += value

    def decrease_thirst(self, value= 10):
        if self.thirst - value < 0:
            self.thirst = 0
        else:
            self.thirst -= value

    def use_drink(self, drink):
        #check if the inventory of drink is > 1 
        self.decrease_thirst(self.drinks[drink])

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

#increased thirst and hunger when time passes
#decreased thirst and hunger when food and drink are consumed

#decreased energy every certain time period of studying, energy reset after break

#decreased happiness every missed day of studying, vise versa


#buttons to use drinks and such
character = Character()

def myFunction():
    print('Button Pressed')

customButton = button.Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
customButton = button.Button(30, 140, 400, 100, 'Button Two (multiPress)', myFunction, True)


while running:
    # Did the user click the window close button?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white

    # # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # font = pygame.font.SysFont(None, 24)
    # hunger = font.render(character.get_hunger(), True, 'blue')
    # thirst = font.render(character.get_thirst(), True, 'blue')
    # energy = font.render(character.get_energy(), True, 'blue')

    # screen.blit(hunger, (20, 20))
    # screen.blit(thirst, (20, 40))
    # screen.blit(energy, (20, 60))

    for object in objects:
        object.process()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()