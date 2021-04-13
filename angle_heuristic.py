import Customer
import numpy as np


def angle_heuristic(angle_matrix, pop_temp, current_customer, customer_list):

    left_set = list(set(customer_list) - set(pop_temp))
    left_set_fix = np.array([i - 1 for i in left_set])
    angle_fix = angle_matrix[left_set_fix]
    m = len(angle_fix)
    for i in range(m):
        angle_fix[i] = abs(angle_matrix[left_set_fix[i]] - angle_matrix[current_customer - 1])
    angle_sort = np.argsort(angle_fix)
    index = left_set_fix[angle_sort[0]] + 1
    return index
