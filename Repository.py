from MyGraph import Graph
from utils import euclidianDistance


class Repository:
    def __init__(self,filename,type):
        self.__graph=None
        self.__filename=filename
        if type=='matrix':
            self.__readGraphByMatrix()
        elif type=='coord':
            self.__readGraphByListOfCoord()
        else:
            pass

    def getGraph(self):
        return self.__graph

    def __readGraphByMatrix(self):
        f = open(self.__filename, "r")
        n = int(f.readline())
        matrix = []
        for i in range(0, n):
            str = f.readline()
            values = str.split(",")
            values = [float(x) for x in values]
            matrix.append(values)
        self.__graph=Graph(matrix)


    def __readGraphByListOfCoord(self):
        nodes = []
        f = open(self.__filename, "r")
        lines = f.readlines()
        for line in lines:
            args = line.split(" ")
            if len(args)!=3:
                continue
            try:
                args[1],args[2]=float(args[1]),float(args[2])
            except Exception:
                continue

            nodes.append([args[0], float(args[1]), float(args[2])])
        n = len(nodes)
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(euclidianDistance(nodes[i], nodes[j]))
            matrix.append(row)
        print(matrix)
        self.__graph=Graph(matrix)

    def writeDataToFile(self,lines):
        outFile=self.__filename.split(".")[0]+'_solution.'+self.__filename.split(".")[1]
        f=open(outFile,'w')
        for line in lines:
            f.write(line+'\n')

