from solverFuncs import *

def main():
   puzzle = []
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   cages = get_cages()
   col = 0
   row = 0
   checks = 0
   backtracks = 0
 
   while row < 5:
      puzzle[row][col] += 1
      checks +=1
      if check_valid(puzzle, cages):
         col += 1
         if col == 5:
            col = 0
            row += 1
      elif puzzle[row][col] == 5:
         while puzzle[row][col] == 5:
            backtracks += 1
            puzzle[row][col] = 0
            col -= 1
            if col < 0 :
               col = 4
               row -= 1

   print("\n--Solution--\n")
   row = 0
   for col in range(5):
      print(puzzle[row][col], end = ' ')
   print(" ")
   row = 1
   for col in range(5):
      print(puzzle[row][col], end = ' ')
   print(" ")
   row = 2
   for col in range(5):
      print(puzzle[row][col], end = ' ')
   print(" ")
   row = 3
   for col in range(5):
      print(puzzle[row][col], end = ' ')
   print(" ")
   row = 4
   for col in range(5):
      print(puzzle[row][col], end = ' ')
   print("\nchecks:", checks, "backtracks:", backtracks)
if __name__ == '__main__':
   main()
