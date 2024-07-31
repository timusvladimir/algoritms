import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Параметры решетки
nx, ny = 200, 200  # Размеры решетки
c = 1.0  # Скорость света в единицах решетки
dx = dy = 1.0  # Шаг по пространству
dt = dx / (2 * c)  # Шаг по времени
nt = 100  # Количество временных шагов

# Инициализация полей
Ez = np.zeros((nx, ny))  # Электрическое поле в z-образной плоскости
Hx = np.zeros((nx, ny))  # Магнитное поле в x-образной плоскости
Hy = np.zeros((nx, ny))  # Магнитное поле в y-образной плоскости


# Функция для обновления полей
def update_fields(Ez, Hx, Hy, dx, dy, dt, c):
    # Обновление магнитных полей
    Hx[:, :-1] -= dt / dx * (Ez[:, 1:] - Ez[:, :-1])
    Hy[:-1, :] += dt / dy * (Ez[1:, :] - Ez[:-1, :])

    # Обновление электрического поля
    Ez[1:-1, 1:-1] += dt / dx * (Hy[1:-1, 1:-1] - Hy[1:-1, :-2]) - dt / dy * (Hx[1:-1, 1:-1] - Hx[:-2, 1:-1])

    return Ez, Hx, Hy


# Моделирование на заданное время
for t in range(nt):
    Ez, Hx, Hy = update_fields(Ez, Hx, Hy, dx, dy, dt, c)

    # Введение плоской волны с линейной поляризацией
    Ez[:, :] = np.sin(2 * np.pi * (t * dt - np.arange(nx)[:, None] * dx) / 10.0)

# Визуализация поля Ez в заданный момент времени в 3D
x = np.arange(nx)
y = np.arange(ny)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Используем `plot_surface` для создания 3D-графика
surf = ax.plot_surface(X, Y, Ez, cmap='RdBu', edgecolor='none', vmin=-1, vmax=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Ez')
ax.set_title('Электрическое поле Ez в заданный момент времени (3D)')

# Добавляем цветовую шкалу
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

plt.show()
