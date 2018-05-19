from collections import defaultdict


# this class represents a directed graph
# using adjacency list representation
class Graph:
    # Constructor 采用字典来存储图
    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        """

        :param u: the node one
        :param v: the node two
        :return: return nothing
        """
        self.graph[u].append(v)

    def BFS(self, s):
        """

        :param s: the source node
        :return:
        """
        visited = [False] * len(self.graph)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop()
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# 广度优先搜素遍历，非递方法使用队列，从一个结点开始，先加入队列，然后出队列，加入
# 儿子结点，诸然后判断
def dfs_traverse_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
        visited.add(start)
        for next_node in graph[start]:
            if visited[next_node] == False:
                dfs_traverse_recursive(next_node, visited)
        return visited


def dfs_traverse(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()


def bfs_traverse(graph, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for next_node in graph[node]:
                queue.append(next_node)
    return visited


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("following is breath first traversal starting from vertex 2")
    print(dfs_traverse_recursive(g, 0))
