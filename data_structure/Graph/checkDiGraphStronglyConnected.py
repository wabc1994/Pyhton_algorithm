from collections import defaultdict

"""
visited = [] 标注每个顶点是否使用过，有向图，判断强连通图采用深度优先搜索便遍历，
正反均能遍历成功的则是强连通图,一个图是强连通图图，则深度优先树是一个颗树，可以遍历所有的节点
Given a directed graph, find out whether the graph is strongly connected or not. 
A directed graph is strongly connected if there is a path between any two pair of vertices. 
For example, following is a strongly connected graph.
https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/
"""


class Graph:
    def __init__(self, vertices_number):
        """
        graph is a dictionary whose value is list, key is 顶点，value 是 连接的顶点集合
        :param vertices_number: 定点集合
        """
        self.v = vertices_number
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self):
        """
        start the number first node
        :return: if all nodes are visited ,return True
        """
        visited = [False] * self.v
        self.dfs_util(0, visited)
        # whether we can  dfs all the node
        if visited == [True] * self.v:
            return True
        return False

    def dfs_util(self, i, visited):
        """

        :param i: the number i represent the node
        :param visited: the 标注数组
        :return:
        """
        visited[i] = True
        for j in self.graph[i]:
            if not (visited[j]):
                self.dfs_util(j, visited)

    def reverse_graph(self):
        """
        transfer v point to u, into u point to v,
        :return:
        """
        g = Graph(self.v)
        for i in range(len(self.graph)):
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def is_sc(self):
        if self.dfs():
            gr = self.reverse_graph()
            if gr.dfs():
                return True
        return False


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(2, 4)
    g.add_edge(4, 2)
    if g.is_sc():
        print("yes")
    else:
        print("no")
