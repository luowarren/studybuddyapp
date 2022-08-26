import pygame
import spritesheet  

pygame.init()
white = (31, 22, 16)
  
# CREATING CANVAS
canvas = pygame.display.set_mode((1280, 720))
  
# TITLE OF CANVAS
pygame.display.set_caption("Study Buddies")
exit = False

# buttons
buttons = pygame.image.load("char/icons.png").convert_alpha()
button = spritesheet.SpriteSheet(buttons, 5)
next = button.get_image(1, 16, 16, 5)
prev = button.get_image(2, 16, 16, 5)


# Sprite
char_x = 570
char_y = 250
velocity = 0.5
still = True
left = True

# background
room = pygame.image.load("char/1.png").convert_alpha()
room = spritesheet.SpriteSheet(room, 0)
room = room.get_image(0, 700, 700, 1.1)

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
char_clothe = {
    'body': 0,
    'hair': 2,
    'hat': 4,
    'shirt': 6,
    'pants': 8,
    'shoes': 10,
}

# SPRITE SHEET
sprite_sheet_image = pygame.image.load("char/global.png").convert_alpha()
sprite_list_right = []
sprite_list_left = []
for j in char_clothe.values():
    if j is None:
        pass
    else:
        sprite_list_right.append(spritesheet.SpriteSheet(sprite_sheet_image, j))
        sprite_list_left.append(spritesheet.SpriteSheet(sprite_sheet_image, j+1))

# create timer
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0


# creating animation list
animation_list_right = []
animation_list_left = []
animation_steps = 8

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

    if still:
        if left:
            for animation in animation_list_left:
                canvas.blit(animation[0], (char_x, char_y))
        else:
            for animation in animation_list_right:
                canvas.blit(animation[0], (char_x, char_y))
    else:
        if left:
            for animation in animation_list_left:
                canvas.blit(animation[frame], (char_x, char_y))
        else:
            for animation in animation_list_right:
                canvas.blit(animation[frame], (char_x, char_y))
        
    # button icons

    # get mouse position
    pos = pygame.mouse.get_pos()

    # stores keys pressed 
    keys = pygame.key.get_pressed()
      
    # if left arrow key is pressed
    



    if keys[pygame.K_a] and char_x > 320:
        char_x -= velocity
        left = True
        still = False

    if keys[pygame.K_d] and char_x < 830:
        char_x += velocity
        left = False
        still = False

    if keys[pygame.K_w] and char_y > 100:
        char_y -= velocity
        still = False
        
    if keys[pygame.K_s] and char_y < 490:
        char_y += velocity
        still = False


    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYUP:
            still = True

    pygame.display.update()




