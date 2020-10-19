import numpy as np
import matplotlib.pyplot as plt
for N in range(1,201):
    sum = 0
    for trial in range(0,4999):
        numbers = np.random.normal(0.0 , 1.0, N)
        maxval = np.max(numbers)
        sum += maxval
    avg = sum/5000
    n = np.arange(1,201)
    n.reshape(1,200)
    avgmax = []
    avgmax.append(avg)
plt.plot(n, avgmax)
plt.ylabel("average maximum values")
plt.xlabel("N")
plt.show()
