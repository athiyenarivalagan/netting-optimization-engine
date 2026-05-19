def find_cycles(graph):
    """
    Detects cycles in a directed graph using DFS with recusive stack tracking.

    Args: 
        graph:
            Directed, weighted adjacency list.
    
    Returns:
        List of cycles.
    """
    cycles = []
    # DFS traversal state:
    # 0 = unvisited
    # 1 = visiting (when entering)
    # 2 = visited (on exit)
    state = {} 
    path = []

    def dfs(node): 
        # Back-edge detected -> extract cycle
        if state.get(node, 0) == 1:
            cycle_start = path.index(node)
            cycles.append(path[cycle_start: ])
            return

        # Skip processed nodes
        if state.get(node, 0) == 2: 
            return 
        
        state[node] = 1
        path.append(node) 
        
        for neighbour, _ in graph[node]:
            dfs(neighbour)
        
        path.pop()
        state[node] = 2

    for node in graph:
        if state.get(node, 0) == 0:
            dfs(node)
    
    return cycles