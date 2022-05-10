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

puzzle[0][0] +=1

print(puzzle[0][0])