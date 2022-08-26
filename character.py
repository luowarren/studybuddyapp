# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

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

    def reset_character(self):
        self.happiness = 50
        self.hunger = 0
        self.thirst = 0
        self.energy = 100

    #happiness methods
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

    #thirst functions
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

    #energy functions
    def reset_energy(self):
        self.energy = 100

    def decrease_energy(self, value=5):
        if self.energy - value < 0:
            self.energy = 0
            print('Break time')
        else:
             self.energy -= value
    
