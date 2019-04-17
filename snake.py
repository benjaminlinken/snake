import os
import pygame


BLACK = (0, 0, 0)
WHILE = (255, 255, 255)

class snake():
    def __init__(self, length=5, headpos=(5, 5), direction = 'right'):
        self.length = length
        self.headpos = headpos
        self.direction = direction

        self.snakebody = [headpos]
        temp_x = headpos[0]
        temp_y = headpos[y]

        for i in range(self.length-1):
            if direction == 'right':
                temp_x = temp_x - 1
            if direction == 'life':
                temp_x = temp_x + 1
            if direction == 'up':
                temp_y = temp_y - 1
            if direction == 'down':
                temp_y = temp_y + 1
            self.snakebody.append([temp_x, temp_y])
    def draw_self(self,screen):
        for pos in self.snakebody:
            pygame.draw.rect(screen, BLACK, (pos[0]*20, pos[1]*20, 20, 20))

