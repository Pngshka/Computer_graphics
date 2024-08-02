import matplotlib.pyplot as plt

# Константы, представляющие положение точек относительно окна
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Функция, определяющая код точки
def computeCode(x, y, xmin, ymin, xmax, ymax):
    """
    Функция вычисляет код точки относительно окна.
    Args:
        x, y: Координаты точки.
        xmin, ymin, xmax, ymax: Границы окна.

    Returns:
        Код точки.
    """
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

# Функция отрисовки окна и отрезка
def plot_window_and_line(xmin, ymin, xmax, ymax, x1, y1, x2, y2):
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Алгоритм Сазерленда-Коэна')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Функция отсечения отрезка
def cohenSutherlandClip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = computeCode(x1, y1, xmin, ymin, xmax, ymax)
    code2 = computeCode(x2, y2, xmin, ymin, xmax, ymax)
    accept = False

    while True:
        # Оба конца отрезка внутри окна
        if code1 == 0 and code2 == 0:
            accept = True
            break
        # Оба конца отрезка находятся с одной стороны окна и не могут быть видны
        elif code1 & code2 != 0:
            break
        else:
            x = 0
            y = 0
            # Выбираем внешнюю точку для обрезки
            outsideCode = code1 if code1 != 0 else code2
            if outsideCode & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outsideCode & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outsideCode & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outsideCode & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Заменяем внешнюю точку на пересечение линии с окном
            if outsideCode == code1:
                x1, y1 = x, y
                code1 = computeCode(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                code2 = computeCode(x2, y2, xmin, ymin, xmax, ymax)

    if accept:
        #print("Отрезок от ({},{}) до ({},{}) виден в окне".format(x1, y1, x2, y2))
        plt.plot([x1, x2], [y1, y2], marker='o', color='red')
    else:
        print("Отрезок полностью или частично за пределами окна")

# Входные данные
xmin, ymin, xmax, ymax = 0, 0, 10, 10
x1, y1 = 0, 0
x2, y2 = 5, 5


plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], color='black')
plt.plot([x1, x2], [y1, y2])
cohenSutherlandClip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
plot_window_and_line(xmin, ymin, xmax, ymax, x1, y1, x2, y2)
