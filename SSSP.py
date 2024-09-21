from collections import defaultdict
import sys

# Increase the recursion limit to 10000
sys.setrecursionlimit(100000)
def journey_to_the_moon(n, edges):
    """Calculates the number of pairs of astronauts from different countries.

    Args:
        n: The total number of astronauts.
        edges: A list of pairs representing connections between astronauts in the same country.

    Returns:
        The number of possible pairs of astronauts from different countries.
    """

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    component_sizes = []

    def dfs(node):
        nonlocal component_size
        visited.add(node)
        component_size += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            component_size = 0
            dfs(node)
            component_sizes.append(component_size)

    total_pairs = 0
    for size in component_sizes:
        print(size)
        total_pairs += size * (n - size)
    return total_pairs // 2  # Divide by 2 to account for double counting

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result = journey_to_the_moon(n, edges)
    print(result)