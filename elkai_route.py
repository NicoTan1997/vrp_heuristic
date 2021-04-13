import elkai
import numpy as np
import math


def elkai_route(Customers_all, routes_temp):
    routes_temp_np = np.array(routes_temp)
    Customers_all = np.array(Customers_all)
    customer_route = Customers_all[routes_temp_np]
    m = len(customer_route)
    distance_route = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            distance_route[i, j] = math.sqrt((customer_route[i].x - customer_route[j].x) ** 2 +
                                             (customer_route[i].y - customer_route[j].y) ** 2)
    routes_new = elkai.solve_int_matrix(distance_route)
    routes_new_fix = np.zeros(len(routes_temp))
    for i in range(len(routes_temp)):
        routes_new_fix[i] = routes_temp_np[routes_new[i]]
    return routes_new_fix.astype(np.int)
