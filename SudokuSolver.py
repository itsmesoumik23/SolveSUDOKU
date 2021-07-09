from math import floor

def getBoxID(row, col):
    colVal = floor(col / 3)
    rowVal = floor(row / 3) * 3
    return colVal+rowVal

def SolveSudoku(board):
    # board -> 9x9 array
    n = len(board)
    # each boxes consisting of n mini squares
    boxes = [dict() for _ in range(n)]
    # total rows and columns also n
    # initiate each cell with empty hashmap
    rows, cols = [dict() for _ in range(n)], [dict() for _ in range(n)]

    # to check the initially determined values.
    for r in range(n):
        for c in range(n):
            if board[r][c] != " ":
                val = board[r][c]
                boxID = getBoxID(r, c)
                # if value found then set the hashmap with that value
                boxes[boxID][val] = True
                rows[r][val] = True
                cols[c][val] = True

    solveBackTrack(board, boxes, rows, cols, 0, 0)
