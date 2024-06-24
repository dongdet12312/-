def can_reach_goal(board):
    n = len(board)
    visited = [[False] * n for _ in range(n)]

    def dfs(x, y):
        if x >= n or y >= n or visited[x][y]:
            return False
        if board[x][y] == 0:
            return False
        if x == n - 1 and y == n - 1:
            return True
        visited[x][y] = True
        jump = board[x][y]
        return dfs(x + jump, y) or dfs(x, y + jump)

    return dfs(0, 0)


# 입력 받기
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
if can_reach_goal(board):
    print("HaruHaru")
else:
    print("Hing")
