from cgitb import text
from tkinter import Spinbox
import pygame
import spritesheet  

pygame.init()
white = (31, 22, 16)
  
# CREATING CANVAS
canvas = pygame.display.set_mode((1280, 720))
  
# TITLE OF CANVAS
pygame.display.set_caption("Study Buddies")
exit = False


# Character
char_x = 570
char_y = 250
velocity = 0.5
still = True
left = False
right = False
front = True
back = False

# Char Object
mood = 0
name = "Timmy"
heal = 50


#fonts
fontObj = pygame.font.Font('fonts/pixel.ttf', 40)
text = fontObj.render(name, True, (240,240,240))

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
health = pygame.transform.scale(health, (66 * ((heal * 3)/100), 4 * 3))


# background
room = pygame.image.load("char/1.png").convert_alpha()
room = spritesheet.SpriteSheet(room, 0)
room = room.get_image(0, 700, 700, 1.1)

# Icons
icon = pygame.image.load("baricon/baricon.png").convert_alpha()

apple = pygame.Surface((32, 32)).convert_alpha()
apple.blit(icon, (0, 0), (192, 544, 224, 576))
apple = pygame.transform.scale(apple, (32 * 2, 32 * 2))

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
    'hair': 5,
    'hair_colour': 1,
    'eye': 1,
}


# SPRITE SHEET
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


# create timer
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0


# creating animation list
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

image_set = {
        'hat': 'hat_pumpkin',
        'shirt': 'suit',
        'pants': 'pants_suit',
    }

current_items = image_set
clothe_right, clothe_left, clothe_front, clothe_back = spritesheet.animate(image_set)


while not exit:
    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame > 7:
            frame = 0
        
    canvas.fill(white)
    canvas.blit(room, (270, -30))

    canvas.blit(computer, (405, 150))
    canvas.blit(computer_animation[frame], (405, 150))

    canvas.blit(text, (90, 18))

    canvas.blit(emoji_list[mood], (20,20))

    canvas.blit(health, (80, 121))
    canvas.blit(bar, (20, 100))

    image_set = {
        'hat': 'hat_pumpkin',
        'shirt': 'suit',
        'pants': 'pants_suit',
    }

    if image_set == current_items:
        pass
    else:
        current_items = image_set
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

    # stores keys pressed 
    keys = pygame.key.get_pressed()
    



    if keys[pygame.K_a] and char_x > 320:
        char_x -= velocity
        left = True
        front = False
        back = False
        right = False
        still = False

    if keys[pygame.K_d] and char_x < 830:
        char_x += velocity
        left = False
        right = True
        front = False
        back = False
        still = False

    if keys[pygame.K_w] and char_y > 100:
        char_y -= velocity
        front = False
        left = False
        back = True
        right = False
        still = False
        
    if keys[pygame.K_s] and char_y < 490:
        char_y += velocity
        front = True
        left = False
        right = False
        back = False
        still = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYUP:
            still = True

    pygame.display.update()




