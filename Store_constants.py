#Screen size
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

#Dictionary
CLOTH_IMAGE = {}
CLOTH_COST = {}


#Item ID
SHIRT = 'S'
SHOE = 'H'
PANT = 'P'
HATS = 'H'
PUMPKIN_HAT = 'PH'
CLOWN_MASK = 'CM'
COWBOY_HAT = 'CH'
SAILOR_SHIRT = 'SS'
OVERALLS = 'O'
SUIT = 'SUIT'
PANTS_SUIT = 'PSUIT'
DRESS = 'D'

#Item Cost
SHIRT_COST = 12
SHOE_COST = 50
PANT_COST = 8
HAT_COST = 5


#Item Happiness
SHIRT_H = 1.2
SHOE_H = 0.8
PANT_H = 1.2
HAT_H = 0/4

# Food Costs and effects, NOTE: cost price is directly proportional to effect e.g. sushi costs $30 and increases hunger by 30
SUSHI	= 30
BURGER = 30
COFFEE	= 20
FRIES	= 10
ICEBLOCK = 10
APPLE	= 10
CARROT	= 10
PIZZA = 20

# clothes prices and effect on happiness
HAT_PUMPKIN = 40
HAT_COWBOY = 40
MASK_CLOWN_BLUE = 30
SAILOR = 30
OVERALLS = 50
SUIT = 50
PANTS_SUIT = 40
DRESS = 50

# Item Dictionary: Item ID -> (IMG, Cost)
ITEMS = {
  PUMPKIN_HAT: ("HAT_PUMPKIN", 40),
  COWBOY_HAT: ("HAT_COWBOY", 40),
  CLOWN_MASK: ("MASK_CLOWN_BLUE", 30),
  SAILOR_SHIRT: ("SAILOR", 30),
  OVERALLS: ("OVERALLS", 50),
  SUIT: ("SUIT", 50),
  PANTS_SUIT: ("PANTS_SUIT", 40),
  DRESS: ("DRESS", 50),
}
