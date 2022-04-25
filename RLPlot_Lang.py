import numpy as np
import sympy as sp
class RLPlotting:

    def getPoles(self): #the poles of a controller-plant system are defined as the roots of the denominator of L(s)
        self.n = len(self.p)
        return np.roots(self.d)

    def getZeroes(self): #the zeroes of a controller-plant system are defined as the roots of the numerator of L(s)
        self.n = len(self.z)
        return np.roots(self.n)

    def getAsymptote(self): #this is the first half of Rule 3: provided the point on the Real Axis that the asymptote intersects
        return (np.sum(self.p) - np.sum(self.z)) / (self.n - self.m)

    def getThetas(self): #this is Part 2 of Rule 3: the angles of the asymptotes with the Real Axis
        theta = [np.pi * (2 * i - 1) / (self.n - self.m) for i in range(self.n - self.m)]
        return theta

    # TODO finish phi
    def getPhis(self): #this is part 1 of rule 4: phi is defined as the departure angle that a branch forms with the horizontal as it leaves a pole
        phis = []
        poles = self.p
        for pole in poles:
            for z in self.z:
                #sum all pole-z angles
            for p in self.p:
                pass
                #sum all pole-p angles
            #add difference of the sums +- 180 to phi
        return phis

    # TODO finish psi
    def getPsis(self): #this is part 2 of rule 4: psi is defined as the arrival angle a branch forms with the horizontal as it enters a zero
        psis = []
        zeros = self.z
        for zero in zeros:
            for z in self.z:
                #sum all pole-z angles
            for p in self.p:
                #sum all pole-p angles
            #add difference of the sums +- 180 to phi
        return psis

    def GetBreakPoints(self):
        s = sp.symbols('s')
        for coeff, i in enumerate(self.numerator):
            n += coeff * s ** (self.m - i)
        for coeff, i in enumerate(self.denominator):
            d += coeff * s ** (self.n - i)
        L = n / d
        derivL = L.diff(s)
        breakpoints = None # TODO extract coeff from derivL, pass through np.roots()
        return breakpoints
    def __init__(self, numerator[], denominator[]):
        self.numerator = numerator
        self.denominator = denominator
        self.m = 0
        self.n = 0
        self.p = self.getPoles()
        self.z = self.getZeroes()
        self.alpha = self.getAsymptote()
        self.thetas = self.getThetas()
        self.phis = self.getPhis()
        self.psis = self.getPsis()
    
    