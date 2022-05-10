from solverFuncs import *
puzzle = []
puzzle.append([0, 0, 0, 0, 0])
puzzle.append([0, 0, 0, 0, 0])
puzzle.append([0, 0, 0, 0, 0])
puzzle.append([0, 0, 0, 0, 0])
puzzle.append([0, 0, 0, 0, 0])
cages = get_cages()
col = 0
row = 0
   
while row < 5:
   puzzle[row][col] += 1
   if check_valid(puzzle, cages):
      col += 1
      if col == 5:
         col = 0
         row += 1
   elif puzzle[row][col] == 5:
      while puzzle[row][col] == 5:
         puzzle[row][col] = 0
         col -= 1
         if col < 0 :
            col = 4
            row -= 1
            
print(puzzle)   
print("solution")