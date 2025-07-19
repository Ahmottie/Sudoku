matrix = [
     [3,0,6,5,0,8,4,0,0],
     [5,2,0,0,0,0,0,0,0],
     [0,8,7,0,0,0,0,3,1],
     [0,0,3,0,1,0,0,8,0],
     [9,0,0,8,6,3,0,0,5],
     [0,5,0,0,9,0,6,0,0],
     [1,3,0,0,0,0,2,5,0],
     [0,0,0,0,0,0,0,7,4],
     [0,0,5,2,0,6,3,0,0],
     ]

def valid(matrix, row, column, number):
     if number in matrix[row]:
          return False

     for x in range(9):
          if matrix[x][column] == number:
               return False

     corner_row = row - (row % 3)
     corner_column = column - (column % 3)

     for i in range(3):
          for j in range(3):
               if matrix[corner_row + i][corner_column + j] == number:
                    return False
     return True

def solver(matrix, row, column):
     if row == 9:
          if column == 8:
               return True
          else:
               row += 1
               column = 0

          if matrix[row][column] > 0:
               return solver(matrix, row, column + 1)

          for number in range(1,10):
               if valid(matrix, row, column, number):

                    matrix[row][column] = number

                    if solver(matrix, row, column + 1):
                         return True

               matrix[row][column] = 0
          return False

if solver(matrix, 0, 0):
     for i in range(9):
          for j in range(9):
               print(matrix[i][j], end="")
else:
     print("No solutions!:(")

