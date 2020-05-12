import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


class Inequality:
    def __init__(self, func, pred, param, frm, to, step=0.001):
        self.step = step
        self.to_x = to
        self.func = func
        self.pred = pred
        self.param = param
        self.from_x = frm

    def to_data(self):
        out = []
        xs = []
        ys = []
        for x in np.arange(self.from_x, self.to_x, self.step):
            res = self.func(x)
            if self.pred(res, self.param):
                xs.append(x)
                ys.append(res)
            else:
                if xs:
                    out.append((xs, ys))
                    xs = []
                    ys = []

        out.append((xs, ys))
        return out


class Plot:
    def __init__(self, ax, ineq, color):
        self.ineq = ineq
        self.color = color
        self.plots = []
        self.ax = ax
        self.update_axes()


    def update_axes(self):
        for p in self.plots: p.remove()
        self.plots = []

        data = self.ineq.to_data()
        for x, y in data:
            l, = self.ax.plot(x, y, color=self.color)
            self.plots.append(l)

    def change_param(self, field_name, data):
        setattr(self.ineq, field_name, data)
        self.update_axes()


def field(fig, name, field_name, plots, left, bottom, width=0.1, height=0.075):
    axbox = plt.axes([left, bottom, width, height])
    text_box = TextBox(axbox, name, initial=str(getattr(plots[0].ineq, field_name)))

    def on_submit(text):
        for p in plots:
            p.change_param(field_name, float(text))
        fig.canvas.draw()

    text_box.on_submit(on_submit)
    return text_box


def fields(fig, plots):
    out = [field(fig, 'From: ', 'from_x', plots, 0.3, 0.9),
           field(fig, 'To: ', 'to_x', plots, 0.5, 0.9),
           field(fig, 'y: ', 'param', plots, 0.7, 0.9)]
    return out


def main():
    init_from = -10
    init_to = 10
    init_step = 0.01
    init_param = 5
    ineq1 = Inequality(lambda x: x ** 2 - 4 * x + 3, lambda res, y: y >= res, init_param,
                       init_from, init_to, init_step)
    ineq2 = Inequality(lambda x: x ** 2 + 4 * x + 3, lambda res, y: y < res,
                       init_param, init_from, init_to, init_step)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    p1 = Plot(ax, ineq1, 'red')
    p2 = Plot(ax, ineq2, 'blue')
    f = fields(fig, [p1, p2])

    ax.axhline(linewidth=0.6, color='black')
    ax.axvline(linewidth=0.6, color='black')
    ax.grid(True)
    ax.set_xlabel('x')
    ax.set_ylabel('y', rotation='horizontal')
    ax.legend((p1.plots[0], p2.plots[0]), ('y ≥ x^2-4x+3', 'y < x^2+4x+3'))
    plt.show()


if __name__ == '__main__':
    main()
