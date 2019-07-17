import pygame
import sys
import random
#set up classes here ----------------------------------------------------
class Corner:
    def __init__(self,start_x,start_y,screen):
        #set up class variables
        self.x = start_x
        self.y = start_y
        self.screen = screen
    def move_x(self,direction):
        # the functions each class gets
        if direction == 1:
            self.x += 1
        else:
            self.x -=1
    def move_y(self,direction):
        if direction == 1:
            self.y -= 1
        else:
            self.y +=1
    def loop(self):
        if self.x < 0:
            self.x = self.screen.get_width()
        elif self.x > self.screen.get_width():
            self.x = 0
        if self.y < 0:
            self.y = self.screen.get_height()
        elif self.y > self.screen.get_height():
            self.y = 0
#add any other classes or functions here

def mouse_inputs():
    pass

# this is the main start of the program
def main():
#have variable set up and other sistem set up here
    pygame.init()
    screen = pygame.display.set_mode((1500, 800))
    clock = pygame.time.Clock()
    side1 = Corner(100,100,screen)
    side2 = Corner(100,400,screen)
    side3 = Corner(400,400,screen)
    side4 = Corner(400, 400, screen)
    side5 = Corner(400,400,screen)
#have any one time things run here


#this is the begining of the loop
    while True:
        #clock.tick(60)
        screen.fill((0,0,0))
        #have what you want to be run here -player input

        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            #add player input into this section
            if event.type == pygame.QUIT:
                sys.exit()
# uses up down left righ
        if pressed_keys[pygame.K_UP]:
            side1.move_y(1)
        if pressed_keys[pygame.K_DOWN]:
            side1.move_y(-1)
        if pressed_keys[pygame.K_LEFT]:
            side1.move_x(-1)
        if pressed_keys[pygame.K_RIGHT]:
            side1.move_x(1)
#uses w s a d
        if pressed_keys[pygame.K_w]:
            side2.move_y(1)
        if pressed_keys[pygame.K_s]:
            side2.move_y(-1)
        if pressed_keys[pygame.K_a]:
            side2.move_x(-1)
        if pressed_keys[pygame.K_d]:
            side2.move_x(1)
# uses y h g j
        if pressed_keys[pygame.K_y]:
            side3.move_y(1)
        if pressed_keys[pygame.K_h]:
            side3.move_y(-1)
        if pressed_keys[pygame.K_g]:
            side3.move_x(-1)
        if pressed_keys[pygame.K_j]:
            side3.move_x(1)
# USE o,L,k,;
        if pressed_keys[pygame.K_o]:
            side4.move_y(1)
        if pressed_keys[pygame.K_l]:
            side4.move_y(-1)
        if pressed_keys[pygame.K_k]:
            side4.move_x(-1)
        if pressed_keys[pygame.K_SEMICOLON]:
            side4.move_x(1)
#use - [ p ]
        if pressed_keys[pygame.K_MINUS]:
            side5.move_y(1)
        if pressed_keys[pygame.K_LEFTBRACKET]:
            side5.move_y(-1)
        if pressed_keys[pygame.K_p]:
            side5.move_x(-1)
        if pressed_keys[pygame.K_RIGHTBRACKET]:
            side5.move_x(1)






      #  side3.move_x(1)
      #  side3.move_y(1)
       # side1.loop()
        #side2.loop()
        #side3.loop()
        #this should be last for it updates the screen
        pygame.draw.polygon(screen,(155,155,155),((side1.x,side1.y),(side2.x,side2.y),(side3.x,side3.y),(side4.x,side4.y),(side5.x,side5.y)))

        pygame.display.update()
main()