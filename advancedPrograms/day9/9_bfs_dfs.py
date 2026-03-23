# BFS and DFS using adjacency list
from collections import deque

def bfs(adj_list, start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(adj_list.get(node, []))
    return result

def dfs(adj_list, start):
    visited = set()
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(adj_list.get(node, [])))
    return result

if __name__ == "__main__":
    n = int(input("Enter number of nodes: "))
    adj_list = {}
    for _ in range(n):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        adj_list[node] = neighbors
    start = input("Enter start node: ")
    print("BFS:", bfs(adj_list, start))
    print("DFS:", dfs(adj_list, start))
