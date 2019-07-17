import pygame
import sys
import random
#set up classes here ----------------------------------------------------
class Corner:
    def __init__(self,start_x,start_y):
        #set up class variables
        self.x = start_x
        self.y = start_y
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
#add any other classes or functions here


# this is the main start of the program
def main():
#have variable set up and other sistem set up here
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    side1 = Corner(100,100)
    side2 = Corner(100,400)
    side3 = Corner(400,400)

#have any one time things run here


#this is the begining of the loop
    while True:
        clock.tick(60)
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

        #this should be last for it updates the screen
        pygame.draw.polygon(screen,(155,155,155),((side1.x,side1.y),(side2.x,side2.y),(side3.x,side3.y)))

        pygame.display.update()
main()