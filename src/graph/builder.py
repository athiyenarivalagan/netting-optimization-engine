from collections import defaultdict

def build_graph(payments):
    """
    • Constructs a directed, weighted adjacency list from a list of Payment objects.
    • The resulting graph is represented as:
        Dict[str, List[Tuple[str, int]]]
        
    • Example:
        A -> [(B, 100), (D, 50)]
        B -> [(C, 100)]

    • Args:
        payments (List[Payment]): List of payment transactions
    • Returns:
        defaultdict(list): Adjacency list representation of the graph
    """

    graph = defaultdict(list)

    for p in payments:
        graph[p.sender].append((p.receiver, p.amount))
        
        # Ensure receiver exists as a node
        graph[p.receiver] 

    return graph