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
    screen = pygame.display.set_mode((1500, 775))
    clock = pygame.time.Clock()
    full_mem = ['start', [345, 357], [637, 131], [803, 356], [408, 86], 'new poly', 189, 199, 215, [426, 137], [100, 100], [758, 243], [436, 291], 'new poly', 155, 155, 155, [522, 520], [580, 102], [662, 437], 'new poly', 129, 133, 109, 'stop']
    mem = full_mem
    temp = []
#have any one time things run here

#this is the begining of the loop
    while True:
        clock.tick(60)
        screen.fill((0,0,0))
        mem = []
        for i in range(len(full_mem)):
            mem.append(full_mem[i])
        #print(mem)
        #have what you want to be run here -player input
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            #add player input into this section if you want them to run one time
            # have the player input be out of the for statment inorder to have it run constently
            if event.type == pygame.QUIT:
                sys.exit()
#-----------------------------------------------------
        del mem[0]
        #print(mem)
        while not mem[0] == 'stop':
            while not mem[0] == 'new poly':
                temp.append(mem[0])
                del mem[0]
               # print(mem)
            pygame.draw.polygon(screen,(mem[1],mem[2],mem[3]),temp)
            temp = []
            del mem[0]
            del mem[0]
            del mem[0]
            del mem[0]
            #print(mem)
        #this should be last for it updates the screen
        pygame.display.update()
main()