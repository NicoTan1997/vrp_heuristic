import Customer
import numpy as np


def demand_heuristic(demand_all, pop_temp, customer_list):
    m = len(demand_all)
    left_set = list(set(customer_list) - set(pop_temp))
    left_set_fix = np.array([i - 1 for i in left_set])
    demand_fix = demand_all[left_set_fix]
    demand_sort = np.argsort(demand_fix)
    index = left_set_fix[demand_sort[len(demand_sort) - 1]] + 1
    return index
