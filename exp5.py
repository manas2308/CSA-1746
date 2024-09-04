from collections import deque

# Function to check if a state is valid
def is_valid_state(state):
    m_left, c_left, m_right, c_right = state
    return (0 <= m_left <= 3 and 0 <= c_left <= 3 and
            0 <= m_right <= 3 and 0 <= c_right <= 3 and
            (m_left == 0 or m_left >= c_left) and
            (m_right == 0 or m_right >= c_right))

# Function to generate possible moves
def get_successors(state, boat_on_left):
    m_left, c_left, m_right, c_right = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    successors = []
    
    if boat_on_left:
        for m, c in moves:
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c)
            if is_valid_state(new_state):
                successors.append((new_state, False))
    else:
        for m, c in moves:
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c)
            if is_valid_state(new_state):
                successors.append((new_state, True))
    
    return successors

# Function to solve the problem using BFS
def bfs_missionaries_cannibals():
    start_state = (3, 3, 0, 0)
    goal_state = (0, 0, 3, 3)
    queue = deque([(start_state, True, [])])  # (state, boat_on_left, path)
    visited = set()
    
    while queue:
        state, boat_on_left, path = queue.popleft()
        
        if state == goal_state:
            return path + [state]
        
        if (state, boat_on_left) in visited:
            continue
        
        visited.add((state, boat_on_left))
        
        for successor, new_boat_on_left in get_successors(state, boat_on_left):
            queue.append((successor, new_boat_on_left, path + [state]))
    
    return None

# Solve the problem
solution = bfs_missionaries_cannibals()
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found")
