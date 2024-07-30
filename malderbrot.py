import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.zeros((height, width))

    for i in range(width):
        for j in range(height):
            mandelbrot_image[j, i] = mandelbrot(x[i] + 1j * y[j], max_iter)

    return (x, y, mandelbrot_image)

def plot_mandelbrot(x, y, mandelbrot_image):
    plt.figure(figsize=(10, 8))
    plt.imshow(mandelbrot_image.T, extent=(x.min(), x.max(), y.min(), y.max()), cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    plt.show()

if __name__ == '__main__':
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5  # Границы комплексной плоскости
    width, height = 1000, 800  # Размер изображения
    max_iter = 300  # Максимальное количество итераций для каждой точки

    x, y, mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plot_mandelbrot(x, y, mandelbrot_image)
