from Customer import *


def eval_pop(Customers_all, routes):
    num_route = len(routes)
    obj = 0
    for i in range(num_route):
        cost_temp = 0
        route_temp = routes[i]
        route_len = len(route_temp)
        for j in range(route_len - 1):
            cost_temp += Customer.get_distance(Customers_all[route_temp[j]], Customers_all[route_temp[j+1]])
        cost_temp = cost_temp + Customer.get_distance(Customers_all[route_temp[0]], Customers_all[route_temp[route_len-1]])
        obj += cost_temp
    return obj
