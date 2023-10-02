
"""
In this project, I compute radiative 2-loop QCD corrections to the process q qb -> g W H -> g l nub H
After quark-antiquark (q and qb) collision a gluon (g), a vector boson (W) and a Higgs (H) appear with subsequent decay of the vector boson into a lepton-antinuetrino (l and nub) pair)
As a result I obtain 2-loop squared amplitude for this process, which allows to compute the cross section measured in CERN (at the Long Hanron Collider)
"""

# PROCESS
# q(p1) + qb(p2) -> e(p3) + nub(p4) + g(p5)

import math, cmath
import numpy as np
from mpmath import *

print("Process: q(p1) + qb(p2) -> g V H -> l(p3) + nub(p4) + g(p5) + H(pH)")
print()

print("-----------------------------------------")
print("PRELIMINARY COMPUTATIONS")
print("-----------------------------------------")

# PARAMETERS (various high energy physics constants used for calculations)
mW = 80.41900
#mW = 80.399000000000001         # W-boson mass
mZ = 91.1876                    # Z-boson mass
mH = 125.00000000000000         # Higgs boson mass 
#Gamma_W = 2.1053999999999999    # W-decay width
Gamma_W = 2.047600
gw2 =0.42650101674334384        # squared electroweak coupling
vev = 246.21845810181634        # vacuum expectation value
musq = 76881.92903248549        # square of the energy scale
mu = math.sqrt(musq)            # energy scale
alpha_s = 1                     # strong coupling
Cf = 4/3                        # Casimir operator of SU(3)
Nc = 3                          # number of colors
C = 1                           # Wilson coefficients
D = 1

# External Momenta
p1 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]     # antiquark
p3 = [86.94997640526997900, -21.701022816585411,  39.355542645382108, -74.434570386874427]       # lepton
p4 = [322.3919309874294800, -101.97160213731860, -296.47360464823691,  75.111592116216357]     # antinuetrino
p5 = [149.6028751502909100, -103.96621515693120, -95.942663470338033,  48.652355394098521]    # gluon
pH = [441.0552174570096900,  227.63884011083519,  353.06072547319292, -49.329377123440487]      # Higgs boson

print("External Momenta:")
print("p1 = [", p1[0], ",", p1[1], ",", p1[2], ",", p1[3], "] (quark)")
print("p2 = [", p2[0], ",", p2[1], ",", p2[2], ",", p2[3], "] (antiquark)")
print("p3 = [", p3[0], ",", p3[1], ",", p3[2], ",", p3[3], "] (lepton)")
print("p4 = [", p4[0], ",", p4[1], ",", p4[2], ",", p4[3], "] (antinuetrino)")
print("p5 = [", p5[0], ",", p5[1], ",", p5[2], ",", p5[3], "] (gluon)")
print("pH = [", pH[0], ",", pH[1], ",", pH[2], ",", pH[3], "] (Higgs)")
print()


# check of the momentum conservation law: p1 + p2 = p3 + p4 + p5 + pH

sumP = []
i = 0
while i < 4:
    sumP.append(p1[i] + p2[i] - p3[i] - p4[i] - p5[i] - pH[i])
    i += 1
sumPround = []
for i in sumP:
    sumPround.append(round(i, 12))

print("Momentum conservation law:")
print("p1 + p2 - p3 - p4 - p5 - pH = ", sumPround)
print()


# check of squared momenta: p1^2 = 0, p2^2 = 0, p3^2 = 0, p4^2 = 0, p5^2 = 0, pH^2 = mH^2 (all particles are massless except for the Higgs boson)
# to obtain squared momenta the Minkowski metrics (1, -1, -1, -1) is used

p1sq = p1[0]**2 - p1[1]**2 - p1[2]**2 - p1[3]**2
p2sq = p2[0]**2 - p2[1]**2 - p2[2]**2 - p2[3]**2
p3sq = p3[0]**2 - p3[1]**2 - p3[2]**2 - p3[3]**2
p4sq = p4[0]**2 - p4[1]**2 - p4[2]**2 - p4[3]**2
p5sq = p5[0]**2 - p5[1]**2 - p5[2]**2 - p5[3]**2
pHsq = pH[0]**2 - pH[1]**2 - pH[2]**2 - pH[3]**2

print("Squared momenta:")
print("p1^2 = ", round(p1sq, 10))
print("p2^2 = ", round(p2sq, 10))
print("p3^2 = ", round(p3sq, 10))
print("p4^2 = ", round(p4sq, 10))
print("p5^2 = ", round(p5sq, 10))
print("pH^2 = ", round(pHsq, 10))
print("mH^2 = ", round(mH**2, 10))
print()

O = np.array([[0], [0], [0], [0]])  # just a zero-vector for comfort notation
p1 = np.array([[p1[0]], [p1[1]], [p1[2]], [p1[3]]]) # quark
p2 = np.array([[p2[0]], [p2[1]], [p2[2]], [p2[3]]]) # antiquark
p3 = np.array([[p3[0]], [p3[1]], [p3[2]], [p3[3]]]) # electron
p4 = np.array([[p4[0]], [p4[1]], [p4[2]], [p4[3]]]) # electron antinuetrino
p5 = np.array([[p5[0]], [p5[1]], [p5[2]], [p5[3]]]) # gluon


# Define external momenta as a matrix 4x6, where the 0-th line consists of zeros (just for convenience of notation)
p = np.hstack((O, p1, p2, p3, p4, p5))

# Define scalar products of momenta as a matrix sij = 2(pi*pj)
print("Mandelstam Variables: sij = 2(pi*pj)")
s = np.zeros((6,6)) # create a 6x6 matrix of zeros
i = 1
j = 1
while i < 6:
    while j < 6:
        if i != j:
            s[i,j] = 2*(p[0,i]*p[0,j] - p[1,i]*p[1,j] - p[2,i]*p[2,j] - p[3,i]*p[3,j]) # fill in the elements of the matrix
            print("s",i,j, "=", s[i,j]) # print the elements of the matrix
        j += 1
    i += 1
    j = 1
print()


# Define a matrix of spinors U_+(pi)
Uplus = np.array([[0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j]])
#print(Uplus)
Uplus[0,1] = 1j*math.sqrt(2*abs(p[0,1]))
Uplus[1,2] = 1j*math.sqrt(2*abs(p[0,2]))
j = 3
while j < 6:
    Uplus[0,j] = math.sqrt(p[0,j] + p[3,j])
    Uplus[1,j] = (p[1,j] + 1j*p[2,j])/math.sqrt(p[0,j] + p[3,j])
    j += 1
#print("Matrix of spinors U_+(pi)")
#print(Uplus)


# Define a matrix of spinors U_-(pi)
Uminus = np.array([[0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j]])
#print(Uminus)
Uminus[3,1] = -1j*math.sqrt(2*abs(p[0,1]))
Uminus[2,2] = 1j*math.sqrt(2*abs(p[0,2]))
j = 3
while j < 6:
    Uminus[2,j] = (p[1,j] - 1j*p[2,j])/math.sqrt(p[0,j] + p[3,j])
    Uminus[3,j] = -math.sqrt(p[0,j] + p[3,j])
    j += 1
#print("Matrix of spinors U_-(pi)")
#print(Uminus)


# Define a matrix of spinors [U_+]bar(pi)
Uplusbar = np.array([[0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j]])
#print(Uplusbar)
Uplusbar[1,2] = 1j*math.sqrt(2*abs(p[0,1]))
Uplusbar[2,3] = 1j*math.sqrt(2*abs(p[0,2]))
i = 3
while i < 6:
    Uplusbar[i,2] = math.sqrt(p[0,i] + p[3,i])
    Uplusbar[i,3] = (p[1,i] - 1j*p[2,i])/math.sqrt(p[0,i] + p[3,i])
    i += 1
#print("Matrix of spinors [U_+]bar(pi)")
#print(Uplusbar)


# Define a matrix of spinors [U_-]bar(pi)
Uminusbar = np.array([[0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j]])
#print(Uminusbar)
Uminusbar[1,1] = -1j*math.sqrt(2*abs(p[0,1]))
Uminusbar[2,0] = 1j*math.sqrt(2*abs(p[0,2]))
i = 3
while i < 6:
    Uminusbar[i,0] = (p[1,i] + 1j*p[2,i])/math.sqrt(p[0,i] + p[3,i])
    Uminusbar[i,1] = -math.sqrt(p[0,i] + p[3,i])
    i += 1
#print("Matrix of spinors [U_-]bar(pi)")
#print(Uminusbar)


# Define a matrix of spinor products A_(ij) = <pipj>
print("Spinor products <pipj>:")
A = np.array([[0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j]])
#print(A)
i = 1;
j = 1;
while i < 6:
    while j < 6:
        if i != j:
            A[i,j] = Uminusbar[i,0] * Uplus[0,j] + Uminusbar[i,1] * Uplus[1,j] + Uminusbar[i,2] * Uplus[2,j] + Uminusbar[i,3] * Uplus[3,j]
            print("< p", i, "p", j, "> = ", A[i,j])
        j += 1
    i += 1
    j = 1
#print(A)
print()


# Define a matrix of spinor products S_(ij) = [pipj]
print("Spinor products [pipj]:")
S = np.array([[0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j]])
#print(S)
i = 1;
j = 1;
while i < 6:
    while j < 6:
        if i != j:
            S[i,j] = Uplusbar[i,0] * Uminus[0,j] + Uplusbar[i,1] * Uminus[1,j] + Uplusbar[i,2] * Uminus[2,j] + Uplusbar[i,3] * Uminus[3,j]
            print("[ p", i, "p", j, "] = ", S[i,j])
        j += 1
    i += 1
    j = 1
#print(S)
print()




                                                                                        # LEADING ORDER (TREE LEVEL)
                                                                                        
                # Particle order: quark(p1), antiquark(p2), lepton(p3), antinuetrino(p4), gluon(p5)

print("-----------------------------------------")
print("LEADING ORDER (TREE LEVEL)")
print("-----------------------------------------")

# Tree-level form factors
print("Tree-level form factors:")
FFtree = [0, (2*s[1,2] + s[1,5] + s[2,5])/(s[1,2]*s[1,5]), 0, -(s[1,5] + s[2,5])/(s[1,2]*s[1,5]), (s[1,5] + s[2,5])/(s[1,2]*s[2,5]), (-s[1,5] + s[2,5])/(s[1,5]*s[2,5]), 0, 0, -2*(s[1,5] + s[2,5])/(s[1,2]*s[1,5]*s[2,5]), 0, 0, 0, (s[1,5] - s[2,5])/(s[1,5]*s[2,5]), 0]
i = 1
while i < 14:
    print("FF_tree[", i, "] =", FFtree[i])
    i += 1
print()



# Tree-level helicity amplitudes: M[quark, antiquark, gluon] (after W-boson decay lepton and antinuetrino are always left-handed)
MLLLtree = 1/2*1/S[5,2]*(2*FFtree[1]*A[1,3]*S[4,2]*S[2,1]*A[1,5] + FFtree[6]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,1]*S[1,4] + FFtree[8]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,2]*S[2,4] + FFtree[10]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,5]*S[5,4] + 2*FFtree[12]*A[1,5]*S[5,2]*S[2,4]*A[3,5])
MLLRtree = -1/2*1/A[5,2]*(2*FFtree[1]*A[1,3]*S[4,2]*A[2,1]*S[1,5] + 2*FFtree[3]*A[1,2]*S[5,2]*A[3,1]*S[1,4] + 2*FFtree[4]*A[1,2]*S[5,2]*A[3,2]*S[2,4] + 2*FFtree[5]*A[1,2]*S[5,2]*A[3,5]*S[5,4] + FFtree[6]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,1]*S[1,4] + FFtree[8]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,2]*S[2,4] + FFtree[10]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,5]*S[5,4] + 2*FFtree[12]*A[1,5]*S[5,2]*A[2,3]*S[4,5] + 4*FFtree[13]*A[1,3]*S[4,5]*A[5,2]*S[5,2])

print("Tree-level helicity amplitudes:")
print("M(L,L,L)_tree = ", MLLLtree)
print("M(L,L,R)_tree = ", MLLRtree)
print()


# Additional global factor: G = gw^3 * mw/sqrt(2) * Prop
Prop1 = 1/(s[1,2] - mW**2 + mW*Gamma_W*1j)  # first weak boson propagator
Prop2 = 1/(s[3,4] - mW**2 + mW*Gamma_W*1j)  # second weak boson propagator
EW = gw2**(3/2) * mW/math.sqrt(2)           # vertex constant
G = Prop1 * Prop2 * EW                      # global factor
print("Global factor G = gw^3 * mW/sqrt(2)/(s34 - mW^2 + i*mW*Г_W)/(s12 - mW^2 + i*mW*Г_W) =", G)


# Tree-level amplitudes including the global factor (W-propagator and electroweak coupling, except for alpha_s)
MLLLtreeTot = MLLLtree * G
MLLRtreeTot = MLLRtree * G
print()
print("Tree-level amplitudes including all the couplings and propagators:")
print("M(L,L,L)_tree = ", MLLLtreeTot)
print("M(L,L,R)_tree = ", MLLRtreeTot)
print()


# Tree-level squared amplitudes (including color summation Cf*Nc and spin average 1/(2Nc)^2)
M2LLLtree = MLLLtreeTot*MLLLtreeTot.conjugate()*(Cf*Nc/((2*Nc)**2))
M2LLRtree = MLLRtreeTot*MLLRtreeTot.conjugate()*(Cf*Nc/((2*Nc)**2))

print("Tree-level squared amplitudes including all the couplings, color summation (Cf*Nc) and spin average (1/(2Nc)^2):")
print("|M(L,L,L)_tree|^2 = ", M2LLLtree.real)
print("|M(L,L,R)_tree|^2 = ", M2LLRtree.real)
print("Sum over left-handed quarks:")
print("|M(L,L,L)_tree|^2 + |M(L,L,R)_tree|^2 =", M2LLLtree.real + M2LLRtree.real, "(Dmitrii)")
print("|M(L,L,L)_tree|^2 + |M(L,L,R)_tree|^2 = 3.1741621417347662e-09 (OpenLoops)") # additional numerical verification is possible using a special program OpenLoops
print()



















