import pygame
import threading
import os

from pynput.keyboard import Key, Listener

import dntos.shell
import dntos.ui

pygame.init()

class game():
  def __init__(self):
    self.screen = pygame.display.set_mode([1280, 720])
    self.donut_img = pygame.image.load('dntos/ui/resources/donut.png')
    self.donut_img = pygame.transform.smoothscale(self.donut_img, (50, 50))
    self.donut = self.screen.blit(self.donut_img, [10, 665])

    self.chrome_img = pygame.image.load('dntos/ui/resources/chrome.png') # chrome.png is of no relation to Google or any Google patents relating to Chrome. <_<
    self.chrome_img = pygame.transform.smoothscale(self.chrome_img, (50, 50))
    self.chrome = self.screen.blit(self.chrome_img, [70, 665]) # it is pure coincidence that all the internal variables for our browser thing have the same name as the most popular browser in the world, no correlation whatsoever.

    self.file_explorer_img = pygame.image.load('dntos/ui/resources/file_explorer.png')
    self.file_explorer_img = pygame.transform.smoothscale(self.file_explorer_img, (50, 50))
    self.file_explorer = self.screen.blit(self.file_explorer_img, [130, 665])

    self.console_img = pygame.image.load('dntos/ui/resources/console.png')
    self.console_img = pygame.transform.smoothscale(self.console_img, (50, 50))
    self.console = self.screen.blit(self.console_img, [190, 665])

    self.x_quit_img = pygame.image.load('dntos/ui/resources/x.png')
    self.x_quit_img = pygame.transform.smoothscale(self.x_quit_img, (30, 30))

    self.hacker_img = pygame.image.load('dntos/ui/resources/hacker.png')
    self.hacker_img = pygame.transform.smoothscale(self.hacker_img, (200, 200))

    self.training_img = pygame.image.load('dntos/ui/resources/training.png')
    self.training_img = pygame.transform.smoothscale(self.training_img, (200, 200))

    self.img_1 = pygame.image.load('dntos/ui/resources/1.png')
    self.img_1 = pygame.transform.smoothscale(self.img_1, (100, 100))
    self.img_1_b = self.screen.blit(self.img_1, [100, 100])


    self.clock = pygame.time.Clock()
    self.font = pygame.font.SysFont(None, 40)
    self.hacker_b = self.screen.blit(self.hacker_img, [300, 300])
    self.training_b = self.screen.blit(self.training_img, [900, 300])


    self.draw_console = False
    self.draw_donut = False# A random variable which does nothing. Don't delete it!
    self.draw_file_explorer = False# A random variable which does nothing. Don't delete it!
    self.draw_chrome = False # A random variable which does nothing. Don't delete it! Oh and I almost forgot, this is of no association with Google, and its purely coincidence its called chrome.


    self.console_text= "Muffin-Man>"
    self.console_output_text = ""


  def console(self):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 40, 1280, 620))
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(0, 0, 1280, 40))
    self.x_quit = screen.blit(x_quit_img, [1230, 5])
    self.console_text_r = font.render(console_text, True, (255, 255, 255))
    self.screen.blit(console_text_r, [10, 50])

    self.console_output_text_r = font.render(console_output_text, True, (255, 255, 255))
    self.screen.blit(console_output_text_r, [10, 100])


    pygame.display.flip() # This does something, what I don't know.
  def reset_screen(self): # This is a function which closes all the windows.
    self.draw_console = False
    self.draw_donut = False# A random variable which does nothing. Don't delete it!
    self.draw_file_explorer = False# A random variable which does nothing. Don't delete it!
    self.draw_chrome = False # A random variable which does nothing. Don't delete it! Oh and I almost forgot, this is of no association with Google, and its purely coincidence its called chrome.

  def training_level_1(self):
      print("yo")
      self.screen.fill((50, 82, 123)) # background

      pygame.draw.rect(self.screen, (10, 10, 10), pygame.Rect(0, 660, 1280, 60)) # taskbar

      self.screen.blit(self.donut_img, [10, 665]) # blit? blit! What does that mean?!
      self.screen.blit(self.chrome_img, [70, 665])
      self.screen.blit(self.file_explorer_img, [130, 665])
      self.screen.blit(self.console_img, [190, 665])

      if (self.draw_console):
          self.console()

      for evetn in event_list: # um, what?!
        if event.type == pygame.MOUSEBUTTONDOWN:
              print("yo #2")
              mouse_pos = pygame.mouse.get_pos()
              try: # this is needed here because x is not always initialized
                  if (x_quit.collidepoint(mouse_pos)):
                      reset_screen()
              except:
                  pass
              if (self.donut.collidepoint(mouse_pos)):
                  self.reset_screen()
                  self.draw_donut = True
              if (self.chrome.collidepoint(mouse_pos)):
                  self.reset_screen()
                  self.draw_chrome = True
              if (self.file_explorer.collidepoint(mouse_pos)):
                  self.reset_screen()
                  self.draw_file_explorer = True
              if (self.console.collidepoint(mouse_pos)):
                  self.reset_screen()
                  self.draw_console = True

args=game()
donut = args.screen.blit(args.donut_img, [10, 665])

pygame.display.set_caption("Donut OS emulator")



# This just a tad bit of house keeping to allow the console to work.


def reset_screen(): # This is a function which closes all the windows.
    draw_console = False
    draw_donut = False# A random variable which does nothing. Don't delete it!
    draw_file_explorer = False# A random variable which does nothing. Don't delete it!
    draw_chrome = False # A random variable which does nothing. Don't delete it! Oh and I almost forgot, this is of no association with Google, and its purely coincidence its called chrome.


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

def listen_for_keys(): # listener for when a key is pressed to them output it in the terminal
    with Listener(
            on_press=on_press
            ) as listener:
        listener.join()

# Nooooooooooooooooooo, not multithreading!!!!!
t1  = threading.Thread(target=listen_for_keys) # a new thread it needed because otherwise the program will keep listenting therefore the ui will not work
t1.start()


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
    args.clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    args.screen.fill((50, 82, 123))

    if (path_selected == False):

        args.screen.blit(args.hacker_img, [300, 300])

        args.screen.blit(args.training_img, [900, 300])

    if (level_selected == False):
        # print("draw some hacker stuff")
        args.screen.blit(args.img_1, [100, 100])

    if(play_level): # after selected is will start the level
        if(path == "T"):
            training_route(level_number)
        if(path == "H"):
            hacker_route(level_number)

    pygame.display.flip()

    for evetn in event_list:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (args.hacker_b.collidepoint(mouse_pos)):
                path_selected = True
                level_selected = False
                path = "H" # makes the path to hacker
            if (args.training_b.collidepoint(mouse_pos)):
                path_selected = True
                level_selected = False
                path = "T" # makes the path to training
            #try:
                #if (args.img_1_b.collidepoint(mouse_pos)):
            args.training_level_1()

            #except:
                #print("dang")

pygame.quit()
os._exit(0)

'''
TODO list
* TODO fix jumping to hacker route from training route at random bug.
'''






