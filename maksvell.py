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


# Функции для расчета полей
def electric_field(x, y, z, t):
    return np.cos(omega * t) * np.sin(np.pi * X) * np.sin(np.pi * Y) * np.sin(np.pi * Z)


def magnetic_field(x, y, z, t):
    return np.cos(omega * t) * np.sin(np.pi * X) * np.sin(np.pi * Y) * np.sin(np.pi * Z)


# Создание фигуры и трехмерных осей
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Визуализация полей в разные моменты времени
for ti in t:
    Ex = electric_field(X, Y, Z, ti)
    Ey = np.zeros_like(Ex)
    Ez = np.zeros_like(Ex)

    Bx = magnetic_field(X, Y, Z, ti)
    By = np.zeros_like(Bx)
    Bz = np.zeros_like(Bx)

    ax.clear()
    ax.quiver(X, Y, Z, Ex, Ey, Ez, length=0.1, normalize=True, color='b', arrow_length_ratio=0.3)
    ax.quiver(X, Y, Z, Bx, By, Bz, length=0.1, normalize=True, color='r', arrow_length_ratio=0.3)

    ax.set_title(f'Fields at time t = {ti:.2f}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.pause(0.1)

plt.show()
