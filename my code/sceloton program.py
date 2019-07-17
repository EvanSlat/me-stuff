import pygame
import sys
import random
#set up classes here ----------------------------------------------------
class Temp:
    def __init__(self):
        #set up class variables
        pass
    def temp(self):
        # the functions each class gets
        pass
#add any other classes or functions here


# this is the main start of the program
def main():
#have variable set up and other sistem set up here
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

#have any one time things run here


#this is the begining of the loop
    while True:
        clock.tick(60)
        screen.fill((0,0,0))
        #have what you want to be run here -player input



        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            #add player input into this section if you want them to run one time
            # have the player input be out of the for statment inorder to have it run constently
            if event.type == pygame.QUIT:
                sys.exit()






        #this should be last for it updates the screen
        pygame.display.update()
main()