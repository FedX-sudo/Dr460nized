import pygame
from pynput.keyboard import Key, Listener
import threading
import os
import dntos.shell

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
             console_output_text = shell.exec(console_text)
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

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    screen.fill((50, 82, 123)) # background
    pygame.draw.rect(screen, (10, 10, 10), pygame.Rect(0, 660, 1280, 60)) # taskbar

    screen.blit(donut_img, [10, 665])
    screen.blit(chrome_img, [70, 665])
    screen.blit(file_explorer_img, [130, 665])
    screen.blit(console_img, [190, 665])

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


pygame.quit()
os._exit(0)

def main():
    logging.info("executing the dntos ui")
    sys.exit(ui.dntos_ux())
