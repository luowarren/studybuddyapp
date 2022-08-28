import pygame

class SpriteSheet:
    def __init__(self, image, idx):
        self.image = image
        self.idx = idx

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.image, (0, 0), ((frame * width), (self.idx * height), (frame * width) + width, (self.idx * height) + height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        return image

image_set = {
    'hat': 'hat_pumpkin',
    'shirt': 'suit',
    'pants': 'suit_pants',
}

def animate(image_set):

    if image_set['hat']:
        sprite_hat_image = pygame.image.load(f"Character/acc/{image_set['hat']}.png").convert_alpha()

    shirt_image = pygame.image.load(f"Character/clothes/{image_set['shirt']}.png").convert_alpha()
    sprite_shirt_image = pygame.Surface((32*8, 1568)).convert_alpha()
    if image_set['shirt'] == 'overalls':
        sprite_shirt_image.blit(shirt_image, (0, 0), (32*8*1, 0, 32*8*(1+1), 1568))
    elif image_set['shirt'] == 'dress':
        sprite_shirt_image.blit(shirt_image, (0, 0), (32*8*6, 0, 32*8*(1+6), 1568))
    elif image_set['shirt'] == 'sailor':
        sprite_shirt_image.blit(shirt_image, (0, 0), (32*8*9, 0, 32*8*(1+9), 1568))
    else:
        sprite_shirt_image.blit(shirt_image, (0, 0), (32*8*0, 0, 32*8*(1+0), 1568))

    pants_image = pygame.image.load(f"Character/clothes/{image_set['pants']}.png").convert_alpha()
    pants_shirt_image = pygame.Surface((32*8, 1568)).convert_alpha()
    pants_shirt_image.blit(pants_image, (0, 0), (32*8*0, 0, 32*8*(1+0), 1568))

    sprite_shoes_image = pygame.image.load("Character/clothes/shoes.png").convert_alpha()
    
    if image_set['hat']:
        sprite_list_right = [
            SpriteSheet(sprite_hat_image, 2),
            SpriteSheet(pants_shirt_image, 2),
            SpriteSheet(sprite_shirt_image, 2),
            SpriteSheet(sprite_shoes_image, 2),
        ]
        sprite_list_left = [
            SpriteSheet(sprite_hat_image, 3),
            SpriteSheet(pants_shirt_image, 3),
            SpriteSheet(sprite_shirt_image, 3),
            SpriteSheet(sprite_shoes_image, 3),
        ]
        sprite_list_front = [
            SpriteSheet(sprite_hat_image, 0),
            SpriteSheet(pants_shirt_image, 0),
            SpriteSheet(sprite_shirt_image, 0),
            SpriteSheet(sprite_shoes_image, 0),
        ]
        sprite_list_back = [
            SpriteSheet(sprite_hat_image, 1),
            SpriteSheet(pants_shirt_image, 1),
            SpriteSheet(sprite_shirt_image, 1),
            SpriteSheet(sprite_shoes_image, 1),
        ]
    else:
        sprite_list_right = [
            SpriteSheet(pants_shirt_image, 2),
            SpriteSheet(sprite_shirt_image, 2),
            SpriteSheet(sprite_shoes_image, 2),
        ]
        sprite_list_left = [
            SpriteSheet(pants_shirt_image, 3),
            SpriteSheet(sprite_shirt_image, 3),
            SpriteSheet(sprite_shoes_image, 3),
        ]
        sprite_list_front = [
            SpriteSheet(pants_shirt_image, 0),
            SpriteSheet(sprite_shirt_image, 0),
            SpriteSheet(sprite_shoes_image, 0),
        ]
        sprite_list_back = [
            SpriteSheet(pants_shirt_image, 1),
            SpriteSheet(sprite_shirt_image, 1),
            SpriteSheet(sprite_shoes_image, 1),
        ]

    animation_list_right = []
    animation_list_left = []
    animation_list_front = []
    animation_list_back = []
    animation_steps = 8

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

    return animation_list_right, animation_list_left, animation_list_front, animation_list_back


char_features = {
    'body': 0,
    'hair': 0,
    'hair_colour': 0,
    'eye': 0,
}

def update_assets(char_features):
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

    sprite_list_front = [
        SpriteSheet(sprite_sheet_image, 0),
        SpriteSheet(sprite_hair_image, 0),
        SpriteSheet(sprite_eye_image, 0),
        SpriteSheet(sprite_blush_image, 0),
    ]

    animation_list_front = []
    animation_steps = 8

    for asset in sprite_list_front:
        new_animation = []
        for x in range(animation_steps):
            new_animation.append(asset.get_image(x, 32, 32, 5))
        animation_list_front.append(new_animation)
    
    return animation_list_front