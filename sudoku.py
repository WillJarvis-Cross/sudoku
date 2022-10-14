from copy import deepcopy
import sys
import random

sys.setrecursionlimit(10000)
def start(puzzle):
    originalPuzzle = deepcopy(puzzle)
    currentSpot = nextOpenSpot(puzzle, 0, 0)
    final = solvePuzzle(puzzle, originalPuzzle, currentSpot[0], currentSpot[1], 1)
    if final == None:
        print("impossible puzzle")
    else:
        print("\nFinal Puzzle Solution:")
        printPuzzle(final)

def solvePuzzle(puzzle, originalPuzzle, x, y, currNum):
    while x != -1:
        newNum = tryFromThisNum(puzzle, x, y, currNum)
        if newNum:
            puzzle[x][y] = newNum
        else:
            if x == 0:     
                return backtrack(puzzle, originalPuzzle, 8, y - 1)
            return backtrack(puzzle, originalPuzzle, x - 1, y)
        x, y = nextOpenSpot(puzzle, x, y)
        currNum = 1
        if x == -1 or x > 8 or y > 8:
            return puzzle

def backtrack(puzzle, originalPuzzle, x, y):
    while x >= 0 and y >= 0:
        if originalPuzzle[x][y] == 0:
            oldNum = puzzle[x][y]
            puzzle[x][y] = 0
            if oldNum == 9:
                if x == 0:
                    return backtrack(puzzle, originalPuzzle, 8, y - 1)
                return backtrack(puzzle, originalPuzzle, x - 1, y)
            
            return solvePuzzle(puzzle, originalPuzzle, x, y, oldNum + 1)
        if x == 0:
            y -= 1
            x = 8
        else:
            x -= 1
    return None

        
def tryFromThisNum(puzzle, xPos, yPos, num):
    while num < 10:
        if isValidNum(puzzle, xPos, yPos, num):           
            return num
        num += 1
    return None


def nextOpenSpot(puzzle, xPos, yPos):
    if xPos <= 8 and yPos <= 8:
        if puzzle[xPos][yPos] == 0:
            return xPos, yPos
        return nextOpenSpot(puzzle, xPos + 1, yPos)
    if yPos > 8:
        return -1, -1
    return nextOpenSpot(puzzle, 0, yPos + 1)

def isValidNum(puzzle, xPos, yPos, num):
    xSection = (xPos // 3) * 3
    ySection = (yPos // 3) * 3

    #checking inside the 3x3 box of this position
    #to see if this number conflicts with this box
    for i in range(3):
        for j in range(3):
            if puzzle[xSection + i][ySection + j] == num:
                return False

    #checking if the number conflicts with a number in its column or row
    for i in range(9):
        if puzzle[i][yPos] == num or puzzle[xPos][i] == num:
            return False
    return True

def printPuzzle(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if j == 8:
                print(puzzle[i][j])
                if i < 8:
                    print("---------------------------------")
            else:
                print(puzzle[i][j], end=" | ")

def randomBoardMaker():
    puzzle = [ [0] * 9 for _ in range(9)]
    numberSpots = random.randint(0, 10)
    i = 0
    while i < 10 + numberSpots:
        nextSpot = (random.randint(0, 8), random.randint(0, 8))
        nextNum = random.randint(0, 8)
        if isValidNum(puzzle, nextSpot[0], nextSpot[1], nextNum):
            puzzle[nextSpot[0]][nextSpot[1]] = nextNum
            i += 1
    printPuzzle(puzzle)
    return puzzle
    

puzzle = [[0,8,0,0,0,0,4,7,0],
          [4,3,0,8,0,0,1,0,0],
          [0,0,2,0,6,0,0,3,0],
          [6,2,0,0,7,8,0,4,0],
          [1,0,8,9,0,0,7,0,6],
          [0,0,0,0,5,2,0,0,0],
          [0,0,0,0,0,0,0,8,0],
          [7,0,0,0,8,6,0,5,0],
          [0,0,0,7,0,0,9,0,3]]

randPuzzle = randomBoardMaker()
start(randPuzzle)