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

    def attempt_buy(self, Item):
        """
        Return Dictionary with ID as key and (Image, Cost) as value.

        Attempts to buy item. Make sure item is in the store, and 
        player has the money to purchase it.
        """
        #If Item is already in player's inventory
        if Item not in self.Store_Item.get_store():
            return self.list_item()

        #If player does not have enough money
        elif CLOTH_COST[Item] >= self.Coin:
            return self.list_item()

        #Buy the item otherwise
        else:
            self.deduct_amount(CLOTH_COST[Item])
            self.Store_Item.remove_item(Item)
            self.remove_item(Item)
            self.Inventory.add_item(Item)
            return self.list_item()
    
    def deduct_amount(self, amount):
        """
        Take away the cost from player's coin.
        """
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
        for ID in self.Store_Item.get_store().keys():
            Images = Images.append(CLOTH_IMAGE(ID))
            Costs = Costs.append(CLOTH_COST(ID))

        #Set the dictionary up and return it
        for n in range(len(self.Store_Item.get_store().keys())):
            Image, Cost= Images[n], Costs[n]
            ID = self.Store_Item.get_store().keys()[n]

            Dictionary[ID] = (Image, Cost)

        return Dictionary
