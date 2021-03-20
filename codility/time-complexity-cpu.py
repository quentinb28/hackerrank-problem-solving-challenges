import random

import time

list1 = [random.randint(-1000, 1000) for i in range(20000)]

times = []

for x in range(100, 20001, 100):
    start_time = time.time()
    list2 = solution(list1[:x])
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)

x = [i for i in range(100, 20001, 100)]

import matplotlib.pyplot as plt
plt.xlabel("No. of elements")
plt.ylabel("Time required")
plt.plot(x, times)
