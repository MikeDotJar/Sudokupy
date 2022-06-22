
def displayBoard(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("--------------------")
        s = ""
        for j in range(len(board)):
            if j % 3 == 0:
                s += "|"
            s += board[i][j] + " "
        print(s)


def isValid(board, k, i, j):

    try:
        board[i][j] = str(k)
    except:
        print(i, " ", j)
        exit()
    row = board[i].copy()
    column = [row[j] for row in board].copy()

    x = (i // 3) * 3
    y = (j // 3) * 3

    box = [board[x][y],board[x][y+1],board[x][y+2],board[x+1][y],board[x+1][y+1],board[x+1][y+2],board[x+2][y],board[x+2][y+1],board[x+2][y+2]]

    row.sort()
    for k in range(1, len(row)):
        if row[k - 1] != "." and row[k - 1] == row[k]:
            return False
    column.sort()
    for k in range(1, len(row)):
        if column[k - 1] != "." and column[k - 1] == column[k]:
            return False
    box.sort()
    for k in range(1, len(row)):
        if box[k - 1] != "." and box[k - 1] == box[k]:
            return False

    return True


def DFS(board, i, j):
    while j < 9 and board[i][j] != ".":
        j += 1

    if j == 9:
        j = 0
        i += 1

    if i == 9:
        return board

    for k in range(1, 10):
        if isValid(board, k, i, j):
            board[i][j] = str(k)
            if DFS(board, i, j):
                return board
        board[i][j] = "."


def isValidStart(board):

    for j in range(len(board)):
        column = [row[j] for row in board].copy()
        column.sort()
        for l in range(1, len(column)):
            if column[l - 1] != "." and column[l - 1] == column[l]:
                return False

    for i in range(len(board)):
        row = board[i].copy()
        row.sort()
        for k in range(1, len(row)):
            if row[k - 1] != "." and row[k - 1] == row[k]:
                return False

    i = 0
    j = 0

    while i < 9:
        box = [board[i][j], board[i][j + 1], board[i][j + 2], board[i + 1][j], board[i + 1][j + 1],
               board[i + 1][j + 2], board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]]
        box.sort()
        for m in range(1, len(box)):
            if box[m - 1] != "." and box[m - 1] == box[m]:
                return False

        j += 3
        if j == 9:
            j = 0
            i += 3

    return True

board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print("Initial Board:")
displayBoard(board)

if isValidStart(board):
    board = DFS(board, 0, 0)
    print("\n\n")
    print("Final Board:")
    displayBoard(board)
else:
    print("This board isn't valid!")

