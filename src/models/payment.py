class Payment:
    def __init__(self, payer, receiver, currency, amount):
        """
        • Represents a directed financial obligation between two parties.
        • Each payment is modelled as an edge in a weighted, directed graph:
            payer -> receiver, where the edge weight is the amount.
        
        • Attributes:
            payer (str): Entity initiating the payment (source node)
            receiver (str): Entity receiving the payment (destination node)
            currency (str): Currency of the transaction
            amount (int): Amount transferred (edge weight)
        
        • NB:
            In actual systems, Decimal should be used instead of int for
            the amount to avoid precision errors.
        """
        self.payer = payer
        self.receiver = receiver
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        # Human readable representation for debugging and logging
        return f"{self.payer} -> {self.receiver}: {self.amount}"