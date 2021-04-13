from Customer import *
from distance_heuristic import *
from angle_heuristic import *
from demand_heuristic import *
import numpy as np
import math
from elkai_route import elkai_route
from gravitation_heuristic import *
from saving_heuristic import *


def route(population, Customers_all, capacity, angle_matrix, distance_matrix, gravitation_matrix, saving_matrix):
    depot = Customers_all[0]
    m = len(Customers_all)
    Customers = Customers_all[1:m]
    vec_temp = 1
    capa_temp = 0
    routes_all = []
    routes_temp = []
    customer_assigned = []
    customer_list = []
    m = m - 1
    for i in range(m):
        customer_list.append(i + 1)

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
            if distance_matrix[i, j] == 0:
                gravitation_matrix[i, j] = 0
            else:
                gravitation_matrix[i, j] = demand_matrix[i] * demand_matrix[j] / (distance_matrix[i, j] ** 2)
    # current_customer = demand_heuristic(demand_matrix, customer_assigned, customer_list)
    # angle_sort = np.argsort(angle_matrix)
    # current_customer = angle_sort[0] + 1
    current_customer = np.random.randint(1, m+1)
    customer_assigned.append(current_customer)
    routes_temp.append(current_customer)
    capa_temp += Customers_all[current_customer].demand

    for i in range(1,m):
        if population[i] == 0:
            index = distance_heuristic(distance_matrix, customer_assigned, current_customer, customer_list)
        elif population[i] == 1:
            index = angle_heuristic(angle_matrix, customer_assigned, current_customer, customer_list)
        elif population[i] == 3:
            index = gravitation_heuristic(gravitation_matrix, customer_assigned, current_customer, customer_list)
        elif population[i] == 2:
            index = saving_heuristic(saving_matrix, customer_assigned, current_customer, customer_list)

        if capa_temp + Customers_all[index].demand <= capacity:
            routes_temp.append(index)
            customer_assigned.append(index)
            current_customer = index
            capa_temp += Customers_all[index].demand
            if i == m-1:
                routes_temp.append(0)
                routes_temp_fix = elkai_route(Customers_all, routes_temp)
                routes_all.append(routes_temp_fix)
        else:
            routes_temp.append(0)
            capa_temp = 0
            routes_temp_fix = elkai_route(Customers_all, routes_temp)
            routes_all.append(routes_temp_fix)
            routes_temp = []
            vec_temp += 1
            current_customer = index
            customer_assigned.append(current_customer)
            routes_temp.append(index)
            capa_temp += Customers_all[current_customer].demand

    return routes_all
