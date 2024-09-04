from collections import deque

# Possible actions
ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'CLEAN']

# Function to check if a position is within the grid boundaries
def is_valid_position(x, y, grid_size):
    return 0 <= x < grid_size and 0 <= y < grid_size

# Function to apply an action to the current state
def apply_action(state, action):
    x, y, grid = state
    grid_size = len(grid)
    new_grid = [row[:] for row in grid]  # Create a copy of the grid

    if action == 'CLEAN':
        new_grid[x][y] = 0
    elif action == 'UP' and is_valid_position(x - 1, y, grid_size):
        x -= 1
    elif action == 'DOWN' and is_valid_position(x + 1, y, grid_size):
        x += 1
    elif action == 'LEFT' and is_valid_position(x, y - 1, grid_size):
        y -= 1
    elif action == 'RIGHT' and is_valid_position(x, y + 1, grid_size):
        y += 1

    return (x, y, new_grid)

# Function to check if the grid is completely clean
def is_goal_state(grid):
    return all(cell == 0 for row in grid for cell in row)

# Function to solve the vacuum cleaner problem using BFS
def bfs_vacuum_cleaner(initial_state):
    queue = deque([(initial_state, [])])  # (state, path)
    visited = set()

    while queue:
        state, path = queue.popleft()
        x, y, grid = state

        if is_goal_state(grid):
            return path

        state_key = (x, y, tuple(tuple(row) for row in grid))
        if state_key in visited:
            continue

        visited.add(state_key)

        for action in ACTIONS:
            new_state = apply_action(state, action)
            queue.append((new_state, path + [action]))

    return None

# Example usage:
initial_grid = [
    [1, 0],  # 1 represents a dirty tile, 0 represents a clean tile
    [1, 1]
]

# Initial state: (x, y) position of the vacuum cleaner, and the grid
initial_state = (0, 0, initial_grid)

# Solve the problem
solution = bfs_vacuum_cleaner(initial_state)

if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found")
