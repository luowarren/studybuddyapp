"""
The logic behind transaction
"""
from operator import itemgetter
from typing_extensions import Self
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
        Self.Inventory = Inventory

        #Player's number of Coin
        Self.Coin = Coin

        #The item player still needs to buy
        Self.Store_Item = Store_Item

    def attempt_buy(Self, Item: ID):
        """
        Return Dictionary with ID as key and (Image, Cost) as value.

        Attempts to buy item. Make sure item is in the store, and 
        player has the money to purchase it.
        """


        #If Item is already in player's inventory
        if Item not in Self.Store_Item.get_store():
            return self.list_item()

        #If player does not have enough money
        elif CLOTH_COST[Item] >= Self.Coin:
            return self.list_item()

        #Buy the item otherwise
        else:
            Self.deduct_amount(CLOTH_COST[Item])
            Self.remove_item(Item)
            Self.Inventory.add_item(Item)
            return self.list_item()

    def remove_item(Self, Item): 
        """
        Should remove the item from the store.
        """
        Self.Store_Item.get_store.pop(Item)
    
    def deduct_amount(Self, amount):
        """
        Take away the cost from player's coin.
        """
        Self.Coin -= amount
    
    def list_item(Self):
        """
        Return a dictionary 
        """

        #Set list and dictionary up.
        Images = []
        Costs = []
        Dictionary = {}

        #get the images and the cost list for items that will be on store.
        for ID in Self.Store_Item.get_store().keys():
            Images = Images.append(CLOTH_IMAGE(ID))
            Costs = Costs.append(CLOTH_COST(ID))

        #Set the dictionary up and return it
        for n in range(len(Self.Store_Item.get_store().keys())):
            Image, Cost= Images[n], Costs[n]
            ID = Self.Store_Item.get_store().keys()[n]

            Dictionary[ID] = (Image, Cost)

        return Dictionary
