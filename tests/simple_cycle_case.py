# tests/test_case_1

from src.models.payment import Payment

payments = [
    Payment("A", "B", "USD", 100),
    Payment("B", "C", "USD", 100),
    Payment("C", "A", "USD", 100), # cycle
    Payment("A", "D", "USD", 50),
    Payment("D", "B", "USD", 30),
]