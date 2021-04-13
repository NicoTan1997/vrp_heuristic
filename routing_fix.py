import Customer
import numpy as np
from distance_heuristic import *
import random
from gravitation_heuristic import *


def routing_fix(Customers_all, capacity, num_vec, customer_list, angle_matrix, distance_matrix, gravitation_matrix):
    len_all = len(Customers_all)
    Customers = Customers_all[1:len_all]
    demand_all = 0
    len_cus = len_all - 1
    demand_matrix = np.zeros(len_cus)
    for i in range(len_cus):
        demand_matrix[i] = int(Customers[i].demand)
        demand_all += Customers[i].demand
    capa_cluster = int(demand_all / num_vec)
    cluster_temp = []
    clusters = []
    customer_assigned = []
    capa_temp = 0
    angle_sort = np.argsort(angle_matrix)
    current_customer = angle_sort[0]
    index = current_customer
    customer_assigned.append(current_customer)
    cluster_temp.append(current_customer)
    capa_temp += Customers_all[current_customer].demand

    for i in range(1, len_cus):
        current_customer = angle_sort[i]
        index = current_customer
        if capa_temp + Customers[index].demand <= capa_cluster:
            cluster_temp.append(index)
            customer_assigned.append(index)
            current_customer = index
            capa_temp += Customers[index].demand
            if i == len_cus:
                clusters.append(cluster_temp)
        else:
            capa_temp = 0
            clusters.append(cluster_temp)
            cluster_temp = []
            customer_assigned.append(current_customer)
            cluster_temp.append(index)

    num_cluster = len(clusters)
    seed_customer = np.zeros(num_cluster)
    customer_clustered = 0
    for i in range(num_cluster):
        current_cluster = np.array(clusters[i])
        angle_clustered = angle_matrix[current_cluster]
        angle_cover = angle_matrix[current_cluster[-1]] - angle_matrix[current_cluster[0]]
        demand_clustered = sum(demand_matrix[current_cluster])
        density_clustered = demand_clustered / angle_cover
        angle_mid = demand_clustered * angle_clustered / 2
        n_deltas = np.array([abs(n - angle_mid) for n in angle_clustered])
        nearest = np.argsort(n_deltas)
        seed_customer[i] = nearest[0]

    seed_clusters = []

    for i in range(len(seed_customer)):
        random_num = random.random()
        current_capacity = 0
        current_customer = seed_customer[i]
        cluster_temp = []
        customer_assigned = []
        cluster_temp.append(current_customer)
        current_capacity += Customers_all[current_customer].demand
        current_customer = distance_heuristic(distance_matrix, cluster_temp, current_customer, customer_list)
        index = current_customer
        while current_capacity + Customers[index].demand <= capacity:
            cluster_temp.append(index)
            customer_assigned.append(index)
            current_customer = seed_customer[i]
            if float(random_num) < 0.5:
                index = distance_heuristic(distance_matrix, cluster_temp, current_customer, customer_list)
            else:
                index = gravitation_heuristic(gravitation_matrix, cluster_temp, current_customer, customer_list)
            current_capacity += Customers[index].demand
        seed_clusters.append(cluster_temp)

    return seed_customer, np.array(seed_clusters)
