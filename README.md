# Netting Optimization Engine

## Problem
In financial systems, entities often owe each other money through a network of payments. This creates redundant obligations that can be reduced through netting.

The goal is to minimize outstanding payments by cancelling flows within cycles.

## Approach

Payments are modelled as a weighted, directed graph:
- Nodes = entities
- Edges = payment obligations (payer → receiver)
- Weights = transaction amounts

The engine:
1. Builds the graph
2. Detects cycles using DFS
3. Nets flows by subtracting the smallest value in each cycle

## Example

```
Input:

A -> B (100)  
B -> C (100)  
C -> A (100)  
A -> D (50)  
D -> B (30)
```

Output:

- Gross: 380  
- Remaining: 80  
- Reduction: 300  
- Efficiency: 78.95%

## How to Run

```bash
python3 -m src.main
```

## Project Structure

```
src/
├── models/        # Payment model
├── graph/         # Graph construction
├── algorithms/    # Cycle detection + netting
├── engine/        # Implementation logic
└── experimental/  # Future work (SCC)
```

## Limitations

- DFS-based cycle detection may miss overlapping cycles
- Overlapping cycles are filtered (MVP simplification)
- Does not yet use strongly connected components (SCC)

## Future Work

- SCC-based netting (more optimal)
- Support multiple edges between entities
- Use Decimal for financial precision
- Scale to larger datasets
