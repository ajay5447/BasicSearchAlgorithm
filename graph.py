'''
author: Ajay Tulsyan
email: atulsyan@wpi.edu
last update: 03/07/2020

Intro: This is code contains three basic search algorithms such as Breadth First Search,
Depth First Search, and Dijkstra, all the three algorithms are written as methods of a
class Graph. The alogorithms are built using adjecency matrix.

Note: """ PLEASE UPDATE THE PATH FOR IMAGES BEFORE RUNNING THIS CODE. 
            THE LINES ON WHICH UPDATE IS NEEDFUL IS 19, 124, and 129. """

'''
from collections import deque
from PIL import Image

class Graph:
    def __init__(self, numberOfVertex):
        im = Image.open("Graph_Without_Weights.png")
        im.show()
        self.vertex = []
        self.Queue = {}
        self.dict = {}
        self.path = []
        self.currentSize = 0
        self.capacity = numberOfVertex
        self._adjMatrix = []
        self._adjMatrix = [
            [0 for j in range(numberOfVertex)] for i in range(numberOfVertex)]
        self._adjMatrixWithWeight = []
        self._adjMatrixWithWeight = [
            [0 for j in range(numberOfVertex)] for i in range(numberOfVertex)]
        self._capacity = numberOfVertex

    def addVertex(self, data):
        self.vertex.append(data) if self.currentSize < self.capacity else print(
            'Capacity full')
        self.currentSize += 1

    def addEdge(self, source, target):
        s = self.vertex.index(
            source) if source in self.vertex else 'invalid source...does not exist in graph'
        t = self.vertex.index(
            target) if target in self.vertex else 'invalid target...does not exist in graph'
        if type(s) == int and type(t) == int:
            self._adjMatrix[s][t] = 1
            self._adjMatrix[t][s] = 1
        elif type(s) != int:
            print(source, '--', s)
        else:
            print(target, '--', t)

    def addEdgeWithWeight(self, source, target, weight):
        s = self.vertex.index(
            source) if source in self.vertex else 'invalid source...does not exist in graph'
        t = self.vertex.index(
            target) if target in self.vertex else 'invalid target...does not exist in graph'
        if type(s) == int and type(t) == int:
            self._adjMatrixWithWeight[s][t] = weight
            self._adjMatrixWithWeight[t][s] = weight
        elif type(s) != int:
            print(source, '--', s)
        else:
            print(target, '--', t)

    def findNeighbour(self, vertex):
        a = self.vertex.index(vertex)
        x = [self.vertex[i]
             for i in range(self.currentSize) if self._adjMatrix[a][i] == 1]
        print(x)

    def breadthFirstSearch(self, startVertex, endVertex=None):
        q = deque()
        result = []
        temp = []
        if startVertex in self.vertex:
            q.append(startVertex)
            temp.append(startVertex)
            while startVertex != endVertex:
                a = self.vertex.index(startVertex)
                for i in range(self.currentSize):
                    if self._adjMatrix[a][i] == 1 and self.vertex[i] not in temp:
                        q.append(self.vertex[i])
                        temp.append(self.vertex[i])
                result.append(q.popleft())
                startVertex = q[0] if len(result) != len(
                    self.vertex) else endVertex
            if startVertex == endVertex:
                if endVertex in self.vertex:
                    result.append(endVertex)
                print('***************************************************************')
                print('The result of BFS--', result)
                print('***************************************************************')
        else:
            print('Invalid start point')

    def depthFirstSearch(self, startVertex, endVertex=None):
        q = deque()
        result = []
        if startVertex in self.vertex:
            q.append(startVertex)
            result.append(startVertex)
            while startVertex != endVertex:
                flag = 0
                a = self.vertex.index(startVertex)
                for i in range(self.currentSize):
                    if self._adjMatrix[a][i] == 1 and self.vertex[i] not in result:
                        q.append(self.vertex[i])
                        result.append(self.vertex[i])
                        startVertex = self.vertex[i]
                        flag += 1
                        break
                if flag == 0:
                    q.pop()
                    startVertex = q[len(
                        q) - 1] if len(result) != len(self.vertex) else endVertex
            print('***************************************************************')
            print('The result of DFS--', result)
            print('***************************************************************')
        else:
            print('Invalid start point')

    def dijkstra(self, startVertex, endVertex=None):
        im = Image.open("GraphWithWeights.png")
        im.show()
        if startVertex == 'Ajay' and endVertex == 'Iowa':
            # This image is only a representation...
            # of cost and path for this specific start and goal
            im = Image.open("Graph_Ajay_Iowa.png")
            im.show()
        start_dump = startVertex
        value = ""
        vertexCost = {self.vertex[i]: 500000 for i in range(len(self.vertex))}
        if startVertex in self.vertex:
            vertexCost[startVertex] = 0
            visited = set()
            while startVertex != None:
                visited.add(startVertex)
                a = self.vertex.index(startVertex)
                for i in range(self.currentSize):
                    if self._adjMatrixWithWeight[a][i] != 0 and self.vertex[i] != visited:
                        cost = self._adjMatrixWithWeight[a][i] + \
                            vertexCost.get(startVertex)
                        if cost < vertexCost.get(self.vertex[i]):
                            vertexCost[self.vertex[i]] = cost
                            self.Queue[self.vertex[i]] = cost
                            self.dict[self.vertex[i]] = startVertex
                if self.Queue != {}:
                    startVertex = min(self.Queue.keys(),
                                      key=(lambda k: self.Queue[k]))
                    self.Queue.pop(startVertex)
                else:
                    startVertex = None
            print('***************************************************************')
            print('Cost for all the vertex in the graph starting from',
                  start_dump, 'is--', vertexCost)
            print('***************************************************************')
            if endVertex in self.dict:
                self.path.append(endVertex)
                value = self.dict[endVertex]
                while vertexCost[value] != 0:
                    self.path.append(value)
                    value = self.dict[value]
            self.path.append(start_dump)
            self.path.reverse()
            print('***************************************************************')
            print('The Shortest path from vertex', start_dump, 'to end vertex',
                  endVertex, 'is ---', self.path, 'with cost', vertexCost[endVertex])
            print('***************************************************************')
        else:
            print('Invalid start point')


if __name__ == "__main__":

    # Here you can the number of vertex in the graph, for the explanation sake
    # I have taken a graph with  11 vertices.
    g = Graph(11)
    g.addVertex('Ajay')
    g.addVertex('Beckham')
    g.addVertex('Carlo')
    g.addVertex('Denim')
    g.addVertex('Eagle')
    g.addVertex('Fradel')
    g.addVertex('Gorden')
    g.addVertex('Hooker')
    g.addVertex('Iowa')
    g.addVertex('Joe')
    g.addVertex('Kevin')


    g.addEdge('Ajay', 'Beckham')
    g.addEdge('Ajay', 'Eagle')
    g.addEdge('Ajay', 'Fradel')
    g.addEdge('Fradel', 'Beckham')
    g.addEdge('Hooker', 'Beckham')
    g.addEdge('Carlo', 'Fradel')
    g.addEdge('Carlo', 'Gorden')
    g.addEdge('Carlo', 'Denim')
    g.addEdge('Denim', 'Eagle')
    g.addEdge('Denim', 'Gorden')
    g.addEdge('Fradel', 'Joe')
    g.addEdge('Hooker', 'Iowa')
    g.addEdge('Iowa', 'Joe')
    g.addEdge('Iowa', 'Kevin')

    # Here you can customize your graphs edges and its weights
    g.addEdgeWithWeight('Ajay', 'Beckham', 10)
    g.addEdgeWithWeight('Ajay', 'Eagle', 15)
    g.addEdgeWithWeight('Ajay', 'Fradel', 5)
    g.addEdgeWithWeight('Fradel', 'Beckham', 8)
    g.addEdgeWithWeight('Hooker', 'Beckham', 12)
    g.addEdgeWithWeight('Carlo', 'Fradel', 18)
    g.addEdgeWithWeight('Carlo', 'Gorden', 3)
    g.addEdgeWithWeight('Carlo', 'Denim', 9)
    g.addEdgeWithWeight('Denim', 'Eagle', 7)
    g.addEdgeWithWeight('Denim', 'Gorden', 6)
    g.addEdgeWithWeight('Fradel', 'Joe', 14)
    g.addEdgeWithWeight('Hooker', 'Iowa', 5)
    g.addEdgeWithWeight('Iowa', 'Joe', 11)
    g.addEdgeWithWeight('Iowa', 'Kevin', 2)

    print(g._adjMatrix)
    print('*************************************************************')
    # Here you can choose to provide end vertex or not, Like in the examples...
    # below, end vertex is provied, but you even skip to choose end vertex.
    g.breadthFirstSearch('Ajay', 'Gorden')
    g.depthFirstSearch('Carlo', 'Ajay')
    
    g.dijkstra('Ajay', 'Iowa')
    
      
