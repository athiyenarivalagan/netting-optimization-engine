from src.graph.builder import build_graph

from src.algorithms.kosaraju import kosaraju_scc
from src.algorithms.scc_filter import build_cyclic_subgraphs
from src.algorithms.balance import compute_balances
from src.algorithms.greedy_settlement import compress_settlements


class SettlementEngine:
    """
    Global greedy settlement compression using net balances.
    """
    def __init__(self, payments):
        self.payments = payments
        self.graph = build_graph(payments)

    def run(self):
        # SCC analysis (kept for diagnostics / graph analysis)
        sccs = kosaraju_scc(self.graph)

        # Cyclic subgraphs (used only for analysis/debugging)
        subgraphs = build_cyclic_subgraphs(
            self.graph,
            sccs
        )

        # GLOBAL balances across full graph
        balances = compute_balances(self.graph)
        
        # Generate compressed settlement flow
        settlements = compress_settlements(balances)

        return settlements