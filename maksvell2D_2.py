import numpy as np
import matplotlib.pyplot as plt

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

# Визуализация поля Ez в заданный момент времени
plt.figure(figsize=(8, 6))
plt.imshow(Ez, cmap='RdBu', vmin=-1, vmax=1, origin='lower')
plt.colorbar(label='Ez')
plt.title('Электрическое поле Ez в заданный момент времени')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
