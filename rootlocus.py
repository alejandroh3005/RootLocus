# Authors: Alejandro Hernandez, Maya Tene
# Created on 4/20/2022

import cmath
import numpy as np
import matplotlib.pyplot as plt
"""
Methods:
        Find Poles and Zeroes
            -return poles[], Zeroes[]
        Rule1():
            -nas n branches starting from n poles (len(poles))
            -m of those approach m zeroes(len(zeros))
            -n-m approach infinity
        Rule2():
            -breakout point left of odd # of p,z
        Rule3():
            -find asymptote intersect with real axis
            -find asymptote angle
        -if n-m = 1, infinity branch approaches opposite sign of alpha * inf on real axis
        Rule4():
            -departure angle of every zero
        - m arrival angles
    Rule5():
        -where breakout points are definitively
"""

def get_characteristic_eq() -> np.vstack:  # PF: parameter/return type hints
    """
    This wil eventually take user-entered coefficients and pad them
    :return:
    """
    # set characteristic equation
    # these examples are from the notes you shared today
    set1 = [[0, 0, 1, 1], [1, 2, 9, 18]]
    set2 = [[0, 0, 0, 1], [1, -1, 1, -1]]
    set3 = [[0, 1, 3], [1, 3, 2]]
    numerator = np.array(set3[0])
    denominator = np.array(set3[1])
    return np.vstack((numerator, denominator))  # why use vstacks? why not?


def get_roots(coefficients:np.vstack) -> tuple:
    """
    I was thinking maybe using some other method but this is so convenient and there's no reason
    to reinvent a (very fancy) wheel
    :param coefficients:
    :return:
    """
    # includes all imaginary roots and super easy to work with
    numerator_roots, denominator_roots = np.roots(coefficients[0]), np.roots(coefficients[1])  # PF: single-line multi-assignment
    return numerator_roots, denominator_roots  # aka zeros and poles  # PF: multiple returns sent as a tuple


def get_asymptotes(roots:tuple) -> tuple:
    """
    I hate how long it took me to finally get this correct & concise :( much wallowing from this part
    :param roots
    :return:
    """
    zeros, poles = roots  # PF: tuple unpacking
    n,m = len(poles), len(zeros)
    # find asymptote point and angles
    # Fun fact: I believe there is only 1 point shared by all asymptotes. I couldn't an example online where this wasn't true
    asymptote_point = (np.sum(poles) - np.sum(zeros)) / (n - m)
    asymptote_angles = [np.pi * (2*i - 1) / (n-m) for i in range(1,n-m+1)]  # PF: comprehensive list
    return asymptote_point, np.array(asymptote_angles)


def plot_root_locus(roots:tuple, asymptotes:tuple) -> None:
    # create and prepare plot
    fig, ax = plt.subplots()
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.axvline(x=0, color='k', lw=1)
    ax.axhline(y=0, color='k', lw=1)
    ax.set_ylim([-5,5])
    ax.set_xlim([-5,5])
    ax.grid(True, which='both')

    # draw poles and zeros
    zeros, poles = roots
    ax.scatter(np.real(poles), np.imag(poles), marker='x')  # whenever you see 'imag', it's getting the coeffs of the imaginary numbers
    ax.scatter(np.real(zeros), np.imag(zeros), marker='o')  # roots (poles/zeros) are just X's and Y's we can plot

    # draw asymptotes from point and angles
    x, angles = asymptotes
    for angle in angles:
        # each asymptote is broken down as a point on the Re-axis and an angle from that axis.
        # we can draw each asymptote one-by-one by connecting points
        length = 10  # length of asymptote line
        pt = cmath.rect(length, angle)  # use some clever complex math to get end points
        x_end = pt.real + x
        y_end = pt.imag
        plt.plot([x,x_end],[0,y_end], color='r',lw=1.5, linestyle='dotted')
    plt.show()


if __name__ == "__main__":
    coeff = get_characteristic_eq()
    rts = get_roots(coefficients=coeff)  # roots = poles and zeros
    asy = get_asymptotes(roots=rts)  # asymptotes = point and angles
    plot_root_locus(roots=rts, asymptotes=asy)