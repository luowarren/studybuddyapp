"""
The logic behind transaction
"""
import pygame

from Store_constants import *
from Inventory import *

class store_logic():
    """
    Handle the logical stuff that's happening after player attempt to buy an item.
    """

    def __init__(self, Inventory, Coin, Store_Item) -> None:
        """
        Initialise the inventory, number of coin, and the store_item.
        """
        #Player's inventory
        self.Inventory = Inventory

        #Player's number of Coin
        self.Coin = Coin

        #The item player still needs to buy
        self.Store_Item = Store_Item

        #Checks if the purchase was successful
        self.purchase = False



    def food_purchase(self, cost):
        if self.Coin >= cost:
            self.Coin -= cost
            self.purchase = True
        else:
            self.purchase = False
        return self.Coin

    def checker(self):
        if self.purchase:
            return True

    def attempt_buy(self, Item):
        """
        Return Dictionary with ID as key and (Image, Cost) as value.

        Attempts to buy item. Make sure item is in the store, and 
        player has the money to purchase it.
        """
        #If Item is already in player's inventory
        if Item not in self.Store_Item.get_store():
            return self.list_item()
            

       # tesing for functionality ...

        #Buy the item otherwise
        else:
            
            purchase_sfx.play()
            self.deduct_amount(ITEMS[Item][1])
            self.Store_Item.remove_item(Item)
            self.Inventory.add_item(Item)
            return self.list_item()

    def deduct_amount(self, amount):
        """
        Take away the cost from player's coin.
        """
        purchase_sfx.play()
        self.Coin -= amount
    
    def list_item(self):
        """
        Return a dictionary 
        """
        #Set list and dictionary up.
        Images = []
        Costs = []
        Dictionary = {}

        #get the images and the cost list for items that will be on store.
        for ID in self.Store_Item.get_store():
            Images.append(ITEMS[ID][0])
            Costs.append(ITEMS[ID][1])

        #Set the dictionary up and return it
        for n in range(len(self.Store_Item.get_store())):
            Image, Cost= Images[n], Costs[n]
            ID = self.Store_Item.get_store()[n]

            Dictionary[ID] = (Image, Cost)

        return Dictionary
    
    def get_inventory(self):
        inventory_img = []
        img = []
        for ID in self.Inventory.get_inventory():
            inventory_img.append(ITEMS[ID][0])

        for counter, destination in enumerate(inventory_img):
            img.append(pygame.image.load(inventory_img[counter]))

        #for counter in img:
            #img[counter] = pygame.transform.scale(img[counter], (32*3.5, 32*3.5))
        """
                        
        for image in inventory_img:
            print(image)
            icon = pygame.image.load(image).convert_alpha()

            shirt = pygame.Surface((32, 32)).convert_alpha()
            img.append(shirt)
        """

        
        return img
        

invent = Inventory()
coin = 100
store = Store()
sl = store_logic(invent, 100, store)
