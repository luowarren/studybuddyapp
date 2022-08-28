
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
velocity = 1.5
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

moving_land = pygame.image.load(f"land.png").convert_alpha()

move_landing = spritesheet.SpriteSheet(moving_land, 0)

animation_step = 5

land_animation = []
for x in range(animation_step):
    land_animation.append(move_landing.get_image(x, 720, 133, 2))

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


BODY_TYPE = char_features['body'] 
HAIR_TYPE = char_features['hair'] 
HAIR_COLOUR = char_features['hair_colour'] 
EYE_TYPE = char_features['eye']

sprite_sheet_image = pygame.image.load(f"Character/characters/char1.png").convert_alpha()
hair_image = pygame.image.load(f"Character/hair/hair0.png").convert_alpha()
eye_image = pygame.image.load("Character/eyes/eyes.png").convert_alpha()
blush_image = pygame.image.load("Character/eyes/blush_all.png").convert_alpha()

sprite_hair_image = pygame.Surface((32*8, 1568)).convert_alpha()
sprite_hair_image.blit(hair_image, (0, 0), (32*8*HAIR_COLOUR, 0, 32*8*(HAIR_COLOUR+1), 1568))

sprite_eye_image = pygame.Surface((32*8, 1568)).convert_alpha()
sprite_eye_image.blit(eye_image, (0, 0), (32*8*EYE_TYPE, 0, 32*8*(EYE_TYPE+1), 1568))

sprite_blush_image = pygame.Surface((32*8, 1568)).convert_alpha()
sprite_blush_image.blit(blush_image, (0, 0), (0, 0, 32*8, 1568))

sprite_list_left = [
    spritesheet.SpriteSheet(sprite_sheet_image, 3),
    spritesheet.SpriteSheet(sprite_hair_image, 3),
    spritesheet.SpriteSheet(sprite_eye_image, 3),
    spritesheet.SpriteSheet(sprite_blush_image, 3),
]


animation_list_left = []
animation_steps = 8

#emojis

for asset in sprite_list_left:
    new_animation = []
    for x in range(animation_steps):
        new_animation.append(asset.get_image(x, 32, 32, 10))
    animation_list_left.append(new_animation)

image_set = char.clothing
clothe_right, clothe_left, clothe_front, clothe_back = spritesheet.animate(image_set)


frame1 = 0
last_update1 = pygame.time.get_ticks()

while not exit:
    # update animation
    if game_menu:
        current_time1 = pygame.time.get_ticks()
        if current_time1 - last_update1 >= 200:
            frame1 += 1
            last_update1 = current_time1
            if frame1 > 4:
                frame1 = 0
        
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= 200:
            frame += 1
            last_update = current_time
            if frame > 7:
                frame = 0

        canvas.fill(white)
        canvas.blit(intro, (0,0))

        canvas.blit(land_animation[frame1], (0, 580))

        for animation in animation_list_left:
            canvas.blit(animation[frame], (900, 280))

        for animation in clothe_left:
            canvas.blit(animation[frame], (900, 280))

        


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
        print(pos)

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
            canvas.blit(store_sign, (0, 400))

            for i in range(4):
                if sale_items[i].type == 'shirt':
                    canvas.blit(sale_items[i].get_pic(), (slot_list[i][0], slot_list[i][1]-30))
                elif sale_items[i].type == 'pants':
                    canvas.blit(sale_items[i].get_pic(), (slot_list[i][0], slot_list[i][1]-50))
                else:
                    canvas.blit(sale_items[i].get_pic(), (slot_list[i][0], slot_list[i][1]))
        
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




