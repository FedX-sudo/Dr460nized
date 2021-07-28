#!/usr/bin/env python3
import pygame
from random import *
from playsound import playsound
# UI Elements such as applications
# This is a small chunk of code which will define the donut


def reset_screen(args): # This is a function which closes all the windows.
  args.draw_console = False
  args.draw_donut = False# A random variable which does nothing. Don't delete it!
  args.draw_file_explorer = False# A random variable which does nothing. Don't delete it!
  args.draw_chrome = False # A random variable which does nothing. Don't delete it! Oh and I almost forgot, this is of no association with Google, and its purely coincidence its called chrome.
  args.draw_mailbox = False # This is the mailbox for level 1

def play(args):
    ''' Creates the desktop that all versions of the hacker and training route will utilize'''

    args.screen.fill((50, 82, 123)) # background

    pygame.draw.rect(args.screen, (10, 10, 10), pygame.Rect(0, 660, 1280, 60)) # taskbar

    # This puts all the icons in the taskbar
    args.screen.blit(args.donut_img, [10, 665])
    args.screen.blit(args.chrome_img, [70, 665])
    args.screen.blit(args.file_explorer_img, [130, 665])
    args.screen.blit(args.console_img, [190, 665])

    # This will open up the console if the icon is clicked
    if args.draw_console:
        pygame.draw.rect(args.screen, (0, 0, 0), pygame.Rect(0, 40, 1280, 620))
        pygame.draw.rect(args.screen, (220, 220, 220), pygame.Rect(0, 0, 1280, 40))
        args.x_quit = args.screen.blit(args.x_quit_img, [1230, 5])

        args.console_text_r = args.myfont.render(args.console_text, True, (255, 255, 255))
        args.screen.blit(args.console_text_r, [10, 50])

        args.console_output_text_r = args.myfont.render(args.console_output_text, True, (255, 255, 255))
        args.screen.blit(args.console_output_text_r, [10, 100])

    # This will open up the C0m0d0 Dr4g0n browser if the icon is clicked
    elif (args.draw_chrome):
        pygame.draw.rect(args.screen, (255, 255, 255), pygame.Rect(0, 40, 1280, 620))
        pygame.draw.rect(args.screen, (220, 220, 220), pygame.Rect(0, 0, 1280, 40))
        args.x_quit = args.screen.blit(args.x_quit_img, [1230, 5])

        # This specifically loads the inbox and mail images that are used in level 1
        if (args.draw_mailbox):
            args.screen.blit(args.mailBack, [0,42])
            if(args.mail_m_question == 1):
                args.screen.blit(args.scam1, [200,300])
            elif(args.mail_m_question == 2):
                args.screen.blit(args.scam2, [200,300])
            elif(args.mail_m_question == 3):
                args.screen.blit(args.nscam1, [200,300])
            elif(args.mail_m_question == 4):
                args.screen.blit(args.scam3, [200,300])
            elif(args.mail_m_question == 5):
                args.screen.blit(args.scam4, [200,300])
            elif(args.mail_m_question == 6):
                args.screen.blit(args.scam5, [200,300])
            elif(args.mail_m_question == 7):
                args.screen.blit(args.nscam2, [200,300])
            elif(args.mail_m_question == 8):
                args.screen.blit(args.scam6, [200,300])


        #console_text_r = font.render(console_text, True, (255, 255, 255))
        #screen.blit(console_text_r, [10, 50])

        #console_output_text_r = font.render(console_output_text, True, (255, 255, 255))
        #screen.blit(console_output_text_r, [10, 100])

    #elif (args.draw_donut):
      #pygame.draw.rect(args.screen, (255, 255, 255), pygame.Rect(10, 550, 200, 100))
      #args.shutdown = args.screen.blit(args.shutdown_img, [1230, 5])

    if(args.level_number == 1 and args.path == "H"):
      pass

    elif(args.level_number == 2 and args.path == "H"):
        if(args.password_2 == ""):
            args.password_2 = randint(0,100)

        if(args.draw_chrome):
            args.chrome_hint_text_r = args.myfont.render(args.chrome_hint_text, True, (252, 172, 25))
            args.screen.blit(args.chrome_hint_text_r, [300, 200])

            args.chrome_q_text = "Guess the number form 0 to 100. Good luck!!"
            args.chrome_q_text_r = args.myfont.render(args.chrome_q_text, True, (252, 172, 25))
            args.screen.blit(args.chrome_q_text_r, [300, 50])

            args.chrome_text_r = args.myfont.render(args.chrome_text, True, (93, 93, 252))
            args.screen.blit(args.chrome_text_r, [100, 100])
    
    if(args.level_number == 1 and args.path == "T"):
      # if level 1 is finished, let the user know they have already completed the level
      if (args.level_one_finished == True):
        pygame.draw.rect(args.screen, (255, 255, 255), pygame.Rect(0, 40, 1280, 620))
        pygame.draw.rect(args.screen, (220, 220, 220), pygame.Rect(0, 0, 1280, 40))
        args.screen.blit(args.x_quit_img, [1230, 5])
        args.screen.blit(args.mailWin, [0,42])
    
      # if the browser hasn't been opened, add an orange square around it to emphasize it 
      elif (args.draw_chrome == False):
          args.mail_m_question = 1
          args.screen.blit(args.orange_img, [69, 664])
          
      # If the mail icon hasn't been clicked yet, draw the normal browser imagery
      elif (args.draw_mailbox == False):
        args.screen.blit(args.duck_img, [550, 50])
        args.screen.blit(args.chrome_logo_img, [355, 150])
        args.screen.blit(args.search_img, [100, -200])
        args.mail = args.screen.blit(args.mail_img, [600, 500])

      # If the mail icon has been clicked, give the user the questions
      else:
        if(args.mail_m_question != 9):
            # Shows the yes and no answer buttons
            args.img_yes_c = args.screen.blit(args.img_yes, [600, 500])
            args.img_no_c = args.screen.blit(args.img_no, [800, 500])
            
        # The general format for the questions is that
        # If the user selects the right answer, they go on the next question
        # If not, they have to start over

        if(args.mail_m_question == 1):
            if(args.mail_m_choice == "y"): #correct answer
                args.mail_m_choice = ""
                args.mail_m_question = 2
            elif (args.mail_m_choice == "n"): #wrong answer
                reset_screen(args)
            
        elif(args.mail_m_question == 2):
            if(args.mail_m_choice == "y"): #correct answer
                args.mail_m_choice = ""
                args.mail_m_question = 3
            elif (args.mail_m_choice == "n"): #wrong answer
                reset_screen(args)
                
        elif(args.mail_m_question == 3):
            if(args.mail_m_choice == "n"): #correct answer
                args.mail_m_choice = ""
                args.mail_m_question = 4
            elif (args.mail_m_choice == "y"): #wrong answer
                reset_screen(args)
                
        elif(args.mail_m_question == 4):
            if(args.mail_m_choice == "y"): #correct answer
                args.mail_m_choice = ""
                args.mail_m_question = 5
            elif (args.mail_m_choice == "n"): #wrong answer
                reset_screen(args)
                
        elif(args.mail_m_question == 5):
            if(args.mail_m_choice == "y"): #correct answer
                args.mail_m_choice = ""
                args.mail_m_question = 6
            elif (args.mail_m_choice == "n"): #wrong answer
                reset_screen(args)
                
        elif(args.mail_m_question == 6):
            if(args.mail_m_choice == "y"): #correct answer
                args.mail_m_choice = ""
                args.mail_m_question = 7
            elif (args.mail_m_choice == "n"): #wrong answer
                reset_screen(args)
                
        elif(args.mail_m_question == 7):
            if(args.mail_m_choice == "n"): #correct answer
                args.mail_m_choice = "" 
                args.mail_m_question = 8
            elif (args.mail_m_choice == "y"): #wrong answer
                reset_screen(args)
                
        elif(args.mail_m_question == 8):
            if(args.mail_m_choice == "y"): #correct answer
                args.mail_m_choice = ""
                args.mail_m_question = 9
            elif (args.mail_m_choice == "n"): #wrong answer
                reset_screen(args)
                
        #This loads the level complete screen and marks level one as finished
        elif(args.mail_m_question == 9):
            args.screen.blit(args.mailWin, [0,42])
            args.level_one_finished = True
            
    elif(args.level_number == 2 and args.path == "T"):
        if(args.draw_chrome):
            if(args.chrome_m_question != 6):
                args.screen.blit(args.img_yes, [500, 550])
                args.screen.blit(args.img_no, [700, 550])
            if(args.chrome_m_question == 1):
                args.chrome_m_text_1 = "Let's say you want to download another browser and go to"
                args.chrome_m_text_2 = "a website called \"browsetheworld.io\"" # unknown publisher / don't trust them with your browsing data
                args.chrome_m_text_3 = "You never heard of this browser before, should you download it?"
                if(args.chrome_m_choice == "n"): # correct choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 2
                elif(args.chrome_m_choice == "y"): # wrong choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 1
                    reset_screen(args)
            elif(args.chrome_m_question == 2):
                args.chrome_m_text_1 = "You search for an image editor called gimp recommended by a friend."
                args.chrome_m_text_2 = "You see that you can download it from \"softwareforall.net\"" # downloading good software from a random site
                args.chrome_m_text_3 = "The website however, looks wierd. Should you download it?"
                if(args.chrome_m_choice == "n"): # correct choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 3
                elif(args.chrome_m_choice == "y"): # wrong choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 1
                    reset_screen(args)
            elif(args.chrome_m_question == 3):
                args.chrome_m_text_1 = "You want to analyse your network and learn how it works."
                args.chrome_m_text_2 = "You search and find a program called wireshark on \"wireshark.org\"."
                args.chrome_m_text_3 = "The software is opensource and has a lot of history. Should you download it?"
                if(args.chrome_m_choice == "y"): # correct choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 4
                elif(args.chrome_m_choice == "n"): # wrong choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 1
                    reset_screen(args)
            elif(args.chrome_m_question == 4):
                args.chrome_m_text_1 = "You want to edit some photos using photoshop but have no money :("
                args.chrome_m_text_2 = "You find a website which claims to give it for free."
                args.chrome_m_text_3 = "Should you download it?"
                if(args.chrome_m_choice == "n"): # correct choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 5
                elif(args.chrome_m_choice == "y"): # wrong choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 1
                    reset_screen(args)
            elif(args.chrome_m_question == 5):
                args.chrome_m_text_1 = "You want to watch an .mp4 but don't like the defualt player."
                args.chrome_m_text_2 = "You search and find a program called VLC media player on \"videolan.org\"."
                args.chrome_m_text_3 = "The software is opensource and you heard of it before. Should you download it?"
                if(args.chrome_m_choice == "y"): # correct choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 6
                elif(args.chrome_m_choice == "n"): # wrong choice
                    args.chrome_m_choice = ""
                    args.chrome_m_question = 1
                    reset_screen(args)
            elif(args.chrome_m_question == 6):
                args.chrome_m_text_1 = "Good Job!"
                args.chrome_m_text_2 = "You completed this level."
                args.chrome_m_text_3 = ""


            args.chrome_m_text_1_r = args.myfont.render(args.chrome_m_text_1, True, (0, 0, 0))
            args.screen.blit(args.chrome_m_text_1_r, [400, 100])
            args.chrome_m_text_2_r = args.myfont.render(args.chrome_m_text_2, True, (0, 0, 0))
            args.screen.blit(args.chrome_m_text_2_r, [400, 150])
            args.chrome_m_text_3_r = args.myfont.render(args.chrome_m_text_3, True, (0, 0, 0))
            args.screen.blit(args.chrome_m_text_3_r, [400, 200])

    pygame.display.flip() # This completely reloads the screen so all previous changes like the background and taskbar are shown

