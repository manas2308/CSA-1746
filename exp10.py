from heapq import heappop, heappush

# A* algorithm implementation
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    def heuristic(a, b):
        # Using Manhattan distance as the heuristic
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Directions for moving up, down, left, right
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Priority queue to store (cost, (x, y))
    open_list = []
    heappush(open_list, (0 + heuristic(start, goal), 0, start))
    
    # To track visited nodes
    came_from = {}
    cost_so_far = {start: 0}
    
    while open_list:
        _, current_cost, current = heappop(open_list)
        
        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path
        
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                new_cost = current_cost + 1
                
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, goal)
                    heappush(open_list, (priority, new_cost, neighbor))
                    came_from[neighbor] = current

    return None  # No path found

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
path = astar(grid, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found.")
