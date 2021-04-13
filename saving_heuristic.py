import Customer
import numpy as np
import math


def saving_heuristic(saving_matrix, pop_temp, current_customer, customer_list):
    left_set = list(set(customer_list) - set(pop_temp))
    left_set_fix = np.array([i - 1 for i in left_set])
    saving_temp = saving_matrix[current_customer - 1, :]
    saving_fix = saving_temp[left_set_fix]
    dis_sort = np.argsort(saving_fix)
    index = left_set_fix[dis_sort[0]] + 1
    return index