import matplotlib.pyplot as plt
import numpy as np
from Customer import *
import nevergrad as ng


def square(x):
    return sum((x - .5) ** 2)


if __name__ == '__main__':
    # x = 30
    # y = 40
    # x1 = 40
    # y1 = 40
    # x2 = 40
    # y2 = 50
    # x3 = 30
    # y3 = 50
    # x4 = 0
    # y4 = 40
    # x = 1
    # y = 2
    # plt.figure()
    # plt.scatter(x, y)
    # plt.show()
    # print(2361.3749965383586)

    optimizer = ng.optimizers.NGOpt(parametrization=2, budget=100)
    recommendation = optimizer.minimize(square)
    print(recommendation.value)
