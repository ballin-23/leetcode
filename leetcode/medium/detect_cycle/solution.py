graph = [
    [],
    [0, 3],
    [0],
    [1, 2]
  ]

def find_cycle(graph, flag):
    for i in range(len(graph)):
        if len(graph[i]) > 0:
            something = dfs_helper(graph, [], i, [], flag)
            break
    print("FLAG: ", something)

# need to use stack for this so push to top and pop from top
def dfs_helper(graph, visited, node_index, path, flag):
    path.append(node_index)
    print("path: ",path)
    visited.append(node_index)
    nodes_to_explore = graph[node_index]
    print("nodes to explore: ",nodes_to_explore, " nodes that have been visited: ", visited)
    for node in nodes_to_explore:
        print(node)
        if node not in visited and not flag:
            return_value = dfs_helper(graph, visited, node, path, flag)
            if (return_value):
                return True
        else:
            print("node: ", node, "path: ", path)
            print(node in path)
            if node in path:
                flag = True
                print("flag is: ", flag)
                return True
    path.pop(len(path)-1)
    return False
    


find_cycle(graph, False)