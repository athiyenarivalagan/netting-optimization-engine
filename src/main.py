from tests.test_complex_graph import payments
# from tests.test_cycle_netting import payments
# from tests.test_acyclic_settlement import payments

from src.engine.cycle_netting_engine import CycleNettingEngine
from src.engine.settlement_engine import SettlementEngine
from src.engine.or_settlement_engine import SettlementOptimizationEngine


def compute_gross(payments):
    """Returns the total gross payment volume before netting"""
    return sum(p.amount for p in payments)


gross = compute_gross(payments)


# =========================================================
# Strategy 1: Cycle Netting
# =========================================================

cycle_engine = CycleNettingEngine(payments)

_, cycle_graph = cycle_engine.run()

cycle_remaining = sum(
    amount
    for edges in cycle_graph.values()
    for _, amount in edges
    if amount > 0
)

cycle_efficiency = (
    gross - cycle_remaining
) / gross


# =========================================================
# Strategy 2: Greedy Settlement Compression
# =========================================================

settlement_engine = SettlementEngine(payments)

greedy_settlements = settlement_engine.run()

greedy_flow = sum(
    amount
    for _, _, amount in greedy_settlements
)

greedy_efficiency = (
    gross - greedy_flow
) / gross


# =========================================================
# Strategy 3: OR-Tools Settlement Optimization
# =========================================================

optimization_engine = SettlementOptimizationEngine(payments)

or_settlements = optimization_engine.run()

or_flow = sum(
    amount
    for _, _, amount in or_settlements
)

or_efficiency = (
    gross - or_flow
) / gross


# =========================================================
# Results
# =========================================================

print("=== Strategy Comparison ===")

print(f"\nGross Exposure: {gross}")


print("\n1. Cycle Netting")
print(f"Remaining Exposure: {cycle_remaining}")
print(f"Efficiency: {cycle_efficiency:.2%}")


print("\n2. Greedy Settlement Compression")
print(f"Settlement Flow: {greedy_flow}")
print(f"Efficiency: {greedy_efficiency:.2%}")
print(f"Transactions: {len(greedy_settlements)}")


print("\n3. OR-Tools Settlement Optimization")
print(f"Settlement Flow: {or_flow}")
print(f"Efficiency: {or_efficiency:.2%}")
print(f"Transactions: {len(or_settlements)}")