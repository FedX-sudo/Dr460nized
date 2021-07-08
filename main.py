import pygame
from pynput.keyboard import Key, Listener
import threading
import os

pygame.init()

screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Donut OS emulator")
clock = pygame.time.Clock()

# donut
donut_img = pygame.image.load('resources/donut.png') # this is the logo of our 'system'
donut_img = pygame.transform.smoothscale(donut_img, (50, 50))
donut = screen.blit(donut_img, [10, 665])

# chrome
chrome_img = pygame.image.load('resources/chrome.png')
chrome_img = pygame.transform.smoothscale(chrome_img, (50, 50))
chrome = screen.blit(chrome_img, [70, 665])

# file explorer
file_explorer_img = pygame.image.load('resources/file_explorer.png')
file_explorer_img = pygame.transform.smoothscale(file_explorer_img, (50, 50))
file_explorer = screen.blit(file_explorer_img, [130, 665])

# console
console_img = pygame.image.load('resources/console.png')
console_img = pygame.transform.smoothscale(console_img, (50, 50))
console = screen.blit(console_img, [190, 665])
draw_console = False
font = pygame.font.SysFont(None, 40)
global console_text
console_text = "Muffin-Man>"
global console_output_text
console_output_text = ""

# quit out of window symbol ( X )
x_quit_img = pygame.image.load('resources/x.png')
x_quit_img = pygame.transform.smoothscale(x_quit_img, (30, 30))

# hacker image
hacker_img = pygame.image.load('resources/hacker.png')
hacker_img = pygame.transform.smoothscale(hacker_img, (200, 200))
hacker_b = screen.blit(hacker_img, [300, 300])

# training image
training_img = pygame.image.load('resources/training.png')
training_img = pygame.transform.smoothscale(training_img, (200, 200))
training_b = screen.blit(training_img, [900, 300])

# 1
img_1 = pygame.image.load('resources/1.png')
img_1 = pygame.transform.smoothscale(img_1, (100, 100))
img_1_b = screen.blit(img_1, [100, 100])


def reset_screen():
    global draw_console
    draw_console = False

def on_press(key):
    if(draw_console):
        print("Key pressed:" + str(key))
        global console_text
        global console_output_text
        if(str(key) == "Key.backspace"):
            console_text = console_text[:-1]
        elif(str(key) == "Key.space"):
            console_text += " "
        elif(str(key) == "Key.shift"):
            pass
        elif(str(key) == "Key.enter"):
            print("execute command")
            console_output_text = "*execute command for: " + console_text[11:] + "*"
            console_text = "Muffin-Man>"
        else:
            console_text += str(key).strip("''")

        if(len(console_text) < 12):
            console_text = "Muffin-Man>"

def listen_for_keys():
    with Listener(
            on_press=on_press
            ) as listener:
        listener.join()

t1 = threading.Thread(target=listen_for_keys)
t1.start()

def training_route(lesson_number):
    print("entering training_route")
    if(lesson_number == 1):
        print("training_route_1")
        screen.fill((50, 82, 123)) # background
        pygame.draw.rect(screen, (10, 10, 10), pygame.Rect(0, 660, 1280, 60)) # taskbar

        screen.blit(donut_img, [10, 665])
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


        pygame.display.flip()

        for evetn in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                try: # this is needed here because x is not always initialized
                    if (x_quit.collidepoint(mouse_pos)):
                        print("quit clicked")
                        reset_screen()
                except:
                    pass
                if (donut.collidepoint(mouse_pos)):
                    print("donut clicked")
                    reset_screen()
                if (chrome.collidepoint(mouse_pos)):
                    print("chrome clicked")
                    reset_screen()
                if (file_explorer.collidepoint(mouse_pos)):
                    print("file_explorer clicked")
                    reset_screen()
                if (console.collidepoint(mouse_pos)):
                    print("console clicked")
                    reset_screen()
                    draw_console = True
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

def hacker_route(lesson_number):
    print("entering hacker_route")
    if(lesson_number == 1):
        print("hacker_route_1")
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

    if(play_level == True):
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
                path = "H"
            if (training_b.collidepoint(mouse_pos)):
                print("training clicked")
                path_selected = True
                level_selected = False
                path = "T"
            try:
                if (img_1_b.collidepoint(mouse_pos)):
                    level_number = 1
                    play_level = True
            except:
                pass

pygame.quit()
os._exit(0)
