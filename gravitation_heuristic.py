import Customer
import numpy as np
import math


def gravitation_heuristic(gravitation_matrix, pop_temp, current_customer, customer_list):
    left_set = list(set(customer_list) - set(pop_temp))
    left_set_fix = np.array([i - 1 for i in left_set])
    distance_temp = gravitation_matrix[current_customer - 1, :]
    distance_fix = distance_temp[left_set_fix]
    dis_sort = np.argsort(distance_fix)
    index = left_set_fix[dis_sort[0]] + 1
    return index