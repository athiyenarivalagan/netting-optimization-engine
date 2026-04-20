from src.models.payment import Payment
from src.engine.netting_engine import NettingEngine

# Simple payment dataset for the MVP demo.
payments = [
    Payment("A", "B", "USD", 100),
    Payment("B", "C", "USD", 100),
    Payment("C", "A", "USD", 100), # cycle
    Payment("A", "D", "USD", 50),
    Payment("D", "B", "USD", 30),
]

def compute_gross(payments):
    """Returns the total gross payment volume before netting"""
    return sum(p.amount for p in payments)

engine = NettingEngine(payments)

gross = compute_gross(payments)
netted, graph = engine.run()

# Sum the remaining amount after cycle netting
remaining = sum(amt for edges in graph.values() for (_, amt) in edges if amt > 0)

efficiency = (gross - remaining) / gross

print(f"Gross: {gross}")
print(f"Remaining: {remaining}")
print(f"Efficiency: {efficiency:.2%}")