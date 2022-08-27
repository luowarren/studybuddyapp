import pygame
from Store_constants import *

class Coin():
    def __init__(self, quantity=0) -> None:
        self.quantity = quantity
    
    def add_coin() -> None:
        self.quantity += 1

    def get_coins() -> int:
        return self.quantity

    def remove_coins(amount):
        self.quantity -= amount