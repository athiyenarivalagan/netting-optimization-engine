from src.graph.builder import build_graph
from src.algorithms.cycle_detection import find_cycles
from src.algorithms.netting import net_cycle

class NettingEngine:
    """
    Coordinates the end-to end payment netting workflow:
        1. Build the payment graph
        2. Detect cycles
        3. Net reducible flows
    """
    def __init__(self, payments):
        self.payments = payments
        self.graph = build_graph(payments)

    def run(self):
        cycles = find_cycles(self.graph)

        # Prefer shorter cycles first before resolving overlaps
        cycles = sorted(cycles, key=len)

        filtered_cycles = []
        used_nodes = set()

        # Keep only non-overlapping cycles to avoid double-netting the same nodes 
        for cycle in cycles:
            overlap = False
            for node in cycle:
                if node in used_nodes:
                    overlap = True
                    break
            
            if not overlap:
                filtered_cycles.append(cycle)
                used_nodes.update(cycle)

        total_netted = 0

        for cycle in filtered_cycles:
            netted = net_cycle(self.graph, cycle)
            total_netted += netted

        # print("Cycles found:", cycles)
        # print("Filtered cycles:", filtered_cycles)
        return total_netted, self.graph