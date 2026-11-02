def issafe(board, row, col, n):

  for i in range(row):
    if board[i][col]==1:
      return False

  i,j=row-1, col-1
  while i>=0 and j>=0:
    if board[i][j] == 1:
      return False
    i-=1
    j-=1

  i,j=row-1, col+1
  while i>=0 and j<n:
    if board[i][j]==1:
      return False
    i-=1
    j+=1
  return True

def solve(board, row, n):
  if row==n:
    return True

  for col in range(n):
    if issafe(board, row, col, n):
      board[row][col] = 1
  
      if solve(board, row+1, n):
        return True
  
      board[row][col]=0

  return False

n=int(input("Enter number of queens"))
board = [[0]*n for i in range(n)]

first = int(input("Enter col for first queen: "))
board[0][first] = 1

if solve(board, 1, n):
  print("Solution: ")
  for i in board:
    print(i)

else:
  print("No solution")
    