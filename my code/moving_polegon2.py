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
    screen = pygame.display.set_mode((1500, 600))
    clock = pygame.time.Clock()
    sides = []
    for i in range(4):
        side = Corner(100,i*100,screen)
        sides.append(side)
    corner_location = []

#have any one time things run here


#this is the begining of the loop
    while True:
        #print("testing")
        clock.tick(60)
        screen.fill((0,0,0))
        #have what you want to be run here -player input

        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            #add player input into this section
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                sides[3].x, sides[3].y = event.pos
# uses up down left righ
        if pressed_keys[pygame.K_UP]:
            sides[0].move_y(1)
          #  print('up')
           # print(sides[0].y)
            #print(sides)
        if pressed_keys[pygame.K_DOWN]:
            sides[0].move_y(-1)
        if pressed_keys[pygame.K_LEFT]:
            sides[0].move_x(-1)
        if pressed_keys[pygame.K_RIGHT]:
            sides[0].move_x(1)
#uses w s a d
        if pressed_keys[pygame.K_w]:
            sides[1].move_y(1)
        if pressed_keys[pygame.K_s]:
            sides[1].move_y(-1)
        if pressed_keys[pygame.K_a]:
            sides[1].move_x(-1)
        if pressed_keys[pygame.K_d]:
            sides[1].move_x(1)
# uses y h g j

      #  side3.move_x(1)
      #  side3.move_y(1)
       # side1.loop()
        #side2.loop()
        #side3.loop()
        #this should be last for it updates the screen
        corner_location = []
        for side in sides:
            #print(side1.x)
            corner_location.append((side.x,side.y))
       #print(corner_location)
        pygame.draw.polygon(screen,(155,155,155),(corner_location))

        pygame.display.update()
main()