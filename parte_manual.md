# Parte Manual — Eulerização do Grafo

## Entrada

```
6
11
2 4 33
3 5 12
3 4 5
4 5 1
2 3 20
1 4 10
1 3 50
0 2 20
0 1 10
4 0 12
5 2 22
```

---

# Passo 1 — Graus de Saída

* 0 → 2
* 1 → 2
* 2 → 2
* 3 → 2
* 4 → 2
* 5 → 1

---

# Passo 2 — Graus de Entrada

* 0 → 1
* 1 → 1
* 2 → 2
* 3 → 2
* 4 → 3
* 5 → 2

---

# Passo 3 — Δ(v) = saída − entrada

| Vértice | Saída | Entrada | Δ(v) |
| ------- | ----- | ------- | ---- |
| 0       | 2     | 1       | +1   |
| 1       | 2     | 1       | +1   |
| 2       | 2     | 2       | 0    |
| 3       | 2     | 2       | 0    |
| 4       | 2     | 3       | -1   |
| 5       | 1     | 2       | -1   |

---

# Passo 4 — Vértices Desbalanceados

Δ > 0 (precisam receber arestas):

* 0 (+1)
* 1 (+1)

Δ < 0 (precisam enviar arestas):

* 4 (-1)
* 5 (-1)

---

# Passo 5 — Caminhos mínimos entre desbalanceados

Possíveis caminhos:

4 → 0  (custo 12)

5 → 1
Menor caminho:
5 → 2 → 3 → 4 → 0 → 1
Custo = 22 + 20 + 5 + 12 + 10 = 69

---

# Passo 6 — Emparelhamento mínimo

Escolha:

* 4 → 0
* 5 → 1 (via caminho mínimo)

---

# Passo 7 — Arestas duplicadas

Adicionar:

```
4 0 12
5 2 22
2 3 20
3 4 5
4 0 12
0 1 10
```

---

# Passo 8 — Grafo Eulerizado

```
6
17
2 4 33
3 5 12
3 4 5
4 5 1
2 3 20
1 4 10
1 3 50
0 2 20
0 1 10
4 0 12
5 2 22
4 0 12
5 2 22
2 3 20
3 4 5
4 0 12
0 1 10
```

---

# Passo 9 — Verificação final

| Vértice | Saída | Entrada |
| ------- | ----- | ------- |
| 0       | 3     | 3       |
| 1       | 3     | 3       |
| 2       | 3     | 3       |
| 3       | 3     | 3       |
| 4       | 4     | 4       |
| 5       | 2     | 2       |

Todos os vértices estão balanceados.

Logo, o grafo é Euleriano.
