import pygame
import sys
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
    screen = pygame.display.set_mode((380, 400))

#have any one time things run here


#this is the begining of the loop
    while True:
        #have what you want to be run here -player input


        #have this in the for loop for buttons to only be regitered one time and out side for it to be constant
        #pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            #add player input into this section
            if event.type == pygame.QUIT:
                sys.exit()






        #this should be last for it updates the screen
        pygame.display.update()
main()