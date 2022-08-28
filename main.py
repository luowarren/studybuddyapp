
import pygame

pygame.init()

import spritesheet 
import random 

pygame.mixer.init()
pygame.mixer.music.load("music/bg_song.mp3")
button_sound = pygame.mixer.Sound("music/button2.wav")
walking_sound = pygame.mixer.Sound("music/walking_sound_effect.mp3")
celebrate = pygame.mixer.Sound("music/celebrate.wav")
purchase = pygame.mixer.Sound("music/purchase.mp3")
equip = pygame.mixer.Sound("music/equip.wav")

pygame.mixer.music.play(-1, 0.0)



brown = (31, 22, 16)
white = (255, 255, 255)
black = (0, 0, 0)


# LEVELS
game_menu = True
character_load = False
buddy_name = False
game_start = False

# CREATING CANVAS
canvas = pygame.display.set_mode((1280, 720))
  
# TITLE OF CANVAS
pygame.display.set_caption("Study Buddies")
exit = False

# GAME LOAD SECTION #
intro = pygame.image.load("intro.png").convert_alpha()
start_button = pygame.Rect(365, 467, 538, 90)

#  CHARACTER CONFIG #
config = pygame.image.load("char_config.png").convert_alpha()
minus_skin = pygame.Rect(437, 311, 42, 38)
minus_hairstyle = pygame.Rect(437, 375, 42, 38)
minus_haircolor = pygame.Rect(437, 443, 42, 38)
minus_eye = pygame.Rect(437, 510, 42, 38)
plus_skin = pygame.Rect(796, 312, 42, 38)
plus_hairstyle = pygame.Rect(796, 377, 42, 38)
plus_haircolor = pygame.Rect(796, 443, 42, 38)
plus_eye = pygame.Rect(796, 510, 42, 38)
set_name = pygame.Rect(435, 586, 403, 68)

# SETTING BUDDY NAME #

name_buddy_screen = pygame.image.load("name_buddy.png").convert_alpha()
clock = pygame.time.Clock()
input_box = pygame.Rect(440, 400, 140, 75)
color_inactive = pygame.Color(black)
color_active = pygame.Color(white)
color = color_inactive
active = False
char_names = ''
done = False

# GAME START SECTION #
# Character
char_x = 570
char_y = 250
velocity = 5
still = True
left = False
right = False
front = True
back = False

#fonts
fontObj = pygame.font.Font('fonts/pixel.ttf', 40)
fontObjsml = pygame.font.Font('fonts/pixel.ttf', 25)

# Bars
emojis = pygame.image.load("char/icons.png").convert_alpha()
emoji = spritesheet.SpriteSheet(emojis, 0)
emoji_list = []

bars = pygame.image.load("bars/healthbar.png").convert_alpha()
bar = pygame.Surface((80, 19)).convert_alpha()
bar.blit(bars, (0, 0), (8, 94, 224, 112))
bar = pygame.transform.scale(bar, (80 * 3, 19 * 3))

health = pygame.Surface((66, 4)).convert_alpha()
#health.blit(bars, (7, 20), (28, 90, 84, 94))
health.blit(bars, (0, 0), (28, 90, 84, 94))


# background
room = pygame.image.load("char/1.png").convert_alpha()
room = spritesheet.SpriteSheet(room, 0)
room = room.get_image(0, 700, 700, 1.1)

# Icons
icon = pygame.image.load("baricon/baricon.png").convert_alpha()

# furniture
furniture = pygame.image.load("interior/interior.png").convert_alpha()

# computer
computer = pygame.Surface((16, 16)).convert_alpha()
computer.blit(furniture, (0, 0), ((0), (32), 16, 48))
computer = pygame.transform.scale(computer, (16 * 5, 16 * 5))

screen = spritesheet.SpriteSheet(furniture, 2)
screen2 = spritesheet.SpriteSheet(furniture, 3)
computer_animation = []

# assets
char_features = {
    'body': 0,
    'hair': 0,
    'hair_colour': 0,
    'eye': 0,
}

current_features = char_features.copy()
animation_front = spritesheet.update_assets(char_features)

# create timer
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0


#emojis
for x in range(1, 7):
    emoji_list.append(emoji.get_image(x, 16, 16, 4))

for x in range(1, 5):
    computer_animation.append(screen.get_image(x, 16, 16, 5))
for x in range(1, 5):
    computer_animation.append(screen2.get_image(x, 16, 16, 5))

class Label():
    def __init__(self, x, y, price):
        self.x = x
        self.y = y
        self.price = price

    def pricelabel(self):
        font = pygame.font.Font('Pixel.ttf', 20)
        label = font.render(self.price, True, (0, 0, 0), (254, 220, 86))
        shop.blit(label, (self.x, self.y))

    def label(self):
        font = pygame.font.Font('Pixel.ttf', 40)
        label = font.render(self.price, True, (0, 0, 0))
        shop.blit(label, (self.x, self.y))

    def balance(self):
        font = pygame.font.Font('Pixel.ttf', 20)
        label = font.render(self.price, True, (180, 0, 0))
        shop.blit(label, (self.x, self.y))

class Button():
    def __init__(self, x, y, image, price, name, item):
        self.image = image
        self.name = name
        self.item = item
        self.price = price
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        # get mouse pos
        pos = pygame.mouse.get_pos()

        # is the cursor colliding w button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print(self.price)
                self.update()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        shop.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        global char, balance
        if char.coins - self.price > 0:
            if self.item != None:
                char.inventory.append(items.Item(self.name, self.item))
                char.coins -= self.price
            elif self.item == None and char.health + self.price <= 100:
                char.health += self.price
                char.coins -= self.price


class Character:
    def __init__(self):
        self.inventory = []
        self.clothing = {
            'hat': None,
            'shirt': 'basic',
            'pants': 'pants',
        }
        self.coins = 500
        self.health = 50
        self.happiness = 0

char = Character()

image_set = char.clothing

current_items = image_set.copy()
clothe_right, clothe_left, clothe_front, clothe_back = spritesheet.animate(image_set)


study_section = pygame.Rect(594, 229, 695-594, 306-229)
study_sign = pygame.image.load("oin.png").convert_alpha()
study_sign = pygame.transform.scale(study_sign, (500 * 0.5, 300 * 0.5))
timer = False

frame_count = 0
frame_rate = 60
minutes = 0
total = 0
target = 0


coins = 0
import items
all_items = [items.Item('carrot'), items.Item('pizza'), items.Item('iceblock'), items.Item('coffee'), items.Item('fries'), items.Item('sushi'), items.Item('burger'), items.Item('apple'), items.Item('hat_pumpkin', 'hat'), items.Item('mask_clown_blue', 'hat'), items.Item('hat_cowboy', 'hat'), items.Item('sailor', 'shirt'), items.Item('overalls', 'shirt'), items.Item('suit', 'shirt'), items.Item('pants_suit', 'pants'), items.Item('dress', 'shirt')]
store_section = pygame.Rect(376, 288, 506-376, 326-288)
store_sign = pygame.image.load("storesign.png").convert_alpha()

vending_section = pygame.Rect(764, 467, 946-764, 648-467)


space_1 = pygame.Rect(58, 498, 135-58, 574-498)
space_2 = pygame.Rect(350, 498, 135-58, 574-498)
space_3 = pygame.Rect(58, 581, 135-58, 574-498)
space_4 = pygame.Rect(350, 581, 135-58, 574-498)

slot_list = [(58, 498), (350, 498), (58, 581), (350, 581)]


inventory_section = pygame.Rect(715, 221, 861-715, 307-221)
inventory_sign = pygame.image.load("inventory.png").convert_alpha()
inventory_sign = pygame.transform.scale(inventory_sign, (1537 * 0.2, 410 * 0.2))
inventory_list = []

first_line = fontObj.render(f"Bank:", True, (240,240,240))
money_balance = fontObjsml.render(f"{char.coins} Study Bucks", True, (240,240,240))

tip1 = fontObjsml.render(f"Study 1 minute and", True, (240,240,240))
tip2 = fontObjsml.render(f"earn 1 study buck!", True, (240,240,240))
tip3 = fontObjsml.render(f"Spend it on food or", True, (240,240,240))
tip4 = fontObjsml.render(f"clothes for your", True, (240,240,240))
tip5 = fontObjsml.render(f"buddy :)", True, (240,240,240))


while not exit:
    # update animation
    if game_menu:

        canvas.fill(white)
        canvas.blit(intro, (0,0))

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONUP and start_button.collidepoint(pos[0], pos[1]):
                pygame.mixer.Sound.play(button_sound)
                game_menu = False
                character_load = True

    pygame.display.update()


    if character_load:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame > 7:
                frame = 0
        
        canvas.fill(white)
        canvas.blit(config, (0,0))

        if current_features != char_features:
            current_features = char_features.copy()
            animation_front = spritesheet.update_assets(char_features)

        pos = pygame.mouse.get_pos()

        for animation in animation_front:
            canvas.blit(animation[frame], (char_x, 50))
        for animation in clothe_front:
            canvas.blit(animation[frame], (char_x, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

            if event.type == pygame.MOUSEBUTTONUP:
                if minus_skin.collidepoint(pos[0], pos[1]):
                    pygame.mixer.Sound.play(button_sound)
                    char_features['body'] -= 1
                    if char_features['body'] < 0:
                        char_features['body'] = 7
                elif minus_hairstyle.collidepoint(pos[0], pos[1]):
                    pygame.mixer.Sound.play(button_sound)
                    char_features['hair'] -= 1
                    if char_features['hair'] < 0:
                        char_features['hair'] = 14
                elif minus_haircolor.collidepoint(pos[0], pos[1]):
                    pygame.mixer.Sound.play(button_sound)
                    char_features['hair_colour'] -= 1
                    if char_features['hair_colour'] < 0:
                        char_features['hair_colour'] = 13
                elif minus_eye.collidepoint(pos[0], pos[1]):
                    pygame.mixer.Sound.play(button_sound)
                    char_features['eye'] -= 1
                    if char_features['eye'] < 0:
                        char_features['eye'] = 13
                elif plus_skin.collidepoint(pos[0], pos[1]):
                    pygame.mixer.Sound.play(button_sound)
                    char_features['body'] += 1
                    if char_features['body'] > 7:
                        char_features['body'] = 0
                elif plus_hairstyle.collidepoint(pos[0], pos[1]):
                    pygame.mixer.Sound.play(button_sound)
                    char_features['hair'] += 1
                    if char_features['hair'] > 14:
                        char_features['hair'] = 0
                elif plus_haircolor.collidepoint(pos[0], pos[1]):
                    pygame.mixer.Sound.play(button_sound)
                    char_features['hair_colour'] += 1
                    if char_features['hair_colour'] > 13:
                        char_features['hair_colour'] = 0
                elif plus_eye.collidepoint(pos[0], pos[1]):
                    pygame.mixer.Sound.play(button_sound)
                    char_features['eye'] += 1
                    if char_features['eye'] > 13:
                        char_features['eye'] = 0
                elif set_name.collidepoint(pos[0], pos[1]):
                    pygame.mixer.Sound.play(button_sound)
                    character_load = False
                    buddy_name = True

                    BODY_TYPE = char_features['body'] 
                    HAIR_TYPE = char_features['hair'] 
                    HAIR_COLOUR = char_features['hair_colour'] 
                    EYE_TYPE = char_features['eye']

                    sprite_sheet_image = pygame.image.load(f"Character/characters/char{BODY_TYPE+1}.png").convert_alpha()
                    hair_image = pygame.image.load(f"Character/hair/hair{HAIR_TYPE}.png").convert_alpha()
                    eye_image = pygame.image.load("Character/eyes/eyes.png").convert_alpha()
                    blush_image = pygame.image.load("Character/eyes/blush_all.png").convert_alpha()

                    sprite_hair_image = pygame.Surface((32*8, 1568)).convert_alpha()
                    sprite_hair_image.blit(hair_image, (0, 0), (32*8*HAIR_COLOUR, 0, 32*8*(HAIR_COLOUR+1), 1568))

                    sprite_eye_image = pygame.Surface((32*8, 1568)).convert_alpha()
                    sprite_eye_image.blit(eye_image, (0, 0), (32*8*EYE_TYPE, 0, 32*8*(EYE_TYPE+1), 1568))

                    sprite_blush_image = pygame.Surface((32*8, 1568)).convert_alpha()
                    sprite_blush_image.blit(blush_image, (0, 0), (0, 0, 32*8, 1568))

                    sprite_list_right = [
                        spritesheet.SpriteSheet(sprite_sheet_image, 2),
                        spritesheet.SpriteSheet(sprite_hair_image, 2),
                        spritesheet.SpriteSheet(sprite_eye_image, 2),
                        spritesheet.SpriteSheet(sprite_blush_image, 2),
                    ]
                    sprite_list_left = [
                        spritesheet.SpriteSheet(sprite_sheet_image, 3),
                        spritesheet.SpriteSheet(sprite_hair_image, 3),
                        spritesheet.SpriteSheet(sprite_eye_image, 3),
                        spritesheet.SpriteSheet(sprite_blush_image, 3),
                    ]
                    sprite_list_front = [
                        spritesheet.SpriteSheet(sprite_sheet_image, 0),
                        spritesheet.SpriteSheet(sprite_hair_image, 0),
                        spritesheet.SpriteSheet(sprite_eye_image, 0),
                        spritesheet.SpriteSheet(sprite_blush_image, 0),
                    ]
                    sprite_list_back = [
                        spritesheet.SpriteSheet(sprite_sheet_image, 1),
                        spritesheet.SpriteSheet(sprite_hair_image, 1),
                        spritesheet.SpriteSheet(sprite_eye_image, 1),
                        spritesheet.SpriteSheet(sprite_blush_image, 1),
                    ]

                    animation_list_right = []
                    animation_list_left = []
                    animation_list_front = []
                    animation_list_back = []
                    animation_steps = 8

                    #emojis
                    for x in range(1, 7):
                        emoji_list.append(emoji.get_image(x, 16, 16, 4))

                    for x in range(1, 5):
                        computer_animation.append(screen.get_image(x, 16, 16, 5))
                    for x in range(1, 5):
                        computer_animation.append(screen2.get_image(x, 16, 16, 5))

                    for asset in sprite_list_right:
                        new_animation = []
                        for x in range(animation_steps):
                            new_animation.append(asset.get_image(x, 32, 32, 5))
                        animation_list_right.append(new_animation)

                    for asset in sprite_list_left:
                        new_animation = []
                        for x in range(animation_steps):
                            new_animation.append(asset.get_image(x, 32, 32, 5))
                        animation_list_left.append(new_animation)

                    for asset in sprite_list_front:
                        new_animation = []
                        for x in range(animation_steps):
                            new_animation.append(asset.get_image(x, 32, 32, 5))
                        animation_list_front.append(new_animation)

                    for asset in sprite_list_back:
                        new_animation = []
                        for x in range(animation_steps):
                            new_animation.append(asset.get_image(x, 32, 32, 5))
                        animation_list_back.append(new_animation)


        pygame.display.update()

    if buddy_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.Sound.play(celebrate)
                        name = char_names
                        buddy_name = False
                        game_start = True
                        text = fontObj.render(name, True, (240,240,240))
                    elif event.key == pygame.K_BACKSPACE:
                        char_names = char_names[:-1]
                    else:
                        char_names += event.unicode

        canvas.fill(white)
        canvas.blit(name_buddy_screen, (0,0))
        # Render the current text.
        txt_surface = fontObj.render(char_names, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        canvas.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(canvas, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


    if game_start:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame > 7:
                frame = 0
        
        health = pygame.transform.scale(health, (66 * ((char.health * 3)/100), 4 * 3))
        
        if char.health > 80:
            char.happiness = 0
        elif char.health > 60:
            char.happiness = 1
        elif char.health > 50:
            char.happiness = 2
        elif char.health > 30:
            char.happiness = 3
        elif char.health > 10:
            char.happiness = 4
        elif char.health > 0:
            char.happiness = 5
        
        canvas.fill(brown)
        canvas.blit(room, (270, -30))

        canvas.blit(first_line, (1000, 50))
        money_balance = fontObjsml.render(f"{char.coins} Study Bucks", True, (240,240,240))
        canvas.blit(money_balance, (1000, 100))    
        canvas.blit(tip1, (1000, 250))    
        canvas.blit(tip2, (1000, 300))
        canvas.blit(tip3, (1000, 350))    
        canvas.blit(tip4, (1000, 400))
        canvas.blit(tip5, (1000, 450))

        canvas.blit(computer, (405, 150))
        canvas.blit(computer_animation[frame], (405, 150))

        canvas.blit(text, (90, 18))

        canvas.blit(emoji_list[char.happiness], (20,20))

        canvas.blit(health, (80, 121))
        canvas.blit(bar, (20, 100))

        if target == total:
            target += 30
            sale_items = [all_items[random.randint(0, len(all_items)-1)], all_items[random.randint(0, len(all_items)-1)], all_items[random.randint(0, len(all_items)-1)], all_items[random.randint(0, len(all_items)-1)]]

        image_set = char.clothing

        if image_set == current_items:
            pass
        else:
            current_items = image_set.copy()
            clothe_right, clothe_left, clothe_front, clothe_back = spritesheet.animate(image_set)

        if still:
            if left:
                for animation in animation_list_left:
                    canvas.blit(animation[0], (char_x, char_y))
                for animation in clothe_left:
                    canvas.blit(animation[0], (char_x, char_y))
            elif right:
                for animation in animation_list_right:
                    canvas.blit(animation[0], (char_x, char_y))
                for animation in clothe_right:
                    canvas.blit(animation[0], (char_x, char_y))
            elif front:
                for animation in animation_list_front:
                    canvas.blit(animation[0], (char_x, char_y))
                for animation in clothe_front:
                    canvas.blit(animation[0], (char_x, char_y))
            elif back:
                for animation in animation_list_back:
                    canvas.blit(animation[0], (char_x, char_y))
                for animation in clothe_back:
                    canvas.blit(animation[0], (char_x, char_y))
        else:
            if left:
                for animation in animation_list_left:
                    canvas.blit(animation[frame], (char_x, char_y))
                for animation in clothe_left:
                    canvas.blit(animation[frame], (char_x, char_y))
            elif right:
                for animation in animation_list_right:
                    canvas.blit(animation[frame], (char_x, char_y))
                for animation in clothe_right:
                    canvas.blit(animation[frame], (char_x, char_y))
            elif front:
                for animation in animation_list_front:
                    canvas.blit(animation[frame], (char_x, char_y))
                for animation in clothe_front:
                    canvas.blit(animation[frame], (char_x, char_y))
            elif back:
                for animation in animation_list_back:
                    canvas.blit(animation[frame], (char_x, char_y))
                for animation in clothe_back:
                    canvas.blit(animation[frame], (char_x, char_y))
            
        # button icons

        # get mouse position
        pos = pygame.mouse.get_pos()


        if study_section.collidepoint(char_x+80, char_y+140) and not timer:
            canvas.blit(study_sign, (500, 10))

        if store_section.collidepoint(char_x+80, char_y+140):
            SCREEN_HEIGHT = 475
            SCREEN_WIDTH = 600
            shop = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
 
            
            SCALE = 5

            BALANCE = 100

            # load images for buttons
            clownmaskpic = pygame.image.load('clownmask.png').convert_alpha()
            cowboypic = pygame.image.load('cowboy.png').convert_alpha()
            dresspic = pygame.image.load('dress.png').convert_alpha()
            overallspic = pygame.image.load('overalls.png').convert_alpha()
            pantssuitpic = pygame.image.load('pantssuit.png').convert_alpha()
            pumpkinpic = pygame.image.load('pumpkin.png').convert_alpha()
            sailorpic = pygame.image.load('sailor.png').convert_alpha()
            suitpic = pygame.image.load('suit.png').convert_alpha()

            sailor = pygame.Surface((32, 32)).convert_alpha()
            sailor.blit(sailorpic, (0, 0), (73*32, 0*32, 74*32, 1*32))
                                    # L1  H1   L2   H2
                                    # 6   17   7    18
            sailor = pygame.transform.scale(sailor, (32*6, 32*6))

            clownmask = pygame.Surface((32, 32)).convert_alpha()
            clownmask.blit(clownmaskpic, (0, 0), (0*32, 0*32, 1*32, 1*32))
            clownmask = pygame.transform.scale(clownmask, (32*4, 32*4))

            pantssuit = pygame.Surface((32, 32)).convert_alpha()
            pantssuit.blit(pantssuitpic, (0, 0), (8*32, 0*32, 9*32, 1*32))
            pantssuit = pygame.transform.scale(pantssuit, (32*6, 32*12))

            cowboy = pygame.Surface((32, 32)).convert_alpha()
            cowboy.blit(cowboypic, (0, 0), (0*32, 0*32, 1*32, 1*32))
            cowboy = pygame.transform.scale(cowboy, (32*SCALE, 32*SCALE))

            overalls = pygame.Surface((32, 32)).convert_alpha()
            overalls.blit(overallspic, (0, 0), (20*32, 8*32, 21*32, 9*32))
            overalls = pygame.transform.scale(overalls, (32*SCALE, 32*SCALE))

            pumpkin = pygame.Surface((32, 32)).convert_alpha()
            pumpkin.blit(pumpkinpic, (0, 0), (0*32, 0*32, 1*32, 1*32))
            pumpkin = pygame.transform.scale(pumpkin, (32*SCALE, 32*SCALE))

            dress = pygame.Surface((32, 32)).convert_alpha()
            dress.blit(dresspic, (0, 0), (48*32, 0*32, 49*32, 1*32))
            dress = pygame.transform.scale(dress, (32*SCALE, 32*SCALE))

            suit = pygame.Surface((32, 32)).convert_alpha()
            suit.blit(suitpic, (0, 0), (0*32, 0*32, 1*32, 1*32))
            suit = pygame.transform.scale(suit, (32*SCALE, 32*SCALE))

            sailor_label = Label(77, 195, ' $30 ')
            sailor_button = Button(5, 1, sailor, 30, 'sailor', 'shirt')
                                # C    R
            clownmask_label = Label(205, 195, ' $30 ')
            clownmask_button = Button(170, 75, clownmask, 30, 'mask_clown_blue', 'hat')
            pumpkin_label = Label(340, 195, ' $40 ')
            pumpkin_button = Button(290, 70, pumpkin, 40, 'hat_pumpkin', 'hat')
            cowboy_label = Label(469, 195, ' $40 ')
            cowboy_button = Button(415, 65, cowboy, 40, 'hat_cowboy', 'hat')

            pantssuit_label = Label(69, 400, ' $40 ')
            pantssuit_button = Button(1, 5, pantssuit, 40, 'pants_suit', 'pants')
            overalls_label = Label(205, 400, ' $50 ')
            overalls_button = Button(153, 240, overalls, 50, 'overalls', 'shirt')
            dress_label = Label(347, 400, ' $50 ')
            dress_button = Button(295, 225, dress, 50, 'dress', 'shirt')
            suit_label = Label(467, 400, ' $50 ')
            suit_button = Button(415, 232, suit, 50, 'suit', 'shirt')

            clothes_label = Label(25, 15, 'Clothes')

                
            shop.fill((209, 237, 242))
            clothes_label.label()
            sailor_label.pricelabel()
            sailor_button.draw()
            clownmask_label.pricelabel()
            clownmask_button.draw()
            pumpkin_label.pricelabel()
            pumpkin_button.draw()
            cowboy_label.pricelabel()
            cowboy_button.draw()

            pantssuit_label.pricelabel()
            pantssuit_button.draw()
            overalls_label.pricelabel()
            overalls_button.draw()
            suit_label.pricelabel()
            dress_label.pricelabel()
            dress_button.draw()
            suit_label.pricelabel()
            suit_button.draw()

            canvas.blit(shop, (0,0))

        if vending_section.collidepoint(char_x+80, char_y+140):
            SCREEN_HEIGHT = 475
            SCREEN_WIDTH = 600
            shop = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
            SCALE = 4

            BALANCE = 100

            # load images for buttons
            icon = pygame.image.load('baricon.png').convert_alpha()

            apple = pygame.Surface((32, 32)).convert_alpha()
            apple.blit(icon, (0, 0), (192, 544, 244, 576))
                                    # L1  H1   L2   H2
                                    # 6   17   7    18
            apple = pygame.transform.scale(apple, (32*SCALE, 32*SCALE))

            carrot = pygame.Surface((32, 32)).convert_alpha()
            carrot.blit(icon, (0, 0), (10*32, 18*32, 11*32, 19*32))
            carrot = pygame.transform.scale(carrot, (32*3.5, 32*3.5))

            pizza = pygame.Surface((32, 32)).convert_alpha()
            pizza.blit(icon, (0, 0), (3*32, 15*32, 11*32, 4*32))
            pizza = pygame.transform.scale(pizza, (32*SCALE, 32*SCALE))

            iceblock = pygame.Surface((32, 32)).convert_alpha()
            iceblock.blit(icon, (0, 0), (8*32, 13*32, 9*32, 14*32))
            iceblock = pygame.transform.scale(iceblock, (32*SCALE, 32*SCALE))

            coffee = pygame.Surface((32, 32)).convert_alpha()
            coffee.blit(icon, (0, 0), (10*32, 14*32, 11*32, 15*32))
            coffee = pygame.transform.scale(coffee, (32*3.5, 32*3.5))

            fries = pygame.Surface((32, 32)).convert_alpha()
            fries.blit(icon, (0, 0), (5*32, 15*32, 6*32, 16*32))
            fries = pygame.transform.scale(fries, (32*SCALE, 32*SCALE))

            sushi = pygame.Surface((32, 32)).convert_alpha()
            sushi.blit(icon, (0, 0), (10*32, 16*32, 11*32, 17*32))
            sushi = pygame.transform.scale(sushi, (32*SCALE, 32*SCALE))

            burger = pygame.Surface((32, 32)).convert_alpha()
            burger.blit(icon, (0, 0), (2*32, 15*32, 11*32, 3*32))
            burger = pygame.transform.scale(burger, (32*3.5, 32*3.5))


            apple_label = Label(77, 195, ' $10 ')
            apple_button = Button(50, 75, apple, 10, 'apple', None)
                                # C    R
            carrot_label = Label(205, 195, ' $10 ')
            carrot_button = Button(175, 75, carrot, 10, 'carrot', None)
            fries_label = Label(340, 195, ' $10 ')
            fries_button = Button(300, 70, fries, 10, 'fries', None)
            iceblock_label = Label(469, 195, ' $10 ')
            iceblock_button = Button(425, 65, iceblock, 10, 'iceblock', None)

            pizza_label = Label(69, 400, ' $20 ')
            pizza_button = Button(35, 275, pizza, 20, 'pizza', None)
            coffee_label = Label(205, 400, ' $20 ')
            coffee_button = Button(190, 275, coffee, 20, 'coffee', None)
            sushi_label = Label(340, 400, ' $30 ')
            sushi_button = Button(310, 275, sushi, 30, 'sushi', None)
            burger_label = Label(467, 400, ' $30 ')
            burger_button = Button(440, 275, burger, 30, 'burger', None)

            food_label = Label(25, 15, 'Food')

            
            shop.fill((245, 242, 208))
            balance = Label(400, 25, ' Health: ' + str(char.health) + '/100 ')
            balance.balance()
            food_label.label()
            apple_label.pricelabel()
            apple_button.draw()
            carrot_label.pricelabel()
            carrot_button.draw()
            fries_label.pricelabel()
            fries_button.draw()
            iceblock_label.pricelabel()
            iceblock_button.draw()

            pizza_label.pricelabel()
            pizza_button.draw()
            coffee_label.pricelabel()
            coffee_button.draw()
            burger_label.pricelabel()
            sushi_label.pricelabel()
            sushi_button.draw()
            burger_label.pricelabel()
            burger_button.draw()

            canvas.blit(shop, (0,0))

        
        if inventory_section.collidepoint(char_x+80, char_y+140):
            canvas.blit(inventory_sign, (630, 0))
            inventory_list = []
            counterer = 0
            for i in char.inventory:
                inventory_list.append(pygame.Rect(634 + 36*counterer, 5, 36, 36))
                if i.type == 'shirt':
                    canvas.blit(i.get_pic(), (634 + 35*counterer - 20, -30))
                elif i.type == 'pants':
                    canvas.blit(i.get_pic(), (634 + 35*counterer - 20, -50))
                else:
                    canvas.blit(i.get_pic(), (634 + 35*counterer - 20, -20))
                counterer += 1
        



        # stores keys pressed 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and char_x > 320:
            timer = False
            frame_count = 0
            frame_rate = 60
            if char_x < 540 and char_y < 160:
                if char_x < 539:
                    char_x -= velocity
                    left = True
                    front = False
                    back = False
                    right = False
                    still = False
            else:
                char_x -= velocity
                left = True
                front = False
                back = False
                right = False
                still = False

        if keys[pygame.K_d] and char_x < 830:
            timer = False
            frame_count = 0
            frame_rate = 60
            char_x += velocity
            left = False
            right = True
            front = False
            back = False
            still = False

        if keys[pygame.K_w] and char_y > 120:
            timer = False
            frame_count = 0
            frame_rate = 60
            if char_x < 540 and char_y < 160:
                pass
            else:
                char_y -= velocity
                front = False
                left = False
                back = True
                right = False
                still = False
            
        if keys[pygame.K_s] and char_y < 490:
            timer = False
            frame_count = 0
            frame_rate = 60
            char_y += velocity
            front = True
            left = False
            right = False
            back = False
            still = False


        if timer:
            total_seconds = frame_count // frame_rate
            if total_seconds // 60 > minutes:
                char.coins += 1
                total += 1
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "Study Time: {0:02}:{1:02}".format(minutes, seconds)
            prefix_clock = fontObjsml.render(f"Your buddy is studying, you should too!", True, (white))
            clock_text = fontObj.render(output_string, True, (white))
            canvas.blit(prefix_clock, [405, 320])
            canvas.blit(clock_text, [470, 350])

            frame_count += 1
            clock.tick(frame_rate)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYUP:
                still = True
                if event.key == pygame.K_y and study_section.collidepoint(char_x+80, char_y+140):
                    pygame.mixer.Sound.play(celebrate)
                    timer = True
            if event.type == pygame.MOUSEBUTTONUP:
                if store_section.collidepoint(char_x+80, char_y+140):
                    if space_1.collidepoint(pos[0], pos[1]):
                        if sale_items[0].get_price() <= char.coins:
                            pygame.mixer.Sound.play(purchase)
                            sale_items[0].fnc(char)
                            char.coins -= sale_items[0].get_price()
                    elif space_2.collidepoint(pos[0], pos[1]):
                        if sale_items[1].get_price() <= char.coins:
                            pygame.mixer.Sound.play(purchase)
                            sale_items[1].fnc(char)
                            char.coins -= sale_items[1].get_price()
                    elif space_3.collidepoint(pos[0], pos[1]):
                        if sale_items[2].get_price() <= char.coins:
                            pygame.mixer.Sound.play(purchase)
                            sale_items[2].fnc(char)
                            char.coins -= sale_items[2].get_price()
                    elif space_4.collidepoint(pos[0], pos[1]):
                        if sale_items[3].get_price() <= char.coins:
                            pygame.mixer.Sound.play(purchase)
                            sale_items[3].fnc(char)
                            char.coins -= sale_items[3].get_price()
                    
                if inventory_section.collidepoint(char_x+80, char_y+140):
                    for idx in range(len(char.inventory)):
                        if inventory_list[idx].collidepoint(pos[0], pos[1]):
                            pygame.mixer.Sound.play(equip)
                            char.inventory[idx].use(char)
            

    pygame.display.update()
