# LAB 4: Greedy Best-First Search
graph = {'S': [('A',2), ('B',1)],
         'A': [('G',10)],
         'B': [('G',4)],
         'G': []}
h = {'S': 4, 'A': 2, 'B': 3, 'G': 0}     # estimated distance to G
def cost_of(path):
    """Add up the REAL edge costs of a finished path."""
    return sum([w for n, w in graph[a] if n == b][0]
               for a, b in zip(path, path[1:]))
def greedy(start, goal):
    queue = [(h[start], [start])]        # (heuristic, path)
    while queue:
        queue.sort()                     # smallest h first
        _, path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path, cost_of(path)   # measure damage only at the end
        for n, w in graph[node]:
            queue.append((h[n], path + [n]))    # <-- w is THROWN AWAY
path, cost = greedy('S', 'G')
print("Greedy path :", path)
print("Actual cost :", cost)