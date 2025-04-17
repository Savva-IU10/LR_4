import matplotlib.pyplot as plt
import numpy as np

def add_circle(ax, center, radius, color, edgecolor='black'):
    """Добавляет круг на ось."""
    circle = plt.Circle(center, radius, color=color, ec=edgecolor)
    ax.add_artist(circle)

def add_polygon(ax, vertices, color, edgecolor='black'):
    """Добавляет многоугольник на ось."""
    polygon = plt.Polygon(vertices, color=color, ec=edgecolor)
    ax.add_artist(polygon)

def draw_bunny():
    fig, ax = plt.subplots(figsize=(5, 7))
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 400)
    ax.set_facecolor('white')

    # Тело
    add_circle(ax, (200, 200), 80, 'lightgray')

    # Голова
    add_circle(ax, (300, 200), 40, 'lightgray')

    # Глаза
    add_circle(ax, (290, 220), 5, 'black')  # Левый глаз
    add_circle(ax, (310, 220), 5, 'black')  # Правый глаз

    # Нос
    add_circle(ax, (300, 210), 5, 'pink')

    # Рот
    plt.plot([295, 305], [195, 195], color='black', linewidth=2)  # Рот ниже

    # Уши
    ear_left = np.array([[290, 230], [250, 300], [290, 280]])
    ear_right = np.array([[310, 230], [350, 300], [310, 280]])
    add_polygon(ax, ear_left, 'lightgray')
    add_polygon(ax, ear_right, 'lightgray')

    # Лапы
    add_circle(ax, (160, 120), 20, 'lightgray')  # Передняя левая лапа
    add_circle(ax, (240, 120), 20, 'lightgray')  # Передняя правая лапа
    add_circle(ax, (130, 120), 25, 'lightgray')  # Задняя левая лапа
    add_circle(ax, (270, 120), 25, 'lightgray')  # Задняя правая лапа

    # Хвост
    add_circle(ax, (120, 200), 15, 'white')  # Измененные координаты

    # Убираем оси
    ax.axis('off')

    # Сохраняем изображение
    plt.savefig('bunny_with_moved_tail.png', bbox_inches='tight')
    plt.show()

draw_bunny()
