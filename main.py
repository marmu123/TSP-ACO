from MyGraph import Graph
from ACO import ACO
from Repository import Repository
from Service import Service
r=Repository("hardE.txt",type='coord')
params={'repo':r,'graph':r.getGraph(),'alpha':0.5,'beta':0.5,'antsNr':15,'q0':0.5,'degrad':0.5,'phero':5}
aco=ACO(params)
serv=Service(aco)
serv.run()#dynamic=False