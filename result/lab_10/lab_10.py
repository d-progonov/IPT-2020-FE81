import matplotlib.pyplot as plt
from matplotlib import pylab
from matplotlib.widgets import Button, Slider, RadioButtons
from numpy import arange
from random import uniform
from math import sin, pi

def pryam(x):
    if x<1 or x>2:
        return 0
    else:
        return 1

def sinus(x):
    if x<0 or x>pi:
        return 0
    else:
        return sin(x)

def pryamPlot():
    xlist = arange(0, 5.0, 0.01)
    ylist = [pryam(x) for x in xlist]
    return [xlist, ylist]

def noisePlot(tau, lvlomega):
    xlist = arange(tau, tau + 5, 0.01)
    ylist = [uniform(-lvlomega,lvlomega) for x in xlist]
    return [xlist, ylist]

def sinPlot():
    xlist = arange(0, 5.0, 0.01)
    ylist = [sinus(x) for x in xlist]
    return [xlist, ylist]

def update(label):
    if label == "Прямоугольный":
        menu.clear()
        pr=pryamPlot()
        menu.plot(pr[0], pr[1])
        menu.grid()
        pylab.draw()
    if label == "Синус":
        menu.clear()
        pr=sinPlot()
        menu.plot(pr[0], pr[1])
        menu.grid()
        pylab.draw()

def onRadioButtonsClicked(label):
        update(label)

if __name__ == '__main__':
    def onButtonConfirmClicked(event):
        global slider_tau
        global slider_mu
        global slider_lvlomega
        global menu
        fig, ax = pylab.subplots()

        pylab.subplot(3, 1, 1)
        if radiobuttons_type.value_selected == 'Прямоугольный':
            pr = pryamPlot()
        if radiobuttons_type.value_selected == 'Синус':
            pr = sinPlot()
        plt.plot(pr[0], pr[1])
        plt.ylim(-1,3)
        plt.grid()
        plt.title('Input signal')

        pylab.subplot(3, 1, 2)
        no = noisePlot(slider_tau.val, slider_lvlomega.val)
        plt.plot(no[0], no[1])
        plt.ylim(-1,3)
        plt.grid()
        plt.title('Additive noise signal')

        pylab.subplot(3, 1, 3)
        ou_y = []
        for i in range(0,500):
            ou_y.append(pr[1][i]*slider_mu.val + no[1][i])
        plt.plot(no[0], ou_y)
        plt.ylim(-1,3)
        plt.grid()
        plt.title('Output signal')

        fig.subplots_adjust(hspace = 0.7)
        pylab.show()

    fig, menu = pylab.subplots()
    update("Прямоугольный")

    fig.subplots_adjust(left=0.07, right=0.95, top=0.9, bottom=0.4)

    axes_button_Confirm = pylab.axes([0.7, 0.05, 0.25, 0.075])
    button_Confirm = Button(axes_button_Confirm, 'Confirm')
    button_Confirm.on_clicked(onButtonConfirmClicked)

    axes_slider_tau = pylab.axes([0.05, 0.25, 0.85, 0.04])
    slider_tau = Slider(axes_slider_tau,
                          label='τ',
                          valmin=0.0,
                          valmax=200.0,
                          valinit=0.0,
                          valfmt='%1.2f')
    axes_slider_mu = pylab.axes([0.05, 0.20, 0.85, 0.04])
    slider_mu = Slider(axes_slider_mu,
                       label='μ',
                       valmin=0.0,
                       valmax=1.0,
                       valinit=1.0,
                       valfmt='%1.2f')
    axes_slider_lvlomega = pylab.axes([0.05, 0.15, 0.85, 0.04])
    slider_lvlomega = Slider(axes_slider_lvlomega,
                       label='lvl',
                       valmin=0.0,
                       valmax=1.0,
                       valinit=0.0,
                       valfmt='%1.2f')

    axes_radiobuttons = pylab.axes([0.05, 0.012, 0.27, 0.12])

    radiobuttons_type = RadioButtons(axes_radiobuttons, ['Прямоугольный', 'Синус'])
    radiobuttons_type.on_clicked(onRadioButtonsClicked)

    pylab.show()