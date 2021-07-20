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

def main():
  args = game()
  ui.startup(args)
