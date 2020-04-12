from Ant import Ant
import operator
from matplotlib import pyplot as plt
class ACO:
    def __init__(self,params):
        self.A=params['alpha']
        self.B=params['beta']
        self.q0=params['q0']
        self.graph=params['graph']
        self.antsNr = params['antsNr']
        self.degrad=params['degrad']
        self.oneAntPheromone=params['phero']
        self.repo = params['repo']
        self.pheromone=[]
        self.population=[]
        self.best=None
        #self.initData()


    # def run(self):
    #
    #     i=0
    #     lines=[]
    #     while True:
    #         i+=1
    #         self.initData()
    #         for ant in self.population:
    #             for _ in range(len(self.graph)-1):
    #                 ant.goToNext()
    #         potentialBest=self.getBestAnt()
    #         if self.best==None or potentialBest.getTotalDist()<self.best.getTotalDist():
    #             self.best=potentialBest
    #
    #         self.updatePheromoneForTheBestAnt()
    #         outString="iter:" + str(i)+' cost: '+ str(self.best.getTotalDist())+' path: '+str(self.best.getPath())+' \n'
    #         print(outString)
    #         lines.append(outString)
    #         if len(lines)>1000:
    #             #salveaza ultimele 1000 de iteratii
    #             self.repo.writeDataToFile(lines)
    #             lines=[]

    def plot(points, path):
        x = []
        y = []
        for point in points:
            x.append(point.x)
            y.append(point.y)
        # noinspection PyUnusedLocal
        y = list(map(operator.sub, [max(y) for i in range(len(points))], y))

        for _ in range(0, len(path)):
            i = path[_ - 1]
            j = path[_]
            plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], color='r', length_includes_head=True)

        # noinspection PyTypeChecker
        plt.xlim(min(x), max(x) * 1.1)
        # noinspection PyTypeChecker
        plt.ylim(min(y), max(y) * 1.1)
        plt.show()


    def getPheromoneOnEdge(self,i,j):
        return self.pheromone[i][j]

    def initData(self):
        # feromonul initial pe toate rutele e 1
        self.pheromone=[[1 for _ in range(0,len(self.graph))] for _ in range(0,len(self.graph))]
        self.population=[Ant(self.graph,self,self.q0) for _ in range(0,self.antsNr)]


    def getBestAnt(self):
        return min(self.population,key=lambda x:x.getTotalDist())

    def updatePheromoneForTheBestAnt(self):
        bestAnt=self.best
        for i in range(0,len(self.graph)):
            for j in range(i+1, len(self.graph)):
                first=bestAnt.getPath()[i]
                second=bestAnt.getPath()[j]
                oldPhero=self.pheromone[first][second]
                self.pheromone[first][second]=self.pheromone[second][first]=(1-self.degrad)*oldPhero+self.degrad*(1/bestAnt.getTotalDist())

        first = bestAnt.getPath()[-1]
        second = bestAnt.getPath()[0]
        oldPhero = self.pheromone[first][second]
        self.pheromone[first][second] = self.pheromone[second][first] = (1 - self.degrad) * oldPhero + self.degrad * (1 / bestAnt.getTotalDist())





