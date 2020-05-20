#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
import math
import matplotlib.pyplot as plt
import numpy as np
def drawPlot(cmd):
    try:
        tmin, tmax, a = [float(x) for x in cmd.split(' ')]
        if a <= 0:
            print('a should be > 0')
            return
        t = np.arange(tmin, tmax, 0.001)
        x = np.true_divide(a * np.power(t, 2), 1 + np.power(t, 2))
        y = np.true_divide(a * np.power(t, 3), 1 + np.power(t, 2))
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.minorticks_on()
        plt.grid(True)
        plt.ylabel('$y={0}*t^3/(1+t^2)$'.format(a), size=8,
            fontweight='bold')
        plt.xlabel('$x={0}*t^2/(1+t^2)$'.format(a), position=(1,0), size=8,
            fontweight='bold')
        [ax.spines[location].set_position('zero') for location in ['left', 'bottom', 'top', 'right']]
        plt.plot(x, y, 'b.-')
        plt.show()
    except Exception as e:
        print(e)

def main():
    print("Hello! Enter 3 numbers (tmin, tmax, a) separated by spaces\n\n")
    while True:
        try:
            cmd = input("Enter tmin, tmax, a > ").strip()
            if cmd != '':
                drawPlot(cmd)
        except EOFError or KeyboardInterrupt:
            print('Goodbye.')
            exit(0)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
