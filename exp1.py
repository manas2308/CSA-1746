from heapq import heappush, heappop

# Heuristic: Manhattan distance
def manhattan(puzzle, goal):
    dist = 0
    for i in range(9):
        if puzzle[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal.index(puzzle[i]), 3)
            dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

# A* search algorithm
def a_star(puzzle, goal):
    goal_flat = [num for row in goal for num in row]
    start_flat = [num for row in puzzle for num in row]

    open_list = []
    closed_list = set()
    heappush(open_list, (manhattan(start_flat, goal_flat), 0, start_flat, None))

    while open_list:
        _, g, current, parent = heappop(open_list)

        if current == goal_flat:
            path = []
            while parent:
                path.append(current)
                current, parent = parent
            return path[::-1]

        closed_list.add(tuple(current))

        zero_index = current.index(0)
        x, y = divmod(zero_index, 3)
        neighbors = []

        # Move the blank tile (0) in four possible directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                neighbor = current[:]
                neighbor[zero_index], neighbor[nx * 3 + ny] = neighbor[nx * 3 + ny], neighbor[zero_index]
                if tuple(neighbor) not in closed_list:
                    heappush(open_list, (g + manhattan(neighbor, goal_flat), g + 1, neighbor, (current, parent)))
    
    return None

def print_puzzle(path):
    for step in path:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()

# Initial puzzle configuration
initial_puzzle = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Goal configuration
goal_puzzle = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Solve the puzzle
solution = a_star(initial_puzzle, goal_puzzle)
if solution:
    print_puzzle(solution)
else:
    print("No solution found")
