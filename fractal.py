import numpy as np
import matplotlib.pyplot as plt

# Определение параметров изображения
width, height = 800, 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 100

# Создание массива координат для пикселей
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y
Z = np.zeros(C.shape, dtype=complex)

# Инициализация массива для хранения количества итераций
iterations = np.zeros(C.shape, dtype=int)

# Итерация для вычисления фрактала Мандельброта
for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask] * Z[mask] + C[mask]
    iterations += mask

# Построение графика
plt.figure(figsize=(10, 10))
plt.imshow(iterations, extent=(xmin, xmax, ymin, ymax), cmap='inferno', vmin=0, vmax=max_iter)
plt.colorbar(label='Количество итераций')
plt.title('Фрактал Мандельброта')
plt.xlabel('Re(C)')
plt.ylabel('Im(C)')
plt.show()