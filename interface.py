import pygame
pygame.init()

LENGTH = 720
WIDTH = 480
background_colour = (251,247,245, 128)
text_colour = (0,0,0)
highlight_colour_blue = (190, 190, 190)
highlight_colour_red = (225, 127, 127, 128)

def main():    

    pygame.init()
    win = pygame.display.set_mode((LENGTH, WIDTH))
    pygame.display.set_caption("Study Buddy App")
    win.fill(background_colour)
    myfont = pygame.font.SysFont('Calibri', 20)
    hour = myfont.render(str("hr             min            sec"), True, text_colour)
    win.blit(hour, (252, 337))    
    pygame.display.update()
    value = myfont.render(str("S T U D Y  T I M E R"), True, text_colour)
    win.blit(value, (270, 245))
    pygame.display.update()
    pygame.display.set_caption('Play Button')
    pygame.display.set_caption('pause')
    pygame.display.set_caption('reset')
    playbutton = pygame.image.load('Pause.jpg') # if your image is in a folder type 'folder/yourimg.png'
    playbuttonX, playbuttonY = 50, 50

    pause = pygame.image.load(r'C:\Users\natha\Pictures\Pause.jpg')
    reset = pygame.image.load(r'C:\Users\natha\Pictures\Reset Button.jpg')
    pygame.draw.circle(win, highlight_colour_blue, (400, 390), 30)
    pygame.draw.circle(win, highlight_colour_blue, (300, 390), 30)

    
    while True: 
        for event in pygame.event.get(): 
            timerfont = pygame.font.SysFont('Calibri', 70) 
            timervalue = timerfont.render(str("00:00:00"), True, text_colour)
            win.blit(timervalue, (225,280))
            pygame.display.update()
            display_surface.blit(playbutton, (0, 0))              
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()