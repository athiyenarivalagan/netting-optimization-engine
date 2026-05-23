from src.graph.builder import build_graph

from src.algorithms.kosaraju import kosaraju_scc
from src.algorithms.scc_filter import build_cyclic_subgraphs
from src.algorithms.balance import compute_balances
from src.algorithms.or_optimizer import optimize_settlements


class SettlementOptimizationEngine:
    """
    Global MIP-based settlement optimization using OR-Tools and SCIP.
    """

    def __init__(self, payments):
        self.payments = payments
        self.graph = build_graph(payments)

    def run(self):

        # SCC analysis (kept for diagnostics / graph analysis)
        sccs = kosaraju_scc(self.graph)
        # print("\nSCCs:", sccs)

        # Cyclic subgraphs (used only for analysis/debugging)
        subgraphs = build_cyclic_subgraphs(
            self.graph,
            sccs
        )

        # print("\nCyclic subgraphs:", subgraphs)

        # GLOBAL balances across full graph
        balances = compute_balances(self.graph)

        print("\nNet balances:", balances)

        # Global MIP settlement optimization
        settlements = optimize_settlements(balances)

        # print("\nOptimized settlements:", settlements)

        return settlements