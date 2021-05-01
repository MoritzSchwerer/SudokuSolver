import pygame
from constants import *
from board import *
from Utils import *
import time

pygame.init()

# window
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku Solver")
icon = pygame.image.load('images/pastime.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 70)
color = []
fontS = pygame.font.Font('freesansbold.ttf', 30)
fontSS = pygame.font.Font('freesansbold.ttf', 24)
start = time.time()


list = getSudoku("sudokus/sudoku.csv")
list = parseIntList(list)

color = initialize_colors(list)

running = True
while running:

    WIN.fill(GRAY)
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if VISUALISATION_INDEX < 7:
                    VISUALISATION_INDEX+=1
            if event.button == 3:
                if VISUALISATION_INDEX > 0:
                    VISUALISATION_INDEX-=1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False



    text = fontS.render('Speed: ' + str(VISUALISATION_SPEEDS[VISUALISATION_INDEX]), True, BLACK)
    text2 = fontSS.render('left click to', True, BLACK)
    text3 = fontSS.render('increase speed', True, BLACK)
    text4 = fontSS.render('right click to', True, BLACK)
    text5 = fontSS.render('decrease speed', True, BLACK)
    text6 = fontSS.render('space to start', True, BLACK)
    text7 = fontSS.render('the simulation', True, BLACK)
    WIN.blit(text, (805, 20))
    WIN.blit(text2, (805, 80))
    WIN.blit(text3, (805, 100))
    WIN.blit(text4, (805, 160))
    WIN.blit(text5, (805, 180))
    WIN.blit(text6, (805, 240))
    WIN.blit(text7, (805, 260))


    global CHECKS
    draw_tiles(WIN, list, font, color)
    pygame.display.update()






start = time.time()
solve(list,font, WIN, color,fontS, start, VISUALISATION_SPEEDS[VISUALISATION_INDEX])


var = True
for i in range (9):
    for j in range(9):
        if not checkBoard(list, i, j):
            var = False

text = ''
if var:
    text = font.render("Success!", True, (210,0,0))
else:
    text = font.render("Could not solve!", True, (210,0,0))

WIN.blit(text, (330, 300))
pygame.display.update()

waitforcancel()

