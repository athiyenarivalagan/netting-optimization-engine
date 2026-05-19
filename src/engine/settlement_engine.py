from src.graph.builder import build_graph

from src.algorithms.kosaraju import kosaraju_scc
from src.algorithms.scc_filter import build_cyclic_subgraphs
from src.algorithms.balance import compute_balances
from src.algorithms.settlement import compress_settlements


class SettlementEngine:
    """
    Coordinate SCC-based settlement compression workflow.
    """
    def __init__(self, payments):
        self.payments = payments
        self.graph = build_graph(payments)

    # def __repr__(self):
    #     return f"Payments: {self.payments} Graph: {self.graph}"

    def run(self):
        # Identify strongly connected payment group 
        sccs = kosaraju_scc(self.graph)
        
        # Extract cyclic SCC subgraphs
        subgraphs = build_cyclic_subgraphs(
            self.graph,
            sccs
        )
        
        # Compute participant net balances
        balances = compute_balances(subgraphs)
        
        # Generate compressed settlement flow
        settlements = compress_settlements(balances)

        return settlements