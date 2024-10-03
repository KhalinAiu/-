import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axis as ax
import matplotlib.ticker as ticker
x = [i for i in range(24)]
y = [(i % 24) // 18 for i in range(21,45)]
plt.plot(x, y, color='red', marker='o', markersize=5)
ax = plt.gca()
plt.title("Желание ботать от времени суток")
plt.ylabel("Желание батать в долях от единицы")
plt.xlabel("Время суток")
plt.grid(True, which='major', axis='both', linestyle='solid') #сетка

ax.set_xticks([i for i in range(24)]) #значения оси по Х
ax.set_yticks([i / 10 for i in range(0, 11, 2)]) 

plt.show()
