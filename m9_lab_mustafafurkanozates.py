import random
import json 
from datetime import datetime
dateTimePlayed = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
playDictionary = {}
userPlayDictionary = {}

# if fh.fileExists("gamelog.json"):
#   content = fh.readFile('gamelog.json')
#   userPlayDictionary = json.loads(content)


EX = 'X'
REALEMPTY = ' '
EMPTY = 'E'
TREASURE = 'T'
MONSTER = 'M'
VENOM = 'V'
SWORD = 'S'
POTION ='P'

whatToAddInGrid = (TREASURE, TREASURE, TREASURE, TREASURE, TREASURE, 
MONSTER, MONSTER, MONSTER, MONSTER, MONSTER,
SWORD, SWORD,
POTION, POTION, POTION,
VENOM, VENOM, VENOM)


NROWS_IN_GRID = 6
NCOLS_IN_GRID = 7

grid = []
emptyGrid = []

for r in range(0, NROWS_IN_GRID): #0-5
  aRow = []
  bRow = []
  for c in range(0, NCOLS_IN_GRID):#0-7
    aRow.append(EMPTY)
    bRow.append(REALEMPTY)
  grid.append(aRow)
  emptyGrid.append(bRow)


def findEmptyCell(aGrid, nRows, nCols):
  #Find a random starting cell that is empty.
  while True:
    row = random.randrange(nRows)
    col = random.randrange(nCols)
    if(aGrid[row][col] == EMPTY):
      return row, col

for item in whatToAddInGrid:
  rowRandom, colRandom = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
  grid[rowRandom][colRandom] = item

# for row in grid:
#   print(row)

#Setting the starting cell
startRow, startCol = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
print('Starting at row:', startRow + 1, 'col:', startCol + 1)

points = 0
nPots = 0
nSwords = 0
# print("\033[H\033[J"

while True:
  #Printing the current situation on the screen
  
  emptyGrid[startRow][startCol] = grid[startRow][startCol]
  # print("\033[H\033[J", end="")
  for row in emptyGrid:
    print(row)
  # for row in grid:
  #   print(row)
  print(f'Score: [{points}] Sword: [{nSwords}] Potion: [{nPots}]')

  #move the user around
  direction = input('Press L, U, R, D to move: ').lower().strip()
  print()
  foundInCell = grid[startRow][startCol]
  backupRow, backupCol = startRow, startCol
  if(direction == 'l'):
    if(startCol == 0):
      startCol = NCOLS_IN_GRID - 1
    else:
      startCol -= 1 
  elif (direction == 'r'):
    if(startCol == NCOLS_IN_GRID - 1):
      startCol = 0
    else:
      startCol += 1      
  elif(direction == 'u'):
    if(startRow == 0):
      startRow = NROWS_IN_GRID - 1
    else:
      startRow -= 1 
  elif(direction == 'd'):
    if(startRow == NROWS_IN_GRID - 1):
      startRow = 0
    else:
      startRow += 1  

  # foundInCell = grid[startRow][startCol]
  
  # print('Now at row', startRow, ' col:', startCol, ' cell contains:', foundInCell)
  if emptyGrid[startRow][startCol] != ' ':
    startRow, startCol = backupRow, backupCol
    print('You already moved there.')
  elif foundInCell == TREASURE:
    points += 1
    print(f'You found a treasure!\n')
    # foundInCell = REALEMPTY
  elif foundInCell == POTION:
    # if nPots == 0:
    nPots += 1
    print('You found a potion!')
    # foundInCell = REALEMPTY
    # elif nPots != 0:
    #   print('You found a potion but you can only carry one.')
  elif foundInCell == SWORD:
    # if nSwords == 0:
    nSwords += 1
    print('You found a sword!')
    # foundInCell = REALEMPTY
    # elif nSwords != 0:
    #   print('You found a sword but you can only carry one.')
  elif foundInCell == MONSTER:
    if nSwords != 0:
      nSwords -= 1
      print('There is a monster attack! You survived with your sword!')
      # foundInCell = REALEMPTY
    elif nSwords == 0:
      print('There is a monster attack! You died.')
      break
  elif foundInCell == VENOM:
    if nPots != 0:
      nPots -= 1
      print('There is a venom attack! You survived with your potion!')
      # foundInCell = REALEMPTY
    elif nPots == 0:
      print('There is a venom attack! You died.')
      break
  points += 1
  
  #grid[startRow][startCol] = EX

