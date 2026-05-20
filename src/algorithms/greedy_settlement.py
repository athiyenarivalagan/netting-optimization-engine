def compress_settlements(balance_map):
    """
    Compress net balances into minimal settlement flows.
    """
    debtors = []
    creditors = []

    for node, balance in balance_map.items():
        if balance < 0:
            debtors.append((node, (-balance)))
        elif balance > 0:
            creditors.append((node, balance))

    # print(f"Debtors = {debtors}", f"Creditors = {creditors}")

    d = 0 
    c = 0
    settlements = []

    # Greedily match debtors to creditors
    while d < len(debtors) and c < len(creditors): 
        debtor_node, debtor_amount = debtors[d]
        creditor_node, creditor_amount = creditors[c]  

        settlement_amount = min(
            debtor_amount, 
            creditor_amount
        )

        settlements.append(
            (
                debtor_node, 
                creditor_node, 
                settlement_amount
            )
        )

        debtor_amount -= settlement_amount
        creditor_amount -= settlement_amount
        
        debtors[d] = (
            debtor_node, 
            debtor_amount
        )
        creditors[c] = (
            creditor_node, 
            creditor_amount
        )
        
        if debtor_amount == 0:
            d += 1
        if creditor_amount == 0:
            c += 1 

    return settlements