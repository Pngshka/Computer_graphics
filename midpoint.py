import numpy as np
import matplotlib.pyplot as plt


def code(arr, x, y):
    Ax = arr[0]
    Ay = arr[1]
    Bx = arr[2]
    By = arr[3]

    l_list = []

    if x < Ax:
        l_list.append(1)
    else:
        l_list.append(0)
    if y <= By:
        l_list.append(0)
    else:
        l_list.append(1)
    if y < Ay:
        l_list.append(1)
    else:
        l_list.append(0)
    if x <= Bx:
        l_list.append(0)
    else:
        l_list.append(1)

    return l_list


def provLocation(mas, st, se):

    u = 0

    x1, y1 = st[0], st[1]
    x2, y2 = se[0], se[1]

    l1_list = code(mas, x1, y1)
    l2_list = code(mas, x2, y2)

    if max(l1_list) == max(l2_list) == 0:
        u = 1

    if u != 1:
        for i in range(4):
            if l1_list[i] * l2_list[i] == 1:
                u = 2
        if u != 2:
            u = 3
    # print(u)
    return u


def window(mas, ax):
    ax.grid()

    window_x = [mas[0], mas[0], mas[2], mas[2], mas[0]]
    window_y = [mas[1], mas[3], mas[3], mas[1], mas[1]]

    ax.plot(window_x, window_y, c='black')


def recMidPoint(mas1, st, se, ax):
    d = provLocation(mas1, st, se)
    # print(d)
    len_seg = np.sqrt((st[0]-se[0])*(st[0]-se[0])+(st[1]-se[1])*(st[1]-se[1]))

    if len_seg < 0.001:
        return

    if d == 1:
        ax.plot([st[0], se[0]], [st[1], se[1]], color='red')
        return
    if d == 2:
        ax.plot([st[0], se[0]], [st[1], se[1]], color='blue')
        return
    if d == 3:
        s = [(st[0] + se[0]) / 2, (st[1] + se[1]) / 2]
        ax.scatter(s[0], s[1], c='green')
        recMidPoint(mas1, st, s, ax)
        recMidPoint(mas1, s, se, ax)


def midPoint(ax):

    ax.set_title('Средней точки')

    x_max=6
    y_max=6
    x_min=0
    y_min=0 #= poly_to_rect(polygon)
    #print(str(x_max)+" "+str(y_max)+" "+str(x_min)+" "+str(y_min))
    w = [x_min, y_min, x_max, y_max]

    s_start = [-5,3]
    s_end = [7,2]

    window(w, ax)

    recMidPoint(w, s_start, s_end, ax)



fig, (mid) = plt.subplots(nrows=1, ncols=1)
midPoint(mid)
plt.show()
