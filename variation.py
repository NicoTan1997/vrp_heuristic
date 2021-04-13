import random
import numpy as np


def crossover(population):
    m = len(population)
    offspring = []
    half_size = int(population.shape[0] / 2)
    pop_len = population.shape[1]
    for i in range(half_size):
        cross_index = random.randint(0, pop_len)
        parent1 = population[i, :]
        parent2 = population[i + half_size, :]
        piece_1 = list(parent1[cross_index:m])
        piece_2 = list(parent2[cross_index:m])
        parent1[cross_index:m] = piece_2
        parent2[cross_index:m] = piece_1
        offspring.append(parent1)
        offspring.append(parent2)
    return np.array(offspring)


def mutation(population):
    m = len(population)
    offspring = []
    pop_len = population.shape[1]
    for i in range(m):
        if float(random.random()) < 0.2:
            cross_index = random.randint(0, pop_len-1)
            population[i, cross_index] = round(3*random.random())
        offspring.append(population[i, :])
    return np.array(offspring)
