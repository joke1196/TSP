from _codecs import latin_1_encode

from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Initializators
from pyevolve import GAllele
from pyevolve import Statistics
from haversine import haversine
from pyevolve import DBAdapters
import random
import os
class City:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

def fitness(chromosome):
   # iterate over the chromosome
    totalDist = 1
    for i in xrange(0,len(chromosome)):
        start = (LAT[chromosome[i]], LON[chromosome[i]])
        if(i == len(chromosome) -1):
            end = (LAT[chromosome[0]], LON[chromosome[0]])
        else:
            end = (LAT[chromosome[i+1]], LON[chromosome[i+1]])
        totalDist += computeDistance(start, end)

    if len(chromosome) != len(set(chromosome)):
        return 1 - ((len(chromosome) - len(set(chromosome))) * 0.05)


    return 15000 - totalDist


def computeDistance(start, end) :
    return haversine(start, end)


def G1DListTSPInitializator(genome, **args):
   """ The initializator for the TSP """
   lst = [i for i in xrange(genome.getListSize())]
   random.shuffle(lst)
   genome.setInternalList(lst)



LAT = [16.47, 16.47, 20.09, 22.39, 25.23, 22.00, 20.47,
      17.20, 16.30, 14.05, 16.53, 21.52, 19.41, 20.09]

LON = [96.10, 94.44, 92.54, 93.37, 97.24, 96.05, 97.02,
      96.29, 97.38, 98.12, 97.38, 95.59, 97.13, 94.55]

# Chromosome representation
genome = G1DList.G1DList(14)
# genome = bitstring
genome.initializator.set(G1DListTSPInitializator)
genome.setParams(rangemin= 0, rangemax=13)

# how to compute the fitness
genome.evaluator.set(fitness)

# GA initialisation
ga = GSimpleGA.GSimpleGA(genome, seed=123)
ga.setPopulationSize(100)
ga.setMutationRate(0.01)
ga.setCrossoverRate(0.9)
ga.selector.set(Selectors.GTournamentSelector)
ga.setElitism(True)


sqlite_adapter = DBAdapters.DBSQLite(identify="tsp")
ga.setDBAdapter(sqlite_adapter)
# Number of generations
ga.setGenerations(250)

# In case we want to monitor the evolution process
# execute the function current_best every generation
#ga.stepCallback.set(current_best)

ga.evolve(freq_stats=10)

# Final best solution
print ga.bestIndividual()
totalDist = 0.0
for i in xrange(len(ga.bestIndividual())):
    start = (LAT[ga.bestIndividual()[i]], LON[ga.bestIndividual()[i]])
    if(i == len(ga.bestIndividual()) -1):
        end = (LAT[ga.bestIndividual()[0]], LON[ga.bestIndividual()[0]])
    else:
        end = (LAT[ga.bestIndividual()[i+1]], LON[ga.bestIndividual()[i+1]])
    totalDist += computeDistance(start, end)
print totalDist


