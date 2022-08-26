"""
The basic inventory requirement
"""
import pygame
from Store_constants import *

class Item():

    def wear(self):

        raise NotImplemented

    def get_id(self):

        return None

class Shoe(Item):

    def buy(self):

        raise NotImplemented
    
    def wear(self):
        raise NotImplemented


class Inventory():

    def __init__(self, coins) -> None:
        self.inventory = {}
        self.coin = coins
    
    def add_item(self, item: Item):
        pass



    
