from collections import deque

"""
Wyobrazmy ze mamy szachownice w ktorej na kazdym polu jest mala liczba np od 1 do 5
Startujemy w gornym lewym rogu i chcemy znalezc najtansza droge do lewego prawego
rogu
"""


def chess(board: list[list[int]]) -> int:
    l = len(board)
    cost = [[float("inf") for i in range(l)] for j in range(l)]
    cost[0][0] = board[0][0]

    def dfs(r: int, c: int) -> int:
        if r == c == l - 1:
            return cost[r][c]

        # bias
        if r + 1 < l and c + 1 < l:
            if cost[r + 1][c + 1] > cost[r][c] + board[r + 1][c + 1]:
                cost[r + 1][c + 1] = min(
                    cost[r + 1][c + 1], cost[r][c] + board[r + 1][c + 1]
                )
                dfs(r + 1, c + 1)
        # down
        elif r + 1 < l:
            if cost[r + 1][c] > cost[r][c] + board[r + 1][c]:
                cost[r + 1][c] = min(cost[r + 1][c], cost[r][c] + board[r + 1][c])
                dfs(r + 1, c)
        # right
        elif c + 1 < l:
            if cost[r][c + 1] > cost[r][c] + board[r][c + 1]:
                cost[r][c + 1] = min(cost[r][c + 1], cost[r][c] + board[r][c + 1])
                dfs(r, c + 1)

    dfs(0, 0)
    return cost[l - 1][l - 1]


if __name__ == "__main__":

    board1 = [[1, 5, 5, 5], [1, 5, 5, 5], [1, 5, 5, 5], [1, 1, 1, 1]]
    board2 = [[2, 2, 2, 2], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    board3 = [[1, 2, 3, 4], [7, 1, 6, 5], [8, 9, 2, 2], [1, 1, 10, 1]]

    print(chess(board3))
