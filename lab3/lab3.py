from collections import deque


print("Ляшенко Илья Денисович")
print("РПИа-о23")
#Реализация стека через массив




def dfs(maze, start, end):
    
    stack = [(start, [start])]
    visited = set()

    while stack:
        (current, path) = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        x, y = current
        if current == end:
            return path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                stack.append(((nx, ny), path + [(nx, ny)]))
    
    return None

def bfs(maze, start, end):
    
    queue = [(start, [start])]
    visited = set([start])

    while queue:
        (current, path) = queue.pop(0)
        x, y = current
        
        if current == end:
            return path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None  # Путь не найден


# Пример использования:
maze = [
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]
start = (0, 0)
end = (3, 3)

# Проверка DFS
path = dfs(maze, start, end)
if path is None:
    print("DFS: Путь не найден")
else:
    print(f"DFS Path: {path}")

# Проверка BFS
path = bfs(maze, start, end)
if path is None:
    print("BFS: Путь не найден")
else:
    print(f"BFS Path: {path}")

