import pygame

def dntos_ux():
  pygame.init()

  screen = pygame.display.set_mode([1280, 720])
  pygame.display.set_caption("Donut OS emulator")

  # donut
  donut_img = pygame.image.load('dntos/resources/donut.png') # this is the logo of our 'system'
  donut_img = pygame.transform.smoothscale(donut_img, (50, 50))
  donut = screen.blit(donut_img, [10, 665])

  # chrome
  chrome_img = pygame.image.load('dntos/resources/chrome.png')
  chrome_img = pygame.transform.smoothscale(chrome_img, (50, 50))
  chrome = screen.blit(chrome_img, [70, 665])

  # file explorer
  file_explorer_img = pygame.image.load('dntos/resources/file_explorer.png')
  file_explorer_img = pygame.transform.smoothscale(file_explorer_img, (50, 50))
  file_explorer = screen.blit(file_explorer_img, [130, 665])

  run = True
  while run:
      event_list = pygame.event.get()
      for event in event_list:
          if event.type == pygame.QUIT:
              run = False

      screen.fill((50, 82, 123)) # background
      pygame.draw.rect(screen, (10, 10, 10), pygame.Rect(0, 660, 1280, 60)) # taskbar

      screen.blit(donut_img, [10, 665])
      screen.blit(chrome_img, [70, 665])
      screen.blit(file_explorer_img, [130, 665])

      pygame.display.flip()

      for evetn in event_list:
          if event.type == pygame.MOUSEBUTTONUP:
              mouse_pos = pygame.mouse.get_pos()
              if (donut.collidepoint(mouse_pos)):
                  print("donut clicked")
              if (chrome.collidepoint(mouse_pos)):
                  print("chrome clicked")
              if (file_explorer.collidepoint(mouse_pos)):
                  print("file_explorer clicked")


  pygame.quit()

