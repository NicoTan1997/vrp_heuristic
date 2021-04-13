import Customer
import numpy as np

def customer_check(seed_customer, seed_clusters, routes_all)
    len_seed = len(seed_customer)
    len_routes = len(routes_all)
    seed_in_routes = []
    for i in range(len_seed):
        for x in range(len_routes):
            try:
                list_no = routes_all[x].index(seed_customer[i])
                break
            except:
                pass
        list_no = x
        seed_in_routes.append(list_no)
    for i in range(len_seed):
        seed_fix_cluster = seed_clusters[i]
        seed_heu_cluster = routes_all[seed_in_routes[i]]
        seed_left_list = list(set(seed_fix_cluster) - set(seed_heu_cluster))
