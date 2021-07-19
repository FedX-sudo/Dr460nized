import pygame
import threading
import os

from pynput.keyboard import Key, Listener

import dntos.shell

pygame.init()

# VVVVVVVVVVV importing image assets. VVVVVVVVVVVVVVVVVV
screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Donut OS emulator")

clock = pygame.time.Clock()

# This is a small chunk of code which will define the donut
donut_img = pygame.image.load('resources/donut.png')
donut_img = pygame.transform.smoothscale(donut_img, (50, 50))
donut = screen.blit(donut_img, [10, 665])

# This small bit of code is defining the C0m0d0 Dr4g0n icon, which id definitely not the Google Chrome icon, or named after Comodo Dragon Browser.
chrome_img = pygame.image.load('resources/chrome.png') # chrome.png is of no relation to Google or any Google patents relating to Chrome. <_<
chrome_img = pygame.transform.smoothscale(chrome_img, (50, 50))
chrome = screen.blit(chrome_img, [70, 665]) # it is pure coincidence that all the internal variables for our browser thing have the same name as the most popular browser in the world, no correlation whatsoever.

# At this point I think you get the point, this is defining out file browser picture...
file_explorer_img = pygame.image.load('resources/file_explorer.png')
file_explorer_img = pygame.transform.smoothscale(file_explorer_img, (50, 50))
file_explorer = screen.blit(file_explorer_img, [130, 665])

# This is defining the Unix terminal emulator icon, which is the only app you need.
console_img = pygame.image.load('resources/console.png')
console_img = pygame.transform.smoothscale(console_img, (50, 50))
console = screen.blit(console_img, [190, 665])

# quit out of window symbol ( X )
x_quit_img = pygame.image.load('resources/x.png')
x_quit_img = pygame.transform.smoothscale(x_quit_img, (30, 30))

# This defines an image depicting an anonymous hacker representing the hacker route.
hacker_img = pygame.image.load('resources/hacker.png')
hacker_img = pygame.transform.smoothscale(hacker_img, (200, 200))
hacker_b = screen.blit(hacker_img, [300, 300])

# This depicts a guy whacking a projector with a sticker to represent someone teaching things.
training_img = pygame.image.load('resources/training.png')
training_img = pygame.transform.smoothscale(training_img, (200, 200))
training_b = screen.blit(training_img, [900, 300])

# This is an image which contains all of the number 1. I miss CLI.
img_1 = pygame.image.load('resources/1.png')
img_1 = pygame.transform.smoothscale(img_1, (100, 100))
img_1_b = screen.blit(img_1, [100, 100])

# ^^^^^^^^^^ few that is done. ^^^^^^^^^^^^^^^^^^^^^^
# VVVVVVVVVV Shoot! More things?! VVVVVVVVVVVVVVVVVVVV



font = pygame.font.SysFont(None, 40)

# This just a tad bit of house keeping to allow the console to work.
global console_text
console_text = "Muffin-Man>"
global console_output_text
console_output_text = ""

# The following variables define weather the apps should be drawn or not.
draw_console = False
draw_donut = False# A random variable which does nothing. Don't delete it!
draw_file_explorer = False# A random variable which does nothing. Don't delete it!
draw_chrome = False # A random variable which does nothing. Don't delete it! Oh and I almost forgot, this is of no association with Google, and its purely coincidence its called chrome.

def create_screen():
    ''' Creates the desktop that all versions of the hacker and training route will utilize'''
    screen.fill((50, 82, 123)) # background

    pygame.draw.rect(screen, (10, 10, 10), pygame.Rect(0, 660, 1280, 60)) # taskbar

    # This puts all the icons in the taskbar
    screen.blit(donut_img, [10, 665])
    screen.blit(chrome_img, [70, 665])
    screen.blit(file_explorer_img, [130, 665])
    screen.blit(console_img, [190, 665])

    # This will open up the console if the icon is clicked
    global draw_console
    if (draw_console == True):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 40, 1280, 620))
        pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(0, 0, 1280, 40))
        x_quit = screen.blit(x_quit_img, [1230, 5])
        console_text_r = font.render(console_text, True, (255, 255, 255))
        screen.blit(console_text_r, [10, 50])

        console_output_text_r = font.render(console_output_text, True, (255, 255, 255))
        screen.blit(console_output_text_r, [10, 100])

    # This will open up the C0m0d0 Dr4g0n browser if the icon is clicked
    global draw_chrome
    if (draw_chrome == True):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 40, 1280, 620))
        pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(0, 0, 1280, 40))
        x_quit = screen.blit(x_quit_img, [1230, 5])
        #console_text_r = font.render(console_text, True, (255, 255, 255))
        #screen.blit(console_text_r, [10, 50])

        #console_output_text_r = font.render(console_output_text, True, (255, 255, 255))
        #screen.blit(console_output_text_r, [10, 100])


    pygame.display.flip() # This completely reloads the screen so all previous changes like the background and taskbar are shown

    for evetn in event_list: # For almost everything the user does
        if event.type == pygame.MOUSEBUTTONDOWN: # If the user clicks down on the left mouse button
            print("mousedown")
            mouse_pos = pygame.mouse.get_pos()
            try: # this is needed here because x is not always initialized
                if (x_quit.collidepoint(mouse_pos)):
                    reset_screen()
                    print("click on x")
            except:
                pass
            # If the user clicks on an icon, open the respective program to that icon
            if (donut.collidepoint(mouse_pos)):
                reset_screen()
                draw_donut = True
            if (chrome.collidepoint(mouse_pos)):
                reset_screen()
                draw_chrome = True
            if (file_explorer.collidepoint(mouse_pos)):
                reset_screen()
                draw_file_explorer = True
            if (console.collidepoint(mouse_pos)):
                reset_screen()
                draw_console = True

def reset_screen(): # This is a function which closes all the windows.
    draw_console = False
    draw_donut = False# A random variable which does nothing. Don't delete it!
    draw_file_explorer = False# A random variable which does nothing. Don't delete it!
    draw_chrome = False # A random variable which does nothing. Don't delete it! Oh and I almost forgot, this is of no association with Google, and its purely coincidence its called chrome.
    pygame.display.update()

def on_press(key): # This is a function which does things when the user does things on the keyboard.
    if(draw_console):
        global console_text
        global console_output_text
        if(str(key) == "Key.backspace"):
            console_text = console_text[:-1]
        elif(str(key) == "Key.space"):
            console_text += " "
        elif(str(key) == "Key.shift"):
            pass
        elif(str(key) == "Key.enter"):
            console_output_text = console_output_text = shell.exec(console_text)
            console_text = "Muffin-Man>"
        else:
            console_text += str(key).strip("''")

        if(len(console_text) < 12):
            console_text = "Muffin-Man>"

    if(draw_chrome):
        print(key)

def listen_for_keys(): # listener for when a key is pressed to them output it in the terminal
    with Listener(
            on_press=on_press
            ) as listener:
        listener.join()

# Nooooooooooooooooooo, not multithreading!!!!!
t1  = threading.Thread(target=listen_for_keys) # a new thread it needed because otherwise the program will keep listenting therefore the ui will not work
t1.start()

def training_route(lesson_number): # this is the training route
    if(lesson_number == 1):
        create_screen()
                    
    elif(lesson_number == 2):
        print("training_route_2")
    elif(lesson_number == 3):
        print("training_route_3")
    elif(lesson_number == 4):
        print("training_route_4")
    elif(lesson_number == 5):
        print("training_route_5")
    elif(lesson_number == 6):
        print("training_route_6")
    elif(lesson_number == 7):
        print("training_route_7")
    elif(lesson_number == 8):
        print("training_route_8")

def hacker_route(lesson_number): # this is the hacker route
    if(lesson_number == 1):


        screen.fill((50, 82, 123)) # background

        pygame.draw.rect(screen, (10, 10, 10), pygame.Rect(0, 660, 1280, 60)) # taskbar

        screen.blit(donut_img, [10, 665]) # blit? blit! What does that mean?!
        screen.blit(chrome_img, [70, 665])
        screen.blit(file_explorer_img, [130, 665])
        screen.blit(console_img, [190, 665])

        global draw_console
        if (draw_console == True):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 40, 1280, 620))
            pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(0, 0, 1280, 40))
            x_quit = screen.blit(x_quit_img, [1230, 5])
            console_text_r = font.render(console_text, True, (255, 255, 255))
            screen.blit(console_text_r, [10, 50])

            console_output_text_r = font.render(console_output_text, True, (255, 255, 255))
            screen.blit(console_output_text_r, [10, 100])


        pygame.display.flip() # This does something, what I don't know.

        for evetn in event_list: # um, what?!
          if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                try: # this is needed here because x is not always initialized
                    if (x_quit.collidepoint(mouse_pos)):
                        reset_screen()
                except:
                    pass
                if (donut.collidepoint(mouse_pos)):
                    reset_screen()
                    draw_donut = True
                if (chrome.collidepoint(mouse_pos)):
                    reset_screen()
                    draw_chrome = True
                if (file_explorer.collidepoint(mouse_pos)):
                    reset_screen()
                    draw_file_explorer = True
                if (console.collidepoint(mouse_pos)):
                    reset_screen()
                    draw_console = True
                    
    elif(lesson_number == 2):
        print("hacker_route_2")
    elif(lesson_number == 3):
        print("hacker_route_3")
    elif(lesson_number == 4):
        print("hacker_route_4")
    elif(lesson_number == 5):
        print("hacker_route_5")
    elif(lesson_number == 6):
        print("hacker_route_6")
    elif(lesson_number == 7):
        print("hacker_route_7")
    elif(lesson_number == 8):
        print("hacker_route_8")

global path_selected
global level_selected
global path
global play_level
global level_number
path_selected = False
level_selected = True
path = ""
play_level = False
level_number = 0

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    screen.fill((50, 82, 123))

    if (path_selected == False):
        screen.blit(hacker_img, [300, 300])
        screen.blit(training_img, [900, 300])

    if (level_selected == False):
        # print("draw some hacker stuff")
        screen.blit(img_1, [100, 100])

    if(play_level == True): # after selected is will start the level
        if(path == "T"):
            training_route(level_number)
        if(path == "H"):
            hacker_route(level_number)

    pygame.display.flip()

    for evetn in event_list:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (hacker_b.collidepoint(mouse_pos)):
                print("hacker clicked")
                path_selected = True
                level_selected = False
                path = "H" # makes the path to hacker
            if (training_b.collidepoint(mouse_pos)):
                print("training clicked")
                path_selected = True
                level_selected = False
                path = "T" # makes the path to training
            try:
                if (img_1_b.collidepoint(mouse_pos)):
                    level_number = 1
                    play_level = True
            except:
                pass

pygame.quit()
os._exit(0)

'''
TODO list
* TODO fix jumping to hacker route from training route at random bug.
'''






