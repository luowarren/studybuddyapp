import pygame
SCALE = 2
SCALE2 = 2.5

icon = pygame.image.load('baricon/baricon.png').convert_alpha()
hat_pumpkin = pygame.image.load('Character/acc/hat_pumpkin.png').convert_alpha()
hat_clown = pygame.image.load('Character/acc/mask_clown_blue.png').convert_alpha()
hat_cowboy = pygame.image.load('Character/acc/hat_cowboy.png').convert_alpha()
sail = pygame.image.load('Character/clothes/sailor.png').convert_alpha()
overal = pygame.image.load('Character/clothes/overalls.png').convert_alpha()
sui = pygame.image.load('Character/clothes/suit.png').convert_alpha()
psui = pygame.image.load('Character/clothes/pants_suit.png').convert_alpha()
dre = pygame.image.load('Character/clothes/dress.png').convert_alpha()


apple = pygame.Surface((32, 32)).convert_alpha()
apple.blit(icon, (0, 0), (192, 544, 244, 576))
apple = pygame.transform.scale(apple, (32*SCALE, 32*SCALE))

carrot = pygame.Surface((32, 32)).convert_alpha()
carrot.blit(icon, (0, 0), (10*32, 18*32, 11*32, 19*32))
carrot = pygame.transform.scale(carrot, (32*SCALE, 32*SCALE))

pizza = pygame.Surface((32, 32)).convert_alpha()
pizza.blit(icon, (0, 0), (3*32, 15*32, 11*32, 4*32))
pizza = pygame.transform.scale(pizza, (32*SCALE, 32*SCALE))

iceblock = pygame.Surface((32, 32)).convert_alpha()
iceblock.blit(icon, (0, 0), (8*32, 13*32, 9*32, 14*32))
iceblock = pygame.transform.scale(iceblock, (32*SCALE, 32*SCALE))

coffee = pygame.Surface((32, 32)).convert_alpha()
coffee.blit(icon, (0, 0), (10*32, 14*32, 11*32, 15*32))
coffee = pygame.transform.scale(coffee, (32*SCALE, 32*SCALE))

fries = pygame.Surface((32, 32)).convert_alpha()
fries.blit(icon, (0, 0), (5*32, 15*32, 6*32, 16*32))
fries = pygame.transform.scale(fries, (32*SCALE, 32*SCALE))

sushi = pygame.Surface((32, 32)).convert_alpha()
sushi.blit(icon, (0, 0), (10*32, 16*32, 11*32, 17*32))
sushi = pygame.transform.scale(sushi, (32*SCALE, 32*SCALE))

burger = pygame.Surface((32, 32)).convert_alpha()
burger.blit(icon, (0, 0), (2*32, 15*32, 11*32, 3*32))
burger = pygame.transform.scale(burger, (32*SCALE, 32*SCALE))

pumpkin = pygame.Surface((32, 32)).convert_alpha()
pumpkin.blit(hat_pumpkin, (0, 0), (0*32, 0*32, 1*32, 1*32))
pumpkin = pygame.transform.scale(pumpkin, (32*SCALE2, 32*SCALE2))

clown = pygame.Surface((32, 32)).convert_alpha()
clown.blit(hat_clown, (0, 0), (0*32, 0*32, 1*32, 1*32))
clown = pygame.transform.scale(clown, (32*SCALE2, 32*SCALE2))

cowboy = pygame.Surface((32, 32)).convert_alpha()
cowboy.blit(hat_cowboy, (0, 0), (0*32, 0*32, 1*32, 1*32))
cowboy = pygame.transform.scale(cowboy, (32*SCALE2, 32*SCALE2))

sailor = pygame.Surface((32, 32)).convert_alpha()
sailor.blit(sail, (0, 0), (0*32, 0*32, 1*32, 1*32))
sailor = pygame.transform.scale(sailor, (32*SCALE2, 32*SCALE2))

overalls = pygame.Surface((32, 32)).convert_alpha()
overalls.blit(overal, (0, 0), (8*32, 0*32, 9*32, 1*32))
overalls = pygame.transform.scale(overalls, (32*SCALE2, 32*SCALE2))

suit = pygame.Surface((32, 32)).convert_alpha()
suit.blit(sui, (0, 0), (0*32, 0*32, 1*32, 1*32))
suit = pygame.transform.scale(suit, (32*SCALE2, 32*SCALE2))

pants_suit = pygame.Surface((32, 32)).convert_alpha()
pants_suit.blit(psui, (0, 0), (0*32, 0*32, 1*32, 1*32))
pants_suit = pygame.transform.scale(pants_suit, (32*SCALE2, 32*SCALE2))

dress = pygame.Surface((32, 32)).convert_alpha()
dress.blit(dre, (0, 0), (47*32, 0*32, 48*32, 1*32))
dress = pygame.transform.scale(dress, (32*SCALE2, 32*SCALE2))


class Item:
    def __init__(self, name, typa=None):
        self.name = name
        self.type = typa


    def fnc(self, character):
        if self.name == 'apple':
            character.health += 10
        elif self.name == 'carrot':
            character.health += 10
        elif self.name == 'pizza':
            character.health += 20
        elif self.name == 'iceblock':
            character.health += 10
        elif self.name == 'coffee':
            character.health += 20
        elif self.name == 'fries':
            character.health += 10
        elif self.name == 'sushi':
            character.health += 30
        elif self.name == 'burger':
            character.health += 30
        else:
            character.inventory.append(self)

        if character.health > 100:
            character.health = 100

    def get_price(self):
        if self.name == 'apple':
            return 10
        elif self.name == 'carrot':
            return 10
        elif self.name == 'pizza':
            return 20
        elif self.name == 'iceblock':
            return 10
        elif self.name == 'coffee':
            return 20
        elif self.name == 'fries':
            return 10
        elif self.name == 'sushi':
            return 30
        elif self.name == 'burger':
            return 30
        else:
            return 50

    def get_pic(self):
        if self.name == 'apple':
            return apple
        elif self.name == 'carrot':
            return carrot
        elif self.name == 'pizza':
            return pizza
        elif self.name == 'iceblock':
            return iceblock
        elif self.name == 'coffee':
            return coffee
        elif self.name == 'fries':
            return fries
        elif self.name == 'sushi':
            return sushi
        elif self.name == 'burger':
            return sushi
        elif self.name == 'hat_pumpkin':
            return pumpkin
        elif self.name == 'mask_clown_blue':
            return clown
        elif self.name == 'hat_cowboy':
            return cowboy
        elif self.name == 'sailor':
            return sailor
        elif self.name == 'overalls':
            return overalls
        elif self.name == 'suit':
            return suit
        elif self.name == 'pants_suit':
            return pants_suit
        elif self.name == 'dress':
            return dress
    
    def use(self, character):
        character.clothing[self.type] = self.name



