import logging
import pygame
from . import ui
from .ui import dntos_ux

def main():
  screen = pygame.display.set_mode([1280, 720])
  pygame.display.set_caption("Donut OS Emulator")

  dntos_ux.main_os()

