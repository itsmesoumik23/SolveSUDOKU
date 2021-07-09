from math import floor

def getBoxID(row, col):
    colVal = floor(col / 3)
    rowVal = floor(row / 3) * 3
    return colVal+rowVal

def SolveSudoku(board):
    # board -> 9x9 array
    n = len(board)
    # each boxes consisting of n mini squares
    boxes = [{} for _ in range(n)]
    # total rows and columns also n
    # initiate each cell with empty hashmap
    rows, cols = [{} for _ in range(n)], [{} for _ in range(n)]


    # to check the initially determined values.
    for r in range(n):
        for c in range(n):
            if board[r][c] != ".":
                val = board[r][c]
                boxID = getBoxID(r, c)
                # if value found then set the hashmap with that value
                boxes[boxID][val] = True
                rows[r][val] = True
                cols[c][val] = True

    solveBackTrack(board, boxes, rows, cols, 0, 0)

# check whether a value is valid in a particular cell or not
# for that we need to check in that row, column and the box containing that cell
def isValid(box, row, col, num):
    if num in box or num in row or num in col:
        return False
    return True

def solveBackTrack(board, boxes, rows, cols, r, c):
    if r == len(board) or c == len(board[0]):
        return True
    else:
        if board[r][c] == ".":
            for num in range(1, 10):    # 1 to 9
                numVal = str(num)
                # setting the value of num in original board
                board[r][c] = numVal

                # get the box id of that cell containing box
                boxID = getBoxID(r, c)
                box = boxes[boxID]
                row = rows[r]
                col = cols[c]


                # now check if it is valid or not
                if isValid(box, row, col, numVal):
                    box[numVal] = True
                    row[numVal] = True
                    col[numVal] = True

                    # now check if we are at end of a row
                    # then we we start from new row with 0th column
                    if c == len(board[0])-1:
                        if solveBackTrack(board, boxes, rows, cols, r+1, 0):
                            return True
                    else:
                        if solveBackTrack(board, boxes, rows, cols, r, c+1):
                            return True
                    box.pop(numVal)
                    row.pop(numVal)
                    col.pop(numVal)

                board[r][c] = "."
        else:
            if c == len(board[0])-1:
                if solveBackTrack(board, boxes, rows, cols, r+1, 0):
                    return True
            else:
                if solveBackTrack(board, boxes, rows, cols, r, c+1):
                    return True
    return False

board = [
  ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
  ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
  ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
  ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
  ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
  ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
  ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
  ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
  ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]

SolveSudoku(board)
print(board)
