"""
查找有向图中所有的强连通分量，使用一个stack和set集合实现，或者一个标志数组
strong_connected_components代表强连通分量

"""
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # 访问完一个结点的所有孩子结点，递归实现，一直遍历到底没有退路的为止
    def DFSUtil(self, u,  visited):
        visited[u] = True
        print(u)
        for i in self.graph[u]:
            if visited[i]  == False:
                self.DFSUtil(i, visited)



    # get the node into the stack, when one node all the
    # children are visited 核心代码快， 最后叠加去，最后一个元素加入stack
    def fillOrder(self,v, visited, stack):
        #marked the current node as visited
        visited[v] = True
        #recur for all the vertices adjacent
        #
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_strong_connected_components(self):
        stack = []
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        gr = self.getTranspose()
        # 第一次深度遍历，按照遍历结束时间放进stack
        visited = [False] * (self.V)
        while stack:
            i = stack.pop()
            #能一次遍历到底
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                print("")

if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    print(g.graph)
    print("following are strongly connected components in the given graph")
    g.print_strong_connected_components()
