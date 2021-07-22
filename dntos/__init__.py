import pygame
import threading
import os
from random import *

from pynput.keyboard import Key, Listener

import dntos.shell
import dntos.ui

pygame.init()



class game():
  def __init__(self):
    self.myfont = pygame.font.SysFont('Hack', 30) # Natural we needed to use the ultimate hacker font (plus bonus nerd fonts are brilliant!).
    
    self.clock = pygame.time.Clock()

    self.screen = pygame.display.set_mode([1280, 720])


    self.donut_img = pygame.image.load('dntos/ui/resources/donut.png')
    self.donut_img = pygame.transform.smoothscale(self.donut_img, (50, 50))
    self.donut = self.screen.blit(self.donut_img, [10, 665])

    self.chrome_img = pygame.image.load('dntos/ui/resources/chrome.png') # chrome.png is of no relation to Google or any Google patents relating to Chrome. <_<
    self.chrome_img = pygame.transform.smoothscale(self.chrome_img, (50, 50))
    self.chrome = self.screen.blit(self.chrome_img, [70, 665]) # it is pure coincidence that all the internal variables for our browser thing have the same name as the most popular browser in the world, no correlation whatsoever.
    self.chrome_logo_img = pygame.image.load('dntos/ui/resources/Comodo.png')

    self.duck_img = pygame.image.load('dntos/ui/resources/duck.png')
    self.duck_img = pygame.transform.smoothscale(self.duck_img, (840,600))

    self.file_explorer_img = pygame.image.load('dntos/ui/resources/file_explorer.png')
    self.file_explorer_img = pygame.transform.smoothscale(self.file_explorer_img, (50, 50))
    self.file_explorer = self.screen.blit(self.file_explorer_img, [130, 665])

    self.console_img = pygame.image.load('dntos/ui/resources/console.png')
    self.console_img = pygame.transform.smoothscale(self.console_img, (50, 50))
    self.console = self.screen.blit(self.console_img, [190, 665])

    self.x_quit_img = pygame.image.load('dntos/ui/resources/x.png')
    self.x_quit_img = pygame.transform.smoothscale(self.x_quit_img, (30, 30))
    self.x_quit = self.screen.blit(self.x_quit_img, [1230, 5])

    self.hacker_img = pygame.image.load('dntos/ui/resources/hacker.png')
    self.hacker_img = pygame.transform.smoothscale(self.hacker_img, (200, 200))

    self.training_img = pygame.image.load('dntos/ui/resources/training.png')
    self.training_img = pygame.transform.smoothscale(self.training_img, (200, 200))

    self.shutdown_img = pygame.image.load('dntos/ui/resources/shutdown.png')
    self.shutdown_img = pygame.transform.smoothscale(self.shutdown_img, (50, 50))

    self.img_1 = pygame.image.load('dntos/ui/resources/1.png')
    self.img_1 = pygame.transform.smoothscale(self.img_1, (100, 100))
    self.img_1_b = self.screen.blit(self.img_1, [100, 100])

    # This is an image which contains all of the number 2.
    self.img_2 = pygame.image.load('dntos/ui/resources/2.png')
    self.img_2 = pygame.transform.smoothscale(self.img_2, (100, 100))
    self.img_2_b = self.screen.blit(self.img_2, [250, 100])


    self.hacker_b = self.screen.blit(self.hacker_img, [300, 300])

    self.training_b = self.screen.blit(self.training_img, [900, 300])

    self.path = ""
    self.path_selected = False

    self.console_text = "Muffin-Man>"
    self.console_output_text = ""

    self.level = 0
    self.level_selected = True

    self.play_level = False


    self.draw_console = False
    self.draw_donut = False
    self.draw_file_explorer = False
    self.draw_chrome = False

    self.event_list = pygame.event.get()


    self.chrome_text = "Password: "
    self.password_2 = "password"
    self.chrome_hint_text = "hint"


  def on_press(self, key): # This is a function which does things when the user does things on the keyboard.
    if(self.draw_console):
        if(str(key) == "Key.backspace"):
            self.console_text = self.console_text[:-1]
        elif(str(key) == "Key.space"):
            self.console_text += " "
        elif(str(key) == "Key.shift"):
            pass
        elif(str(key) == "Key.enter"):
            self.console_output_text = self.console_output_text = shell.exec(self.console_text)
            self.console_text = "Muffin-Man>"
        else:
            self.console_text += str(key).strip("''")

        if(len(self.console_text) < 12):
            self.console_text = "Muffin-Man>"

    elif(self.draw_chrome):
        if(str(key) == "Key.backspace"):
            self.chrome_text = self.chrome_text[:-1]
        elif(str(key) == "Key.space"):
            self.chrome_text += " "
        elif(str(key) == "Key.shift"):
            pass
        elif(str(key) == "Key.enter"):
            print("guess:" + self.chrome_text[10:])
            if(int(self.password_2) == int(self.chrome_text[10:])):
                self.chrome_hint_text = "Correct! The password was " + str(self.password_2)
            elif(int(self.password_2) > int(self.chrome_text[10:])):
                self.chrome_hint_text = "Password too low"
            elif(int(self.password_2) < int(self.chrome_text[10:])):
                self.chrome_hint_text = "Password too high"
            self.chrome_text = "Password: "
        else:
            self.chrome_text += str(key).strip("''")

        if(len(self.chrome_text) < 10):
            self.chrome_text = "Password: "

  def listen_for_keys(self): # listener for when a key is pressed to them output it in the terminal
      with Listener(
              on_press=self.on_press
              ) as listener:
          listener.join()
  def multithreading(self):
    self.t1  = threading.Thread(target=self.listen_for_keys) # a new thread it needed because otherwise the program will keep listenting therefore the ui will not work

    self.t1.start()






args = game()
args.multithreading()
run = True
while run:
  args.clock.tick(100000)
  args.mouse_pos = pygame.mouse.get_pos()
  event_list = pygame.event.get()
  for event in event_list:
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()
      os._exit(0)

  args.screen.fill((50, 82, 123))

  if not args.path_selected:
    args.screen.blit(args.hacker_img, [300, 300])
    args.screen.blit(args.training_img, [900,300])

  if not args.level_selected:
    args.screen.blit(args.img_1, [100, 100])
    args.screen.blit(args.img_2, [250, 100])

  if args.play_level:
    ui.play(args)

  pygame.display.flip()
  args.event_list = pygame.event.get()
  for evnt in args.event_list:

      if evnt.type == pygame.MOUSEBUTTONDOWN:

          if (args.hacker_b.collidepoint(args.mouse_pos)):
              args.path_selected = True
              args.level_selected = False
              path = "H" # makes the path to hacker
          elif (args.training_b.collidepoint(args.mouse_pos)):
              args.path_selected = True
              args.level_selected = False
              path = "T" # makes the path to training
          elif (args.x_quit.collidepoint(args.mouse_pos)):
              ui.reset_screen(args)
          elif (args.donut.collidepoint(args.mouse_pos)):
              ui.reset_screen(args)
              args.draw_donut = True
          elif (args.chrome.collidepoint(args.mouse_pos)):
              ui.reset_screen(args)
              args.draw_chrome = True
          elif (args.file_explorer.collidepoint(args.mouse_pos)):
              ui.reset_screen(args)
              args.draw_file_explorer = True
          elif (args.console.collidepoint(args.mouse_pos)):
              ui.reset_screen(args)
              args.draw_console = True
          try:
              if (args.img_1_b.collidepoint(args.mouse_pos)):
                  args.level_number = 1
                  args.play_level = True
              elif (args.img_2_b.collidepoint(args.mouse_pos)):
                  args.level_number = 2
                  args.play_level = True
              elif (args.x_quit.collidepoint(args.mouse_pos)):
                  ui.reset_screen(args)
          except:
              pass
