from collections import deque

def bfs(x, y, team, visited, graph):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny] and graph[nx][ny] == team:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1

    return count

# 입력 처리
n, m = map(int, input().split())
graph = [input().strip() for _ in range(m)]

def solve_war_battle(n, m, graph):
    visited = [[False] * m for _ in range(n)]
    white_power = 0
    blue_power = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if graph[i][j] == 'W':
                    white_power += bfs(i, j, 'W', visited, graph) ** 2
                else:
                    blue_power += bfs(i, j, 'B', visited, graph) ** 2

    return white_power, blue_power

# 전투력 계산
white_power, blue_power = solve_war_battle(n, m, graph)
print(white_power, blue_power)
