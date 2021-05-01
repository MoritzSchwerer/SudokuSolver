#!/usr/bin/env python3

import pygame
from constants import *
import time



def draw_tiles(win, board, font, color):

        for row in range(ROWS):
            for col in range(COLS):
                if color[row][col] == True:
                    pygame.draw.rect(win, (0,210,0), (col*SQUARE_SIZE + 201, row*SQUARE_SIZE + 3, SQUARE_SIZE, SQUARE_SIZE))

        #pygame.draw.rect(win, (211,211,211), (row*SQUARE_SIZE + 200, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        width = 2
        for col in range(COLS + 1):
            if(col%3 == 0):
                width = 4
            pygame.draw.line(win, BLACK, (col * SQUARE_SIZE + 200,2), (col * SQUARE_SIZE + 200,HEIGHT//ROWS * ROWS + 2), width=width)
            width = 2


        for row in range(ROWS + 1):
            if(row%3 == 0):
                width = 4
            pygame.draw.line(win, BLACK, (200, row * SQUARE_SIZE + 2), (800//COLS * COLS + 3, row * SQUARE_SIZE + 2), width=width)
            width = 2


        for row in range(ROWS):
            for col in range(COLS):
               text = font.render(str(board[col][row]), True, BLACK)
               win.blit(text, (215 + row * SQUARE_SIZE,4 + col * SQUARE_SIZE))


def draw_scores(win, checks, font, start):
    font = pygame.font.Font('freesansbold.ttf', 30)

    text = font.render('Checks:', True, BLACK)
    text2 = font.render(str(checks), True, BLACK)
    win.blit(text, (10,10))
    win.blit(text2, (10,40))


    text = font.render('Time: ' + str(round(time.time() - start, 2)), True, BLACK)
    win.blit(text, (10, 80))
