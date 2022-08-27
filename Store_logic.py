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
    Handle the logical stuff that's happening after buying items.
    """

    def __init__(self, Inventory, Coin, Store_Item) -> None:
        #Player's inventory
        Self.Inventory = Inventory

        #Player's available Coin
        Self.Coin = Coin

        #The item player still needs to buy
        Self.Store_Item = Store_Item

    def attempt_buy(Self, Item: ID):
        """
        Should determine if player can buy item. If player can buy the item,
        then add it into inventory and deduct the cost, otherwise tell player 
        they can't buy the item.
        """

        #In the end, just return whatever the player can still buy.

        #If Item is already in player's inventory
        if Item not in Self.Store_Item.get_store():
            return self.list_item()

        #If player does not have enough money
        elif CLOTH_COST[Item] >= Self.Coin:
            return self.list_item()

        #Buy the item otherwise
        else:
            item_ID = self.Store_Item.get_store()
            Self.deduct_amount(CLOTH_COST[Item])
            Self.remove_item(Item)
            Self.Inventory.add_item(Item)
            return self.list_item()

    def remove_item(Self, Item): 
        """
        Should remove the item from the store since player has it.
        """
        Self.Store_Item.get_store.pop(Item)
    
    def deduct_amount(Self, amount):
        Self.Coin -= amount
    
    def list_item(Self):
        #get images for all the thing in the store currently
        Images = []
        Costs = []
        Dictionary = {}
        for ID in Self.Store_Item.get_store().keys():
            Images = Images.append(CLOTH_IMAGE(ID))
            Costs = Costs.append(CLOTH_COST(ID))

        for n in range(len(Self.Store_Item.get_store().keys())):
            Image, Cost= Images[n], Costs[n]
            ID = Self.Store_Item.get_store().keys()[n]

            Dictionary[ID] = (Image, Cost)

        return Dictionary
