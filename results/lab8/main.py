#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle
import math
import matplotlib.pyplot as plt
import numpy as np  

def interpret(cmd):
  try:
    xmin, xmax, a, b = [float(x) for x in cmd.split(' ')]
    x = np.arange(xmin, xmax, 0.001)
    y = a*np.sin(b*x)

    fig = plt.figure()#figsize=(5, 2))
    ax = fig.add_subplot(111)
    ax.minorticks_on()
    plt.grid(True)
    plt.ylabel('${0} \cdot sin({1} \cdot x)$'.format(a, b), position=(0,1), size=20, fontweight='bold', rotation='horizontal')
    plt.xlabel('$x$', position=(1,0), size=20, fontweight='bold',)
    [ax.spines[location].set_position('zero') for location in ['left', 'bottom', 'top', 'right']]

    plt.plot(x, y, 'b.-')
    plt.show()
  except Exception as e:
    handle(e)

def main():
  print("Enter 4 numbers (xmin, xmax, a, b) separated by spaces\n\n")
  while True:
    try:
      cmd = input("lab8> ").strip()
      if cmd != '':
        interpret(cmd)
    
    except EOFError or KeyboardInterrupt:
      print('Bye!')
      exit(0)
    except Exception as e:
      handle(e)

if __name__ == "__main__":
  main()
