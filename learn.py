import numpy as np
from random import sample, uniform, randint
from operator import add
from math import ceil
import matplotlib.pyplot as plt

data = [[0, 94, 76, 141, 91, 60, 120, 145, 91, 74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24], [94, 76, 141, 91, 60, 120, 145, 91, 74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94], [76, 141, 91, 60, 120, 145, 91, 74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0], [141, 91, 60, 120, 145, 91, 74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156], [91, 60, 120, 145, 91, 74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231], [60, 120, 145, 91, 74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64], [120, 145, 91, 74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93], [145, 91, 74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108], [91, 74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68], [74, 90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37], [90, 55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150], [55, 145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130], [145, 108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130, 57], [108, 41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130, 57, 233], [41, 49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130, 57, 233, 26], [49, 33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130, 57, 233, 26, 62], [33, 151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130, 57, 233, 26, 62, 140], [151, 69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130, 57, 233, 26, 62, 140, 61], [69, 111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130, 57, 233, 26, 62, 140, 61, 229], [111, 24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130, 57, 233, 26, 62, 140, 61, 229, 120], [24, 94, 0, 156, 231, 64, 93, 108, 68, 37, 150, 130, 57, 233, 26, 62, 140, 61, 229, 120, 57]]
populationSize = 5000
generations = 10
pointsize = len(data[0])-1
parentPool = 20
mutationRate = 0.04

def eval_fitness():
    distances = []
    # print(tours)
    for x in tours:

        tourdis = [list(map(int, ([0] + x))), list(map(int, (x + [0])))]
        distance = sum([data[tourdis[0][i]][tourdis[1][i]] for i in range(pointsize)])
        distances.append(1/distance)
    return distances

def roulette(p):
    # maxdis = sum(fitness for fitness in modF)
    # pick = uniform(0, maxdis)
    # current = 0
    # for fitness in modF:
    #     current += fitness
    #     if current > pick:
    #         return modF.index(fitness)

    #picking out best parents
    tmodF = sorted(modF)[::-1]
    return modF.index(tmodF[p])



def cross():
    #5 - 2
    ind = randint(0,ceil(pointsize/2))
    parent1 = parents[randint(0,parentPool-1)][ind:ind+int(pointsize/2)]
    parent2 = parents[randint(0,parentPool-1)]
    child = [0 for i in range(pointsize)]

    child[ind:ind+int(pointsize/2)] = parent1
    cind = 0
    pind = 0


    while 0 in child:

        if parent2[pind] not in child:
            if child[cind] == 0:
                child[cind] = parent2[pind]
            cind+=1
        else:
            pind+=1

    return child

def mutate():

    for i in tours:
        chance = randint(0,1000)/1000

        if (chance)<mutationRate:
            ind = randint(0,ceil(pointsize/3))

            i[ind:ind + int(pointsize/3)] = sample(i[ind:ind + int(pointsize/3)], int(pointsize/3))
#init
tours = []
for i in range(populationSize):
    tours.append(sample(list(range(1,pointsize+1)), pointsize))
"""
print(tours)
print(len(tours[0]))
"""

#mainloop
dislis = []
for i in range(generations):
    if i % 10 == 0:
        print(str((i/generations) * 100) + "%")
    #evaluation
    fitness = []

    #determine fitness of tour
    modF = eval_fitness()
    dislis.append(sum([1/i for i in modF])/populationSize)
    #termination condition irrelevant due to capped generations
    # print(modF)
    # print([1/i for i in modF])

    #selection
    parents = []
    for p in range(parentPool):
        parents.append(tours[roulette(p)])
    # print(tours)
    # print(parents)
    #crossover
    tours = []
    for p in range(populationSize):
        tours.append(cross())
    #mutate
    mutate()
print("plot")
print(dislis)
plt.plot(list(range(0,generations)),dislis)
plt.show()