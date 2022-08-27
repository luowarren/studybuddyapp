
import pygame
from pygame.locals import *
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')
pygame.init()

width = 480
height = 240
canvas = pygame.display.set_mode((width, height))

pygame.display.set_caption("Stopwatch: The Game")

fontObj1 = pygame.font.Font(pygame.font.match_font('Calibri'), 64)
fontObj2 = pygame.font.Font(pygame.font.match_font('Calibri'), 24)

gold_color = pygame.Color(255, 215, 0)
dkgold_color = pygame.Color(184, 134, 0)
white_color = pygame.Color(255, 255, 255)

butt1_col = gold_color
butt2_col = gold_color
butt3_col = gold_color

time=0
e=0
success_counter=0
total_attempts=0
flag=0
stop_count=0
started=False
go = False

def format_time(time):
    global e
    e = time
    if (time < 10):
        return "0" + ":" + "00" + "." + str(time)
    elif (time>=10):
        d=time % 10
        c=time // 10
        if(c <= 59):
            if(c < 10):
                # c is single digit
                return "0" + ":" + "0" + str(c) + "." + str(d)
            else: 
                # c is double digit
                return "0" + ":" + str(c) + "." + str(d)
        else:
            a=c // 60
            c=c % 60
            if(c < 10):
                return str(a) + ":" + "0" + str(c) + "." + str(d)
            else:
                return str(a) + ":" + str(c) + "." + str(d)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def time_start():
    global stop_count,started, go
    stop_count=0
    started, go=True, True

# stop button handler
def time_stop():
    global go
    global flag,started
    global stop_count
    global success_counter, total_attempts, e
    if go: 
        go = False
	
    flag=1
    stop_count += 1
    #keeping count of number of times stop button is clicked
    e=e%10
    
    if (flag == 1 and stop_count == 1 and started==True):
        #if more than once stop is clicked then this
        #condition fails as stop_count exceeds 1
        if(e==0):
            success_counter += 1
        total_attempts += 1
    flag=0
	
# reset button handler
def time_reset():
    global success_counter, total_attempts
    global go, started, stop_count, time
    if go:
        go = False
    started=False
    time=00
    stop_count=0
    success_counter=0
    total_attempts=0

# timer handler function
def t_stpw():
    global time
    
    if go:
        time += 1
            

def draw_handler(canvas):


    canvas.fill((0, 0, 0))


    text_stpw = fontObj1.render(format_time(time), True, white_color)
    text_start = fontObj2.render("Start", True, white_color)
    text_stop = fontObj2.render("Stop", True, white_color)
    text_reset = fontObj2.render("Reset", True, white_color)


    text_stpw_sz = fontObj1.size(format_time(time))
    

    canvas.blit(text_stpw, ((width - text_stpw_sz[0] + 80) // 2,
                            (height - text_stpw_sz[1]) // 2))

    # button text drawing
    canvas.blit(text_start, (27, 66))     
    canvas.blit(text_stop, (28, 106))
    canvas.blit(text_reset, (23, 146))
    
    # button rectangles
    pygame.draw.rect(canvas, butt1_col, (10, 68, 80, 25), 1)    
    pygame.draw.rect(canvas, butt2_col, (10, 108, 80, 25), 1)
    pygame.draw.rect(canvas, butt3_col, (10, 148, 80, 25), 1)   
   
    # update the display
    pygame.display.update()


def mc_handler(pos):
    global butt1_col, butt2_col, butt3_col
    #print(pos)
    

    if 10 <= pos[0] <= 90 and 68 <= pos[1] <= 93:
        time_start()
        
        butt1_col = dkgold_color
        pygame.time.set_timer(timer_butt, TIMER_BUTT_ON)

        
    if 10 <= pos[0] <= 90 and 108 <= pos[1] <= 133:
        time_stop()

        butt2_col = dkgold_color
        pygame.time.set_timer(timer_butt, TIMER_BUTT_ON)
        
    if 10 <= pos[0] <= 90 and 148 <= pos[1] <= 173:
        time_reset()

        butt3_col = dkgold_color
        pygame.time.set_timer(timer_butt, TIMER_BUTT_ON)        


def t_butt():
    global butt1_col, butt2_col, butt3_col
    
    if butt1_col == dkgold_color:
        butt1_col = gold_color
        
    if butt2_col == dkgold_color:
        butt2_col = gold_color
        
    if butt3_col == dkgold_color:
        butt3_col = gold_color

    pygame.time.set_timer(timer_butt, TIMER_OFF)

TIMER_OFF = 0

# timer for stopwatch -- 100 milliseconds when on
TIMER_STPW_ON = 100

# set the timer name to its user event for readability
timer_stpw = USEREVENT + 1
# start the timer 
pygame.time.set_timer(timer_stpw, TIMER_STPW_ON)

# timer for button state -- 100 milliseconds when on
TIMER_BUTT_ON = 100

# set the timer name to its user event for readability
timer_butt = USEREVENT + 2

def main():
    # initialize loop until quit variable
    running = True

    clock = pygame.time.Clock()


    while running:
        
        # event queue iteration
        for event in pygame.event.get():
            
            # window GUI ('x' the window)
            if event.type == pygame.QUIT:
                running = False
                
            # mouseclick events    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                # just respond to left mouse clicks
                if pygame.mouse.get_pressed()[0]:
                    mc_handler(pygame.mouse.get_pos())
                    
            # timers
            elif event.type == timer_stpw:
                t_stpw()
                
            elif event.type == timer_butt:
                t_butt()

        draw_handler(canvas)
        clock.tick(60)
    pygame.quit ()

if __name__ == '__main__': main() 