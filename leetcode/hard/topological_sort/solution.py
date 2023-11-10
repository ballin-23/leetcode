def topologicalSort(jobs, deps):
    # create dag
    graph = create_graph(jobs, deps)
    # dfs
    explored = []
    stack = []
    for job in jobs:
        dfs(job, graph, explored, stack)
    # return something
    stack.reverse()
    print(stack)

def create_graph(jobs, deps):
    graph = {}
    for job in jobs:
        arr = []
        for dep in deps:
            if dep[0] == job:
                arr.append(dep[1])
        graph[job] = arr
    print(graph)
    return graph

def dfs(start, graph, explored, stack):
    children = graph[start]
    print("children: ", children, " of: ", start, "--- explored: ", explored)
    for child in children:
        if child not in explored:
            explored.append(child)
            dfs(child, graph, explored, stack)
            print("back from dfs of this node: ", child, " this was the start: ", start)
    if start not in stack:
        stack.append(start)

def intersection(children, explored):
    for child in children:
        if child in explored:
            return True
    return False

jobs = [1, 2, 3, 4]
deps = [[1, 2],[1, 3],[3, 2],[4, 2],[4, 3]]

topologicalSort(jobs, deps)