import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создание сетки в трехмерном пространстве
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
z = np.linspace(-2, 2, 50)
X, Y, Z = np.meshgrid(x, y, z)

# Константы и параметры времени
epsilon0 = 1.0
mu0 = 1.0
omega = 1.0
t = np.linspace(0, 2 * np.pi, 100)


# Функция для расчета компоненты поля
def electric_field(x, y, z, t):
    k = np.pi  # Волновой вектор (можно изменять)
    return np.sin(k * X) * np.cos(k * Y) * np.cos(omega * t - k * Z)


# Создание фигуры и трехмерных осей
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Визуализация поля в разные моменты времени
for ti in t:
    Ex = electric_field(X, Y, Z, ti)

    ax.clear()
    ax.set_title(f'Electric Field at time t = {ti:.2f}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.scatter(X, Y, Z, c=Ex, cmap='viridis', alpha=0.6)

    plt.pause(0.1)

plt.show()
