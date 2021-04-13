import numpy as np
from Customer import *
import xlrd
import assignment_generate
from variation import *
from eval_pop import *
import math
import matplotlib.pyplot as plt


if __name__ == '__main__':

    workBook = xlrd.open_workbook('c1.xlsx')
    sheet1_content1 = workBook.sheet_by_name('Sheet1')
    capacity = int(sheet1_content1.cell(4, 1).value)
    dimension = int(sheet1_content1.cell(3, 1).value - 1)
    num_vec = int(sheet1_content1.cell(5, 1).value)
    Customers_all = []
    depot = Customer(0)
    depot.setCor(30, 40)
    Customers_all.append(depot)

    for i in range(1, dimension + 1):
        c = Customer(i)
        c.setCor(sheet1_content1.cell(i + 9, 1).value, sheet1_content1.cell(i + 9, 2).value)
        c.setDemand(sheet1_content1.cell(i + 10 + dimension, 1).value)
        angle = Customer.calculateDepotAngle(c.x, c.y, depot.x, depot.y)
        c.setAngleWithDepot(angle)
        Customers_all.append(c)
    Customers = Customers_all[1:dimension + 1]
    m = len(Customers)
    demand_matrix = np.zeros(m)
    for i in range(m):
        demand_matrix[i] = int(Customers[i].demand)

    angle_matrix = np.zeros(m)
    for i in range(m):
        angle_matrix[i] = int(Customers[i].angleWithDepot)

    distance_matrix = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            distance_matrix[i, j] = math.sqrt((Customers[i].x - Customers[j].x) ** 2 +
                                              (Customers[i].y - Customers[j].y) ** 2)

    gravitation_matrix = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            gravitation_matrix[i, j] = demand_matrix[i] * demand_matrix[j] / (distance_matrix[i, j] ** 2)

    saving_matrix = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            saving_matrix[i, j] = Customer.get_saving(Customers[i], Customers[j], depot.x, depot.y)

    pop_size = 10
    # population = np.random.randint(0, 4, size=[pop_size, dimension])
    population = np.zeros((pop_size, dimension))
    pop_obj = np.zeros(pop_size)
    for i in range(pop_size):
        routes_all = assignment_generate.route(population[i, :], Customers_all, capacity, angle_matrix, distance_matrix, gravitation_matrix, saving_matrix)
        pop_obj[i] = eval_pop(Customers_all, routes_all)

    plt.figure()
    generation = 200
    off_obj = np.zeros(pop_size)
    for i in range(generation):
        offspring_1 = crossover(population)
        offspring_2 = mutation(offspring_1)
        for j in range(pop_size):
            routes_all = assignment_generate.route(offspring_2[j,:], Customers_all, capacity, angle_matrix, distance_matrix, gravitation_matrix, saving_matrix)
            off_obj[j] = eval_pop(Customers_all, routes_all)
        pop_off = np.vstack((population, offspring_2))
        pop_off_obj = np.hstack((pop_obj,off_obj))
        obj_sort = np.argsort(pop_off_obj)
        population = pop_off[obj_sort[0:pop_size], :]
        pop_obj = pop_off_obj[obj_sort[0:pop_size]]
        obj_sort = np.argsort(pop_obj)
        plt.scatter(i,pop_obj[obj_sort[0]] , c = 'r')

    obj_sort = np.argsort(pop_obj)
    print(pop_obj[obj_sort[0]])
    plt.show()
    # routes_final = assignment_generate.route(population, Customers_all, capacity)
    # final_obj = eval_pop(Customers_all, routes_final)
    # obj_sort = np.argsort(final_obj)
    # routes_result = assignment_generate.route(population[obj_sort[1], :], Customers_all, capacity)
    # print(eval_pop(Customers_all, routes_result))
