from PIL import Image
import matplotlib.pyplot as plt


def image_to_ascii(image_path, width=100):
    # Загрузите изображение
    img = Image.open(image_path)

    # Измените размер изображения
    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * width)
    img = img.resize((width, new_height))

    # Преобразуйте изображение в градации серого
    img_gray = img.convert('L')

    # Определите набор символов для отображения градаций серого
    chars = "@%#*+=-:. "  # Более детализированный набор символов
    num_chars = len(chars)

    pixels = img_gray.load()
    ascii_image = ""

    for y in range(img_gray.height):
        for x in range(img_gray.width):
            pixel = pixels[x, y]
            # Преобразование значений серого (0-255) в диапазон индексов символов
            ascii_index = pixel * (num_chars - 1) // 255
            ascii_image += chars[ascii_index]
        ascii_image += "\n"

    return ascii_image


# Путь к изображению
image_path = 'einstein.jpg'  # Замените на путь к вашему изображению

# Преобразуйте изображение в псевдографику
ascii_art = image_to_ascii(image_path, width=100)

# Отображение изображения
plt.figure(figsize=(10, 10))
plt.text(0.5, 0.5, ascii_art, fontsize=8, fontfamily='monospace', ha='center', va='center', color='black')
plt.axis('off')  # Отключить оси для чистого отображения изображения
plt.show()
