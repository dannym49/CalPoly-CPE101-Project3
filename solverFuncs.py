# These are the required functions for this project.
#
# I highly recommend adding functions to check a single
# row, check a single column, and check a single cage.

def check_rows_valid(puzzle):
   for row in range(5):
        for col in range(5):
         #this nested for loop grabs an entire row and goes through each column
         #to check if the value for the column appears more than once in that row
            if puzzle[row].count(puzzle[row][col]) > 1 and puzzle[row][col] != 0:
               return False
   return True
     
def check_columns_valid(puzzle):
   for col in range(5):
      index_value=[]
      for row in range(5):
         index_value.append(puzzle[row][col])
         #row is the first index which is the row, 
         #i is the index of that individual row
         if index_value.count(puzzle[row][col]) > 1 and puzzle[row][col] != 0:
               return False
   return True

def check_cages_valid(puzzle, cages):
   for cage in cages:
      val=[]
      for num in cage[2:]:
            val.append(puzzle[num//5][num%5])
      if (sum(val) != cage[0] and 0 not in val) or (0 in val and sum(val) >= cage[0]):
         return False
   return True   
       
def check_valid(puzzle, cages):
   return check_rows_valid(puzzle) and check_columns_valid(puzzle) and check_cages_valid(puzzle, cages)
      

def get_cages():
   numCages=input("Number of cages: ")
   cage=[]
   for i in range(int(numCages)):
      cageList = input("Cage number %d: " % i )
      cage.append(cageList.split())
      for j in range(len(cage[i])):
         cage[i][j] = int(cage[i][j])
   return cage