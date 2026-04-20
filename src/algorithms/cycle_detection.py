def find_cycles(graph):
    """
    • Detects cycles in a directed graph using DFS with recusive stack tracking.
    • A cycle is detected when a node is revisted while still in the current DFS
      path (recursion stack). 
    
    • Args: 
        graph (Dict[str, List[Tuple[str, int]]]): Adjacency list representation
        of a directed, weighted graph.
    • Returns:
        List[List[str]]: List of cycles, where each cycle is represented as a list 
        of nodes.
    """
    cycles = []
    state = {} # 0 = unvisited, 1 = visiting, 2 = visited
    path = []

    def dfs(node): 
        if state.get(node, 0) == 1:
            # Found a cycle -> extract from current path
            cycle_start = path.index(node)
            cycles.append(path[cycle_start: ])
            return

        if state.get(node, 0) == 2:
            return # already processed
        
        state[node] = 1
        path.append(node) 
        
        for neighbour, _ in graph[node]:
            dfs(neighbour)
        
        path.pop()
        state[node] = 2

    for node in graph: # A, B, C, D
        if state.get(node, 0) == 0:
            dfs(node)
    
    return cycles