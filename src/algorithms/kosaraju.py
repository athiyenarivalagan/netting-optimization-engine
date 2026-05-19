from collections import defaultdict

def build_transpose_graph(graph):
    """
    Reverse all graph edges for the second DFS pass.
    """
    transpose = defaultdict(list)

    for v in graph:
        for neighbour, amount in graph[v]:
            transpose[neighbour].append((v, amount))

    return transpose


def dfs_order(node, graph, visited, finish_order):
    """
    DFS traversal to compute node finishing order.
    """
    visited.add(node) 

    for neighbour, _ in graph[node]:
        if neighbour not in visited:
            dfs_order(
                neighbour, 
                graph, 
                visited, 
                finish_order
            )

    finish_order.append(node) 


def dfs_scc(node, transpose, visited, component):
    """
    DFS traversal on the transpose graph to extract SCCs.
    """
    visited.add(node)
    component.append(node)

    for neighbour, _ in transpose[node]:
        if neighbour not in visited:
            dfs_scc(
                neighbour, 
                transpose, 
                visited, 
                component
            )


def kosaraju_scc(graph):
    """
    Identify strongly connected components using Kosaraju's algorithm
    """
    visited = set()
    finish_order = []
    sccs = []
    
    # First DFS pass:
    # compute node finishing order
    for node in graph: 
        if node not in visited:
            dfs_order(
                node, 
                graph, 
                visited, 
                finish_order
            )

    # Reverse graph edges
    transpose = build_transpose_graph(graph)

    visited.clear()
    
    # Second DFS pass:
    # extract SCCs from transpose graph 
    for node in reversed(finish_order): 
        if node not in visited:
            component = []
            dfs_scc(
                node, 
                transpose, 
                visited, 
                component
            )
            sccs.append(component)

    return sccs