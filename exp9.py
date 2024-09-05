import itertools

# Function to solve TSP using dynamic programming
def tsp(graph):
    n = len(graph)
    dp = [[float('inf')] * (1 << n) for _ in range(n)]
    
    # Base case: start from node 0
    dp[0][1] = 0
    
    # Iterate over subsets of nodes
    for subset_size in range(2, n + 1):
        for subset in itertools.combinations(range(1, n), subset_size - 1):
            subset_mask = 1  # start with node 0 included
            for s in subset:
                subset_mask |= (1 << s)
                
            for u in subset:
                u_mask = subset_mask & ~(1 << u)
                dp[u][subset_mask] = min(dp[v][u_mask] + graph[v][u] for v in range(n) if (subset_mask & (1 << v)) and v != u)
    
    # Complete the tour
    final_mask = (1 << n) - 1
    return min(dp[u][final_mask] + graph[u][0] for u in range(1, n))

# Example usage with graph as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

result = tsp(graph)
print(f"Minimum tour cost: {result}")
