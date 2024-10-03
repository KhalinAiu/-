import matplotlib.pyplot as plt

x = ['Белуга', 'Калуга', 'Таймень', 'Севрюга', 'Сазан']
y = [2000, 1000, 80, 70, 40]
plt.bar(x, y, alpha=0.5 )
plt.plot(x, y, color='purple', marker='o', markersize=7)
plt.xlabel('Вид рыбы')
plt.ylabel('Масса в кг')
plt.title('Максимальная масса крупнейших рыб Росии')
plt.show()