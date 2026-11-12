
class Solution:
    def solveNQueens(self, n):
        result = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return

            for col in range(n):
                valid = True

                for i in range(row):
                    if board[i][col] == 'Q':
                        valid = False
                        break

                    if abs(row - i) == abs(col - next(
                        j for j in range(n) if board[i][j] == 'Q'
                    )):
                        valid = False
                        break

                if valid:
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        backtrack(0)
        return result
