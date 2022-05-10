puzzle = []
            #i 0  1  2  3  4
puzzle.append([5, 1, 2, 3, 4])#row 0
puzzle.append([1, 2, 3, 4, 5])#row 1
puzzle.append([2, 3, 0, 5, 1])#row 2
puzzle.append([3, 0, 0, 1, 2])#row 3
puzzle.append([0, 0, 0, 0, 0])#row 4
cages = []
cages.append([6, 2, 0, 5])
cages.append([7, 3, 2, 6, 7])
cages.append([9, 2, 4, 9])

checks = 2
backtracks = 1
def check_rows_valid(puzzle):
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
    print("\n")
print("--Solution--\n")
check_rows_valid(puzzle)
print("checks: ", checks, "backtrack: ", backtracks)