from collections import defaultdict

def build_cyclic_subgraphs(graph, sccs):
    """
    Extract cyclic SCC subgraphs from the payment graph
    """
    scc_subgraphs = defaultdict(list)

    for scc in sccs:
        # Skip single-node SCCs without self-loop
        if len(scc) == 1:
            node = scc[0]
            has_self_loop = any( 
                neighbour == node 
                for neighbour, _ in graph[node]
            )
            if not has_self_loop:
                continue
        
        scc_set = set(scc)

        # 3. Build internal subgraph
        for node in scc_set:
            for neighbour, amount in graph[node]:
                if neighbour in scc_set:
                    scc_subgraphs[node].append(
                        (neighbour, amount)
                    )

    return scc_subgraphs