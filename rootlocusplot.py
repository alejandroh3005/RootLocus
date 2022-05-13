import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import cmath

class RLPlotting:
    def getPoles(self):  # the poles of a controller-plant system are defined as the roots of the denominator of L(s)
        return np.roots(self.denominator)

    def getZeroes(self):  # the zeroes of a controller-plant system are defined as the roots of the numerator of L(s)
        return np.roots(self.numerator)

    def getAsymptote(self):  # this is the first half of Rule 3: provided the point on the Real Axis that the asymptote intersects
        return (np.sum(self.p) - np.sum(self.z)) / (self.n - self.m)

    def getThetas(self):  # this is Part 2 of Rule 3: the angles of the asymptotes with the Real Axis
        return np.array([np.pi * (2 * i - 1) / (self.n - self.m) for i in range(1, self.n - self.m + 1)])

    def getPhis(
            self):  # this is part 1 of rule 4: phi is defined as the departure angle that a branch forms with the horizontal as it leaves a pole
        phis = []
        poles = self.p
        pz, pp = 0, 0
        for pole in poles:
            for z in self.z:
                # sum all pole-z angles
                pz += np.angle(pole - z, deg=True)
            for p in self.p:
                # sum all pole-p angles
                pp += np.angle(pole - p, deg=True)
            # add difference of the sums +- 180 to phi
            phis.append(pz - pp)  # TODO +-180 check
            pz = pp = 0
        return phis

    def getPsis(
            self):  # this is part 2 of rule 4: psi is defined as the arrival angle a branch forms with the horizontal as it enters a zero
        psis = []
        zeros = self.z
        zp, zz = 0, 0
        for zero in zeros:
            for p in self.p:
                # sum all zero-z angles
                zp += np.angle(zero - p, deg=True)
            for z in self.z:
                # sum all pole-p angles
                zz += np.angle(zero - z, deg=True)
            # add difference of the sums +- 180 to psis
            psis.append(zp - zz)  # TODO +- 180 check
            zp = zz = 0
        return psis

    def getBreakPoints(self):
        s = sp.symbols('s')
        n = d = 0
        n = sp.Poly.from_list(self.numerator, gens=s)
        d = sp.Poly.from_list(self.denominator, gens=s)
        L = n / d
        derivL = L.diff(s)
        breakpoints = sp.solve(derivL)
        return breakpoints

    def plot(self) -> tuple:
        """
        Create and display root locus plot: a plot of critical points, branches, and asymptotes
        """
        poles = self.p
        zeros = self.z
        x = self.alpha
        bp = self.bp
        angles = self.thetas

        # create and prepare plot
        fig, ax = plt.subplots()
        ax.set_xlabel('Real')
        ax.set_ylabel('Imaginary')
        ax.axvline(x=0, color='k', lw=1)
        ax.axhline(y=0, color='k', lw=1)
        ax.grid(True, which='both')

        # draw poles as X's and zeros as O's TODO plot breakpoints
        ax.scatter(np.real(poles), np.imag(poles), marker='x')
        ax.scatter(np.real(zeros), np.imag(zeros), marker='o')
        bp_x, bp_y = [point.as_real_imag()[0] for point in bp], [point.as_real_imag()[1] for point in bp]
        ax.scatter(bp_x, bp_y, marker='+')

        # draw asymptote lines from point and angles
        for angle in angles:
            # each asymptote is broken down as a point on the Re-axis and an angle from that axis.
            # we can draw each asymptote line by connecting two endpoints
            length = 10  # length of line
            pt = cmath.rect(length, angle)  # use some clever complex math to get endpoints
            x_end = pt.real + x
            y_end = pt.imag
            plt.plot([x, x_end], [0, y_end], color='r', lw=1.5, linestyle='dotted')

        # draw branches
        colors = ['r', 'g', 'b', 'm', 'c']  # possible colors
        num, dem = np.array(self.numerator), np.array(self.denominator)
        gains = np.linspace(0.0, 100.0, num=5000)
        roots = []
        for gain in gains:
            ch_eq = dem + gain * num
            ch_roots = np.roots(ch_eq)
            ch_roots.sort()
            roots.append(ch_roots)
        # get real and imaginary values
        real_vals = np.real(roots)
        imag_vals = np.imag(roots)
        # temp_real_vals = real_vals[1:-1, :]
        # temp_imag_vals = imag_vals[1:-1, :]
        color_range = range(real_vals[1:-1, :].shape[1])
        # plot the values of each root by color
        for r, i, j in zip(real_vals[1:-1, :].T, imag_vals[1:-1, :].T, color_range):
            ax.plot(r, i, color=colors[j])
        # return generated figure
        return ax, fig

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.p = self.getPoles()
        self.z = self.getZeroes()
        self.m = len(self.z)
        self.n = len(self.p)
        self.alpha = self.getAsymptote()
        self.thetas = self.getThetas()
        self.phis = self.getPhis()
        self.psis = self.getPsis()
        self.bp = self.getBreakPoints()

    def __str__(self):
        pass  # TODO print all the things
        num = f"User input numerator coefficients: {self.numerator}\n"
        den = f"User input denominator coefficients: {self.denominator}\n"
        m = f"Number of zeros (m): {self.m}\n"
        n = f"Number of poles (n): {self.n}\n"
        p = f"Poles: {self.p}\n"
        z = f"Zeroes: {self.z}\n"
        alpha = f"Asymptote Real Axis Intersections (\u03B1): {self.alpha:.4}\n"
        theta = f"Asymptote Angles (\u03B8): {list(np.round(self.thetas, 4))}\n"
        phis = f"Branch Departure Angles (\u03C6): {self.phis}\n"
        psis = f"Branch Arrival Angles (\u03C8): {self.psis}\n"
        bp = f"Breakout Points: {self.bp}\n"
        return num + den + m + n + p + z + alpha + theta + phis + psis + bp

if __name__ == "__main__":
    n = input("Enter numerator coefficients using space as separator: ")
    numerator = [int(i) for i in n.split()]
    d = input("Enter denominator coefficients using space as separator: ")
    denominator = [int(i) for i in d.split()]

    RL = RLPlotting(numerator, denominator)
    print(RL)
    ax, fig = RL.plot()
    plt.show()