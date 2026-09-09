class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    square_index = (i // 3) * 3 + (j // 3)
                    if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in squares[square_index]:
                        return False

                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    squares[square_index].add(board[i][j])
        return True