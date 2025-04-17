import matplotlib.pyplot as plt
import numpy as np

def draw_bunny():
    fig, ax = plt.subplots(figsize=(5, 7))
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 400)
    ax.set_facecolor('white')

    # Тело
    body = plt.Circle((200, 200), 80, color='lightgray', ec='black')
    ax.add_artist(body)

    # Голова
    head = plt.Circle((300, 200), 40, color='lightgray', ec='black')
    ax.add_artist(head)

    # Глаза
    eye_left = plt.Circle((290, 220), 5, color='black')  # Левый глаз
    eye_right = plt.Circle((310, 220), 5, color='black') # Правый глаз
    ax.add_artist(eye_left)
    ax.add_artist(eye_right)

    # Нос
    nose = plt.Circle((300, 210), 5, color='pink', ec='black')
    ax.add_artist(nose)

    # Рот
    plt.plot([295, 305], [195, 195], color='black', linewidth=2)  # Рот ниже

    # Уши (уголки вверх)
    ear_left = np.array([[290, 230], [250, 300], [290, 280]])
    ear_right = np.array([[310, 230], [350, 300], [310, 280]])
    ax.add_artist(plt.Polygon(ear_left, color='lightgray', ec='black'))
    ax.add_artist(plt.Polygon(ear_right, color='lightgray', ec='black'))

    # Лапы (опущены ниже туловища)
    front_leg_left = plt.Circle((160, 120), 20, color='lightgray', ec='black')  # Опущена ниже
    front_leg_right = plt.Circle((240, 120), 20, color='lightgray', ec='black') # Опущена ниже
    ax.add_artist(front_leg_left)
    ax.add_artist(front_leg_right)

    back_leg_left = plt.Circle((130, 120), 25, color='lightgray', ec='black')
    back_leg_right = plt.Circle((270, 120), 25, color='lightgray', ec='black')
    ax.add_artist(back_leg_left)
    ax.add_artist(back_leg_right)

    # Хвост (подвинут чуть правее)
    tail = plt.Circle((120, 200), 15, color='white', ec='black')  # Измененные координаты
    ax.add_artist(tail)

    # Убираем оси
    ax.axis('off')

    # Сохраняем изображение
    plt.savefig('bunny_with_moved_tail.png', bbox_inches='tight')
    plt.show()

draw_bunny()
