# Criado para o trabalho

from collections import defaultdict, deque

class DirectedEulerianCycle:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)
        self.in_degree = [0] * V
        self.out_degree = [0] * V

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.out_degree[u] += 1
        self.in_degree[v] += 1

    def has_eulerian_cycle(self):
        for v in range(self.V):
            if self.in_degree[v] != self.out_degree[v]:
                return False
        return True

    def find_cycle(self):
        if not self.has_eulerian_cycle():
            return None
        
        adj_iter = {v: deque(self.adj[v]) for v in range(self.V)}

        start = 0
        for v in range(self.V):
            if self.out_degree[v] > 0:
                start = v
                break

        stack = [start]
        cycle = []

        while stack:
            v = stack[-1]
            if adj_iter[v]:
                stack.append(adj_iter[v].popleft())
            else:
                cycle.append(stack.pop())

        if len(cycle) != sum(self.out_degree) + 1:
            return None

        return cycle[::-1]