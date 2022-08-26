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
    myfont = pygame.font.SysFont('Calibri', 20)
    pygame.draw.rect(win, highlight_colour_blue, (200, 270, 300, 100)) #position, x and y dimension
    hour = myfont.render(str("hr             min            sec"), True, text_colour)
    win.blit(hour, (252, 337))    
    pygame.display.update()
    value = myfont.render(str("S T U D Y  T I M E R"), True, text_colour)
    win.blit(value, (200, 245))
    pygame.display.update()
    pygame.draw.circle(win, highlight_colour_blue, (300, 100), 10)
    pygame.draw.circle(win, highlight_colour_blue, (200, 270), 10)

    
    while True: 
        for event in pygame.event.get(): 
            timerfont = pygame.font.SysFont('Calibri', 70) 
            timervalue = timerfont.render(str("00:00:00"), True, text_colour)
            win.blit(timervalue, (225,280))
            pygame.display.update()              
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()