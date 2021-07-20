#!/usr/bin/env python3
import pygame
# UI Elements such as applications
# This is a small chunk of code which will define the donut

def startup(args):
  ''' Creates the desktop that all versions of the hacker and training route will utilize'''
  args.screen.fill((50, 82, 123)) # background

  pygame.draw.rect(args.screen, (10, 10, 10), pygame.Rect(0, 660, 1280, 60)) # taskbar

  # This puts all the icons in the taskbar
  args.screen.blit(args.donut_img, [10, 665])
  args.screen.blit(args.chrome_img, [70, 665])
  args.screen.blit(args.file_explorer_img, [130, 665])
  args.screen.blit(args.console_img, [190, 665])

  # This will open up the console if the icon is clicked
  if (args.draw_console):
      pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 40, 1280, 620))
      pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(0, 0, 1280, 40))
      args.x_quit = screen.blit(x_quit_img, [1230, 5])
      args.console_text_r = font.render(args.console_text, True, (255, 255, 255))
      args.screen.blit(console_text_r, [10, 50])

      console_output_text_r = font.render(console_output_text, True, (255, 255, 255))
      args.screen.blit(console_output_text_r, [10, 100])

def reset_screen(args): # This is a function which closes all the windows.
  args.draw_console = False
  args.draw_donut = False# A random variable which does nothing. Don't delete it!
  args.draw_file_explorer = False# A random variable which does nothing. Don't delete it!
  args.draw_chrome = False # A random variable which does nothing. Don't delete it! Oh and I almost forgot, this is of no association with Google, and its purely coincidence its called chrome.
