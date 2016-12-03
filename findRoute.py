#!/usr/bin/python

import random
from utilities import *

def getTotalDist(route, cityData):
    totalDist = 0
    for i in range(len(route)):
        city1 = route[i]
        city2 = route[i-1]
        if city2 not in cityData[city1]['distances']:
            totalDist += 1.0
        else:
            totalDist += cityData[city1]['distances'][city2]
    return totalDist

def mutate(route, maxMutations = 3):
    route = list(route)
    numMutations = random.randint(1,maxMutations)
    for _ in range(numMutations):
        i = random.randint(0, len(route) -1)
        j = i
        while i == j:
            j = random.randint(0, len(route) -1)
            route[i], route[j] = route[j], route[i]
    return tuple(route)

def shuffleMutate(route):
    route = list(route)
    random.shuffle(route)
    return tuple(route)

def generatePopulation(baseRoute, popSize):
    population = []
    for _ in range(popSize):
        population.append(shuffleMutate(baseRoute))
    return population

def nextGeneration(population, cityData, popSize):
    popFitness = {}
    for route in population:
        if route in popFitness:
            continue

        popFitness[route] = getTotalDist(route, cityData)

    newPop = []

    topRanksSize = popSize /10
    for rank, route in enumerate(sorted(popFitness, key=popFitness.get)[:topRanksSize]):
        newPop.append(route)
        for offspring in range(2):
            newPop.append(mutate(route, 3))
        for offspring in range(7):
            newPop.append(shuffleMutate(route))

    best = sorted(popFitness, key=popFitness.get)[0]
    return newPop, best, popFitness[best]

def runGeneticAlgo(cityData, genSize = 1000, popSize = 100):
    cities = cityData.keys()
    pop = generatePopulation(cities, popSize)
    for gen in range(1,genSize+1):
        pop,best, bestVal = nextGeneration(pop, cityData, popSize)
        if gen % 10 == 0:
            print "Gen {}".format(gen)
            print best
            print bestVal
            print

def test():
    cd = readYamlData('out.yaml')
    runGeneticAlgo(cd)

if __name__ == "__main__":
    test()
