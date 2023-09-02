import numpy as np
import matplotlib.pyplot as plt
plt.axis([0, 220, 80, 0])
plt.axis('on')
dx = 10
dy = -10

plt.xticks(np.arange(0, 220, dx))
plt.yticks(np.arange(80, 0, dy))


def twowheels():
    x = [11, 11, 12, 12, 11]
    y = [47, 49, 49, 47, 47]
    plt.plot(x, y, linewidth=1, linestyle='-', color='k')
    x1 = [28, 28, 29, 29, 28]
    plt.plot(x1, y, linewidth=1, linestyle='-', color='k')


def daline():
    yourmom = [7, 50]
    yourdad = [49, 49]
    plt.plot(yourmom, yourdad, linewidth=1, color='k')


def red():
    x2 = [2, 2, 42, 42, 2]
    y2 = [9, 58, 58, 9, 9]
    plt.plot(x2, y2, linewidth=3, color='r')


def fivelines():
    x = [7, 33]
    uno = [42, 42]
    dos = [42.5, 42.5]
    tres = [45.25, 45.25]
    quattro = [45.75, 45.75]
    cinco = [46.25, 46.25]
    plt.plot(x, uno, linewidth=1, color='k')
    plt.plot(x, dos, linewidth=1, color='k')
    plt.plot(x, tres, linewidth=1, color='k')
    plt.plot(x, quattro, linewidth=1, color='k')
    plt.plot(x, cinco, linewidth=1, color='k')


def base():
    x = [9, 31]
    y = [47, 47]
    plt.plot(x, y, linewidth=1, color='k')


def flashlights():
    x1 = [7.5, 7.5, 10, 10, 7.5]
    x2 = [10, 10, 12.5, 12.5, 10]
    x3 = [27.5, 27.5, 30, 30, 27.5]
    x4 = [30, 30, 32.5, 32.5, 30]
    y = [39, 41, 41, 39, 39]
    plt.plot(x1, y, linewidth=1, color='k')
    plt.plot(x2, y, linewidth=1, color='k')
    plt.plot(x3, y, linewidth=1, color='k')
    plt.plot(x4, y, linewidth=1, color='k')

def vertical():
    x = [7, 7]
    x2 = [33, 33]
    y = [31.5, 46.3]
    plt.plot(x, y, linewidth=1, color='k')
    plt.plot(x2, y, linewidth=1, color='k')


def frontwindows():
    # ----Inner most
    xinn = [10.5, 29.5]
    yinn = [32, 32]
    plt.plot(xinn, yinn, linewidth=1, color='k')
    plt.plot([12, 10.5], [20, 32], linewidth=1, color='k')
    plt.plot([28, 29.5], [20, 32], linewidth=1, color='k')
    # ----2nd most
    xin = [10, 30]
    yin = [32.5, 32.5]
    plt.plot(xin, yin, linewidth=1, color='k')
    plt.plot([11.5, 10], [19.5, 32.5], linewidth=1, color='k')
    plt.plot([28.5, 30], [19.5, 32.5], linewidth=1, color='k')
    # ----Outer most
    x = [9.5, 30.5]
    y = [33, 33]
    plt.plot([11, 9.5], [19, 33], linewidth=1, color='k')
    plt.plot([29, 30.5], [19, 33], linewidth=1, color='k')
    plt.plot(x, y, linewidth=1, color='k')


def windowcurves():
    # lowestcurve
    x_offset = 20
    y_offset = 20
    a = 8
    b = 1
    p1 = 0 * np.pi / 180
    p2 = 180 * np.pi / 180
    dp = (p2 - p1) / 180.
    xplast = 28
    yplast = 20

    for p in np.arange(p1, p2 + dp, dp):
        if (np.tan(p) ** 2.) != 0:
            xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
            yp = -np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
            if p > np.pi / 2:
                xp = -xp

            plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=1, color='k')
            xplast = xp + x_offset
            yplast = yp + y_offset

    # middle curve
    x_offset = 20
    y_offset = 19.5
    a = 8.5
    b = 1
    p1 = 0 * np.pi / 180
    p2 = 180 * np.pi / 180
    dp = (p2 - p1) / 180.
    xplast = 28.5
    yplast = 19.5

    for p in np.arange(p1, p2 + dp, dp):
        if (np.tan(p) ** 2.) != 0:
            xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
            yp = -np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
            if p > np.pi / 2:
                xp = -xp

            plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=1, color='k')
            xplast = xp + x_offset
            yplast = yp + y_offset

    # top curve
    x_offset = 20
    y_offset = 19
    a = 9
    b = 1
    p1 = 0 * np.pi / 180
    p2 = 180 * np.pi / 180
    dp = (p2 - p1) / 180.
    xplast = 29
    yplast = 19

    for p in np.arange(p1, p2 + dp, dp):
        if (np.tan(p) ** 2.) != 0:
            xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
            yp = -np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
            if p > np.pi / 2:
                xp = -xp

            plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=1, color='k')
            xplast = xp + x_offset
            yplast = yp + y_offset


def straightlowercurve():
    plt.plot([31, 33], [47, 46.3], linewidth=1, color='k')
    plt.plot([9, 7], [47, 46.3], linewidth=1, color='k')


def curvedidagonals():
    plt.plot([8, 7], [18.15, 31.5], linewidth=1, color='k')
    plt.plot([33, 32], [31.5, 18.15], linewidth=1, color='k')


def roofellipse():
    x_offset = 20
    y_offset = 18.3
    a = 12
    b = 3.15
    p1 = 0 * np.pi / 180
    p2 = 180 * np.pi / 180
    dp = (p2 - p1) / 180.
    xplast = 32.1
    yplast = 19.29255201942563

    # print(np.arange(p1,p2+dp,dp))
    for p in np.arange(p1, p2 + dp, dp):
        if (np.tan(p) ** 2.) != 0:
            xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
            yp = -np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
            if p > np.pi / 2:
                xp = -xp

                # Line below print in POS y quadrant
            plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=1, color='k')
            # print('POS:', 'P1:', xplast, yplast, 'P2:', xp, yp, )
            xplast = xp + x_offset
            yplast = yp + y_offset


def lowerellipseroof():
    x_offset = 20
    y_offset = 19.5
    a = 12
    b = 1.5
    p1 = 0 * np.pi / 180
    p2 = 180 * np.pi / 180
    dp = (p2 - p1) / 180.
    xplast = 32.14
    yplast = 20.038


    for p in np.arange(p1, p2 + dp, dp):
        if (np.tan(p) ** 2.) != 0:
            xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
            yp = -np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
            if p > np.pi / 2:
                xp = -xp

                # Line below print in POS y quadrant
            plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=1, color='k')
            # print([xplast, xp + x_offset], [yplast, yp + y_offset])
            xplast = xp + x_offset
            yplast = yp + y_offset

def colortime():
    x_offset = 20
    y_offset = 18.3
    a = 12
    b = 3.15
    p1 = 0 * np.pi / 180
    p2 = 180 * np.pi / 180
    dp = (p2 - p1) / 1000.
    xplast = 32.1
    y1plast = 19.29255201942563

    c = 9
    d = 1

    for p in np.arange(p1, p2 + dp, dp):
        if (np.tan(p) ** 2.) != 0:
            xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
            yp = -np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
            y2p = np.abs(c * d * (c * c + d * d / (np.tan(p) ** 2.)) ** -.5)
            if p > np.pi / 2:
                xp = -xp
            plt.fill([xplast, xp + x_offset], [y1plast, yp + y_offset], linewidth=3, color='k')
            xplast = xp + x_offset
            y1plast = y2p + y_offset

    plt.fill([7.9,8,8.8,7.9],[19.5,18.5,18.9,19.5], color = 'k')
    plt.fill([31.1,32.13,32,31.1], [19, 19.5, 18.5, 19], color='k')
    plt.fill([32.1,33,33,30.5,29,30,31,32.1],[19.5,31.5,33,33,18.5,18.65,18.9,19.5], color = 'b')
    plt.fill([8, 7, 7, 9.5, 11, 9,8.333,8], [19.5, 31.5, 33, 33, 18.5,18.9, 19.153,19.5], color='b')
    plt.fill([11, 9.5, 30.5, 29,27.3,24.5, 20,15.5,12.4, 11], [18.5, 33, 33, 18.5,18.3,18.1,18,18.1,18.3, 18.5], color='y')
    plt.fill([12,10.5,29.5,28,26,24,22,20,18,16,14,12], [20,32,32,20,19.3,19.2,19.1,19,19.1,19.2,19.3,20], color = 'grey')
    plt.fill([7,7,33,33,7], [33,46.3,46.3,33,33], color = 'b')
    plt.fill([7,7,33,33,7],[45.25,46.25,46.25,45.25,45.25],color = 'red')
    plt.fill([7.5, 7.5, 12.5, 12.5, 7.5],[39, 41, 41, 39, 39],color = 'y')
    plt.fill([27.5, 27.5, 32.5, 32.5, 27.5], [39, 41, 41, 39, 39], color='y')
    plt.fill([11, 11, 12, 12, 11],[47, 49, 49, 47, 47], color = 'k')
    plt.fill([28, 28, 29, 29, 28],[47, 49, 49, 47, 47], color = 'k')
    plt.fill([7,7,33,33,7],[42.5,42,42,42.5,42.5], color = 'grey')
    plt.fill([7,7,33,33,7],[45.25,42.5,42.5,45.25,45.25], color = 'b')
    plt.fill([7,9,31,33,7],[46.3,47,47,46.3,46.3], color = 'b')

twowheels()
daline()
red()
fivelines()
base()
flashlights()
vertical()
straightlowercurve()
frontwindows()
windowcurves()
curvedidagonals()
roofellipse()
lowerellipseroof()
colortime()
plt.show()
