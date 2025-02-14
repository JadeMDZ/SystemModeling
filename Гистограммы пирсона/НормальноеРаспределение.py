import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Параметры
n = 1000  # Количество генераций
a = -3
b = 3
probabilities = [0.0215, 0.137, 0.34, 0.34, 0.137, 0.0215]
bins = np.linspace(a, b, len(probabilities) + 1)
p = np.array(probabilities)
k = np.zeros(len(p), dtype=int)  # Указываем, что это целочисленный массив
pcum = np.cumsum(p)  # Кумулятивные вероятности

# Генерация случайных чисел на основе кумулятивных вероятностей
for i in range(n):
    r = np.random.rand()
    for j in range(len(pcum)):
        if r < pcum[j]:
            k[j] += 1
            break

# Построение гистограммы
values = (bins[:-1] + bins[1:]) / 2  # Средние значения для бинов
plt.bar(values, k, width=(bins[1] - bins[0]), alpha=0.7, color='blue', edgecolor='black', label='Гистограмма')

# Вычисление среднего и стандартного отклонения
mean = np.sum(values * p)
std_dev = np.sqrt(np.sum(p * (values - mean) ** 2))

# Создание значений для оси X для теоретической кривой
x = np.linspace(a, b, 1000)
y = norm.pdf(x, mean, std_dev) * n * (bins[1] - bins[0])  # Масштабируем под количество

# Наложение кривой нормального распределения
plt.plot(x, y, color='red', label='Нормальное распределение')

expected_counts = n * p  
deviations = (k - expected_counts) ** 2 / expected_counts

# Печать индивидуальных отклонений и итогового значения
total_deviation = np.sum(deviations)  # Общее отклонение

for i in range(len(k)):
    print(f"Бин {i + 1}: Эмпирическое значение (k) = {k[i]}, Ожидаемое значение (np) = {expected_counts[i]:.2f}, Отклонение = {deviations[i]:.4f}")

print(f"\nОбщее отклонение = {total_deviation:.4f}")

# Настройка графика
plt.title(f'Отклонение {total_deviation:.4f}')
plt.xlabel('Значения')
plt.ylabel('Количество')
plt.xticks(np.linspace(a, b, 7))  # Установка меток по оси X
plt.legend()
plt.grid(axis='y')

plt.show()