# Authors: Alejandro Hernandez, Maya Tene
# Last updated: 5/4/2022
import cmath
import numpy as np
import matplotlib.pyplot as plt

def get_characteristic_eq() -> np.vstack:  # PF: parameter/return type hints
    """
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

def compute_critical_points(coefficients:np.vstack) -> tuple:
    """
    :param coefficients:
    :return:
    """
    # includes all imaginary roots and super easy to work with
    numerator_roots, denominator_roots = np.roots(coefficients[0]), np.roots(coefficients[1])  # PF: single-line multi-assignment
    return numerator_roots, denominator_roots  # aka zeros and poles  # PF: multiple returns sent as a tuple


def get_asymptotes(critical_points:tuple) -> tuple:
    """
    :param critical_points:
    :return:
    """
    zeros, poles = critical_points  # PF: tuple unpacking
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
    crt_pts = compute_critical_points(coefficients=coeff)  # roots = poles and zeros
    asymp = get_asymptotes(critical_points=crt_pts)  # asymptotes = point and angles

    # create a list of evenly spaced gains
    gains = np.linspace(0.0, 10.0, num=1000)

    plot_root_locus(roots=crt_pts, asymptotes=asymp)