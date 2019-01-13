import heapq
import sys
import queue

num_str = sys.stdin.readline().split()
n = int(num_str[0])
m = int(num_str[1])

incoming_edges = [0] * n
nodes = []
for i in range(m):
    compared_str = sys.stdin.readline().split()
    # a -> b
    a = int(compared_str[0])
    b = int(compared_str[1])
    incoming_edges[b - 1] += 1
    nodes.append((a, b))

l = []
s = queue.Queue()
for i in range(len(incoming_edges)):
    if incoming_edges[i] == 0:
        s.put(i + 1)

while(not s.empty()):
    u = s.get()
    l.append(str(u))
    graph = [(a, b) for a, b in nodes if a == u]
    for a, b in graph:
        incoming_edges[b - 1] -= 1
        if incoming_edges[b - 1] == 0:
            s.put(b)

results = ' '.join(l)
print(results)