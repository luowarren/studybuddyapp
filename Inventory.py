"""
The basic inventory requirement
"""
import pygame
from Store_constants import *

class Inventory():

    def __init__(self) -> None:
        self.inventory = []
    
    def add_item(self, item: str):
        self.inventory.append(item)

    def get_inventory(self) -> list:
        return self.inventory

class Store():

    def __init__(self) -> None:
        self.store = []
    
    def remove_item(self, item: str):
        self.store.remove(item)
    
    def get_store(self) -> None:
        return self.store

class Item():

    def __init__(self):
        raise NotImplemented

    def buy(self):

        raise NotImplemented

    def wear(self):

        raise NotImplemented

    def get_id(self):

        return None

class Shoe(Item):

    _id = SHOE

    def buy(self):

        raise NotImplemented
    
    def wear(self):
        raise NotImplemented





    
