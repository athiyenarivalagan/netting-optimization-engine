# Cross Border Netting & Settlement Optimization Engine


## Problem Statement

Financial institutions and payment networks often process obligations independently, leading to redundant settlement flows, increased liquidity requirements, and unnecessary external transfers.

For example:

- Company A owes Company B $100
- Company B owes Company C $100
- Company C owes Company A $100

Naively, $300 of settlement flow is processed externally even though the net economic obligation is zero.

This project explores graph-based and optimization-driven approaches for compressing settlement obligations through:
- Cycle netting
- Global balance compression
- Mixed Integer Programming (MIP) optimization


## Design Evolution

My initial approach focused on cycle netting using Depth-First Search (DFS) to detect reducible payment cycles in the settlement graph.

During implementation, I realized that DFS-based cycle detection primarily identifies individual cyclic structures and does not naturally scale towards globally optimal settlement compression. Enumerating all possible cycles also introduces significant scalability challenges for larger payment networks.

To improve the graph analysis layer, I implemented Strongly Connected Component (SCC) decomposition using Kosaraju’s algorithm. SCCs group mutually reachable nodes within the directed payment graph, enabling more structured identification of cyclic payment regions and multilateral netting opportunities.

Initially, greedy settlement compression and OR-Tools optimization were applied only within SCC-scoped cyclic subgraphs. While this improved local settlement efficiency, it did not guarantee globally optimal settlement structures because acyclic debtor-creditor relationships outside SCCs were excluded from optimization.

The architecture was later extended towards global balance optimization by computing net balances across the full payment graph before applying:

- Greedy settlement compression
- Mixed Integer Programming (MIP) optimization using OR-Tools + SCIP

This transition evolved the project from local graph-based netting towards global settlement optimization.


## Key Technical Insight

Local cycle-based reductions improve settlement efficiency but do not guarantee globally optimal settlement structures.

Early SCC-scoped optimization experiments improved local settlement efficiency but excluded acyclic debtor-creditor relationships from optimization.

The project therefore evolved from SCC-local optimization towards global balance optimization using Mixed Integer Programming (MIP).


## Features

- DFS-based cycle detection
- Kosaraju SCC decomposition
- Graph-based settlement modelling
- Greedy global settlement compression
- MIP optimization using OR-Tools + SCIP
- Settlement flow and efficiency analysis
- Comparative optimization strategies
 

## System Architecture

```
Raw Payment Graph
│
├── Cycle Netting Engine
│     └── Local cycle reduction
│
├── Greedy Settlement Engine
│     └── Global balance compression
│
└── OR-Tools Optimization Engine
      └── MIP transaction minimization
```


### Decision Variables
- `x_ij` = settlement flow from debtor `i` to creditor `j`
- `y_ij ∈ {0, 1}` = whether settlement edge `(i, j)` is active

### Objective
Minimize the number of active settlement transactions:

$$
\min \sum_{i,j} y_{ij}
$$

### Constraints

Debtor balance constraint:

$$
\sum_j x_{ij} = d_i
$$

Creditor balance constraint:

$$
\sum_i x_{ij} = c_j
$$

Big-M activation constraint:

$$
x_{ij} \leq M y_{ij}
$$


## Example Results

### Test Case 1 — Complex Multi-SCC Settlement Graph

| Strategy | Settlement Flow | Transactions | Efficiency |
|---|---:|---:|---:|
| Cycle Netting | 280 | - | 44.00% |
| Greedy Compression | 155 | 8 | 69.00% |
| MIP Optimization (OR-Tools + SCIP) | 155 | 7 | 69.00% |

Key Insight:
- Local cycle reductions significantly reduce redundant payment flows.
- Global balance compression further reduces settlement requirements.
- MIP optimization achieves a lower transaction count than the greedy strategy while preserving the same settlement flow efficiency.

---

### Test Case 2 — Pure Cycle Netting Scenario

| Strategy | Settlement Flow | Transactions | Efficiency |
|---|---:|---:|---:|
| Cycle Netting | 80 | - | 78.95% |
| Greedy Compression | 50 | 2 | 86.84% |
| MIP Optimization (OR-Tools + SCIP) | 50 | 2 | 86.84% |

Key Insight:
- Cyclic obligations can be heavily compressed through multilateral netting.
- Remaining obligations are globally settled through balance compression.

---

### Test Case 3 — Acyclic Global Settlement

| Strategy | Settlement Flow | Transactions | Efficiency |
|---|---:|---:|---:|
| Cycle Netting | 300 | - | 0.00% |
| Greedy Compression | 300 | 3 | 0.00% |
| MIP Optimization (OR-Tools + SCIP) | 300 | 3 | 0.00% |

Key Insight:
- No cyclic redundancies existed in the payment graph.
- Settlement optimization therefore focused purely on minimizing transaction structure across global net balances.


## Repo Structure

```
src/
├── algorithms/    # Graph algorithms, settlement compression, optimization logic
├── engine/        # Workflow orchestration engines
├── graph/         # Graph construction utilities
├── models/        # Payment data models
└── tests/         # Scenario and integration test cases
```

## Technologies Used

- Python
- OR-Tools
- SCIP
- Graph Algorithms
- DFS
- Kosaraju SCC
- Mixed Integer Programming (MIP)

## Future Work

- multi-currency optimization
- FX batching constraints
- settlement deadline
- liquidity constraints
- scenario simulation
- AI-assisted optimization workflows

## How to Run

```
pip install -r requirements.txt
python -m src.main
```
