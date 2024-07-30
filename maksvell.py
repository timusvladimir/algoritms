import numpy as np
import matplotlib.pyplot as plt

# Создание сетки
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Параметры поля и времени
epsilon0 = 1.0
mu0 = 1.0
omega = 1.0
t = np.linspace(0, 2 * np.pi, 100)


# Функции для расчета полей
def electric_field(x, y, t):
    return np.cos(omega * t) * np.sin(np.pi * X) * np.sin(np.pi * Y)


def magnetic_field(x, y, t):
    return np.cos(omega * t) * np.sin(np.pi * X) * np.sin(np.pi * Y)


# Создание фигуры
fig = plt.figure(figsize=(12, 6))

# Подграфики для электрического и магнитного полей
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Визуализация полей в разные моменты времени
for ti in t:
    Ex = electric_field(X, Y, ti)
    Bx = magnetic_field(X, Y, ti)

    ax1.clear()
    ax1.set_title('Electric Field')
    ax1.streamplot(X, Y, Ex, np.zeros_like(Ex), color='b', linewidth=1)

    ax2.clear()
    ax2.set_title('Magnetic Field')
    ax2.streamplot(X, Y, Bx, np.zeros_like(Bx), color='r', linewidth=1)

    plt.pause(0.1)

plt.show()
