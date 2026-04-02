import os
from algs4.edge_weighted_digraph import EdgeWeightedDigraph
from algs4.directed_eulerian_cycle import DirectedEulerianCycle

caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    "..",
    "data",
    "entrada_original.txt"
)

caminho_arquivo_eurelizado = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    "..",
    "data",
    "entrada_eulerizada.txt"
)

with open(caminho_arquivo_eurelizado, 'r') as f:
    graph = EdgeWeightedDigraph(file=f)
    
is_balanced = True
print("Dígrafo Eurelizado")
print(graph)
print("-" * 30)
print(f"{'Vértice':<8} | {'Entrada':<8} | {'Saída':<8}")
print("-" * 30)
    
for v in range(graph.V):
    in_g = graph.in_degree(v)
    out_g = graph.out_degree(v)
    
    if(in_g != out_g): 
        is_balanced = False
        
    print(f"{v:<8} | {in_g:<8} | {out_g:<8}")

resultado_final = "Sim" if is_balanced else "Não"

print("-" * 30)
print(f"Grafo balanceado: {resultado_final}")

euler = DirectedEulerianCycle(graph)
    
print("\n--- Resultado do Algoritmo de Hierholzer ---")
if euler.has_eulerian_cycle():
    print("Ciclo Euleriano encontrado:")
    
    caminho = [str(v) for v in euler.cycle()]
    print(" -> ".join(caminho))
    print(euler.total_weight())
else:
    print("O grafo não possui um Ciclo Euleriano.")
    print("Certifique-se de que o grafo é conexo e balanceado.")