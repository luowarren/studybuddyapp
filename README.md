import time 

current_time = 00

def increment():
    global current_time
    current_time += 1
    display()

    time.sleep(1)
    increment()

def display():
    global current_time
    minutes = current_time // 60
    seconds = current_time % 60
    hour = current_time // 3600

    print (str(hour)+':'+str(minutes)+':'+str(seconds))

increment()
