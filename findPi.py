import numpy as np
from math import pi
def checkArr(arr, size):
    x = arr[0]
    y = arr[1]
    return ((((x ** 0.5) - 0.5) * size) ** 2 + (((y ** 0.5) - 0.5) * size) ** 2)< (size**2)/4

def simulate(n, size): #n: Number of simulations, size: Size of Square/Circle
    successes = filter(lambda x: checkArr(x, size), np.random.rand(n, 2))
    return 4 * len(list(successes))/n

estimate = sum(simulate(1000, 0.5) for i in range(1000))/1000
print(f"Estimated Value: {estimate}")
print(f"Actual Value: {pi}")
print(f"Difference: {abs(estimate - pi)}")
