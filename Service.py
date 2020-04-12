from ACO import ACO
from random import randint
class Service:
    def __init__(self,aco:ACO):
        self.aco=aco
    def run(self,dynamic=False):
        i=0
        lines=[]
        while True:
            i+=1
            self.aco.initData()
            if dynamic==True and i%100==0:
                outs=self.changeCostOfAnEdge()
                lines.append(outs)
            for ant in self.aco.population:
                for _ in range(len(self.aco.graph)-1):
                    ant.goToNext()
            potentialBest=self.aco.getBestAnt()
            if self.aco.best==None or potentialBest.getTotalDist()<self.aco.best.getTotalDist():
                self.aco.best=potentialBest

            self.aco.updatePheromoneForTheBestAnt()
            outString="iter:" + str(i)+' cost: '+ str(self.aco.best.getTotalDist())+' path: '+str(self.aco.best.getPath())+' \n'
            print(outString)
            lines.append(outString)
            if len(lines)>1000:
                #salveaza ultimele 1000 de iteratii
                self.aco.repo.writeDataToFile(lines)
                lines=[]

    def changeCostOfAnEdge(self):
        # ind1 = randint(0, len(self.aco.graph) - 1)
        # ind2 = ind1
        # while ind1==ind2:
        #     ind2 = randint(0, len(self.aco.graph) - 1)

        #scop demonstrativ
        ind1=self.aco.best.path[-1]
        ind2=self.aco.best.path[0]


        newCost=self.aco.best.getTotalDist()/2
        oldCost=self.aco.graph.getMatrix()[ind1][ind2]
        self.aco.graph.setEdge(ind1,ind2,newCost)
        self.aco.graph.setEdge(ind2, ind1, newCost)
        outs="Edge: ["+str(ind1)+","+str(ind2)+"] oldCost: "+str(oldCost)+" newCost: "+str(newCost)+"\n\n\n"
        print(outs)
        return outs