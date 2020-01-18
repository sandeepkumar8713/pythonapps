# https://leetcode.com/problems/evaluate-division/
# https://leetcode.com/problems/evaluate-division/discuss/412161/Python-Solution-Beats-98
# Question : Equations are given in the format A / B = k, where A and B are variables represented as
# strings, and k is a real number (floating point number). Given some queries, return the answers. If
# the answer does not exist, return -1.0.
#
# Example: Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# According to the example above:
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
#
#
# Used : For given equations, make a weighted directed graph. Here operands will be vertices. The weight from a->b
#        will be value and from b->a will be 1/value. Now for the given query, do bfs where a is start and b is end.
#        While traversing the graph, keep multiplying its weight and saving it back in queue. When end is found,
#        return the corresponding product.
#        Logic : def BFS(graph, numerator, denominator):
#        queue = [], visited = set()
#        queue.append([numerator, 1])
#        result = None
#        while len(queue) > 0:
#           var = queue.pop(0)
#           if var[0] == denominator:
#               result = var[1]
#                break
#           for adj in graph[var[0]]:
#               if adj not in visited:
#                   visited.add(adj)
#                   res = var[1] * graph[var[0]][adj]
#                   queue.append([adj, res])
#           if result == None: return -1.0
#        return result
# Complexity : O(V + E)


def calcEquation(equations, values, queries):
    def createGraph(eqns, vals):
        graph = {}
        for i in range(len(eqns)):
            if eqns[i][0] not in graph:
                graph[eqns[i][0]] = {eqns[i][1]: vals[i]}
            else:
                graph[eqns[i][0]][eqns[i][1]] = vals[i]
            if eqns[i][1] not in graph:
                graph[eqns[i][1]] = {eqns[i][0]: (1.0 / vals[i])}
            else:
                graph[eqns[i][1]][eqns[i][0]] = 1.0 / vals[i]
        return graph

    def BFS(graph, numerator, denominator):
        queue = []
        visited = set()
        queue.append([numerator, 1])
        result = None
        while len(queue) > 0:
            var = queue.pop(0)
            if var[0] == denominator:
                result = var[1]
                break
            for adj in graph[var[0]]:
                if adj not in visited:
                    visited.add(adj)
                    res = var[1] * graph[var[0]][adj]
                    queue.append([adj, res])

        if result is None:
            return -1.0

        return result

    graph = createGraph(equations, values)
    results = []
    for query in queries:
        if query[0] not in graph or query[1] not in graph:
            results.append(-1.0)
            continue
        elif query[0] == query[1]:
            results.append(1.0)
            continue
        results.append(BFS(graph, query[0], query[1]))
    return results


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calcEquation(equations, values, queries))
