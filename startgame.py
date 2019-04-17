import os
import pygame
import time
import random

from snake import snake

BLACK = (0, 0, 0)
WHILE = (255, 255, 255)
RED = (255, 0, 0)
ROWS = 255

class game:
    def __init__(self):
        self.level = 0
        self.score = 0
        self.snake = snake()
        self.start_pos = []
        self.fruitPos = []
        self.screen = pygame.display.set_mode((ROWS, ROWS))
    def start(self):
        self.drawscreen()

    def check_status(self):
        snake = self.snake
        if snake.snakebody[0] == self.fruitPos:
            return 1
        if snake.snakebody[0] in snake.snakebody[1:]:
            return -1
        if snake.snakebody[0] in self.start_pos:
            return -1
        return 0

    def drawscreen(self):
        self.screen.fill(WHILE)
        scoreText = self.scoreFont.render(u'score: ' + str(self.score), True, BLACK)
        levelText = self.scoreFont.render(u'level: ' + str(self.level), True, BLACK)
        pygame.draw.line(self.screen, BLACK, (0, 50), (512, 50), 3)
        self.screen.blit(scoreText, (25, 115))
        self.screen.blit(levelText, (25, 271))
        self.snake.draw_self(self.screen)
        self.drawFruit()
        self.drawObstacle()

    def drawFruit(self):
        if not self.isFruitShowing:
            tempPos = None
            while not tempPos or tempPos in self.snake.snakebody:
                fX = random.randint(0, ROWS-1)
                fY = random.randint(0, ROWS-1)
                tempPos = (fX, fY)
            self.fruitPos = tempPos
        pygame.draw.rect(self.screen, BLACK, \
                             (self.fruitPos[0] * 20, self.fruitPos[1] * 20, 20, 20))
        self.isFruitShowing = True

    def drawObstacle(self):
        if self.level < 5:
            return
        if 5 < self.level < 10:
            fX = random.randint(0, ROWS - 1)
            fY = random.randint(0, ROWS - 1)
            self.start_pos.append((fX, fY))
            tmp = []
            while not tmp:
                for i in range(5):
                    tmp = random.randint(0, 1)
                    if tmp == 0:
                        fX = fX + 1
                        self.start_pos.append(fX, fY)
                    else:
                        fY = fY + 1
                        self.start_pos.append(fX, fY)
                tmp = [val for val in self.start_poc if val in self.snake.snakebody]
            for pos in self.start_poc:
                pygame.draw.rect(self.screen, RED, (pos[0] * 20, pos[1] * 20, 20, 20))

        if self.level > 20:
            fX = random.randint(0, ROWS - 1)
            fY = random.randint(0, ROWS - 1)
            self.start_pos.append((fX, fY))
            tmp = []
            while not tmp:
                for i in range(10):
                    tmp = random.randint(0, 1)
                    if tmp == 0:
                        fX = fX + 1
                        self.start_pos.append(fX, fY)
                    else:
                        fY = fY + 1
                        self.start_pos.append(fX, fY)
                tmp = [val for val in self.start_poc if val in self.snake.snakebody]
            for pos in self.start_poc:
                pygame.draw.rect(self.screen, RED, (pos[0] * 20, pos[1] * 20, 20, 20))


if __name__ == '__main__':
    game = game()
    game.start()
