import numpy as np
import matplotlib.pyplot as plt

size = 400
x_peregorodka = 40
p1 = [0, 20]
p2 = [20, 0]
p3 = [40, 20]
p4 = [60, 0]
p5 = [80, 20]
p6 = [60, 40]
p7 = [60, 100]
p8 = [80, 130]
p9 = [60, 150]
p10 = [40, 130]
p11 = [20, 150]
p12 = [-100, 130]
p13 = [20, 100]
p14 = [20, 40]
p15 = [0, 20, True, *p2]
points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]

x_peregorodka = 10
p1 = [1, 5]
p2 = [30, 10]
p3 = [20, 4, True, *p1]
points = [p1, p2, p3]

# x_peregorodka = 40
# p1 = [0, 20]
# p2 = [20, 0]
# p3 = [50, 0]
# p4 = [60, 10]
# p5 = [80, -10]
# p6 = [80, 50]
# p7 = [70, 30]
# p8 = [50, 50]
# p9 = [30, 50]
# p10 = [0, 20, True, *p2]
# points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


def get_pixel(x, y):
    return [int(size / 2 + x), int(size / 2 - y)]


def do_pixel_red(x, y):
    pixel = get_pixel(x, y)
    res[pixel[1]][pixel[0]] = [254, 0, 0]


def do_pixel_black(x, y):
    pixel = get_pixel(x, y)
    res[pixel[1]][pixel[0]] = [0, 0, 0]


def print_peregorodka():
    for y in range(size):
        do_pixel_black(x_peregorodka, y)


def print_figure():
    for i in range(len(points) - 1):
        p_start = points[i]
        p_end = points[i + 1]
        line = bresenham_line(p_start[0], p_start[1], p_end[0], p_end[1])
        for j in line:
            do_pixel_black(*j)
        # exit()


def bresenham_line(x0, y0, x1, y1) -> list:
    pixels = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    slope = dy > dx

    if slope:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = abs(y1 - y0)
    error = dx >> 1
    ystep = 1 if y0 < y1 else -1
    y = y0

    for x in range(x0, x1 + 1):
        coord = [y, x] if slope else [x, y]
        pixels.append(coord)
        error -= dy
        if error < 0:
            y += ystep
            error += dx

    return pixels


def invert_pixel(x, y):
    pixel = get_pixel(x, y)

    real_pixel = res[pixel[1]][pixel[0]]
    if real_pixel[0] != 0:
        res[pixel[1]][pixel[0]] = [0, 0, 0]
    else:
        res[pixel[1]][pixel[0]] = [254, 254, 254]

    # real_pixel = res[pixel[1]][pixel[0]]
    # real_pixel[0] = (real_pixel[0] + 255) % 255
    # real_pixel[1] = (real_pixel[1] + 255) % 255
    # real_pixel[2] = (real_pixel[2] + 255) % 255
    # print("x,y = " + str(x) + " " + str(y))
    # print("pixel_color = " + str(real_pixel))


def alg_from_line(p1, p2, p1_last, p2_last):
    line = bresenham_line(p1[0], p1[1], p2[0], p2[1])
    if (p1_last != None and np.sign(p1[1] - p1_last[1]) != np.sign(p1[1] - p2[1])):
        line = list(filter(lambda p: p[1] != p1[1], line))
    if (len(p2)>2 and p2[2] == True):
        p_start_figure = p2
        p_second_figure = [p2[3], p2[4]]
        if (p1_last != None and np.sign(p2[1] - p_second_figure[1]) != np.sign(p2[1] - p1[1])):
            line = list(filter(lambda p: p[1] != p2[1], line))
    left_points = []
    right_points = []
    for p in line:
        if (p[0] < x_peregorodka):
            left_points.append(p)
        else:
            right_points.append(p)

    last_point = None
    for left_point in left_points:
        if (last_point != None) and last_point[1] == left_point[1]:
            continue
        while left_point[0] < x_peregorodka:
            invert_pixel(*left_point)
            left_point[0] += 1
        last_point = left_point

    last_point = None
    for right_point in right_points:
        if (last_point != None) and last_point[1] == right_point[1]:
            continue
        while right_point[0] > x_peregorodka:
            invert_pixel(*right_point)
            right_point[0] -= 1
        last_point = right_point


white_pixel = [255, 255, 255]

res = list([[white_pixel for b in range(size)] for a in range(size)])
# print(res)
# res[3][4] = [254, 0, 0]  # рисуем красный пиксель
p1_last = None
p2_last = None
# plt.grid(True)
print_figure()
print_peregorodka()
for i in range(len(points) - 1):
    p_start = points[i]
    p_end = points[i + 1]
    if (p_start[1] == p_end[1]):
        continue
    alg_from_line(p_start, p_end, p1_last, p2_last)
    plt.imshow(res)
    plt.pause(0.0001)
    p1_last = p_start
    p2_last = p_end

plt.show()

# exit()
