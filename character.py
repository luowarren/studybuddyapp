# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# set up sprite sheet

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True

class Character():
    def __init__(self, happiness = 0, health = 100, energy = 100):
        self.happiness = happiness
        self.health = health
        self.energy = energy

        while self.energy > 0:




# Done! Time to quit.
pygame.quit()ft