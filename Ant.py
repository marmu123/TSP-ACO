from random import randint,random,uniform
from MyGraph import Graph

class Ant:
    def __init__(self, distanceGraph:Graph, colony, q0):
        #colonia are:
        # - matricea feromonului depus de furnici
        # - metrica de distanta(inversul ei pentru a fi maxim)
        # - coef. alpha si beta(A,B)

        self.colony=colony
        self.path=[]
        self.visited=[]
        self.total=0
        self.q0=q0
        self.distanceGraph=distanceGraph

        #plasare furnica intr un oras aleator
        #se adauga nodul de start in vectorul de noduri vizitate
        start=randint(0, len(self.distanceGraph)-1)
        self.visited.append(start)
        self.path.append(start)

    def goToNext(self):
        q=random()
        nextNode=-1
        if q<self.q0:
            nextNode=self.calculateNextNode()
        else:
            nextNode=self.calculateProbab()
        self.path.append(nextNode)
        self.visited.append(nextNode)
        first = self.path[-2]
        second = self.path[-1]
        self.total+=self.distanceGraph.getMatrix()[first][second]
        oldPhero=self.colony.pheromone[first][second]

        #actualizare feromon dupa deplasarea cu o muchie
        self.colony.pheromone[first][second]=(1-self.colony.degrad)*oldPhero+self.colony.degrad*self.colony.oneAntPheromone

    def calculateNextNode(self):
        nextNode=-1
        maxi=-1
        last=self.path[-1]
        for i in range(0, len(self.distanceGraph)):
            if i not in self.visited:
                rez=(self.colony.getPheromoneOnEdge(last,i)**self.colony.A)*((1/self.distanceGraph.getMatrix()[last][i])**self.colony.B)
                if rez>maxi:
                    maxi=rez
                    nextNode=i
        return nextNode

    def calculateProbab(self):
        nextNode=-1
        maxi=-1
        summ=0
        last=self.path[-1]
        for i in range(0,len(self.distanceGraph)):
            if i not in self.visited:
                summ+=(self.colony.getPheromoneOnEdge(last,i)**self.colony.A)*((1/self.distanceGraph.getMatrix()[last][i])**self.colony.B)

        partialProbs=[0]
        nodes=[None]
        for i in range(0,len(self.distanceGraph)):
            if i not in self.visited:
                up=(self.colony.getPheromoneOnEdge(last,i)**self.colony.A)*((1/self.distanceGraph.getMatrix()[last][i])**self.colony.B)
                rez=up/summ
                nodes.append(i)
                partialProbs.append(partialProbs[-1]+rez)

        r=uniform(0,partialProbs[-1])
        index=0
        while index!=len(partialProbs) and r>partialProbs[index]:
            index+=1
        if index==len(partialProbs):
           index-=1
        return nodes[index]

    def getPath(self):
        return self.path

    def getTotalDist(self):
        return self.total+self.distanceGraph.getMatrix()[self.path[-1]][self.path[0]]

