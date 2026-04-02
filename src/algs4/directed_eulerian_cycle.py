from algs4.stack import Stack

class DirectedEulerianCycle:
    def __init__(self, G):
        self._path = None      
        self._is_balanced = True
        self._total_weight = 0.0
        if G.E == 0:
            return
        
        for v in range(G.V):
            if G.out_degree(v) != G.in_degree(v):
                self.balance = False
                return

        adj = [iter(G.adj[v]) for v in range(G.V)]      

        s = self._non_isolated_vertex(G)
        
        if s == -1: 
            return
             
        aux_stack = Stack()
        aux_stack.push(s)

        self._path = Stack()
        while not aux_stack.is_empty():
            v = aux_stack.pop()
            
            while True:
                try:
                    edge = next(adj[v])
                    aux_stack.push(v)
                    self._total_weight += edge.weight
                    v = edge.To() 
                except StopIteration:
                    break
            
            self._path.push(v)

        if self._path.size() != G.E + 1:
            self._path = None
            self._total_weight = 0.0

    def cycle(self):
        return self._path
    
    def balance(self):
        return self._is_balanced

    def has_eulerian_cycle(self) -> bool:
        return self._path is not None

    def _non_isolated_vertex(self, G):
        for v in range(G.V):
            if G.out_degree(v) > 0:
                return v
        return -1
    
    def total_weight(self) -> float:
        return self._total_weight