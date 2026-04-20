def net_cycle(graph, cycle):
    # Net the cycle by subtracting the smallest edge amount
    # from every edge in the cycle.

    min_flow = float('inf')

    # Find the smallest edge amount in the cycle.
    for i in range(len(cycle)):
        u = cycle[i]
        v = cycle[(i + 1) % len(cycle)] # wrap last node back to first

        for _, (neighbour, amt) in enumerate(graph[u]):
            if neighbour == v:
                min_flow = min(min_flow, amt)

    # Subtract min_flow from each edge in the cycle
    for i in range(len(cycle)):
        u = cycle[i]
        v = cycle[(i + 1) % len(cycle)]

        for idx, (neighbour, amt) in enumerate(graph[u]):
            if neighbour == v:
                graph[u][idx] = (neighbour, amt - min_flow)
        
    return min_flow