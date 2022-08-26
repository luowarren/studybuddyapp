"""
The GUI interface of the store
"""


import pygame
pygame.font.init()
from Store_constants import *
from Inventory import *

class store():
    def toggle_shop(shop):
        """
        This function should see if player's mouse has clicked on the shop button.
        If it does, return true else false. 

        Parameters:
        shop: The coordinate of the shop.
        """
        shop_rect = shop.get_rect()
        #See if player has touched onto the shop rectangle coordinate
        if player.rect.colliderect(shop.rect):
            return True
        else:
            return False


    def display_shop():
        """
        This function should display the shop which includes image, price and happiness stats.
        """
        screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # Run code to display your shop


    def main():
        """
        Put the two function together and run the store gui :)
        """
        shop = pygame.transform.scale(pygame.image.load("shop.png"), (60, 60))
        open_shop = False
        if toggle_shop(shop):
            display_shop()
