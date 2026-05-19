# from tests.simple_cycle_case import payments
from tests.multi_scc_case import payments
from src.engine.cycle_netting_engine import CycleNettingEngine
from src.engine.settlement_engine import SettlementEngine


def compute_gross(payments):
    """Returns the total gross payment volume before netting"""
    return sum(p.amount for p in payments)

gross = compute_gross(payments)

# Strategy 1
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


# Strategy 2
settlement_engine = SettlementEngine(payments)

settlements = settlement_engine.run()

settlement_remaining = sum(
    amount
    for _, _, amount in settlements
)

settlement_efficiency = (
    gross - settlement_remaining
) / gross


print("=== Strategy Comparison ===")

print(f"Gross Exposure: {gross}")

print("\nCycle Netting:")
print(f"Remaining: {cycle_remaining}")
print(f"Efficiency: {cycle_efficiency:.2%}")

print("\nSettlement Compression:")
print(f"Remaining: {settlement_remaining}")
print(f"Efficiency: {settlement_efficiency:.2%}")