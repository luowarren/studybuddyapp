
import pygame
import spritesheet 


pygame.init()
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
velocity = 1
still = True
left = False
right = False
front = True
back = False

# Char Object
mood = 0
name = "Timmy"
heal = 100


#fonts
fontObj = pygame.font.Font('fonts/pixel.ttf', 40)

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

# SPRITE SHEET



# create timer
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0


# creating animation list

#emojis
for x in range(1, 7):
    emoji_list.append(emoji.get_image(x, 16, 16, 4))

for x in range(1, 5):
    computer_animation.append(screen.get_image(x, 16, 16, 5))
for x in range(1, 5):
    computer_animation.append(screen2.get_image(x, 16, 16, 5))


image_set = {
        'hat': None,
        'shirt': 'basic',
        'pants': 'pants',
    }

current_items = image_set
clothe_right, clothe_left, clothe_front, clothe_back = spritesheet.animate(image_set)


study_section = pygame.Rect(594, 229, 695-594, 306-229)
study_sign = pygame.image.load("oin.png").convert_alpha()
study_sign = pygame.transform.scale(study_sign, (500 * 0.5, 300 * 0.5))
timer = False

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
                    char_features['body'] -= 1
                    if char_features['body'] < 0:
                        char_features['body'] = 7
                elif minus_hairstyle.collidepoint(pos[0], pos[1]):
                    char_features['hair'] -= 1
                    if char_features['hair'] < 0:
                        char_features['hair'] = 14
                elif minus_haircolor.collidepoint(pos[0], pos[1]):
                    char_features['hair_colour'] -= 1
                    if char_features['hair_colour'] < 0:
                        char_features['hair_colour'] = 13
                elif minus_eye.collidepoint(pos[0], pos[1]):
                    char_features['eye'] -= 1
                    if char_features['eye'] < 0:
                        char_features['eye'] = 13
                elif plus_skin.collidepoint(pos[0], pos[1]):
                    char_features['body'] += 1
                    if char_features['body'] > 7:
                        char_features['body'] = 0
                elif plus_hairstyle.collidepoint(pos[0], pos[1]):
                    char_features['hair'] += 1
                    if char_features['hair'] > 14:
                        char_features['hair'] = 0
                elif plus_haircolor.collidepoint(pos[0], pos[1]):
                    char_features['hair_colour'] += 1
                    if char_features['hair_colour'] > 13:
                        char_features['hair_colour'] = 0
                elif plus_eye.collidepoint(pos[0], pos[1]):
                    char_features['eye'] += 1
                    if char_features['eye'] > 13:
                        char_features['eye'] = 0
                elif set_name.collidepoint(pos[0], pos[1]):
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
            
        canvas.fill(brown)
        canvas.blit(room, (270, -30))

        canvas.blit(computer, (405, 150))
        canvas.blit(computer_animation[frame], (405, 150))

        canvas.blit(text, (90, 18))

        canvas.blit(emoji_list[mood], (20,20))

        canvas.blit(health, (80, 121))
        canvas.blit(bar, (20, 100))

        image_set = {
            'hat': None,
            'shirt': 'basic',
            'pants': 'pants',
        }

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

        print(char_x, char_y)
        print(pos)

        if study_section.collidepoint(char_x+80, char_y+140):
            canvas.blit(study_sign, (500, 10))


        # stores keys pressed 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and char_x > 320:
            timer = False
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
            char_x += velocity
            left = False
            right = True
            front = False
            back = False
            still = False

        if keys[pygame.K_w] and char_y > 120:
            timer = False
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
            char_y += velocity
            front = True
            left = False
            right = False
            back = False
            still = False


        if timer:
            pass


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYUP:
                still = True
                if event.key == pygame.K_y and study_section.collidepoint(char_x+80, char_y+140):
                    timer = True
            

    pygame.display.update()




