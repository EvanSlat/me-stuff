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
#-----------------------------------------------------------------------------
#moving the points
class PointControl:
    def __init__ (self,sides,screen):
        self.current_corner = 0
        self.sides = sides
        self.screen = screen
    def moving_points(self,pressed_keys):
        if pressed_keys[pygame.K_w]:
            self.sides[self.current_corner].move_y(1)
        if pressed_keys[pygame.K_s]:
            self.sides[self.current_corner].move_y(-1)
        if pressed_keys[pygame.K_a]:
            self.sides[self.current_corner].move_x(-1)
        if pressed_keys[pygame.K_d]:
            self.sides[self.current_corner].move_x(1)
    #selectinve the points
    def corner_select(self,event,pressed_keys):
       # for event in pygame.event.get():
        if pressed_keys[pygame.K_LEFT] and event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP and event.button == 4:
            self.current_corner -= 1
        # print(current_corner)
        if pressed_keys[pygame.K_RIGHT] and event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP and event.button == 5:
            self.current_corner += 1
        # print(current_corner)
        if self.current_corner > len(self.sides) - 1:
            self.current_corner = 0
            # print(current_corner)
        if self.current_corner < 0:
            self.current_corner = len(self.sides) - 1
        #print(current_corner)
    #added points
    def add_points(self,event,pressed_keys):
        if pressed_keys[pygame.K_UP] and event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            side = Corner(100, 100, self.screen)
            self.sides.insert(self.current_corner,side)
        if pressed_keys[pygame.K_DOWN] and event.type == pygame.KEYUP and len(self.sides) > 3:
            del self.sides[self.current_corner]
            self.current_corner = 0
    # the drawling
    def draw_poly(self):
        corner_location = []
        for side in self.sides:
            # print(side1.x)
            corner_location.append((side.x, side.y))
        # print(corner_location)
        pygame.draw.polygon(self.screen, (155, 155, 155), (corner_location))

        # making it put a dot on the corner being controlled
        # print(current_corner)
        pygame.draw.circle(self.screen, (255, 255, 255), (self.sides[self.current_corner].x, self.sides[self.current_corner].y), 2)
# this is the main start of the program----------------------------------------------------------------------
def main():
#have variable set up and other sistem set up here
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    sides = []
    for i in range(3):
        side = Corner(100,100,screen)
        sides.append(side)
    corner_location = []
    #print(len(sides))
    point_control = PointControl(sides,screen)

#have any one time things run here


#this is the begining of the loop
    while True:
        #print("testing")
        clock.tick(30)
        screen.fill((0,0,0))
        #have what you want to be run here -player input

        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            #add player input into this section
            if event.type == pygame.QUIT:
                sys.exit()
#---------------------------------------------------------------------------------------basic control over poligon
# adding and removing corners
            point_control.add_points(event, pressed_keys)
# make it so that corner come to the mouse
            if event.type == pygame.MOUSEBUTTONUP and (event.button == 1 or event.button == 3):
                point_control.sides[point_control.current_corner].x, point_control.sides[point_control.current_corner].y = event.pos
# select witch corner is being used
            point_control.corner_select(event,pressed_keys)
#uses w s a d manuwal changung corner location
        point_control.moving_points(pressed_keys)
#---------------------------------------------------------------------------------------side parts of control
#make them all move
        if pressed_keys[pygame.K_u]:
            for side in point_control.sides:
                side.move_x(1)
                side.move_y(1)
      # make the corners loop  optionaly [q]
        if pressed_keys[pygame.K_q]:
            for side in point_control.sides:
                side.loop()

#------------------------------------drawling onto the screen
        #this is the draw section
        point_control.draw_poly()
        pygame.display.update()
main()