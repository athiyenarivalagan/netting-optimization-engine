def net_cycle(graph, cycle):
    """
    Reduce flow across a cycle by subtracting the minimum edge weight
    from every edge in the cycle.
    """
    min_flow = float('inf')

    # Identify bottleneck flow within the cycle
    n = len(cycle)
    for i in range(n):
        u = cycle[i]
        # Find the next node in the cycle
        v = cycle[(i + 1) % n]  

        for neighbour, amt in graph[u]:
            if neighbour == v:
                min_flow = min(min_flow, amt)

    # Apply flow reduction across the cycle
    for i in range(n):
        u = cycle[i]
        v = cycle[(i + 1) % n]

        for idx, (neighbour, amt) in enumerate(graph[u]):
            if neighbour == v:
                graph[u][idx] = (neighbour, amt - min_flow)
        
    return min_flow