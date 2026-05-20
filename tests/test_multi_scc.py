# tests/test_case_2

from src.models.payment import Payment

payments = [
    Payment("A", "B", "USD", 100),
    Payment("A", "D", "USD", 40),
    Payment("B", "C", "USD", 70),
    Payment("B", "E", "USD", 20),
    Payment("C", "A", "USD", 50),
    Payment("C", "D", "USD", 10), # SCC 1
    Payment("D", "E", "USD", 60),
    Payment("E", "F", "USD", 30),
    Payment("F", "D", "USD", 20),
    Payment("F", "G", "USD", 15), # SCC 2
    Payment("G", "H", "USD", 25), # Acyclic chain
    Payment("I", "I", "USD", 10), # Self-loop SCC
    Payment("J", "K", "USD", 50), # Disconnected acyclic component
]