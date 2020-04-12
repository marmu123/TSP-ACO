class Graph:
    def __init__(self, matrix):
        self.matrix=matrix

    def getNumberOfNodes(self):
        return len(self.matrix)

    def getMatrix(self):
        return self.matrix

    def getEdge(self,i,j):
        return self.matrix[i][j]

    def setEdge(self,i,j,val):
        self.matrix[i][j]=val

    def __len__(self):
        return self.getNumberOfNodes()