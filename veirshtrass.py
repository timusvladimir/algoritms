import matplotlib.pyplot as plt
import numpy as np


def weierstrass(x, a, b, max_iter):
    y = np.zeros_like(x)
    for n in range(max_iter):
        y += np.cos(b ** n * np.pi * x) / (a ** n)
    return y


def plot_weierstrass(a, b, max_iter, num_points):
    x = np.linspace(-10, 10, num_points)
    y = weierstrass(x, a, b, max_iter)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='b', linewidth=1.5)
    plt.title('Weierstrass Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    a = 0.5  # Параметр a
    b = 3  # Параметр b
    max_iter = 500  # Максимальное количество итераций
    num_points = 100  # Количество точек для построения

    plot_weierstrass(a, b, max_iter, num_points)
