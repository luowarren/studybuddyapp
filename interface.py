import pygame

LENGTH = 720
WIDTH = 480
background_colour = (251,247,245, 128)
text_colour = (52, 31, 151, 128)
highlight_colour_blue = (150,255, 255, 128)
highlight_colour_red = (225, 127, 127, 128)

def main():    
    pygame.init()
    win = pygame.display.set_mode((LENGTH, WIDTH))
    pygame.display.set_caption("Study Buddy App")
    win.fill(background_colour)
    myfont = pygame.font.SysFont('Calibri', 90)
    pygame.draw.rect(win, highlight_colour_blue, (200, 250, 300, 100)) #position, x and y dimension
    pygame.display.update()
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//100, pos[1]//100))
                pygame.display.update()
                
            if event.type == pygame.QUIT:
                pygame.quit()
                return
main()