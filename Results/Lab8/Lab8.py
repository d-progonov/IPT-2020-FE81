import matplotlib.pyplot as plt
import numpy as np

def graph1(x, y, fun):
    ans1 = []
    ans2 = []
    for i in range(len(x)):
        for j in range(len(y)):
            if y[j]< fun[i]:
                ans1.append(x[i])
                ans2.append(y[j])
    return ans1, ans2

def graph2(x, y, fun):
    ans1 = []
    ans2 = []
    for i in range(len(x)):
        for j in range(len(y)):
            if y[j] >= fun[i] and y[j] >= -1*fun[i]:
                ans1.append(x[i])
                ans2.append(y[j])
    return ans1, ans2

x = np.linspace(-10, 10, 501)
y = np.linspace(-5, 10, 501)


y01 = (x**2)/2
ans11, ans12 = graph1(x, y, y01)

y02 = x
ans21, ans22 = graph2(x, y, y02)

plt.plot(ans11,ans12,"ro-")
plt.show()

plt.plot(ans21,ans22,"bo-")
plt.show()
