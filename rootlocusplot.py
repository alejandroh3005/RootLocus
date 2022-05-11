import numpy as np
import sympy as sp

class RLPlotting:
    def getPoles(self): #the poles of a controller-plant system are defined as the roots of the denominator of L(s)
        return np.roots(self.denominator)

    def getZeroes(self): #the zeroes of a controller-plant system are defined as the roots of the numerator of L(s)
        return np.roots(self.numerator)

    def getAsymptote(self):  # this is the first half of Rule 3: provided the point on the Real Axis that the asymptote intersects
        return (np.sum(self.p) - np.sum(self.z)) / (self.n - self.m)

    def getThetas(self):  # this is Part 2 of Rule 3: the angles of the asymptotes with the Real Axis
        theta = [np.pi * (2 * i - 1) / (self.n - self.m) for i in range(self.n - self.m)]
        return theta

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
        zp = 0
        zz = 0
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
        n = sp.Poly.from_list(self.numerator, gens = s)
        d = sp.Poly.from_list(self.denominator, gens = s)
        L = n / d
        derivL = L.diff(s)
        breakpoints = sp.solve(derivL)
        return breakpoints

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.p = self.getPoles()
        self.z = self.getZeroes()
        self.m = len(self.p)
        self.n  = len(self.z)
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
        alpha = f"Asymptote Real Axis Intersections (\u03B1): {self.alpha}\n"
        theta = f"Asymmptote Angles (\u03B8): {self.thetas}\n"
        phis = f"Branch Departure Angles (\u03C6): {self.phis}\n"
        psis = f"Branch Arrival Angles (\u03C8): {self.psis}\n"
        bp = f"Breakout Points: {self.bp}\n"
        return num + den + m + n + p + z + alpha + theta + phis + psis + bp


if __name__ == "__main__":
    n = input("Enter numerator coefficients using space as seperator: ")
    numerator = [int(i) for i in n.split()]
    d = input("Enter denominator coefficients using space as seperator: ")
    denominator = [int(i) for i in d.split()]
    RL = RLPlotting(numerator, denominator)
    print(RL)
    
