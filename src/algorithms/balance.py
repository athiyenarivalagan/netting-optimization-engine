def compute_balances(scc_subgraphs):
    """
    Compute net participant balances within cyclic SCC subgraphs
    """
    balance_map = {}

    for node in scc_subgraphs:
        for neighbour, amount in scc_subgraphs[node]:
            # Outgoing obligation
            balance_map[node] = (
                balance_map.get(node, 0) - amount
            )  
            # Incoming obligation
            balance_map[neighbour] = (
                balance_map.get(neighbour, 0) + amount
            ) 

    return balance_map 