# LAB 5: A* Search   (Lab 4 with three lines changed)
graph = {'S': [('A',2), ('B',1)],
         'A': [('G',10)],
         'B': [('G',4)],
         'G': []}
h = {'S': 4, 'A': 2, 'B': 3, 'G': 0}
# ---- check the heuristic never overestimates ----
true_cost = {'S': 5, 'A': 10, 'B': 4, 'G': 0}
for node in h:
    ok = "OK" if h[node] <= true_cost[node] else "VIOLATION"
    print(f"  h({node}) = {h[node]}   true = {true_cost[node]}   {ok}")
def astar(start, goal):
    queue = [(h[start], 0, [start])]      # (f, g, path)  <-- CHANGE 1
    while queue:
        queue.sort()                      # smallest f first
        f, g, path = queue.pop(0)         # <-- CHANGE 2
        node = path[-1]
        if node == goal:
            return path, g                # g IS the answer, already tracked
        for n, w in graph[node]:
            queue.append((g + w + h[n],   # new f      <-- CHANGE 3
                          g + w,          # new g
                          path + [n]))
path, cost = astar('S', 'G')
print("A* path :", path)
print("Cost    :", cost)