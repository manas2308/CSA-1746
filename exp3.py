from collections import deque

def is_valid_state(state, m, n):
    x, y = state
    return 0 <= x <= m and 0 <= y <= n

def bfs_water_jug(m, n, d):
    visited = set()
    queue = deque([(0, 0)])  # Starting with both jugs empty
    visited.add((0, 0))
    
    while queue:
        x, y = queue.popleft()

        if x == d or y == d:
            return f"Solution found: {x} liters in Jug 1 and {y} liters in Jug 2"

        # Possible states
        next_states = [
            (m, y),  # Fill Jug 1
            (x, n),  # Fill Jug 2
            (0, y),  # Empty Jug 1
            (x, 0),  # Empty Jug 2
            (x - min(x, n - y), y + min(x, n - y)),  # Pour Jug 1 to Jug 2
            (x + min(y, m - x), y - min(y, m - x))   # Pour Jug 2 to Jug 1
        ]

        for state in next_states:
            if state not in visited and is_valid_state(state, m, n):
                visited.add(state)
                queue.append(state)
    
    return "No solution found"

# Define jug capacities and the target amount
m = 4  # Capacity of Jug 1
n = 3  # Capacity of Jug 2
d = 2  # Desired amount

# Solve the problem
result = bfs_water_jug(m, n, d)
print(result)
