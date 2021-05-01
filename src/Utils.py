import csv
import random
from src.board import *
from src.constants import *


def getSudoku(string):
    with open(string, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        list = []
        for row in reader:
            temp = []
            for pos in row:
                temp.append(pos)
            list.append(temp)
    return list


def writeSudoku(list, string):
    with open(string, 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')

        for row in list:
            writer.writerow(row)


def generateRandomSudoku():
    list = []
    for i in range(0, 9):
        temp = []
        for j in range(1, 10):
            temp.append(random.randrange(0, 10, 1))
        list.append(temp)

    return list


def checkRows(list, x, y):
    for i in range(0, 9):
        if i != y and list[x][i] == list[x][y]:
            return False
        if i != x and list[i][y] == list[x][y]:
            return False
    return True


def checkSquare(list, x, y):
    tempx = x // 3
    tempy = y // 3
    rangexlow = tempx * 3
    rangeylow = tempy * 3

    for i in range(rangexlow, rangexlow + 3):
        for j in range(rangeylow, rangeylow + 3):
            if i != x and j != y and list[i][j] == list[x][y]:
                return False
    return True


def checkBoard(list, x, y):
    return checkRows(list, x, y) and checkSquare(list, x, y)


def parseIntList(list):
    result = []
    for row in list:
        temp = []
        for pos in row:
            temp.append(int(pos))
        result.append(temp)

    return result

def solve(list, font, WIN, color, fontS, start, speed):

    temp = findNext(list, font, WIN, color, fontS, start, speed)
    if not temp:
        return True
    else:
        x, y = temp

    for i in range(1, 10):
        global CHECKS
        CHECKS+=1
        list[x][y] = i
        if checkBoard(list, x, y):

            color[x][y] = True

            if solve(list, font, WIN, color, fontS, start, speed):
                visualize(list, font, WIN, color, fontS, start)
                return True

            list[x][y] = 0
            color[x][y] = False
    list[x][y] = 0
    color[x][y] = False
    return False


def findNext(list, font, WIN, color, fontS, start, speed):
    if CHECKS % speed == 0:
        visualize(list, font, WIN, color, fontS, start)

    for i in range(0, 9):
        for j in range(0, 9):
            if list[i][j] == 0:
                return i, j


def visualize(list, font, WIN, color, fontS, start):
        WIN.fill(GRAY)
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()


        global CHECKS
        draw_scores(WIN, CHECKS, fontS, start)
        draw_tiles(WIN, list, font, color)
        pygame.display.update()


def waitforcancel():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False


def initialize_colors(list):
    color = []
    for i in range(9):
        temp = []
        for j in range(9):
            if list[i][j] != 0:
                temp.append(True)
            else:
                temp.append(False)
        color.append(temp)
    return color

