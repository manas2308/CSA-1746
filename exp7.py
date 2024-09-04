from collections import deque

def bfs(graph, start):
    # Initialize a queue with the start node
    queue = deque([start])
    # Initialize a set to keep track of visited nodes
    visited = set()
    # List to store the order of visited nodes
    order = []

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()

        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            # Add the node to the order list
            order.append(node)

            # Enqueue all adjacent nodes that haven't been visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
# Perform BFS from the start node
bfs_order = bfs(graph, start_node)

print("BFS Order:", bfs_order)
