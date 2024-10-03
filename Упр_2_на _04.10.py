import matplotlib.pyplot as plt
population = [1450, 1419, 345, 283, 8170 - 1450 - 1419 - 345 - 283]
y = ['Индия', 'Китай', 'США', 'Индонезия', 'Другие']

plt.pie(population, labels = y, autopct='%1.1f%%')
plt.title('Население Земли по государствам')
plt.scatter
plt.show()