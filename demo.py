from Customer import *
import xlrd
import xlwt
import numpy as np
from eval_pop import *
from math import sqrt, degrees, atan2
import elkai
from variation import crossover, mutation
import random
from routing_fix import routing_fix
import matplotlib.pyplot as plt

import numpy as np
from Customer import *
import xlrd
import assignment_generate
from variation import *
from eval_pop import *
import math

if __name__ == '__main__':
    a = 4*np.ones(10)
    print(a)
    # workBook = xlrd.open_workbook('c1.xlsx')
    # sheet1_content1 = workBook.sheet_by_name('Sheet1')
    # capacity = int(sheet1_content1.cell(4, 1).value)
    # dimension = int(sheet1_content1.cell(3, 1).value - 1)
    # num_vec = int(sheet1_content1.cell(5, 1).value)
    # Customers_all = []
    # depot = Customer(0)
    # depot.setCor(30, 40)
    # Customers_all.append(depot)
    #
    # for i in range(1, dimension + 1):
    #     c = Customer(i)
    #     c.setCor(sheet1_content1.cell(i + 9, 1).value, sheet1_content1.cell(i + 9, 2).value)
    #     c.setDemand(sheet1_content1.cell(i + 10 + dimension, 1).value)
    #     angle = Customer.calculateDepotAngle(c.x, c.y, depot.x, depot.y)
    #     c.setAngleWithDepot(angle)
    #     Customers_all.append(c)
    # Customers = Customers_all[1:dimension + 1]
    # m = len(Customers)
    # demand_matrix = np.zeros(m)
    # for i in range(m):
    #     demand_matrix[i] = int(Customers[i].demand)
    #
    # angle_matrix = np.zeros(m)
    # for i in range(m):
    #     angle_matrix[i] = int(Customers[i].angleWithDepot)
    #
    #
    # distance_matrix = np.zeros((m, m))
    # for i in range(m):
    #     for j in range(m):
    #         distance_matrix[i, j] = math.sqrt((Customers[i].x - Customers[j].x) ** 2 +
    #                                           (Customers[i].y - Customers[j].y) ** 2)
    #
    # gravitation_matrix = np.zeros((m, m))
    # for i in range(m):
    #     for j in range(m):
    #         if distance_matrix[i, j] == 0:
    #             gravitation_matrix[i, j] = 0
    #         else:
    #             gravitation_matrix[i, j] = demand_matrix[i] * demand_matrix[j] / (distance_matrix[i, j] ** 2)
    #
    # saving_matrix = np.zeros((m, m))
    # for i in range(m):
    #     for j in range(m):
    #         saving_matrix[i, j] = Customer.get_saving(Customers[i], Customers[j], depot.x, depot.y)
    #
    # pop_size = 100
    # # population = np.random.randint(0, 4, size=[pop_size, dimension])
    # population = np.ones((pop_size, dimension))
    # pop_obj = np.zeros(pop_size)
    # routes_pop = []
    # for i in range(pop_size):
    #     routes_all = assignment_generate.route(population[i, :], Customers_all, capacity, angle_matrix, distance_matrix,
    #                                            gravitation_matrix, saving_matrix)
    #     routes_pop.append(routes_all)
    #     pop_obj[i] = eval_pop(Customers_all, routes_all)
    #
    # obj_sort = np.argsort(pop_obj)
    # print(pop_obj[obj_sort[0]])
    # #plot
    # plt.figure()
    # plt.scatter(depot.x, depot.y, c='r')
    # color_list = ['y', 'g', 'b' ]
    # for i in range(3):
    #     # plt.scatter(depot.x, depot.y, 'r')
    #     route_temp = np.array(routes_all[i])
    #     for j in range(len(route_temp)):
    #         plt.scatter(Customers_all[route_temp[j]].x, Customers_all[route_temp[j]].y,  c=color_list[i])
    # plt.show()
    # plt.figure()
    # color_list = ['r','y', 'g', 'b']
    # for i in range(len(Customers_all)):
    #     route_temp = Customers_all[i]
    #     plt.scatter(route_temp.x, route_temp.y, c = color_list[i])
    # plt.show()
    # x = 30
    # y = 40
    # x1 = 40
    # y1 = 40
    # x2 = 40
    # y2 = 50
    # x3 = 30
    # y3 = 50
    # x4 = 30
    # y4 = 0
    # print(calculateDepotAngle(x, y, x1, y1))
    # print(calculateDepotAngle(x, y, x2, y2))
    # print(calculateDepotAngle(x, y, x3, y3))
    # print(calculateDepotAngle(x, y, x4, y4))
    # population = np.random.randint(0, 2, size=[6, 6])
    # print(population)
    # offspring = crossover(population)
    # #
    # print(offspring)
    # nums = np.array([1, 2, 3.1, 0, 4])
    # ave \
    #         pass
    # list_no = x
    # print(list_no)
    # seed_cluster = np.array(lst[list_no])
    # print(type(seed_cluster))

