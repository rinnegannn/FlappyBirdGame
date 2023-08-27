# Aryan Verma
# 6/14/2022
# Final Project

# Variables 
import pygame
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()
size = (500,700)
screen = pygame.display.set_mode(size)
done = False
SCREENMODE  = 0
LIGHTBLUE = (176, 244, 255)
GREEN = (57, 224, 16)
BROWN = (120, 94, 66)
GGREEN = (102,255,51)
M_BROWN = (247, 203, 141)
LIGHTBROWN = (252, 229, 197)
ROSYBROWN = (139,69,19)
WHITE = (255,255,255) 
BLACK = (0,0,0)
BROWNN = (255, 216, 161)
BBROWN = (186, 144, 84)
bird = pygame.image.load('Flappy Bird bird.png')
bird = pygame.transform.scale(bird,(100,85))
dest = 0
posi = 400
amount = 0
start = 500
count = 0 
pygame.mixer.Sound('point.wav')
pygame.mixer.music.load('point.wav')
size_y = random.randrange(150,305)
size_y1 = random.randrange(200,305)

# Mouse Position

clock=pygame.time.Clock()
while not done:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
        # Mouse Position
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
    
        
        
        if SCREENMODE == 0:
        # Background 
            city = pygame.image.load('City Scape for Flappy Bird.png')
            screen.blit(city,[0,0])
            
            # Menu and text on launch
            # Logo
            logo = pygame.image.load('flappy bird logo.png')
            logo = pygame.transform.scale(logo,(300,100))
            screen.blit(logo,[100,20])     
            # Play Image and Box           
            pygame.draw.rect(screen,M_BROWN,[110,180,280,400])
            
            pygame.draw.rect(screen,LIGHTBROWN,[120,200,260,50])
            play = pygame.image.load('Flappy Bird Menu (1).png')
            play = pygame.transform.scale(play,(90,40))
            screen.blit(play,[200,205])  
            if (120 <= x and x <= 380) and (200 <= y and y <= 250):
                pygame.draw.rect(screen,ROSYBROWN,[120,200,260,50])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0] == True:
                        SCREENMODE = 2            
            
            # Instruction Image and Box 
            pygame.draw.rect(screen,LIGHTBROWN,[120,280,260,50])
            instruct = pygame.image.load('Flappy Bird Menu (2).png')
            instruct = pygame.transform.scale(instruct,(180,50))
            screen.blit(instruct,[160,285]) 
            if (120 <= x and x <= 380) and (280 <= y and y <= 330):
                pygame.draw.rect(screen,ROSYBROWN,[120,280,260,50])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0] == True:
                        SCREENMODE = 1
                   
               
            # Exit Image and Box 
            pygame.draw.rect(screen,LIGHTBROWN,[120,360,260,50])
            exit = pygame.image.load('Flappy Bird Menu (3).png')
            exit = pygame.transform.scale(exit,(90,40))
            screen.blit(exit,[200,365])     
            
            if (120 <= x and x <= 380) and (360 <= y and y <= 410):
                pygame.draw.rect(screen,ROSYBROWN,[120,360,260,50])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0] == True:
                        done = True
        
        # This switches to the Instructions Tab after intrsuctions box is clicked               
        if SCREENMODE == 1:
            
            # Provides fonts
            pygame.draw.rect(screen,BROWN,[0,130,500,600])
            font = pygame.font.SysFont('Verdana', 50, True, False)
            text = font.render("Instructions", True, GREEN)
            screen.blit(text,[90,130])
            font1 = pygame.font.SysFont('Times New Roman', 25, True, False)
            font1_2 = pygame.font.SysFont('Times New Roman', 15, True, False)
            text1 = font1.render("Mousebinds:", True, WHITE)
            text1_2 = font1_2.render("Mouse -", True, WHITE)
            font1_3 = pygame.font.SysFont('Times New Roman', 15, False, False)
            text1_3 = font1_3.render("Tapping or holding the right mouse button will make the bird fly, when not the bird will drop.", True, WHITE)
            text1_31 = font1_3.render("the bird will drop.", True, WHITE)
            font1_4 = pygame.font.SysFont('Times New Roman', 25, True, False)
            text1_4 = font1_4.render("Objective:", True, WHITE)    
            
            font1_5 = pygame.font.SysFont('Times New Roman', 15, False, False)
            text1_5 = font1_5.render("Your main objective is trying to avoid polls by flying and getting as far as you can. ", True, WHITE)    
            text_6 = font1_5.render("Try your best to get a high score and in general have a fun time :)", True, WHITE)    
            
            # Prints fonts
            screen.blit(text1,[20,210])
            screen.blit(text1_2,[20,250])
            screen.blit(text1_3,[73,250])
            screen.blit(text1_31,[20,270])
            screen.blit(text1_4,[20,300])
            screen.blit(text1_5,[20,340])
            screen.blit(text_6,[20,360])
            
            
            fnt = pygame.font.SysFont('Times New Roman', 25, True, False)
            txt = fnt.render("< Back", True, GREEN)    
            pygame.draw.rect(screen,LIGHTBROWN,[10,640,120,50])
            screen.blit(txt,[20,650])
            
            if (10 <= x and x <= 130) and (640 <= y and y <= 690):
                pygame.draw.rect(screen,ROSYBROWN,[10,640,120,50])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0] == True:
                        SCREENMODE = 0 
    
    # Back to Menu Box
    if SCREENMODE ==3:
        pygame.draw.rect(screen,BROWNN,[0,0,500,700])
        pygame.draw.rect(screen,BBROWN,[110,280,280,70])
        back = pygame.image.load('Back to Menu.png')
        back = pygame.transform.scale(back,(200,50))
        screen.blit(back,[150,290])
        if (110 <= x and x <= 390) and (280 <= y and y <= 350):
            pygame.draw.rect(screen,ROSYBROWN,[110,280,280,70])
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                if buttons[0] == True:
                    SCREENMODE = 0         
        
    # Gameplay Screenmode              
    if SCREENMODE == 2:      
        city = pygame.image.load('City Scape for Flappy Bird.png')
        screen.blit(city,[0,0])
        screen.blit(bird,[dest,posi])       
        posi = posi + 2
        if start != 0:                    
            pygame.draw.rect(screen,GGREEN,[start,0,50,size_y])    
            pygame.draw.rect(screen,BLACK,[start,0,50,size_y],2)
            pygame.draw.rect(screen,GGREEN,[start,500,50,size_y1])    
            pygame.draw.rect(screen,BLACK,[start,500,50,size_y1],2)  
            start = start - 3
            pygame.draw.rect(screen,ROSYBROWN,[350,0,150,50])
            score_font = pygame.font.SysFont('Times New Roman', 35, True, False)
            score_text = score_font.render("Score:" + str(count), True, WHITE)
            screen.blit(score_text,[350,0])
        #Gameplay 
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                if buttons[0] == True:
                    screen.blit(bird,[dest,posi])
                    posi = posi - 6
            
        if posi <= 0:
            posi = 0        
                                    

        if (start <= dest and dest <= start+50) and (0 <= posi and posi <= size_y):
            SCREENMODE = 3 
            start = 500
            posi = 400
            amount = 0   
            count= 0
                
        if (start <= dest and dest <= start+50) and (450 <= posi and posi <= 700):
            SCREENMODE = 3 
            start = 500
            posi = 400
            amount = 0 
            count = 0
        
        if dest >= start:
            count = count + 1
            pygame.mixer.music.play()           
            
        
        if start <= 0:
            start = 550
            size_y = random.randrange(150,305) 
            size_y1 = random.randrange(200,305)

       
        
            
        
             
    if posi >= 600:
        SCREENMODE = 3 
        start = 500
        posi = 400
        amount = 0
        count = 0
                      
    
    
    
    pygame.display.flip()
    
             
    
                          

    clock.tick(240)
    pygame.display.flip()



    


pygame.quit()