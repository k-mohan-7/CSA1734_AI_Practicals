import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_best_first_search(maze, start, end):
    open_list = []
    came_from = {}
    visited = set()
    
    heapq.heappush(open_list, (heuristic(start, end), start))
    came_from[start] = None
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while open_list:
        current_heuristic, current = heapq.heappop(open_list)
        
        if current == end:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        visited.add(current)
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < len(maze)) and (0 <= neighbor[1] < len(maze[0])):
                if maze[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    heapq.heappush(open_list, (heuristic(neighbor, end), neighbor))
    
    return None

maze = [
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)
path = greedy_best_first_search(maze, start, end)
print("Path from start to end:", path)
