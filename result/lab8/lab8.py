import matplotlib.pyplot as plt
import numpy as np

def get_limits():
    try:
        left = float(input('Left limit of x = '))
        right = float(input('Right limit of x = '))
        if right - left > 0 and right - left <= 2000:
            return (left, right)
        else:
            print('Bad input! Using default [-10;10]')
            return (-10, 10)
    except:
        print('Bad input! Using default [-10;10]')
        return (-10, 10)

def get_points(ox, new_ox, new_oy, pos):
    if ox[pos] > 0:
        y1 = np.sqrt( (ox[pos]-1) ** 4 )
        y2 = -1 * y1
        new_ox.append(ox[pos])
        new_oy.append(y1)
        new_ox.append(ox[pos])
        new_oy.append(y2)
    elif ox[pos] <= 0:
        y3 = np.sqrt( (ox[pos]+1) ** 4 )
        y4 = -1 * y3
        new_ox.append(ox[pos])
        new_oy.append(y3)
        new_ox.append(ox[pos])
        new_oy.append(y4)

    if len(ox) - 1 != pos:
        return True
    else:
        return False


def main():
    left, right = get_limits()
    ox, oy = [],[]
    x = np.arange(left, right, 0.001).tolist()
    pos = 0
    while get_points(x, ox, oy, pos):
        pos += 1
    plt.plot(ox, oy)
    plt.show()


main()
