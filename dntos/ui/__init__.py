import pygame
# UI Elements such as applications
# This is a small chunk of code which will define the donut
def img_import(screen):
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



def Console(screen):
    ui.img_import(screen)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 40, 1280, 620))
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(0, 0, 1280, 40))
    x_quit = screen.blit(x_quit_img, [1230, 5])
    console_text_r = font.render(console_text, True, (255, 255, 255))
    screen.blit(console_text_r, [10, 50])

    console_output_text_r = font.render(console_output_text, True, (255, 255, 255))
    screen.blit(console_output_text_r, [10, 100])


