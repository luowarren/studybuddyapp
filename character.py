# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True

class Character():
    def __init__(self, happiness = 0, health = 100, energy = 100):
        self.happiness = happiness
        self.health = health
        self.energy = energy

    def increase_happiness(self, value=5):
        if self.happiness <= 95:
            self.happiness += value
    
    def decrease_health(self, value=10):
        self.health -= value
    
    def reset_health(self):
        self.health = 100

    def decrease_energy(self, value=5):
        self.energy -= value
    
    def reset_energy(self, )