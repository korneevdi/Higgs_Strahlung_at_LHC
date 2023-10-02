
import math, cmath
import numpy as np
from mpmath import *

"""
In this project, I compute radiative 2-loop QCD corrections to the process q qb -> g W H -> g l nub H
After quark-antiquark (q and qb) collision a gluon (g), a vector boson (W) and a Higgs (H) appear with subsequent decay of the vector boson into a lepton-antinuetrino (l and nub) pair)
As a result I obtain 2-loop squared amplitude for this process, which allows to compute the cross section measured in CERN (at the Long Hanron Collider)
"""

# PROCESS
# q(p1) + qb(p2) -> VH + jets -> e(p3) + nub(p4) + H(pH) + jets
print("Considered process: q(p1) + qb(p2) -> VH + jets -> e(p3) + nub(p4) + H(pH) + jets")
print()

# LEADING ORDER, ONE-LOOP, TWO-LOOP
# q(p1) + qb(p2) -> e(p3) + nub(p4) + g(p5) + H(pH)

print("Tree-level and one-loop process with real emission: q(p1) + qb(p2) -> gVH -> l(p3) + nub(p4) + g(p5) + H(pH)")
print()

print("-----------------------------------------")
print("PRELIMINARY COMPUTATIONS")
print("-----------------------------------------")

# PARAMETERS (various high energy physics constants used for calculations)
mW = 80.419                     # W-boson mass
mZ = 91.188                     # Z-boson mass
mH = 125.0                      # Higgs boson mass 
Gamma_W = 2.085                 # W-boson decay width
Gamma_Z = 2.4952                # Z-boson decay width
cosW = mW/mZ                    # cosine of the Weinberg angle
sinW = math.sqrt(1 - cosW**2)   # sine of the Weinberg angle
gW = 0.6530704531238141         # electroweak coupling
vev = 246.21845810181634        # vacuum expectation value
mu = 91.188                     # energy scale
musq = mu**2                    # square of the energy scale
alpha_s = 1                     # strong coupling
Cf = 4/3                        # Casimir operator of SU(3)
Nc = 3                          # number of colors

# for (u db -> W) and (d ub -> W) BosonType = 1, for (u ub -> Z) and (d db -> Z) BosonType = 2
BosonType = 1

# for SM TheoryType = 1, for SMEFT TheoryType = 2
TheoryType = 1

# GENERAL SETTINGS (SM/SMEFT and W/Z)

I3 = 0      # lepton isospin (positron)
Q = 1       # lepton electric charge (positron)

# BosonType settings
if BosonType == 1:
    mV = mW
    Gamma_V = Gamma_W
    a = 1/math.sqrt(2)
    b = 0
    vq = 1/(2*math.sqrt(2))
    aq = 1/(2*math.sqrt(2))
else:
    if BosonType == 2:
        mV = mZ
        Gamma_V = Gamma_Z
        a = I3/cosW
        b = -Q * sinW**2 / cosW
        vq = I3/2 - Q*sinW**2
        aq = I3/2
    else:
        import sys
        sys.exit("BosonType should be equal to 1 (for W) or 2 (for Z)")

# TheoryType settings
if TheoryType == 1:
    A = 0
    B = 0
    C = 0
    D = 0
else:
    if TheoryType == 2:
        A = 1
        B = 1
        C = 1
        D = 1
    else:
        import sys
        sys.exit("TheoryType should be equal to 1 (for SM) or 2 (for SMEFT)")

    



print("BosonType: ", BosonType)
print("TheoryType: ", TheoryType)
print("mV = ", mV)
print("Gamma_V = ", Gamma_V)
print("a = ", a)
print("b = ", b)
print("vq = ", vq)
print("aq = ", aq)
print("Wilson coefficients:")
print("A = ", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)
print()


# External Momenta

# P1
p1 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]     # antiquark
p5 = [86.94997640526997900, -21.701022816585411,  39.355542645382108, -74.434570386874427]       # antinuetrino
p4 = [322.3919309874294800, -101.97160213731860, -296.47360464823691,  75.111592116216357]     # lepton
p3 = [149.6028751502909100, -103.96621515693120, -95.942663470338033,  48.652355394098521]    # gluon
pH = [441.0552174570096900,  227.63884011083519,  353.06072547319292, -49.329377123440487]      # Higgs boson

# P2
"""
p1 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]     # antiquark
p4 = [408.09769343864940, -151.58297471069091,  -43.368211642550193, 376.41138052233600]       # antinuetrino
p3 = [212.02666673552400, -13.563737621454340, -112.81797905507730,  -179.00680442553411]     # lepton
p5 = [158.79955431793871, 73.137815818506667, 9.3452151582977017,  -140.64432197042041]    # gluon
pH = [221.07608550788780,  92.008896513638575,  146.84097553932980, -56.760254126381483]      # Higgs boson
"""

                          


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
print("Spinor products of momenta: sij = 2(pi*pj)")
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
Ang = np.array([[0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j]])
i = 1;
j = 1;
while i < 6:
    while j < 6:
        if i != j:
            Ang[i,j] = Uminusbar[i,0] * Uplus[0,j] + Uminusbar[i,1] * Uplus[1,j] + Uminusbar[i,2] * Uplus[2,j] + Uminusbar[i,3] * Uplus[3,j]
            print("< p", i, "p", j, "> = ", Ang[i,j])
        j += 1
    i += 1
    j = 1
print()


# Define a matrix of spinor products S_(ij) = [pipj]
print("Spinor products [pipj]:")
Sq = np.array([[0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j]])
i = 1;
j = 1;
while i < 6:
    while j < 6:
        if i != j:
            Sq[i,j] = Uplusbar[i,0] * Uminus[0,j] + Uplusbar[i,1] * Uminus[1,j] + Uplusbar[i,2] * Uminus[2,j] + Uplusbar[i,3] * Uminus[3,j]
            print("[ p", i, "p", j, "] = ", Sq[i,j])
        j += 1
    i += 1
    j = 1
print()

# Global factor settings
prop1 = 1 / (s[1,2] - s[1,5] - s[2,5] - mV**2 + 1j*mV*Gamma_V)
prop2 = 1 / (s[3,4] - mV**2 + 1j*mV*Gamma_V)



GlobFac_SM = 1j * gW**3 * mV**3/(mW**2) * prop1 * prop2
GlobFac_SMEFT = gW * prop2

print("Global factors:")
print("G = ", GlobFac_SM, " (Standard Model)")
print("G = ", GlobFac_SMEFT, " (SMEFT)")
print()




                                                                                        # LEADING ORDER (TREE LEVEL)
                                                                                        
                # Particle order: quark(p1), antiquark(p2), lepton(p3), antinuetrino(p4), gluon(p5)

print("-----------------------------------------")
print("TREE LEVEL")
print("-----------------------------------------")


# SM tree-level helicity amplitudes iM(quark, antiquark, gluon, lepton, antilepton)
MLRLLLtreeSM = 0 * GlobFac_SM
MLRRLLtreeSM = 0 * GlobFac_SM
MRLLLLtreeSM = 0 * GlobFac_SM
MRLRLLtreeSM = 0 * GlobFac_SM
MLLLLLtreeSM = 2 * (vq + aq) * (a + b) * (Sq[1,2] * Sq[1,4] * Ang[2,3] / (Sq[1,5] * Sq[2,5]) + Sq[1,4] * Ang[3,5] / Sq[2,5]) * GlobFac_SM
MLLRLLtreeSM = 2 * (vq + aq) * (a + b) * (Ang[1,2] * Sq[4,1] * Ang[2,3] / (Ang[1,5] * Ang[2,5]) + Sq[4,5] * Ang[2,3] / Ang[1,5]) * GlobFac_SM
MRRLLLtreeSM = 2 * (vq - aq) * (a + b) * (Sq[1,2] * Sq[2,4] * Ang[1,3] / (Sq[1,5] * Sq[2,5]) - Sq[2,4] * Ang[3,5] / Sq[1,5]) * GlobFac_SM
MRRRLLtreeSM = 2 * (vq - aq) * (a + b) * (Ang[1,2] * Sq[4,2] * Ang[1,3] / (Ang[1,5] * Ang[2,5]) - Sq[4,5] * Ang[1,3] / Ang[2,5]) * GlobFac_SM
MLRLRRtreeSM = 0 * GlobFac_SM
MLRRRRtreeSM = 0 * GlobFac_SM
MRLLRRtreeSM = 0 * GlobFac_SM
MRLRRRtreeSM = 0 * GlobFac_SM
MLLLRRtreeSM = 2 * (vq + aq) * b * (Sq[1,2] * Ang[2,4] * Sq[1,3] / (Sq[1,5] * Sq[2,5]) + Ang[4,5] * Sq[1,3] / Sq[2,5]) * GlobFac_SM
MLLRRRtreeSM = 2 * (vq + aq) * b * (Ang[1,2] * Ang[2,4] * Sq[1,3] / (Ang[1,5] * Ang[2,5]) - Ang[2,4] * Sq[3,5] / Ang[1,5]) * GlobFac_SM
MRRLRRtreeSM = 2 * (vq - aq) * b * (Sq[1,2] * Ang[1,4] * Sq[2,3] / (Sq[1,5] * Sq[2,5]) - Ang[4,5] * Sq[2,3] / Sq[1,5]) * GlobFac_SM
MRRRRRtreeSM = 2 * (vq - aq) * b * (Ang[1,2] * Ang[1,4] * Sq[2,3] / (Ang[1,5] * Ang[2,5]) + Ang[1,4] * Sq[3,5] / Ang[2,5]) * GlobFac_SM

# SMEFT tree-level helicity amplitudes iM(quark, antiquark, gluon, lepton, antilepton)
MLRLLLtreeSMEFT = 4 * A * (a + b) * Sq[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] / (Sq[1,5] * Sq[2,5]) * GlobFac_SM
MLRRLLtreeSMEFT = 4 * A * (a + b) * (Ang[1,2] * Sq[1,4] * Sq[2,4] * Ang[4,3] / (Ang[1,5] * Ang[2,5]) + Ang[3,4] * Sq[4,5] * (-Sq[1,4]/Ang[2,5] + Sq[2,4]/Ang[1,5])) * GlobFac_SMEFT
MRLLLLtreeSMEFT = 4 * B * (a + b) * (Sq[2,1] * Ang[1,3] * Ang[2,3] * Sq[3,4] / (Sq[1,5] * Sq[2,5]) + Ang[3,5] * Sq[3,4] * (Ang[2,3]/Sq[1,5] - Ang[1,3]/Sq[2,5])) * GlobFac_SMEFT
MRLRLLtreeSMEFT = 4 * B * (a + b) * Ang[1,2] * Ang[1,3] * Ang[2,3] * Sq[3,4] / (Ang[1,5] * Ang[2,5]) * GlobFac_SMEFT
MLLLLLtreeSMEFT = 2 * C * (a + b) * (Sq[1,2] * Sq[1,4] * Ang[2,3] / (Sq[1,5] * Sq[2,5]) + Sq[1,4] * Ang[3,5] / Sq[2,5]) * GlobFac_SMEFT
MLLRLLtreeSMEFT = 2 * C * (a + b) * (Ang[1,2] * Sq[4,1] * Ang[2,3] / (Ang[1,5] * Ang[2,5]) + Sq[4,5] * Ang[2,3] / Ang[1,5]) * GlobFac_SMEFT
MRRLLLtreeSMEFT = 2 * D * (a + b) * (Sq[1,2] * Sq[2,4] * Ang[1,3] / (Sq[1,5] * Sq[2,5]) - Sq[2,4] * Ang[3,5] / Sq[1,5]) * GlobFac_SMEFT
MRRRLLtreeSMEFT = 2 * D * (a + b) * (Ang[1,2] * Sq[4,2] * Ang[1,3] / (Ang[1,5] * Ang[2,5]) - Sq[4,5] * Ang[1,3] / Ang[2,5]) * GlobFac_SMEFT

MLRLRRtreeSMEFT = 4 * A * b * Sq[1,2] * Sq[1,3] * Sq[2,3] * Ang[3,4] / (Sq[1,5] * Sq[2,5]) * GlobFac_SMEFT
MLRRRRtreeSMEFT = 4 * A * b * (Ang[2,1] * Sq[1,3] * Sq[2,3] * Ang[3,4] / (Ang[1,5] * Ang[2,5]) + Sq[3,5] * Ang[3,4] * (Sq[2,3]/Ang[1,5] - Sq[1,3]/Ang[2,5])) * GlobFac_SMEFT
MRLLRRtreeSMEFT = 4 * B * b * (Sq[1,2] * Ang[1,4] * Ang[2,4] * Sq[4,3] / (Sq[1,5] * Sq[2,5]) + Sq[3,4] * Ang[4,5] * (-Ang[1,4]/Sq[2,5] + Ang[2,4]/Sq[1,5])) * GlobFac_SMEFT
MRLRRRtreeSMEFT = 4 * B * b * Ang[1,2] * Ang[1,4] * Ang[2,4] * Sq[3,4] / (Ang[1,5] * Ang[2,5]) * GlobFac_SM
MLLLRRtreeSMEFT = 2 * C * b * (Sq[1,2] * Ang[2,4] * Sq[1,3] / (Sq[1,5] * Sq[2,5]) + Ang[4,5] * Sq[1,3] / Sq[2,5]) * GlobFac_SMEFT
MLLRRRtreeSMEFT = 2 * C * b * (Ang[1,2] * Ang[2,4] * Sq[1,3] / (Ang[1,5] * Ang[2,5]) - Ang[2,4] * Sq[3,5] / Ang[1,5]) * GlobFac_SMEFT
MRRLRRtreeSMEFT = 2 * D * b * (Sq[1,2] * Ang[1,4] * Sq[2,3] / (Sq[1,5] * Sq[2,5]) - Ang[4,5] * Sq[2,3] / Sq[1,5]) * GlobFac_SMEFT
MRRRRRtreeSMEFT = 2 * D * b * (Ang[1,2] * Ang[1,4] * Sq[2,3] / (Ang[1,5] * Ang[2,5]) + Ang[1,4] * Sq[3,5] / Ang[2,5]) * GlobFac_SMEFT


print("Standard Model tree-level helicity amplitudes iM(quark, antiquark, gluon, lepton, antilepton):")
print("M(L,R,L,L,L)_tree = ", MLRLLLtreeSM)
print("M(L,R,R,L,L)_tree = ", MLRRLLtreeSM)
print("M(R,L,L,L,L)_tree = ", MRLLLLtreeSM)
print("M(R,L,R,L,L)_tree = ", MRLRLLtreeSM)
print("M(L,L,L,L,L)_tree = ", MLLLLLtreeSM)
print("M(L,L,R,L,L)_tree = ", MLLRLLtreeSM)
print("M(R,R,L,L,L)_tree = ", MRRLLLtreeSM)
print("M(R,R,R,L,L)_tree = ", MRRRLLtreeSM)

print("M(L,R,L,R,R)_tree = ", MLRLRRtreeSM)
print("M(L,R,R,R,R)_tree = ", MLRRRRtreeSM)
print("M(R,L,L,R,R)_tree = ", MRLLRRtreeSM)
print("M(R,L,R,R,R)_tree = ", MRLRRRtreeSM)
print("M(L,L,L,R,R)_tree = ", MLLLRRtreeSM)
print("M(L,L,R,R,R)_tree = ", MLLRRRtreeSM)
print("M(R,R,L,R,R)_tree = ", MRRLRRtreeSM)
print("M(R,R,R,R,R)_tree = ", MRRRRRtreeSM)
print()

print("SMEFT tree-level helicity amplitudes iM(quark, antiquark, gluon, lepton, antilepton):")
print("M(L,R,L,L,L)_tree = ", MLRLLLtreeSMEFT)
print("M(L,R,R,L,L)_tree = ", MLRRLLtreeSMEFT)
print("M(R,L,L,L,L)_tree = ", MRLLLLtreeSMEFT)
print("M(R,L,R,L,L)_tree = ", MRLRLLtreeSMEFT)
print("M(L,L,L,L,L)_tree = ", MLLLLLtreeSMEFT)
print("M(L,L,R,L,L)_tree = ", MLLRLLtreeSMEFT)
print("M(R,R,L,L,L)_tree = ", MRRLLLtreeSMEFT)
print("M(R,R,R,L,L)_tree = ", MRRRLLtreeSMEFT)

print("M(L,R,L,R,R)_tree = ", MLRLRRtreeSMEFT)
print("M(L,R,R,R,R)_tree = ", MLRRRRtreeSMEFT)
print("M(R,L,L,R,R)_tree = ", MRLLRRtreeSMEFT)
print("M(R,L,R,R,R)_tree = ", MRLRRRtreeSMEFT)
print("M(L,L,L,R,R)_tree = ", MLLLRRtreeSMEFT)
print("M(L,L,R,R,R)_tree = ", MLLRRRtreeSMEFT)
print("M(R,R,L,R,R)_tree = ", MRRLRRtreeSMEFT)
print("M(R,R,R,R,R)_tree = ", MRRRRRtreeSMEFT)
print()


# Tree-level squared amplitudes (including color summation Cf*Nc and spin average 1/(2Nc)^2)
# neglect terms of the order Wilson**2
M2LRLLLtree = (MLRLLLtreeSM * MLRLLLtreeSM.conjugate() + (2 * MLRLLLtreeSM * MLRLLLtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2LRRLLtree = (MLRRLLtreeSM * MLRRLLtreeSM.conjugate() + (2 * MLRRLLtreeSM * MLRRLLtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2RLLLLtree = (MRLLLLtreeSM * MRLLLLtreeSM.conjugate() + (2 * MRLLLLtreeSM * MRLLLLtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2RLRLLtree = (MRLRLLtreeSM * MRLRLLtreeSM.conjugate() + (2 * MRLRLLtreeSM * MRLRLLtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2LLLLLtree = (MLLLLLtreeSM * MLLLLLtreeSM.conjugate() + (2 * MLLLLLtreeSM * MLLLLLtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2LLRLLtree = (MLLRLLtreeSM * MLLRLLtreeSM.conjugate() + (2 * MLLRLLtreeSM * MLLRLLtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2RRLLLtree = (MRRLLLtreeSM * MRRLLLtreeSM.conjugate() + (2 * MRRLLLtreeSM * MRRLLLtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2RRRLLtree = (MRRRLLtreeSM * MRRRLLtreeSM.conjugate() + (2 * MRRRLLtreeSM * MRRRLLtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))

M2LRLRRtree = (MLRLRRtreeSM * MLRLRRtreeSM.conjugate() + (2 * MLRLRRtreeSM * MLRLRRtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2LRRRRtree = (MLRRRRtreeSM * MLRRRRtreeSM.conjugate() + (2 * MLRRRRtreeSM * MLRRRRtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2RLLRRtree = (MRLLRRtreeSM * MRLLRRtreeSM.conjugate() + (2 * MRLLRRtreeSM * MRLLRRtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2RLRRRtree = (MRLRRRtreeSM * MRLRRRtreeSM.conjugate() + (2 * MRLRRRtreeSM * MRLRRRtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2LLLRRtree = (MLLLRRtreeSM * MLLLRRtreeSM.conjugate() + (2 * MLLLRRtreeSM * MLLLRRtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2LLRRRtree = (MLLRRRtreeSM * MLLRRRtreeSM.conjugate() + (2 * MLLRRRtreeSM * MLLRRRtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2RRLRRtree = (MRRLRRtreeSM * MRRLRRtreeSM.conjugate() + (2 * MRRLRRtreeSM * MRRLRRtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))
M2RRRRRtree = (MRRRRRtreeSM * MRRRRRtreeSM.conjugate() + (2 * MRRRRRtreeSM * MRRRRRtreeSMEFT).real) * (Cf*Nc/((2*Nc)**2))


print("Squared tree-level helicity amplitudes:")
print("|M(L,R,L,L,L)_tree|^2 = ", M2LRLLLtree.real)
print("|M(L,R,R,L,L)_tree|^2 = ", M2LRRLLtree.real)
print("|M(R,L,L,L,L)_tree|^2 = ", M2RLLLLtree.real)
print("|M(R,L,R,L,L)_tree|^2 = ", M2RLRLLtree.real)
print("|M(L,L,L,L,L)_tree|^2 = ", M2LLLLLtree.real)
print("|M(L,L,R,L,L)_tree|^2 = ", M2LLRLLtree.real)
print("|M(R,R,L,L,L)_tree|^2 = ", M2RRLLLtree.real)
print("|M(R,R,R,L,L)_tree|^2 = ", M2RRRLLtree.real)

print("|M(L,R,L,R,R)_tree|^2 = ", M2LRLRRtree.real)
print("|M(L,R,R,R,R)_tree|^2 = ", M2LRRRRtree.real)
print("|M(R,L,L,R,R)_tree|^2 = ", M2RLLRRtree.real)
print("|M(R,L,R,R,R)_tree|^2 = ", M2RLRRRtree.real)
print("|M(L,L,L,R,R)_tree|^2 = ", M2LLLRRtree.real)
print("|M(L,L,R,R,R)_tree|^2 = ", M2LLRRRtree.real)
print("|M(R,R,L,R,R)_tree|^2 = ", M2RRLRRtree.real)
print("|M(R,R,R,R,R)_tree|^2 = ", M2RRRRRtree.real)

# Total tree-level squared amplitude
M2tree = M2LRLLLtree.real + M2LRRLLtree.real + M2RLLLLtree.real + M2RLRLLtree.real + M2LLLLLtree.real + M2LLRLLtree.real + M2RRLLLtree.real + M2RRRLLtree.real + M2LRLRRtree.real + M2LRRRRtree.real + M2RLLRRtree.real + M2RLRRRtree.real + M2LLLRRtree.real + M2LLRRRtree.real + M2RRLRRtree.real + M2RRRRRtree.real

print("Total tree-level squared amplitude:")
print("|M_tree|^2 = ", M2tree)
print()



# OpenLoops & MadGraph results
OpenLoopsRes = 3.8305580356531853E-009 # P1
#OpenLoopsRes = 1.0622265520776929E-011 # P2

#OpenLoopsRes = 4.2298820425566844E-011 # T3
#OpenLoopsRes = 5.9737839579143591E-010 # T4
#OpenLoopsRes = 2.1564977816288064E-011 # T5
#OpenLoopsRes = 2.1353768988401058E-010 # T6

print("OpenLoops & MadGraph result:")
print("|M_tree|^2 = ", OpenLoopsRes)

print("ratio Dmitrii/OpenLoops: ", M2tree / OpenLoopsRes)









"""





                                                                                        # NEXT-TO-LEADING ORDER (ONE LOOP)

                # Particle order: quark(p1), antiquark(p2), lepton(p3), antinuetrino(p4), gluon(p5)

print("-----------------------------------------")
print("NEXT-TO-LEADING ORDER (ONE LOOP)")
print("-----------------------------------------")

# One-loop form factors
print("One-loop unrenormalized form factors")
print("1/eps^2 poles:")
FFnloEPS2 = [0]
FFnloEPS2.append((s[1,5]*s[2,5]**2*(s[1,5] + s[2,5])*(s[1,5] - 2*Nc**2*s[1,5] + s[1,5]**2 - 2*(-1 + Nc**2)*s[2,5]) + s[1,2]**3*(s[1,5]**2*(1 - Nc**2*s[2,5]) + s[1,5]*s[2,5]*(4 + s[2,5] - 2*Nc**2*(2 + s[2,5])) + s[2,5]**2*(3 + s[2,5] - Nc**2*(4 + s[2,5]))) - s[1,2]**2*(s[1,5]**3*(-1 + (3 + Nc**2)*s[2,5]) + s[1,5]**2*(1 + 5*(-1 + Nc**2)*s[2,5] + Nc**2*s[2,5]**2) + s[1,5]*s[2,5]*(1 + 2*(-3 + 5*Nc**2)*s[2,5] + (-1 + Nc**2)*s[2,5]**2) + s[2,5]**2*(1 - s[2,5]**2 + Nc**2*s[2,5]*(5 + s[2,5]))) + s[1,2]*(s[1,5]**4*s[2,5] + s[2,5]**3*(1 + s[2,5] - Nc**2*s[2,5]) + s[1,5]**3*(-1 + s[2,5] - Nc**2*s[2,5] - 2*s[2,5]**2) - s[1,5]**2*s[2,5]*(3 + (-3 + 8*Nc**2)*s[2,5] + Nc**2*s[2,5]**2) - s[1,5]*s[2,5]**3*(-5 + Nc**2*(8 + s[2,5]))))/(16*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])))
FFnloEPS2.append(0)
FFnloEPS2.append((1/(16*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])**2*s[2,5]*(s[1,2] + s[2,5])))*(2*s[1,2]**5*s[1,5]*s[2,5] - s[1,5]**2*s[2,5]**2*(s[1,5]**2 + s[2,5]) + s[1,2]**4*(2*s[1,5]**2*s[2,5] + s[2,5]*(-1 + 2*Nc**2*s[2,5]) + s[1,5]*(1 + s[2,5] + Nc**2*s[2,5] + 2*s[2,5]**2)) + s[1,2]**3*(s[2,5]**2*(1 + 2*Nc**2*s[2,5]) + s[1,5]**2*(2 + s[2,5] + 2*Nc**2*s[2,5] + 2*s[2,5]**2) + s[1,5]*(-1 - (1 + Nc**2)*s[2,5] + (2 + 5*Nc**2)*s[2,5]**2)) + s[1,2]**2*(-s[2,5]**2 + s[1,5]**3*(1 + 2*(-1 + Nc**2)*s[2,5]) + s[1,5]*s[2,5]*(-2 - (1 + Nc**2)*s[2,5] + 3*(1 + Nc**2)*s[2,5]**2) + s[1,5]**2*(-2 - 3*s[2,5] + (-4 + 7*Nc**2)*s[2,5]**2)) - s[1,2]*(s[1,5]**4*s[2,5] + s[2,5]**3 + s[1,5]**3*(1 - 2*(-2 + Nc**2)*s[2,5]**2) + s[1,5]*s[2,5]*(2*s[2,5]*(1 + 2*s[2,5]) - Nc**2*(2 + 3*s[2,5])) + s[1,5]**2*s[2,5]*(s[2,5]*(2 + s[2,5]) + Nc**2*(-2 + s[2,5] - 2*s[2,5]**2)))))
FFnloEPS2.append((1/(16*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2))*(s[1,5]**2*s[2,5]**2*(1 + s[2,5]**2) - s[1,2]**4*(2*Nc**2*s[1,5]**2 + s[2,5] + s[1,5]*(-1 + s[2,5] + Nc**2*s[2,5])) + s[1,2]**3*(-2*Nc**2*s[1,5]**3 + s[2,5] - 2*s[2,5]**2 - s[1,5]**2*(2 + (2 + 5*Nc**2)*s[2,5]) - s[1,5]*(-1 + s[2,5] - Nc**2*s[2,5] + (3 + 2*Nc**2)*s[2,5]**2)) - s[1,2]**2*((-2 + s[2,5])*s[2,5]**2 + s[1,5]**3*(1 + 3*(1 + Nc**2)*s[2,5]) + s[1,5]*s[2,5]*(-4 - 3*s[2,5] + 2*(-1 + Nc**2)*s[2,5]**2) + s[1,5]**2*(-2 - (-3 + Nc**2)*s[2,5] + (-2 + 7*Nc**2)*s[2,5]**2)) + s[1,2]*(s[2,5]**3 + s[1,5]**3*(1 + 2*s[2,5] + (1 - 2*Nc**2)*s[2,5]**2) + s[1,5]*s[2,5]*(s[2,5] + s[2,5]**3 - 2*Nc**2*(1 + s[2,5])) + s[1,5]**2*s[2,5]*(4 + s[2,5] + 4*s[2,5]**2 + Nc**2*(-3 + s[2,5] - 2*s[2,5]**2)))))
FFnloEPS2.append((2*s[1,2]**3*s[1,5]*s[2,5]*(-s[1,5] + s[2,5]) + s[1,5]*s[2,5]*(s[1,5] + s[2,5])*((-1 + 2*Nc**2)*s[1,5] + s[2,5]*(-2*Nc**2 + s[2,5])) - s[1,2]**2*(s[1,5] + s[2,5])*((-1 + Nc**2)*s[2,5] + s[1,5]**2*(-1 + 2*s[2,5]) - s[1,5]*(-2 + Nc**2 + 2*s[2,5]**2)) + s[1,2]*(s[2,5]**2*(-1 - (1 + Nc**2)*s[2,5] + s[2,5]**2) + s[1,5]**2*(1 + (1 + Nc**2)*s[2,5] + s[2,5]**2 - 2*(-1 + Nc**2)*s[2,5]**3) - s[1,5]*s[2,5]**2*(4 - s[2,5] + Nc**2*(1 + 2*s[2,5])) + s[1,5]**3*(s[2,5] - 2*s[2,5]**2 + Nc**2*(1 + 2*s[2,5] + 2*s[2,5]**2))))/(16*Nc*math.pi**2*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])))
FFnloEPS2.append(-((s[1,2]**2*s[2,5]*(-1 + s[1,5] + s[2,5]) + s[1,5]*(-1 + s[2,5])*(s[1,5]**2 - s[2,5] + s[1,5]*s[2,5]) - s[1,2]*(2*s[1,5]**3 + s[1,5]**2*(1 - 2*s[2,5]) + (-1 + s[2,5])*s[2,5]))/(4*(Nc*math.pi**2*s[1,5]*(s[1,2] + s[1,5])**2*(s[1,5] + s[2,5])))))
FFnloEPS2.append(0)
FFnloEPS2.append((2*s[1,2]*((1 + Nc**2)*s[1,5]**2 + s[1,5]*(-1 + Nc**2*(-1 + s[2,5])) - s[2,5])*s[2,5] - s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + 2*s[1,2]**3*((-1 + Nc**2)*s[1,5] + Nc**2*s[2,5]) + s[1,2]**2*(s[2,5]*(-2 - 2*s[1,5] - s[1,5]**2 + 2*s[2,5] + s[1,5]*s[2,5]) + 2*Nc**2*(s[1,5]**2 + 3*s[1,5]*s[2,5] + s[2,5]**2)))/(8*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])))
FFnloEPS2.append(0)
FFnloEPS2.append((s[1,2]*(s[1,5]*s[2,5] - (-1 + s[2,5])*s[2,5] + s[1,5]**2*(-3 + 2*s[2,5]) + s[1,2]*(-1 + s[1,5]**2 + s[2,5]**2 + s[1,5]*(-3 + 2*s[2,5]))))/(4*Nc*math.pi**2*s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])**2))
FFnloEPS2.append(0)
FFnloEPS2.append(-((2*s[1,2]**3*s[1,5]*(s[1,5] - s[2,5])*s[2,5] + s[1,5]*s[2,5]*(s[1,5] + s[2,5])*((-1 + 2*Nc**2)*s[1,5] + s[2,5]*(-2*Nc**2 + s[2,5])) + s[1,2]**2*(s[1,5] + s[2,5])*(s[2,5] - 2*Nc**2*s[2,5] + s[1,5]**2*(1 + 2*s[2,5]) + 2*s[1,5]*(-1 + Nc**2 - s[2,5]**2)) + s[1,2]*(s[1,5]*s[2,5]**2*(-1 - 2*Nc**2 + s[2,5]) + s[2,5]**3*(-2*Nc**2 + s[2,5]) + s[1,5]**2*s[2,5]*(-2 + 2*Nc**2 + s[2,5] - 2*s[2,5]**2) + s[1,5]**3*(-1 + 2*Nc**2 + s[2,5] + 2*s[2,5]**2)))/(16*(Nc*math.pi**2*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])))))
FFnloEPS2.append(0)

i = 1
while i < 14:
    print("FF_nlo[", i, "] =", FFnloEPS2[i])
    i += 1
print()

print("1/eps poles:")
FFnloEPS1 = [0]
FFnloEPS1.append(((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - 2*s[1,5]*(s[1,2] + s[1,5])*(3*s[2,5]**2*(s[1,5] + s[2,5]) + 2*s[1,2]*s[2,5]*(s[1,5] + 2*s[2,5]) + s[1,2]**2*(s[1,5] + 3*s[2,5])) - 2*Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[1,2]**2 + 2*s[1,5]*s[2,5] + s[1,2]*(s[1,5] + s[2,5] + s[1,5]*s[2,5])) - 2*s[2,5]*(s[1,2] + s[2,5])*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[1,5] + s[2,5] + 6*s[1,5]*s[2,5])) + 4*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5])))) + 2*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5]))))*cmath.log(4) - 2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(-3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(1 + cmath.log(4)) + s[1,2]*s[1,5]*(1 + s[2,5] + cmath.log(4) + s[2,5]*cmath.log(16)) + s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))) - (s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(-4*Nc**2*s[1,5]*s[2,5] + 8*s[1,2]*s[2,5]*(1 + 2*s[2,5])*cmath.log(2) + s[1,2]*s[1,5]*(2 + cmath.log(16) + s[2,5]*(-9 - Nc**2 + cmath.log(16))) + 2*s[1,2]*(s[1,5] + 2*s[2,5] + s[1,5]*s[2,5] + 4*s[2,5]**2)*cmath.log(-(musq/s[1,5]))) - s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(-4*Nc**2*s[1,5]*s[2,5] + 8*s[1,2]*s[1,5]*(1 + 2*s[1,5])*cmath.log(2) + s[1,2]*s[2,5]*(2 + cmath.log(16) + s[1,5]*(-9 - Nc**2 + cmath.log(16))) + 2*s[1,2]*(4*s[1,5]**2 + s[2,5] + s[1,5]*(2 + s[2,5]))*cmath.log(-(musq/s[2,5]))) - 2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2]*s[1,5] + 4*s[1,2]*s[2,5] + 3*s[1,5]*s[2,5] + 2*s[2,5]**2 - 2*(s[2,5]**2 + s[1,2]*(s[1,5] + 2*s[2,5]))*(1 + cmath.log(2)) - (s[2,5]**2 + s[1,2]*(s[1,5] + 2*s[2,5]))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 2*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(4*s[1,2]*s[1,5] + 2*s[1,5]**2 - 2*s[1,5]*(2*s[1,2] + s[1,5]) + 2*s[1,2]*s[2,5] - (s[1,2] + 3*s[1,5])*s[2,5] + (s[1,5]**2 + s[1,2]*(2*s[1,5] + s[2,5]))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 4*Nc**2*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(2*s[1,2] - s[1,5]*s[2,5] + s[1,2]*(s[1,5] + s[2,5]) - s[1,2]*(2 + s[1,5] + s[2,5]) - 1/2*s[1,2]*(2 + s[1,5] + s[2,5])*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 2*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5]))))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))/(32*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])))
FFnloEPS1.append(0 + 0j)
FFnloEPS1.append((1/(32*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])**2*s[2,5]*(s[1,2] + s[2,5]))*(2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + 3*s[2,5] + 4*s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,2]*(s[1,2] + s[1,5])**2*s[2,5]*(s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(2*s[1,5] + s[2,5])) - (-1 + Nc**2)*s[1,2]*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + 2*s[1,5] + 3*s[2,5])) + 2*s[1,2]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]**3*s[1,5] + 4*s[1,2]**2*s[1,5]**2 + 3*s[1,5]*s[2,5] + s[1,2]*(3*s[1,5]**3 - s[2,5] + 8*s[1,5]*s[2,5])) + 4*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2))) + 2*Nc**2*s[1,5]*s[2,5]*(4*s[1,5]*s[2,5] + s[1,2]*(1 + 7*s[2,5] + 7*s[1,5]**2*s[2,5] + s[1,5]*(7 + 11*s[2,5] + 7*s[2,5]**2))) + 4*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2)))*cmath.log(2) - 2*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5])*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(1 + cmath.log(4)) + s[1,2]*s[1,5]*(3 + cmath.log(4) + s[2,5]*(5 + cmath.log(16))) + s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))) - (s[1,2] + s[1,5])**2*(8*Nc**2*s[1,5]*s[2,5] - 8*s[1,2]*s[2,5]**2*cmath.log(2) + s[1,2]*s[1,5]*(6 + cmath.log(16) + s[2,5]*(21 + 17*Nc**2 + cmath.log(16))) + 2*s[1,2]*(s[1,5] + s[1,5]*s[2,5] - 2*s[2,5]**2)*cmath.log(-(musq/s[1,5]))) - 2*s[2,5]*(s[1,2] + s[2,5])*(4*Nc**2*s[1,5]*s[2,5] + s[1,2]*(s[2,5]*(1 + cmath.log(4)) + s[1,5]**2*(16 + 12*Nc**2 + cmath.log(16)) + s[1,5]*(4 + cmath.log(16) + s[2,5]*(19 + 8*Nc**2 + cmath.log(64)))) + s[1,2]*(2*s[1,5]**2 + s[2,5] + s[1,5]*(2 + 3*s[2,5]))*cmath.log(-(musq/s[2,5]))) + 2*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5])*(s[1,2]*s[1,5] + 3*s[1,5]*s[2,5] + 2*s[2,5]**2 + 2*(s[1,2]*s[1,5] - s[2,5]**2)*(1 + cmath.log(2)) + (s[1,2]*s[1,5] - s[2,5]**2)*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 2*(s[1,2] + s[1,5])**2*s[2,5]*(s[1,2] + s[2,5])*(-s[1,2]*s[2,5] + 3*s[1,5]*s[2,5] + 2*s[1,2]*(2*s[1,5] + s[2,5]) + (-s[1,5]**2 + s[1,2]*(2*s[1,5] + s[2,5]))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 2*Nc**2*(s[1,2] + s[1,5])**2*s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]*(s[1,5] - s[2,5]) + 4*s[1,5]*s[2,5] + 2*s[1,2]*(s[1,5] + s[2,5])*(1 + cmath.log(2)) + s[1,2]*(s[1,5] + s[2,5])*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 2*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2)))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))))
FFnloEPS1.append((1/(32*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2)*(-2*s[1,2]*(s[1,2] + 3*s[1,5] + 4*s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[2,5])**2*(s[1,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 2*s[2,5])) + (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + 3*s[1,5] + 2*s[2,5])) - 2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(3*s[1,5]*s[2,5] + s[1,2]*(-s[1,5] + s[2,5] + 8*s[1,5]*s[2,5] + 7*s[2,5]**2)) - 2*Nc**2*s[1,5]*s[2,5]*(4*s[1,5]*s[2,5] + s[1,2]*(1 + 7*s[2,5] + 7*s[1,5]**2*s[2,5] + s[1,5]*(7 + 11*s[2,5] + 7*s[2,5]**2))) - 4*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5])))) - 4*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5]))))*cmath.log(2) + 2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])**2*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(3 + cmath.log(4)) + s[1,2]*s[1,5]*(1 + cmath.log(4) + s[2,5]*(5 + cmath.log(16))) + s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))) + 2*s[1,5]*(s[1,2] + s[1,5])*(4*Nc**2*s[1,5]*s[2,5] + s[1,2]*s[2,5]*(4 + cmath.log(16) + s[2,5]*(16 + 12*Nc**2 + cmath.log(16))) + s[1,2]*s[1,5]*(1 + cmath.log(4) + s[2,5]*(19 + 8*Nc**2 + cmath.log(64))) + s[1,2]*(s[1,5] + 3*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5]))*cmath.log(-(musq/s[1,5]))) + (s[1,2] + s[2,5])**2*(8*Nc**2*s[1,5]*s[2,5] - 8*s[1,2]*s[1,5]**2*cmath.log(2) + s[1,2]*s[2,5]*(6 + cmath.log(16) + s[1,5]*(21 + 17*Nc**2 + cmath.log(16))) + 2*s[1,2]*(-2*s[1,5]**2 + s[2,5] + s[1,5]*s[2,5])*cmath.log(-(musq/s[2,5]))) + 2*s[1,5]*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])**2*(s[1,2]*s[1,5] - 3*s[1,5]*s[2,5] - 2*s[1,2]*(s[1,5] + 2*s[2,5]) + (s[2,5]**2 - s[1,2]*(s[1,5] + 2*s[2,5]))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) - 2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])**2*(2*s[1,5] + (s[1,2] + 3*s[1,5])*s[2,5] - 2*(s[1,5] - s[1,2]*s[2,5])*(1 + cmath.log(2)) - (s[1,5] - s[1,2]*s[2,5])*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) - 2*Nc**2*s[1,5]*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])**2*(4*s[1,5]*s[2,5] + 2*s[1,2]*(-s[1,5] + s[2,5]) + 2*s[1,2]*(s[1,5] + s[2,5])*(1 + cmath.log(2)) + s[1,2]*(s[1,5] + s[2,5])*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) - 2*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5]))))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))))
FFnloEPS1.append((1/(32*Nc*math.pi**2*s[1,5]*s[2,5]))*(-((2*(s[1,5] - s[2,5])*(s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(1 + cmath.log(4)) + s[1,2]*s[1,5]*(1 + cmath.log(4) + s[2,5]*(3 + cmath.log(16))) + s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))))/(s[1,5] + s[2,5])) + (s[2,5]*((-5 + Nc**2)*s[1,5] - 4*s[2,5]*cmath.log(2)) - 2*s[1,2]*(s[2,5]**2*cmath.log(4) + s[1,5]*(1 + cmath.log(4) + s[2,5]*(3 + cmath.log(4)))) - 2*(s[2,5]**2 + s[1,2]*(s[1,5] + s[1,5]*s[2,5] + s[2,5]**2))*cmath.log(-(musq/s[1,5])))/(s[1,2] + s[2,5]) + (2*s[1,2]*(s[1,5]**2*cmath.log(4) + s[2,5]*(1 + cmath.log(4) + s[1,5]*(3 + cmath.log(4)))) + s[1,5]*(-((-5 + Nc**2)*s[2,5]) + s[1,5]*cmath.log(16)) + 2*((1 + s[1,2])*s[1,5]**2 + s[1,2]*s[2,5] + s[1,2]*s[1,5]*s[2,5])*cmath.log(-(musq/s[2,5])))/(s[1,2] + s[1,5]) + 2*Nc**2*(s[1,5] - s[2,5])*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) - 2*(s[1,2]*s[2,5] + s[1,5]*s[2,5] + s[1,5]*cmath.log(4) + s[1,2]*s[2,5]*cmath.log(4) + (s[1,5] + s[1,2]*s[2,5])*cmath.log(-(musq/s[1,2])) + (s[1,5] + s[1,2]*s[2,5])*cmath.log(-(musq/s[2,5])) - s[1,5]*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) - s[1,2]*s[2,5]*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*(s[1,2]*s[1,5] + s[1,5]*s[2,5] + (s[1,2]*s[1,5] + s[2,5]**2)*cmath.log(-(musq/s[1,2])) + (s[1,2]*s[1,5] + s[2,5]**2)*cmath.log(-(musq/s[1,5])) - s[1,2]*s[1,5]*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) - s[2,5]**2*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + (1/((s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])))*2*(s[1,5] - s[2,5])*(s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(1 - cmath.log(4) + Nc**2*(1 + cmath.log(4))) + s[1,2]*(s[2,5]*(1 + s[2,5])*(1 + cmath.log(4)) + s[1,5]**2*(1 + s[2,5])*(1 + cmath.log(4) + s[2,5]*(4 + Nc**2*(3 + cmath.log(16)))) + s[1,5]*(1 + cmath.log(4) + s[2,5]**2*(5 + cmath.log(4) + Nc**2*(3 + cmath.log(16))) + s[2,5]*(5 + cmath.log(256)))) + ((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 4*s[1,5]*s[2,5] + (1 + 2*Nc**2)*s[1,5]*s[2,5]**2 + s[2,5]*(1 + s[2,5]) + s[1,5]**2*(1 + s[2,5] + 2*Nc**2*s[2,5] + 2*Nc**2*s[2,5]**2)))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))))
FFnloEPS1.append((1/(512*Nc*math.pi**2*s[1,5]))*(-(48/s[2,5]) - (64*Nc**2*(2*s[1,2] + s[2,5]))/s[1,2] + Nc**2*(8 + (4*s[2,5])/s[1,2]) + (64*(s[1,5] + s[2,5] + 4*s[1,5]*s[2,5] + s[2,5]*cmath.log(16) + s[1,5]*s[2,5]*cmath.log(16) + 2*(1 + s[1,5])*s[2,5]*cmath.log(-(musq/s[1,2]))))/s[2,5] + (4*(Nc**2*s[1,5]**2*s[2,5] + 2*s[1,2]*s[1,5]*(s[1,5] + s[2,5])*(Nc**2 + 16*(2 + cmath.log(4))) + 2*s[1,2]**2*(s[1,5]*(Nc**2 + 16*(1 + 2*s[2,5])*(1 + cmath.log(4))) + 8*s[2,5]*(1 + cmath.log(16)) + 16*s[1,5]**2*(3 + cmath.log(16))) + 32*s[1,2]*(s[1,2] + s[1,5] + 2*s[1,2]*s[1,5])*(s[1,5] + s[2,5])*cmath.log(-(musq/s[2,5]))))/(s[1,2]*(s[1,2] + s[1,5])**2) + 64*(s[2,5] - 2*(s[1,5] + s[2,5]) - 4*(s[1,5] + s[2,5])*cmath.log(2) - 2*(s[1,5] + s[2,5])*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) - (1/(s[1,2]*(s[1,2] + s[1,5])**2*s[2,5]*(s[1,5] + s[2,5])))*64*(Nc**2*s[1,5]**2*s[2,5]**2*(s[1,5] + s[2,5]) + s[1,2]**3*s[1,5]*(1 + s[2,5]*(5 + cmath.log(16))) + s[1,2]*s[1,5]*(2*s[1,5]*s[2,5]**2*(5 + 2*Nc**2 + cmath.log(16)) + s[2,5]**2*(4 + 2*Nc**2*s[2,5] + cmath.log(16)) + s[1,5]**2*(1 + s[2,5]*(7 + 2*Nc**2 + cmath.log(16)))) + s[1,2]**2*(s[1,5]*s[2,5]**2*(9 + 2*Nc**2 + 8*cmath.log(4)) + s[2,5]**2*(1 + cmath.log(16)) + 2*s[1,5]**2*(1 + s[2,5]*(6 + Nc**2 + cmath.log(16)) + s[2,5]**2*(7 + cmath.log(256)))) + 2*s[1,2]*s[2,5]*(s[1,2]**2*s[1,5] + s[1,5]*(s[1,5]**2 + s[2,5] + 2*s[1,5]*s[2,5]) + s[1,2]*(s[2,5] + 4*s[1,5]*s[2,5] + s[1,5]**2*(2 + 4*s[2,5])))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))))
FFnloEPS1.append(0 + 0j)
FFnloEPS1.append((-((-1 + Nc**2)*s[1,2]*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 2*Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(3*s[1,5]*s[2,5] + s[1,2]*(3 + 2*s[1,5] + 4*s[2,5])) + 2*s[1,2]*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(3*(s[1,5] + s[2,5]) + s[1,2]*(1 + 5*s[1,5] + 4*s[2,5])) + 2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(3*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[1,5]*(2 + 4*s[2,5]) + s[1,2]*s[2,5]*(3 + 5*s[2,5])) + 4*s[1,2]*(s[1,5] + s[2,5])*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5]) - Nc**2*s[1,5]*s[2,5]*(2 + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - s[1,5]*(s[1,2] + s[1,5])*(s[1,2] - s[2,5] + s[1,2]*s[2,5])) + 4*s[1,2]*(s[1,5] + s[2,5])*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5]) - Nc**2*s[1,5]*s[2,5]*(2 + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - s[1,5]*(s[1,2] + s[1,5])*(s[1,2] - s[2,5] + s[1,2]*s[2,5]))*cmath.log(2) - 2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) - s[1,2]*s[1,5]*cmath.log(4) + s[1,2]*s[2,5]*(2 + s[1,5] + cmath.log(4)) + s[1,2]*(-s[1,5] + s[2,5])*cmath.log(-(musq/s[1,2]))) - (s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(6*Nc**2*s[1,5]*s[2,5] + s[1,2]*(s[2,5]*(4 + s[1,5]*(11 + 3*Nc**2 - 4*cmath.log(2))) + s[2,5]**2*(4 + 8*Nc**2 - 8*cmath.log(2)) - 4*s[1,5]*cmath.log(2)) - 2*s[1,2]*(s[1,5] + s[1,5]*s[2,5] + 2*s[2,5]**2)*cmath.log(-(musq/s[1,5]))) - (s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(6*Nc**2*s[1,5]*s[2,5] - 8*s[1,2]*s[1,5]**2*cmath.log(2) + s[1,2]*s[2,5]*(4 + cmath.log(16) + s[1,5]*(19 + 7*Nc**2 + cmath.log(16))) + 2*s[1,2]*(-2*s[1,5]**2 + s[2,5] + s[1,5]*s[2,5])*cmath.log(-(musq/s[2,5]))) + 2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(2*s[1,2]*s[1,5] + 2*s[2,5] + 2*s[1,2]*s[2,5] + 3*s[1,5]*s[2,5] - 2*(s[1,2]*s[1,5] + s[2,5]) - (s[1,2]*s[1,5] + s[2,5])*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + (s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*((4*s[1,2] + 6*s[1,5])*s[2,5] - 2*(s[1,5] - s[1,2]*s[2,5])*cmath.log(4) - 2*(s[1,5] - s[1,2]*s[2,5])*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) - 2*Nc**2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(2*s[1,2]*s[1,5] - 3*s[1,5]*s[2,5] - 2*s[1,2]*(s[1,5] + s[2,5]) - s[1,2]*(s[1,5] + s[2,5])*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 2*s[1,2]*(s[1,5] + s[2,5])*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5]) - Nc**2*s[1,5]*s[2,5]*(2 + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - s[1,5]*(s[1,2] + s[1,5])*(s[1,2] - s[2,5] + s[1,2]*s[2,5]))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))/(16*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])))
FFnloEPS1.append(0 + 0j)
FFnloEPS1.append((1/(128*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])**2))*(-16*Nc**2*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])**2 - 16*s[1,2]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])**2*(s[1,2] + 2*s[2,5]) + (s[1,2] + s[1,5])*(s[1,5] + s[2,5])**2*(s[1,2]**2 + 4*Nc**2*s[2,5] + 2*s[1,2]*s[2,5]) + 16*s[1,2]*(s[1,2] + s[1,5])*(2*s[1,5]*s[2,5]*(s[2,5]**2 + s[1,5]**2*(1 + s[2,5]) + s[1,5]*s[2,5]*(2 + s[2,5])) - s[1,2]*(s[1,5]*(-1 + 6*s[2,5]*(1 + cmath.log(4))) + s[2,5]*(1 + cmath.log(16))) - 2*s[1,2]*(1 + 3*s[1,5])*s[2,5]*cmath.log(-(musq/s[1,2]))) - 4*s[2,5]*(s[1,5] + s[2,5])**2*(-Nc**2*s[1,5] - 4*s[1,2]*s[1,5] + 4*s[1,2]**2*(1 + s[1,5])*(1 + cmath.log(16)) + 8*s[1,2]**2*(1 + s[1,5])*cmath.log(-(musq/s[2,5]))) + 16*s[1,2]*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])**2*(s[1,2] - 2*s[1,5] + s[1,2]*cmath.log(16) + 2*s[1,2]*cmath.log(-(musq/s[1,2])) + 2*s[1,2]*cmath.log(-(musq/s[2,5])) - 2*s[1,2]*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) - 16*(Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])**2 - 4*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5]) + s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(2*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 2*s[2,5])) + s[1,2]*s[2,5]*(s[1,5]**3 + 3*s[1,2]*s[2,5] + s[1,5]*s[2,5]*(7*s[1,2] + s[2,5]) + 2*s[1,5]**2*(s[2,5] + 2*s[1,2]*s[2,5])) - 2*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(4) - 2*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))))
FFnloEPS1.append(0 + 0j)
FFnloEPS1.append((-4*Nc**2*s[1,5]*(s[1,5] - s[2,5])*s[2,5]*(s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 4*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5]) - 2*s[2,5]*(s[1,2] + s[2,5])*(2*s[1,5]**2 + s[1,2]*s[2,5] + (2 + s[1,2])*s[1,5]*s[2,5]) + 2*s[1,5]*(s[1,2] + s[1,5])*(s[1,2]*s[1,5]*(1 + s[2,5]) + 2*s[2,5]*(s[1,5] + s[2,5])) + 4*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5])*cmath.log(2) + 2*(s[1,2] + s[1,5])*(s[1,5] - s[2,5])*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(1 + cmath.log(4)) + s[1,2]*s[1,5]*(1 + cmath.log(4) + s[2,5]*(3 + cmath.log(16))) + s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))) + (s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(3*(-1 + Nc**2)*s[1,5]*s[2,5] - 4*s[2,5]**2*cmath.log(2) - 2*s[1,2]*s[2,5]**2*cmath.log(4) + 2*s[1,2]*s[1,5]*(1 + s[2,5])*(1 + cmath.log(4)) + 2*(-s[2,5]**2 + s[1,2]*(s[1,5] + s[1,5]*s[2,5] - s[2,5]**2))*cmath.log(-(musq/s[1,5]))) - (s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(3*(-1 + Nc**2)*s[1,5]*s[2,5] - 4*s[1,5]**2*cmath.log(2) - 2*s[1,2]*s[1,5]**2*cmath.log(4) + 2*s[1,2]*(1 + s[1,5])*s[2,5]*(1 + cmath.log(4)) - 2*((1 + s[1,2])*s[1,5]**2 - s[1,2]*s[2,5] - s[1,2]*s[1,5]*s[2,5])*cmath.log(-(musq/s[2,5]))) + 2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(-s[1,2]*s[1,5] + s[1,5]*s[2,5] - (s[1,2]*s[1,5] - s[2,5]**2)*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*((s[1,2] - s[1,5])*s[2,5] - (s[1,5] - s[1,2]*s[2,5])*cmath.log(4) - (s[1,5] - s[1,2]*s[2,5])*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 2*Nc**2*(s[1,2] + s[1,5])*(s[1,5] - s[2,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5])*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))/(32*(Nc*math.pi**2*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5]))))
FFnloEPS1.append(0 + 0j)
i = 1
while i < 14:
    print("FF_nlo[", i, "] =", FFnloEPS1[i])
    i += 1
print()

print("Finite parts:")
FFnloFIN = [0]
FFnloFIN.append(((-((s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(-72*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(1 + cmath.log(2)) + s[1,2]*(-math.pi**2*s[2,5] - math.pi**2*s[1,5]*(1 + 2*s[2,5]) + 24*s[2,5]*(1 + cmath.log(2) + cmath.log(2)**2) + 24*s[1,5]*(1 + cmath.log(2) + cmath.log(2)**2 + s[2,5]*(1 + cmath.log(2) + 2*cmath.log(2)**2))) + 12*(-3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(1 + cmath.log(4)) + s[1,2]*s[1,5]*(1 + s[2,5] + cmath.log(4) + s[2,5]*cmath.log(16)))*cmath.log(-(musq/s[1,2])) + 6*s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))**2)) + (s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(24*Nc**2*s[1,5]*s[2,5]*(3 + cmath.log(4)) + s[1,2]*(math.pi**2*s[1,5]*(1 + s[2,5]) + 2*math.pi**2*s[2,5]*(1 + 2*s[2,5]) + 12*s[2,5]*(-4*cmath.log(2)**2 + s[2,5]*(1 + Nc**2 - 8*cmath.log(2)**2)) + 12*s[1,5]*(-2 - 2*cmath.log(2)**2 - cmath.log(4) + s[2,5]*(10 - 2*cmath.log(2)**2 + Nc**2*(2 + cmath.log(2)) + cmath.log(512)))) + 6*(4*Nc**2*s[1,5]*s[2,5] + s[1,2]*s[1,5]*(-2 + s[2,5]*(9 + Nc**2 - 4*cmath.log(2)) - 4*cmath.log(2)) - 8*s[1,2]*s[2,5]*(1 + 2*s[2,5])*cmath.log(2))*cmath.log(-(musq/s[1,5])) - 6*s[1,2]*(s[1,5] + 2*s[2,5] + s[1,5]*s[2,5] + 4*s[2,5]**2)*cmath.log(-(musq/s[1,5]))**2) + s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(math.pi**2*s[1,2]*(4*s[1,5]**2 + s[2,5] + s[1,5]*(2 + s[2,5])) + 12*(Nc**2*s[1,5]*s[2,5]*(6 + cmath.log(16)) + s[1,2]*(-4*s[1,5]*cmath.log(2)**2 + s[1,5]**2*(1 + Nc**2 - 8*cmath.log(2)**2) - s[2,5]*(2 + 2*cmath.log(2)**2 + cmath.log(4)) + s[1,5]*s[2,5]*(10 - 2*cmath.log(2)**2 + Nc**2*(2 + cmath.log(2)) + cmath.log(512)))) + 6*(4*Nc**2*s[1,5]*s[2,5] + s[1,2]*s[2,5]*(-2 + s[1,5]*(9 + Nc**2 - 4*cmath.log(2)) - 4*cmath.log(2)) - 8*s[1,2]*s[1,5]*(1 + 2*s[1,5])*cmath.log(2))*cmath.log(-(musq/s[2,5])) - 6*s[1,2]*(4*s[1,5]**2 + s[2,5] + s[1,5]*(2 + s[2,5]))*cmath.log(-(musq/s[2,5]))**2) - 3*(-4*(-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - 4*(-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 8*s[1,5]*(s[1,2] + s[1,5])*(3*s[2,5]**2*(s[1,5] + s[2,5]) + 2*s[1,2]*s[2,5]*(s[1,5] + 2*s[2,5]) + s[1,2]**2*(s[1,5] + 3*s[2,5])) + 8*Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[1,2]**2 + 2*s[1,5]*s[2,5] + s[1,2]*(s[1,5] + s[2,5] + s[1,5]*s[2,5])) + 8*s[2,5]*(s[1,2] + s[2,5])*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[1,5] + s[2,5] + 6*s[1,5]*s[2,5])) + 4*s[2,5]*(2*s[1,5]*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - 2*Nc**2*s[1,5]*(s[1,5] + s[2,5])*(s[1,2]*s[1,5] - s[1,5]*s[2,5] + s[1,2]**2*(1 + s[2,5])) - 2*s[1,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5]))) - math.pi**2*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5])))) - 4*(4 - math.pi**2/3)*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5])))) + 2*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 2*s[1,5]*(s[1,2] + s[1,5])*(3*s[2,5]**2*(s[1,5] + s[2,5]) + 2*s[1,2]*s[2,5]*(s[1,5] + 2*s[2,5]) + s[1,2]**2*(s[1,5] + 3*s[2,5])) + 2*Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[1,2]**2 + 2*s[1,5]*s[2,5] + s[1,2]*(s[1,5] + s[2,5] + s[1,5]*s[2,5])) + 2*s[2,5]*(s[1,2] + s[2,5])*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[1,5] + s[2,5] + 6*s[1,5]*s[2,5])))*cmath.log(4) - 8*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5]))))*cmath.log(4) - 2*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5]))))*cmath.log(4)**2 - 8*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5]))))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 2*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 2*s[1,5]*(s[1,2] + s[1,5])*(3*s[2,5]**2*(s[1,5] + s[2,5]) + 2*s[1,2]*s[2,5]*(s[1,5] + 2*s[2,5]) + s[1,2]**2*(s[1,5] + 3*s[2,5])) + 2*Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[1,2]**2 + 2*s[1,5]*s[2,5] + s[1,2]*(s[1,5] + s[2,5] + s[1,5]*s[2,5])) + 2*s[2,5]*(s[1,2] + s[2,5])*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[1,5] + s[2,5] + 6*s[1,5]*s[2,5])) - 2*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5]))))*cmath.log(4))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) - 2*(-((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(2*s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]**2 - s[1,2]*s[2,5] - s[2,5]**2) + Nc**2*s[1,2]*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5] + 2*s[1,2]*(1 + s[2,5]) + s[1,5]*(2 + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + s[1,5])*(s[2,5] + s[1,5]*(2 + 3*s[2,5]))))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2) - 2*Nc**2*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(36*s[1,5]*s[2,5] - 1/2*math.pi**2*s[1,2]*(2 + s[1,5] + s[2,5]) + 12*s[1,5]*s[2,5]*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) - s[1,2]*(2 + s[1,5] + s[2,5])*(math.pi**2 + 3*cmath.log(s[2,5]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))))) + (s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(48*(s[1,5]**2 + s[1,2]*(2*s[1,5] + s[2,5])) - math.pi**2*(s[1,5]**2 + s[1,2]*(2*s[1,5] + s[2,5])) - 24*(s[1,2]*(4*s[1,5] + s[2,5]) + s[1,5]*(2*s[1,5] + 3*s[2,5])) + 12*(s[1,2] - 3*s[1,5])*s[2,5]*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) - 2*(s[1,5]**2 + s[1,2]*(2*s[1,5] + s[2,5]))*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[2,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2]))))) - (s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(math.pi**2*(s[2,5]**2 + s[1,2]*(s[1,5] + 2*s[2,5])) + 24*(s[2,5]*(3*s[1,5] + 2*s[2,5]) + s[1,2]*(s[1,5] + 4*s[2,5]))*(1 + cmath.log(2)) - 24*(s[2,5]**2 + s[1,2]*(s[1,5] + 2*s[2,5]))*(2 + cmath.log(2)**2 + cmath.log(4)) - 12*(s[2,5]*(-3*s[1,5] + s[2,5]*cmath.log(4)) + s[1,2]*(s[1,5] + s[1,5]*cmath.log(4) + s[2,5]*cmath.log(16)))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*(s[2,5]**2 + s[1,2]*(s[1,5] + 2*s[2,5]))*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2]))))))*(192*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5]))))
FFnloFIN.append(0 + 0j)
FFnloFIN.append(-(1/(192*(Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])**2*s[2,5]*(s[1,2] + s[2,5]))))*((s[1,2] + s[1,5])**2*(s[1,2] + s[2,5])*(72*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(1 + cmath.log(2)) + s[1,2]*(-math.pi**2*s[2,5] - math.pi**2*s[1,5]*(1 + 2*s[2,5]) + 24*s[2,5]*(1 + cmath.log(2) + cmath.log(2)**2) + 24*s[1,5]*(3 + cmath.log(2)**2 + cmath.log(8) + s[2,5]*(5 + 2*cmath.log(2)**2 + cmath.log(32)))) + 12*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(1 + cmath.log(4)) + s[1,2]*s[1,5]*(3 + cmath.log(4) + s[2,5]*(5 + cmath.log(16))))*cmath.log(-(musq/s[1,2])) + 6*s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))**2) + (s[1,2] + s[1,5])**2*(96*Nc**2*s[1,5]*s[2,5]*(1 + cmath.log(2)) + s[1,2]*(-math.pi**2*s[1,5]*(1 + s[2,5]) + 2*s[2,5]**2*(6 + 6*Nc**2 + math.pi**2 - 24*cmath.log(2)**2) + 12*s[1,5]*(6 + 2*cmath.log(2)**2 + s[2,5]*(23 + 21*cmath.log(2) + 2*cmath.log(2)**2 + Nc**2*(19 + 17*cmath.log(2))) + cmath.log(64))) + 6*(8*Nc**2*s[1,5]*s[2,5] - 8*s[1,2]*s[2,5]**2*cmath.log(2) + s[1,2]*s[1,5]*(6 + cmath.log(16) + s[2,5]*(21 + 17*Nc**2 + cmath.log(16))))*cmath.log(-(musq/s[1,5])) + 6*s[1,2]*(s[1,5] + s[1,5]*s[2,5] - 2*s[2,5]**2)*cmath.log(-(musq/s[1,5]))**2) + s[2,5]*(s[1,2] + s[2,5])*(96*Nc**2*s[1,5]*s[2,5]*(1 + cmath.log(2)) + s[1,2]*(s[2,5]*(-math.pi**2 + 24*(1 + cmath.log(2) + cmath.log(2)**2)) + s[1,5]*(-math.pi**2*(2 + 3*s[2,5]) + 24*(4 + 2*cmath.log(2)**2 + cmath.log(16) + s[2,5]*(20 + 19*cmath.log(2) + 3*cmath.log(2)**2 + Nc**2*(9 + cmath.log(256))))) + s[1,5]**2*(408 - 2*math.pi**2 + 384*cmath.log(2) + 48*cmath.log(2)**2 + 24*Nc**2*(13 + cmath.log(4096)))) + 12*(4*Nc**2*s[1,5]*s[2,5] + s[1,2]*(s[2,5]*(1 + cmath.log(4)) + s[1,5]**2*(16 + 12*Nc**2 + cmath.log(16)) + s[1,5]*(4 + cmath.log(16) + s[2,5]*(19 + 8*Nc**2 + cmath.log(64)))))*cmath.log(-(musq/s[2,5])) + 6*s[1,2]*(2*s[1,5]**2 + s[2,5] + s[1,5]*(2 + 3*s[2,5]))*cmath.log(-(musq/s[2,5]))**2) - 3*(8*s[1,2]*s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + 3*s[2,5] + 4*s[1,2]*s[2,5]) + 4*s[1,2]*s[2,5]*(2*(1 + s[1,2])*s[1,5]*(s[1,2] + s[1,5])**2 + 2*(1 + s[1,2])*s[1,5]*s[2,5]*(s[1,2] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])) - 4*(-1 + Nc**2)*s[1,2]*(s[1,2] + s[1,5])**2*s[2,5]*(s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(2*s[1,5] + s[2,5])) - 4*(-1 + Nc**2)*s[1,2]*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + 2*s[1,5] + 3*s[2,5])) + 8*s[1,2]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]**3*s[1,5] + 4*s[1,2]**2*s[1,5]**2 + 3*s[1,5]*s[2,5] + s[1,2]*(3*s[1,5]**3 - s[2,5] + 8*s[1,5]*s[2,5])) + math.pi**2*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2))) + 4*(4 - math.pi**2/3)*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2))) + 8*Nc**2*s[1,5]*s[2,5]*(4*s[1,5]*s[2,5] + s[1,2]*(1 + 7*s[2,5] + 7*s[1,5]**2*s[2,5] + s[1,5]*(7 + 11*s[2,5] + 7*s[2,5]**2))) + 16*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2)))*cmath.log(2) + 4*(2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + 3*s[2,5] + 4*s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,2]*(s[1,2] + s[1,5])**2*s[2,5]*(s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(2*s[1,5] + s[2,5])) - (-1 + Nc**2)*s[1,2]*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + 2*s[1,5] + 3*s[2,5])) + 2*s[1,2]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]**3*s[1,5] + 4*s[1,2]**2*s[1,5]**2 + 3*s[1,5]*s[2,5] + s[1,2]*(3*s[1,5]**3 - s[2,5] + 8*s[1,5]*s[2,5])) + 2*Nc**2*s[1,5]*s[2,5]*(4*s[1,5]*s[2,5] + s[1,2]*(1 + 7*s[2,5] + 7*s[1,5]**2*s[2,5] + s[1,5]*(7 + 11*s[2,5] + 7*s[2,5]**2))))*cmath.log(2) + 8*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2)))*cmath.log(2)**2 + 8*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2)))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 2*(2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + 3*s[2,5] + 4*s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,2]*(s[1,2] + s[1,5])**2*s[2,5]*(s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(2*s[1,5] + s[2,5])) - (-1 + Nc**2)*s[1,2]*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + 2*s[1,5] + 3*s[2,5])) + 2*s[1,2]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]**3*s[1,5] + 4*s[1,2]**2*s[1,5]**2 + 3*s[1,5]*s[2,5] + s[1,2]*(3*s[1,5]**3 - s[2,5] + 8*s[1,5]*s[2,5])) + 2*Nc**2*s[1,5]*s[2,5]*(4*s[1,5]*s[2,5] + s[1,2]*(1 + 7*s[2,5] + 7*s[1,5]**2*s[2,5] + s[1,5]*(7 + 11*s[2,5] + 7*s[2,5]**2))) + 4*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2)))*cmath.log(2))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 2*s[1,2]*((-1 + Nc**2)*(s[1,2] + s[1,5])**2*s[2,5]**2*(s[1,2] + s[1,5] + s[2,5]) + s[1,5]*(s[1,2] + s[1,5])**2*(s[1,2] + s[2,5] + s[1,2]*s[2,5]) - (-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(s[1,2]*(1 + s[2,5]) - s[1,5]*(s[1,5] + s[2,5])) + s[2,5]*(s[1,2] + s[2,5])*(2*s[1,2]**3*s[1,5] + 2*s[1,2]**2*s[1,5]**2 + s[1,5]*s[2,5] + s[1,2]*(s[2,5] + 2*s[1,5]*s[2,5])) - Nc**2*s[1,5]*s[2,5]*(-2 - 3*s[2,5] + s[1,5]**2*s[2,5] + s[1,5]*(-2 + s[2,5] + s[2,5]**2)))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2) + Nc**2*(s[1,2] + s[1,5])**2*s[2,5]*(s[1,2] + s[2,5])*(math.pi**2*s[1,2]*(s[1,5] + s[2,5]) - 48*(s[1,2]*(s[1,5] - s[2,5]) + 2*s[1,5]*s[2,5])*(1 + cmath.log(2)) - 24*s[1,2]*(s[1,5] + s[2,5])*(2 + cmath.log(2)**2 + cmath.log(4)) - 24*(2*s[1,5]*s[2,5] + s[1,2]*s[2,5]*cmath.log(2) + s[1,2]*s[1,5]*(2 + cmath.log(2)))*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*s[1,2]*(s[1,5] + s[2,5])*(math.pi**2 + 3*cmath.log(s[2,5]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))))) - (s[1,2] + s[1,5])**2*s[2,5]*(s[1,2] + s[2,5])*(24*(2*s[1,5]**2 - s[1,2]*s[2,5] + 3*s[1,5]*s[2,5]) + math.pi**2*(s[1,5]**2 - s[1,2]*(2*s[1,5] + s[2,5])) + 48*(-s[1,5]**2 + s[1,2]*(2*s[1,5] + s[2,5])) + 12*(3*s[1,5]*s[2,5] + s[1,2]*(4*s[1,5] + s[2,5]))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*(s[1,5]**2 - s[1,2]*(2*s[1,5] + s[2,5]))*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[2,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2]))))) + (s[1,2] + s[1,5])**2*(s[1,2] + s[2,5])*(math.pi**2*(s[1,2]*s[1,5] - s[2,5]**2) - 24*(s[1,2]*s[1,5] + s[2,5]*(3*s[1,5] + 2*s[2,5]))*(1 + cmath.log(2)) - 24*(s[1,2]*s[1,5] - s[2,5]**2)*(2 + cmath.log(2)**2 + cmath.log(4)) - 12*(s[1,2]*s[1,5]*(3 + cmath.log(4)) + s[2,5]*(3*s[1,5] - s[2,5]*cmath.log(4)))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*(s[1,2]*s[1,5] - s[2,5]**2)*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2])))))))
FFnloFIN.append((1/(192*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2))*((s[1,2] + s[1,5])*(s[1,2] + s[2,5])**2*(72*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(1 + cmath.log(2)) + s[1,2]*(-math.pi**2*s[2,5] - math.pi**2*s[1,5]*(1 + 2*s[2,5]) + 24*s[2,5]*(3 + cmath.log(2)**2 + cmath.log(8)) + 24*s[1,5]*(1 + cmath.log(2) + cmath.log(2)**2 + s[2,5]*(5 + 2*cmath.log(2)**2 + cmath.log(32)))) + 12*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(3 + cmath.log(4)) + s[1,2]*s[1,5]*(1 + cmath.log(4) + s[2,5]*(5 + cmath.log(16))))*cmath.log(-(musq/s[1,2])) + 6*s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))**2) + s[1,5]*(s[1,2] + s[1,5])*(96*Nc**2*s[1,5]*s[2,5]*(1 + cmath.log(2)) + s[1,2]*(-2*math.pi**2*s[2,5]*(1 + s[2,5]) + s[1,5]*(-math.pi**2*(1 + 3*s[2,5]) + 24*(1 + cmath.log(2) + cmath.log(2)**2 + s[2,5]*(20 + 19*cmath.log(2) + 3*cmath.log(2)**2 + Nc**2*(9 + cmath.log(256))))) + 24*s[2,5]*(4 + 2*cmath.log(2)**2 + cmath.log(16) + s[2,5]*(17 + 16*cmath.log(2) + 2*cmath.log(2)**2 + Nc**2*(13 + cmath.log(4096))))) + 12*(4*Nc**2*s[1,5]*s[2,5] + s[1,2]*s[2,5]*(4 + cmath.log(16) + s[2,5]*(16 + 12*Nc**2 + cmath.log(16))) + s[1,2]*s[1,5]*(1 + cmath.log(4) + s[2,5]*(19 + 8*Nc**2 + cmath.log(64))))*cmath.log(-(musq/s[1,5])) + 6*s[1,2]*(s[1,5] + 3*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5]))*cmath.log(-(musq/s[1,5]))**2) + (s[1,2] + s[2,5])**2*(96*Nc**2*s[1,5]*s[2,5]*(1 + cmath.log(2)) + s[1,2]*(2*s[1,5]**2*(6 + 6*Nc**2 + math.pi**2 - 24*cmath.log(2)**2) + s[1,5]*s[2,5]*(276 - math.pi**2 + 252*cmath.log(2) + 24*cmath.log(2)**2 + 12*Nc**2*(19 + 17*cmath.log(2))) + s[2,5]*(-math.pi**2 + 24*(3 + cmath.log(2)**2 + cmath.log(8)))) + 6*(8*Nc**2*s[1,5]*s[2,5] - 8*s[1,2]*s[1,5]**2*cmath.log(2) + s[1,2]*s[2,5]*(6 + cmath.log(16) + s[1,5]*(21 + 17*Nc**2 + cmath.log(16))))*cmath.log(-(musq/s[2,5])) + 6*s[1,2]*(-2*s[1,5]**2 + s[2,5] + s[1,5]*s[2,5])*cmath.log(-(musq/s[2,5]))**2) - 3*(8*s[1,2]*(s[1,2] + 3*s[1,5] + 4*s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + 4*s[1,2]*s[1,5]*(2*(1 + s[1,2])*s[1,5]*(s[1,2] + s[1,5])*s[2,5] + 2*(1 + s[1,2])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])**2*(s[1,5] + s[2,5])) - 4*(-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[2,5])**2*(s[1,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 2*s[2,5])) - 4*(-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + 3*s[1,5] + 2*s[2,5])) + 8*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(3*s[1,5]*s[2,5] + s[1,2]*(-s[1,5] + s[2,5] + 8*s[1,5]*s[2,5] + 7*s[2,5]**2)) + 8*Nc**2*s[1,5]*s[2,5]*(4*s[1,5]*s[2,5] + s[1,2]*(1 + 7*s[2,5] + 7*s[1,5]**2*s[2,5] + s[1,5]*(7 + 11*s[2,5] + 7*s[2,5]**2))) + math.pi**2*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5])))) + 4*(4 - math.pi**2/3)*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5])))) + 16*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5]))))*cmath.log(2) + 4*(2*s[1,2]*(s[1,2] + 3*s[1,5] + 4*s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 - (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[2,5])**2*(s[1,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 2*s[2,5])) - (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + 3*s[1,5] + 2*s[2,5])) + 2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(3*s[1,5]*s[2,5] + s[1,2]*(-s[1,5] + s[2,5] + 8*s[1,5]*s[2,5] + 7*s[2,5]**2)) + 2*Nc**2*s[1,5]*s[2,5]*(4*s[1,5]*s[2,5] + s[1,2]*(1 + 7*s[2,5] + 7*s[1,5]**2*s[2,5] + s[1,5]*(7 + 11*s[2,5] + 7*s[2,5]**2))))*cmath.log(2) + 8*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5]))))*cmath.log(2)**2 + 8*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5]))))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 2*(2*s[1,2]*(s[1,2] + 3*s[1,5] + 4*s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 - (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[2,5])**2*(s[1,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 2*s[2,5])) - (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(1 + 3*s[1,5] + 2*s[2,5])) + 2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(3*s[1,5]*s[2,5] + s[1,2]*(-s[1,5] + s[2,5] + 8*s[1,5]*s[2,5] + 7*s[2,5]**2)) + 2*Nc**2*s[1,5]*s[2,5]*(4*s[1,5]*s[2,5] + s[1,2]*(1 + 7*s[2,5] + 7*s[1,5]**2*s[2,5] + s[1,5]*(7 + 11*s[2,5] + 7*s[2,5]**2))) + 4*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5]))))*cmath.log(2))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 2*s[1,2]*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5])**2 + (-1 + Nc**2)*s[1,5]**2*(s[1,2] + s[2,5])**2*(s[1,2] + s[1,5] + s[2,5]) - (-1 + Nc**2)*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2]*(1 + s[1,5]) - s[2,5]*(s[1,5] + s[2,5])) - Nc**2*s[1,5]*s[2,5]*(s[1,5]**2*s[2,5] - 2*(1 + s[2,5]) + s[1,5]*(-3 + s[2,5] + s[2,5]**2)) + s[1,5]*(s[1,2] + s[1,5])*(s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 2*s[1,5]*s[2,5] + 2*s[2,5]*(1 + s[2,5]))))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2) + Nc**2*s[1,5]*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])**2*(math.pi**2*s[1,2]*(s[1,5] + s[2,5]) + 48*(s[1,2]*(s[1,5] - s[2,5]) - 2*s[1,5]*s[2,5])*(1 + cmath.log(2)) - 24*s[1,2]*(s[1,5] + s[2,5])*(2 + cmath.log(2)**2 + cmath.log(4)) - 24*(2*s[1,5]*s[2,5] + s[1,2]*s[1,5]*cmath.log(2) + s[1,2]*s[2,5]*(2 + cmath.log(2)))*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*s[1,2]*(s[1,5] + s[2,5])*(math.pi**2 + 3*cmath.log(s[2,5]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))))) - (s[1,2] + s[1,5])*(s[1,2] + s[2,5])**2*(math.pi**2*(s[1,5] - s[1,2]*s[2,5]) + 24*(s[1,2]*s[2,5] + s[1,5]*(2 + 3*s[2,5]))*(1 + cmath.log(2)) - 24*(s[1,5] - s[1,2]*s[2,5])*(2 + cmath.log(2)**2 + cmath.log(4)) + 12*(s[1,5]*(3*s[2,5] - cmath.log(4)) + s[1,2]*s[2,5]*(3 + cmath.log(4)))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*(s[1,5] - s[1,2]*s[2,5])*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[2,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2]))))) + s[1,5]*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])**2*(48*(s[2,5]**2 - s[1,2]*(s[1,5] + 2*s[2,5])) + math.pi**2*(-s[2,5]**2 + s[1,2]*(s[1,5] + 2*s[2,5])) + 24*(s[1,2]*s[1,5] - s[2,5]*(3*s[1,5] + 2*s[2,5])) - 12*(3*s[1,5]*s[2,5] + s[1,2]*(s[1,5] + 4*s[2,5]))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*(-s[2,5]**2 + s[1,2]*(s[1,5] + 2*s[2,5]))*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2])))))))
FFnloFIN.append(-(1/(192*(Nc*math.pi**2*s[1,5]*s[2,5])))*(24*(s[1,2] + s[1,5])*s[2,5] - math.pi**2*(s[1,5] + s[1,2]*s[2,5]) - 48*(s[1,2]*s[1,5] + s[2,5]**2) + math.pi**2*(s[1,2]*s[1,5] + s[2,5]**2) + 24*(s[1,2]*s[1,5] + s[2,5]*(-s[1,5] + 2*s[2,5])) + 12*(s[1,2] + s[1,5])*s[2,5]*cmath.log(4) + 6*(s[1,5] + s[1,2]*s[2,5])*cmath.log(4)**2 + (1/(s[1,5] + s[2,5]))*(s[1,5] - s[2,5])*(24*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(1 + cmath.log(2)) + s[1,2]*(-math.pi**2*s[2,5] - math.pi**2*s[1,5]*(1 + 2*s[2,5]) + 24*s[2,5]*(1 + cmath.log(2) + cmath.log(2)**2) + 24*s[1,5]*(1 + cmath.log(2) + cmath.log(2)**2 + s[2,5]*(3 + 2*cmath.log(2)**2 + cmath.log(8)))) + 12*(s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(1 + cmath.log(4)) + s[1,2]*s[1,5]*(1 + cmath.log(4) + s[2,5]*(3 + cmath.log(16))))*cmath.log(-(musq/s[1,2])) + 6*s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))**2) - (1/(s[1,2] + s[2,5]))*(s[2,5]*(12*(-5 + Nc**2)*s[1,5]*(1 + cmath.log(2)) + s[2,5]*(6 + 6*Nc**2 + math.pi**2 - 24*cmath.log(2)**2)) + s[1,2]*(math.pi**2*s[1,5]*(1 + s[2,5]) + s[2,5]**2*(6 + 6*Nc**2 + math.pi**2 - 24*cmath.log(2)**2) - 24*s[1,5]*(1 + cmath.log(2) + cmath.log(2)**2 + s[2,5]*(3 + cmath.log(2)**2 + cmath.log(8)))) - 6*(2*s[1,2]*(s[2,5]**2*cmath.log(4) + s[1,5]*(1 + cmath.log(4) + s[2,5]*(3 + cmath.log(4)))) + s[2,5]*(-((-5 + Nc**2)*s[1,5]) + s[2,5]*cmath.log(16)))*cmath.log(-(musq/s[1,5])) - 6*(s[2,5]**2 + s[1,2]*(s[1,5] + s[1,5]*s[2,5] + s[2,5]**2))*cmath.log(-(musq/s[1,5]))**2) - (1/(s[1,2] + s[1,5]))*(-((1 + s[1,2])*s[1,5]**2*(6 + 6*Nc**2 + math.pi**2 - 24*cmath.log(2)**2)) + s[1,2]*s[2,5]*(-math.pi**2 + 24*(1 + cmath.log(2) + cmath.log(2)**2)) + s[1,5]*s[2,5]*(-math.pi**2*s[1,2] + 60*(1 + cmath.log(2)) - 12*Nc**2*(1 + cmath.log(2)) + 24*s[1,2]*(3 + cmath.log(2)**2 + cmath.log(8))) + 6*(2*s[1,2]*(s[1,5]**2*cmath.log(4) + s[2,5]*(1 + cmath.log(4) + s[1,5]*(3 + cmath.log(4)))) + s[1,5]*(-((-5 + Nc**2)*s[2,5]) + s[1,5]*cmath.log(16)))*cmath.log(-(musq/s[2,5])) + 6*((1 + s[1,2])*s[1,5]**2 + s[1,2]*s[2,5] + s[1,2]*s[1,5]*s[2,5])*cmath.log(-(musq/s[2,5]))**2) - 12*s[1,5]*(s[1,2] + s[2,5])*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 12*(s[1,2]*s[2,5]*(1 + cmath.log(4)) + s[1,5]*(s[2,5] + cmath.log(4)))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + (1/((s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])))*(s[1,5] - s[2,5])*(s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(-12 - math.pi**2 - 24*cmath.log(2) + 24*cmath.log(2)**2 + Nc**2*(math.pi**2 - 12*(3 + 2*cmath.log(2)**2 + cmath.log(4)))) + s[1,2]*(s[2,5]*(1 + s[2,5])*(math.pi**2 - 24*(1 + cmath.log(2) + cmath.log(2)**2)) + s[1,5]**2*(1 + s[2,5])*(math.pi**2*(1 + 2*Nc**2*s[2,5]) - 24*(1 + cmath.log(2) + cmath.log(2)**2 + s[2,5]*(3 + Nc**2*(4 + 2*cmath.log(2)**2 + cmath.log(8)) + cmath.log(16)))) + s[1,5]*(math.pi**2*(1 + 4*s[2,5] + (1 + 2*Nc**2)*s[2,5]**2) - 24*(1 + cmath.log(2) + cmath.log(2)**2 + s[2,5]*(5 + 4*cmath.log(2)**2 + cmath.log(32)) + s[2,5]**2*(4 + cmath.log(2)**2 + Nc**2*(4 + 2*cmath.log(2)**2 + cmath.log(8)) + cmath.log(32))))) - 12*(s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(1 - cmath.log(4) + Nc**2*(1 + cmath.log(4))) + s[1,2]*(s[2,5]*(1 + s[2,5])*(1 + cmath.log(4)) + s[1,5]**2*(1 + s[2,5])*(1 + cmath.log(4) + s[2,5]*(4 + Nc**2*(3 + cmath.log(16)))) + s[1,5]*(1 + cmath.log(4) + s[2,5]**2*(5 + cmath.log(4) + Nc**2*(3 + cmath.log(16))) + s[2,5]*(5 + cmath.log(256)))))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) - 6*((-1 + Nc**2)*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 4*s[1,5]*s[2,5] + (1 + 2*Nc**2)*s[1,5]*s[2,5]**2 + s[2,5]*(1 + s[2,5]) + s[1,5]**2*(1 + s[2,5] + 2*Nc**2*s[2,5] + 2*Nc**2*s[2,5]**2)))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2) + 3*Nc**2*(s[1,5] - s[2,5])*(math.pi**2 + 2*cmath.log(s[2,5]/(4*s[1,5]))**2 - 2*cmath.log(-(musq/s[1,5]))**2 - 2*cmath.log(-(musq/s[2,5]))**2 + 2*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 4*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 4*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5])))) - 2*(s[1,5] + s[1,2]*s[2,5])*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[2,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2])))) + 2*(s[1,2]*s[1,5] + s[2,5]**2)*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2]))))))
FFnloFIN.append(0 + 0j)
FFnloFIN.append(0 + 0j)
FFnloFIN.append(-((s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(36*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(2 + cmath.log(4)) + s[1,2]*(math.pi**2*s[1,5] - math.pi**2*s[2,5] + 6*s[1,5]*(-2 - cmath.log(4)**2 + s[2,5]*(6 + cmath.log(16))) + 6*s[2,5]*(6 + cmath.log(4)**2 + cmath.log(256))) + 12*(3*s[1,5]*s[2,5]*(s[1,5] + s[2,5]) - s[1,2]*s[1,5]*cmath.log(4) + s[1,2]*s[2,5]*(2 + s[1,5] + cmath.log(4)))*cmath.log(-(musq/s[1,2])) + 6*s[1,2]*(-s[1,5] + s[2,5])*cmath.log(-(musq/s[1,2]))**2) + (s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(12*Nc**2*s[1,5]*s[2,5]*(7 + cmath.log(64)) + s[1,2]*(math.pi**2*s[1,5]*(1 + s[2,5]) + 48*s[2,5]*(1 + cmath.log(2)) + 2*s[2,5]**2*(math.pi**2 + 6*(5 - 4*cmath.log(2)**2 + cmath.log(16)) + 6*Nc**2*(9 + cmath.log(256))) + 12*s[1,5]*(-1 - 2*cmath.log(2)**2 + s[2,5]*(12 - 2*cmath.log(2)**2 + Nc**2*(4 + cmath.log(8)) + cmath.log(2048)))) + 6*(6*Nc**2*s[1,5]*s[2,5] + s[1,2]*(s[2,5]*(4 + s[1,5]*(11 + 3*Nc**2 - 4*cmath.log(2))) + s[2,5]**2*(4 + 8*Nc**2 - 8*cmath.log(2)) - 4*s[1,5]*cmath.log(2)))*cmath.log(-(musq/s[1,5])) - 6*s[1,2]*(s[1,5] + s[1,5]*s[2,5] + 2*s[2,5]**2)*cmath.log(-(musq/s[1,5]))**2) + (s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(12*Nc**2*s[1,5]*s[2,5]*(7 + cmath.log(64)) + s[1,2]*(2*s[1,5]**2*(6 + 6*Nc**2 + math.pi**2 - 24*cmath.log(2)**2) + s[2,5]*(-math.pi**2 + 12*(3 + 2*cmath.log(2)**2 + cmath.log(16))) + s[1,5]*s[2,5]*(240 - math.pi**2 + 228*cmath.log(2) + 24*cmath.log(2)**2 + 12*Nc**2*(8 + cmath.log(128)))) + 6*(6*Nc**2*s[1,5]*s[2,5] - 8*s[1,2]*s[1,5]**2*cmath.log(2) + s[1,2]*s[2,5]*(4 + cmath.log(16) + s[1,5]*(19 + 7*Nc**2 + cmath.log(16))))*cmath.log(-(musq/s[2,5])) + 6*s[1,2]*(-2*s[1,5]**2 + s[2,5] + s[1,5]*s[2,5])*cmath.log(-(musq/s[2,5]))**2) - 3*(-4*(-1 + Nc**2)*s[1,2]*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - 4*(-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 8*Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(3*s[1,5]*s[2,5] + s[1,2]*(3 + 2*s[1,5] + 4*s[2,5])) + 8*s[1,2]*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(3*(s[1,5] + s[2,5]) + s[1,2]*(1 + 5*s[1,5] + 4*s[2,5])) + 8*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(3*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[1,5]*(2 + 4*s[2,5]) + s[1,2]*s[2,5]*(3 + 5*s[2,5])) + math.pi**2*s[1,2]*(s[1,5] + s[2,5])*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5]) - Nc**2*s[1,5]*s[2,5]*(2 + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - s[1,5]*(s[1,2] + s[1,5])*(s[1,2] - s[2,5] + s[1,2]*s[2,5])) - 4/3*(-12 + math.pi**2)*s[1,2]*(s[1,5] + s[2,5])*(s[1,2]**2*((-2 + Nc**2)*s[1,5] + Nc**2*s[2,5]) + s[1,2]*(s[1,5]**2*(-2 + Nc**2 - s[2,5]) + Nc**2*s[2,5]**2 + s[1,5]*s[2,5]*(-2 + 4*Nc**2 + s[2,5])) + s[1,5]*s[2,5]*(-s[1,5] - s[2,5] + Nc**2*(-2 + s[1,5] + s[2,5]))) - 4*(-((-1 + Nc**2)*s[1,2]*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(s[1,2] + s[2,5])*(-((2 + s[1,2])*s[1,5]**2) + s[1,2]*s[2,5] - 2*s[1,5]*s[2,5]) + Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] - s[1,5]*s[2,5]) + s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(-2*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] - s[2,5]**2))) + 16*s[1,2]*(s[1,5] + s[2,5])*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5]) - Nc**2*s[1,5]*s[2,5]*(2 + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - s[1,5]*(s[1,2] + s[1,5])*(s[1,2] - s[2,5] + s[1,2]*s[2,5]))*cmath.log(2) + 4*(-((-1 + Nc**2)*s[1,2]*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 2*Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(3*s[1,5]*s[2,5] + s[1,2]*(3 + 2*s[1,5] + 4*s[2,5])) + 2*s[1,2]*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(3*(s[1,5] + s[2,5]) + s[1,2]*(1 + 5*s[1,5] + 4*s[2,5])) + 2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(3*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[1,5]*(2 + 4*s[2,5]) + s[1,2]*s[2,5]*(3 + 5*s[2,5])))*cmath.log(2) + 8*s[1,2]*(s[1,5] + s[2,5])*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5]) - Nc**2*s[1,5]*s[2,5]*(2 + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - s[1,5]*(s[1,2] + s[1,5])*(s[1,2] - s[2,5] + s[1,2]*s[2,5]))*cmath.log(2)**2 + 8*s[1,2]*(s[1,5] + s[2,5])*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5]) - Nc**2*s[1,5]*s[2,5]*(2 + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - s[1,5]*(s[1,2] + s[1,5])*(s[1,2] - s[2,5] + s[1,2]*s[2,5]))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 2*(-((-1 + Nc**2)*s[1,2]*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5])) - (-1 + Nc**2)*s[1,2]*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 2*Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(3*s[1,5]*s[2,5] + s[1,2]*(3 + 2*s[1,5] + 4*s[2,5])) + 2*s[1,2]*s[1,5]*s[2,5]*(s[1,2] + s[2,5])*(3*(s[1,5] + s[2,5]) + s[1,2]*(1 + 5*s[1,5] + 4*s[2,5])) + 2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(3*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[1,5]*(2 + 4*s[2,5]) + s[1,2]*s[2,5]*(3 + 5*s[2,5])) + 4*s[1,2]*(s[1,5] + s[2,5])*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5]) - Nc**2*s[1,5]*s[2,5]*(2 + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - s[1,5]*(s[1,2] + s[1,5])*(s[1,2] - s[2,5] + s[1,2]*s[2,5]))*cmath.log(2))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 2*s[1,2]*(s[1,5] + s[2,5])*((s[1,2] + s[1,5] + s[1,2]*s[1,5])*s[2,5]*(s[1,2] + s[2,5]) - Nc**2*s[1,5]*s[2,5]*(2 + s[1,5] + s[2,5]) + (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) - s[1,5]*(s[1,2] + s[1,5])*(s[1,2] - s[2,5] + s[1,2]*s[2,5]))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2) - Nc**2*(s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(-48*s[1,2]*s[1,5] + 84*s[1,5]*s[2,5] + 48*s[1,2]*(s[1,5] + s[2,5]) - math.pi**2*s[1,2]*(s[1,5] + s[2,5]) + 12*(2*s[1,2] + 3*s[1,5])*s[2,5]*(cmath.log(-(musq/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) - 2*s[1,2]*(s[1,5] + s[2,5])*(math.pi**2 + 3*cmath.log(s[2,5]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))))) - (s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(36*(s[1,2] + 2*s[1,5])*s[2,5] + math.pi**2*(s[1,5] - s[1,2]*s[2,5]) + 6*(4*s[1,2] + 6*s[1,5])*s[2,5]*cmath.log(4) - 6*(s[1,5] - s[1,2]*s[2,5])*cmath.log(4)**2 + 12*(s[1,5]*(3*s[2,5] - cmath.log(4)) + s[1,2]*s[2,5]*(2 + cmath.log(4)))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*(s[1,5] - s[1,2]*s[2,5])*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[2,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2]))))) + (s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(12*s[1,2]*s[1,5] + 48*(s[1,2]*s[1,5] + s[2,5]) - math.pi**2*(s[1,2]*s[1,5] + s[2,5]) - 24*((2 + 3*s[1,5])*s[2,5] + 2*s[1,2]*(s[1,5] + s[2,5])) - 12*(2*s[1,2] + 3*s[1,5])*s[2,5]*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) - 2*(s[1,2]*s[1,5] + s[2,5])*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2]))))))/(96*(Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5]))))
FFnloFIN.append(0 + 0j)
FFnloFIN.append((1/(384*Nc*math.pi**2*s[1,2]*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])**2))*(8*s[1,2]*(s[1,2] + s[1,5])*(12*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*(s[2,5]*(1 + cmath.log(4)) + s[1,5]*(1 + s[2,5])*(2 + cmath.log(4))) + s[1,2]*(s[2,5]*(math.pi**2 - 6*(3 + cmath.log(4) + cmath.log(4)**2)) + 3*s[1,5]*(2 + s[2,5]*(-28 + math.pi**2 - 12*cmath.log(4) - 6*cmath.log(4)**2) + cmath.log(16))) - 6*(-2*s[1,5]*s[2,5]*(s[2,5]**2 + s[1,5]**2*(1 + s[2,5]) + s[1,5]*s[2,5]*(2 + s[2,5])) + s[1,2]*(s[1,5]*(-1 + 6*s[2,5]*(1 + cmath.log(4))) + s[2,5]*(1 + cmath.log(16))))*cmath.log(-(musq/s[1,2])) - 6*s[1,2]*(1 + 3*s[1,5])*s[2,5]*cmath.log(-(musq/s[1,2]))**2) + 3*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])**2*(s[1,2]**2*(1 + cmath.log(4)) + 4*Nc**2*s[2,5]*(3 + cmath.log(4)) + s[1,2]*s[2,5]*(5 + cmath.log(16)) + (s[1,2]**2 + 4*Nc**2*s[2,5] + 2*s[1,2]*s[2,5])*cmath.log(-(musq/s[1,5]))) - 4*s[2,5]*(s[1,5] + s[2,5])**2*(-12*s[1,2]*s[1,5]*(2 + cmath.log(4)) - 3*Nc**2*s[1,5]*(3 + cmath.log(4)) - 2*s[1,2]**2*(math.pi**2*(1 + s[1,5]) - 6*(3 + cmath.log(4) + cmath.log(4)**2 + s[1,5]*(4 + cmath.log(4) + cmath.log(4)**2))) + 3*(-Nc**2*s[1,5] - 4*s[1,2]*s[1,5] + 4*s[1,2]**2*(1 + s[1,5])*(1 + cmath.log(16)))*cmath.log(-(musq/s[2,5])) + 12*s[1,2]**2*(1 + s[1,5])*cmath.log(-(musq/s[2,5]))**2) + 48*s[1,2]*(s[1,2] + s[1,5])*(s[1,5] + s[2,5])**2*(s[1,2] - 2*(s[1,2] + 2*s[2,5]) - (s[1,2] + 2*s[2,5])*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) - 48*Nc**2*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])**2*(3 + cmath.log(-((4*musq)/s[1,5])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 24*(2*s[1,2]**3*s[1,5]*(s[1,5] + s[2,5]) - 4*s[1,2]*s[1,5]**2*s[2,5]*(s[1,5] + s[2,5]) - 2*Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])**2 + math.pi**2*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5]) - 4/3*(-12 + math.pi**2)*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5]) + 2*s[1,2]**2*(s[1,5]**3 + s[2,5]**2 + 2*s[1,5]*s[2,5]**2 + 2*s[1,5]**2*s[2,5]**2) - 2*(Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])**2 + s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(2*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 2*s[2,5])) + s[1,2]*s[2,5]*(s[1,5]**3 + 3*s[1,2]*s[2,5] + s[1,5]*s[2,5]*(7*s[1,2] + s[2,5]) + 2*s[1,5]**2*(s[2,5] + 2*s[1,2]*s[2,5])))*cmath.log(4) + 2*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(4)**2 - 2*(Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])**2 + s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(2*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 2*s[2,5])) + s[1,2]*s[2,5]*(s[1,5]**3 + 3*s[1,2]*s[2,5] + s[1,5]*s[2,5]*(7*s[1,2] + s[2,5]) + 2*s[1,5]**2*(s[2,5] + 2*s[1,2]*s[2,5])) - 2*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(4))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 2*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 - 4*(Nc**2*s[1,5]*s[2,5]*(s[1,5] + s[2,5])**2 + s[1,2]*s[1,5]*(s[1,2] + s[1,5])*(2*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*(s[1,5] + 2*s[2,5])) + s[1,2]*s[2,5]*(s[1,5]**3 + 3*s[1,2]*s[2,5] + s[1,5]*s[2,5]*(7*s[1,2] + s[2,5]) + 2*s[1,5]**2*(s[2,5] + 2*s[1,2]*s[2,5])) - 2*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(4) - 2*s[1,2]**2*(1 + s[1,5])*s[2,5]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) - 24*s[1,2]*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])**2*(-6*s[1,2] + math.pi**2*s[1,2] + 4*s[1,5] - 4*s[1,2]*cmath.log(2) + 8*s[1,5]*cmath.log(2) - 8*s[1,2]*cmath.log(2)**2 + 2*s[1,2]*cmath.log(s[1,2]/(4*s[2,5]))**2 - 2*s[1,2]*cmath.log(-(musq/s[1,2])) + 4*s[1,5]*cmath.log(-(musq/s[1,2])) - 8*s[1,2]*cmath.log(2)*cmath.log(-(musq/s[1,2])) - 2*s[1,2]*cmath.log(-(musq/s[1,2]))**2 - 2*s[1,2]*cmath.log(-(musq/s[2,5])) + 4*s[1,5]*cmath.log(-(musq/s[2,5])) - 8*s[1,2]*cmath.log(2)*cmath.log(-(musq/s[2,5])) - 2*s[1,2]*cmath.log(-(musq/s[2,5]))**2 + 2*s[1,2]*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) - 4*s[1,5]*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 8*s[1,2]*cmath.log(2)*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) + 2*s[1,2]*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 4*s[1,2]*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 4*s[1,2]*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2]))))))
FFnloFIN.append(0 + 0j)
FFnloFIN.append((1/(192*Nc*math.pi**2*s[1,5]*(s[1,2] + s[1,5])*s[2,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])))*(-((s[1,2] + s[1,5])*(s[1,5] - s[2,5])*(s[1,2] + s[2,5])*(-24*s[1,5]*s[2,5]*(s[1,5] + s[2,5])*cmath.log(2) + s[1,2]*(-math.pi**2*s[2,5] - math.pi**2*s[1,5]*(1 + 2*s[2,5]) + 24*s[2,5]*(1 + cmath.log(2) + cmath.log(2)**2) + 24*s[1,5]*(1 + cmath.log(2) + cmath.log(2)**2 + s[2,5]*(3 + 2*cmath.log(2)**2 + cmath.log(8)))) + 12*(-s[1,5]*s[2,5]*(s[1,5] + s[2,5]) + s[1,2]*s[2,5]*(1 + cmath.log(4)) + s[1,2]*s[1,5]*(1 + cmath.log(4) + s[2,5]*(3 + cmath.log(16))))*cmath.log(-(musq/s[1,2])) + 6*s[1,2]*(s[1,5] + s[2,5] + 2*s[1,5]*s[2,5])*cmath.log(-(musq/s[1,2]))**2)) - (s[1,2] + s[1,5])*(s[1,5] + s[2,5])*(s[1,2]*(-math.pi**2*s[1,5]*(1 + s[2,5]) + s[2,5]**2*(6 + 6*Nc**2 + math.pi**2 - 24*cmath.log(2)**2) + 24*s[1,5]*(1 + cmath.log(2) + cmath.log(2)**2 + s[2,5]*(2 + cmath.log(2) + cmath.log(2)**2))) + s[2,5]*(s[2,5]*(6 + 6*Nc**2 + math.pi**2 - 24*cmath.log(2)**2) + 12*s[1,5]*(-2 - cmath.log(8) + Nc**2*(4 + cmath.log(8)))) + 6*(3*(-1 + Nc**2)*s[1,5]*s[2,5] - 4*s[2,5]**2*cmath.log(2) - 2*s[1,2]*s[2,5]**2*cmath.log(4) + 2*s[1,2]*s[1,5]*(1 + s[2,5])*(1 + cmath.log(4)))*cmath.log(-(musq/s[1,5])) + 6*(-s[2,5]**2 + s[1,2]*(s[1,5] + s[1,5]*s[2,5] - s[2,5]**2))*cmath.log(-(musq/s[1,5]))**2) + (s[1,2] + s[2,5])*(s[1,5] + s[2,5])*((1 + s[1,2])*s[1,5]**2*(6 + 6*Nc**2 + math.pi**2 - 24*cmath.log(2)**2) + s[1,2]*s[2,5]*(-math.pi**2 + 24*(1 + cmath.log(2) + cmath.log(2)**2)) + s[1,5]*s[2,5]*(-math.pi**2*s[1,2] + 24*s[1,2]*(2 + cmath.log(2) + cmath.log(2)**2) - 12*(2 + cmath.log(8)) + 12*Nc**2*(4 + cmath.log(8))) + 6*(3*(-1 + Nc**2)*s[1,5]*s[2,5] - 4*s[1,5]**2*cmath.log(2) - 2*s[1,2]*s[1,5]**2*cmath.log(4) + 2*s[1,2]*(1 + s[1,5])*s[2,5]*(1 + cmath.log(4)))*cmath.log(-(musq/s[2,5])) - 6*((1 + s[1,2])*s[1,5]**2 - s[1,2]*s[2,5] - s[1,2]*s[1,5]*s[2,5])*cmath.log(-(musq/s[2,5]))**2) + 3*(-math.pi**2*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5]) + 4/3*(-12 + math.pi**2)*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5]) + 4*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*(-((-1 + Nc**2)*s[1,2]**2) + 2*s[1,5]*s[2,5] + s[1,2]*(s[1,5] - Nc**2*s[1,5] + s[2,5] - Nc**2*s[2,5] + 2*s[1,5]*s[2,5])) + 4*(4*Nc**2*s[1,5]*(s[1,5] - s[2,5])*s[2,5]*(s[1,5] + s[2,5]) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 2*s[2,5]*(s[1,2] + s[2,5])*(2*s[1,5]**2 + s[1,2]*s[2,5] + (2 + s[1,2])*s[1,5]*s[2,5]) - 2*s[1,5]*(s[1,2] + s[1,5])*(s[1,2]*s[1,5]*(1 + s[2,5]) + 2*s[2,5]*(s[1,5] + s[2,5])))*cmath.log(2) - 8*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5])*cmath.log(2)**2 + 2*(4*Nc**2*s[1,5]*(s[1,5] - s[2,5])*s[2,5]*(s[1,5] + s[2,5]) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 2*s[2,5]*(s[1,2] + s[2,5])*(2*s[1,5]**2 + s[1,2]*s[2,5] + (2 + s[1,2])*s[1,5]*s[2,5]) - 2*s[1,5]*(s[1,2] + s[1,5])*(s[1,2]*s[1,5]*(1 + s[2,5]) + 2*s[2,5]*(s[1,5] + s[2,5])) - 4*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5])*cmath.log(2))*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))) - 2*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5])*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 4*(4*Nc**2*s[1,5]*(s[1,5] - s[2,5])*s[2,5]*(s[1,5] + s[2,5]) - (-1 + Nc**2)*(s[1,2] + s[1,5])*s[2,5]*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + (-1 + Nc**2)*s[1,5]*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(s[1,2] + s[1,5] + s[2,5]) + 2*s[2,5]*(s[1,2] + s[2,5])*(2*s[1,5]**2 + s[1,2]*s[2,5] + (2 + s[1,2])*s[1,5]*s[2,5]) - 2*s[1,5]*(s[1,2] + s[1,5])*(s[1,2]*s[1,5]*(1 + s[2,5]) + 2*s[2,5]*(s[1,5] + s[2,5])) - 4*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5])*cmath.log(2) - 2*(s[1,5] - s[2,5])*(s[1,5] + s[2,5])*((-2 + Nc**2)*s[1,2]**2 + s[1,2]*s[1,5]*(-2 + Nc**2 - s[2,5]) + (-2 + Nc**2)*s[1,2]*s[2,5] + (-1 + Nc**2)*s[1,5]*s[2,5])*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5]))))) + 3*Nc**2*(s[1,2] + s[1,5])*(s[1,5] - s[2,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(math.pi**2 + 2*cmath.log(s[2,5]/(4*s[1,5]))**2 - 2*cmath.log(-(musq/s[1,5]))**2 - 2*cmath.log(-(musq/s[2,5]))**2 + 2*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 4*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 4*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5])))) - (s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(24*s[1,2]*s[2,5] + math.pi**2*(s[1,5] - s[1,2]*s[2,5]) + 12*(s[1,2] - s[1,5])*s[2,5]*cmath.log(4) - 6*(s[1,5] - s[1,2]*s[2,5])*cmath.log(4)**2 + 12*(s[1,2]*s[2,5]*(1 + cmath.log(4)) - s[1,5]*(s[2,5] + cmath.log(4)))*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[2,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) + 2*(s[1,5] - s[1,2]*s[2,5])*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[2,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[2,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] + s[1,5] - 3*s[2,5])/(4*s[2,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2]))))) + (s[1,2] + s[1,5])*(s[1,2] + s[2,5])*(s[1,5] + s[2,5])*(24*s[1,5]*s[2,5] - 24*(s[1,2]*s[1,5] + (s[1,5] - 2*s[2,5])*s[2,5]) + 48*(s[1,2]*s[1,5] - s[2,5]**2) - math.pi**2*(s[1,2]*s[1,5] - s[2,5]**2) + 12*s[1,5]*(s[1,2] - s[2,5])*(cmath.log(-(musq/s[1,2])) + cmath.log(-(musq/s[1,5])) - cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))) - 2*(s[1,2]*s[1,5] - s[2,5]**2)*(math.pi**2 + 3*cmath.log(s[1,2]/(4*s[1,5]))**2 - 3*cmath.log(-(musq/s[1,2]))**2 - 3*cmath.log(-(musq/s[1,5]))**2 + 3*cmath.log(-(musq/(s[1,2] + s[1,5] + s[2,5])))**2 + 6*polylog(2,-((s[1,2] - 3*s[1,5] + s[2,5])/(4*s[1,5]))) + 6*polylog(2,-((-3*s[1,2] + s[1,5] + s[2,5])/(4*s[1,2])))))))
FFnloFIN.append(0 + 0j)
i = 1
while i < 14:
    print("FF_nlo[", i, "] =", FFnloFIN[i])
    i += 1
print()


# One-loop helicity amplitudes: M[quark, antiquark, gluon] (for W-boson production leptons are always left-handed)
print("One-loop helicity amplitudes")
# 1/eps^2 pole
MLLLnloEPS2 = 1/2*1/S[5,2]*(2*FFnloEPS2[1]*A[1,3]*S[4,2]*S[2,1]*A[1,5] + FFnloEPS2[6]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,1]*S[1,4] + FFnloEPS2[8]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,2]*S[2,4] + FFnloEPS2[10]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,5]*S[5,4] + 2*FFnloEPS2[12]*A[1,5]*S[5,2]*S[2,4]*A[3,5])
MLLRnloEPS2 = -1/2*1/A[5,2]*(2*FFnloEPS2[1]*A[1,3]*S[4,2]*A[2,1]*S[1,5] + 2*FFnloEPS2[3]*A[1,2]*S[5,2]*A[3,1]*S[1,4] + 2*FFnloEPS2[4]*A[1,2]*S[5,2]*A[3,2]*S[2,4] + 2*FFnloEPS2[5]*A[1,2]*S[5,2]*A[3,5]*S[5,4] + FFnloEPS2[6]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,1]*S[1,4] + FFnloEPS2[8]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,2]*S[2,4] + FFnloEPS2[10]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,5]*S[5,4] + 2*FFnloEPS2[12]*A[1,5]*S[5,2]*A[2,3]*S[4,5] + 4*FFnloEPS2[13]*A[1,3]*S[4,5]*A[5,2]*S[5,2])
print("1/eps^2 pole:")
print("M(L,L,L)_nlo =", MLLLnloEPS2)
print("M(L,L,R)_nlo =", MLLRnloEPS2)
print()

# 1/eps pole
MLLLnloEPS1 = 1/2*1/S[5,2]*(2*FFnloEPS1[1]*A[1,3]*S[4,2]*S[2,1]*A[1,5] + FFnloEPS1[6]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,1]*S[1,4] + FFnloEPS1[8]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,2]*S[2,4] + FFnloEPS1[10]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,5]*S[5,4] + 2*FFnloEPS1[12]*A[1,5]*S[5,2]*S[2,4]*A[3,5])
MLLRnloEPS1 = -1/2*1/A[5,2]*(2*FFnloEPS1[1]*A[1,3]*S[4,2]*A[2,1]*S[1,5] + 2*FFnloEPS1[3]*A[1,2]*S[5,2]*A[3,1]*S[1,4] + 2*FFnloEPS1[4]*A[1,2]*S[5,2]*A[3,2]*S[2,4] + 2*FFnloEPS1[5]*A[1,2]*S[5,2]*A[3,5]*S[5,4] + FFnloEPS1[6]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,1]*S[1,4] + FFnloEPS1[8]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,2]*S[2,4] + FFnloEPS1[10]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,5]*S[5,4] + 2*FFnloEPS1[12]*A[1,5]*S[5,2]*A[2,3]*S[4,5] + 4*FFnloEPS1[13]*A[1,3]*S[4,5]*A[5,2]*S[5,2])
print("1/eps pole:")
print("M(L,L,L)_nlo =", MLLLnloEPS1)
print("M(L,L,R)_nlo =", MLLRnloEPS1)
print()

# finite remainder
MLLLnloFIN = 1/2*1/S[5,2]*(2*FFnloFIN[1]*A[1,3]*S[4,2]*S[2,1]*A[1,5] + FFnloFIN[6]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,1]*S[1,4] + FFnloFIN[8]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,2]*S[2,4] + FFnloFIN[10]*A[1,5]*S[5,2]*S[2,1]*A[1,5]*A[3,5]*S[5,4] + 2*FFnloFIN[12]*A[1,5]*S[5,2]*S[2,4]*A[3,5])
MLLRnloFIN = -1/2*1/A[5,2]*(2*FFnloFIN[1]*A[1,3]*S[4,2]*A[2,1]*S[1,5] + 2*FFnloFIN[3]*A[1,2]*S[5,2]*A[3,1]*S[1,4] + 2*FFnloFIN[4]*A[1,2]*S[5,2]*A[3,2]*S[2,4] + 2*FFnloFIN[5]*A[1,2]*S[5,2]*A[3,5]*S[5,4] + FFnloFIN[6]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,1]*S[1,4] + FFnloFIN[8]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,2]*S[2,4] + FFnloFIN[10]*A[1,5]*S[5,2]*A[2,1]*S[1,5]*A[3,5]*S[5,4] + 2*FFnloFIN[12]*A[1,5]*S[5,2]*A[2,3]*S[4,5] + 4*FFnloFIN[13]*A[1,3]*S[4,5]*A[5,2]*S[5,2])
print("Finite part:")
print("M(L,L,L)_nlo =", MLLLnloFIN)
print("M(L,L,R)_nlo =", MLLRnloFIN)
print()


# One-loop helicity amplitudes including the global factor
print("One-loop amplitudes including all the couplings and propagators")
MLLLnloTotEPS2 = MLLLnloEPS2 * G
MLLRnloTotEPS2 = MLLRnloEPS2 * G
print("1/eps^2 pole:")
print("M(L,L,L)_nlo = ", MLLLnloTotEPS2)
print("M(L,L,R)_nlo = ", MLLRnloTotEPS2)
print()

MLLLnloTotEPS1 = MLLLnloEPS1 * G
MLLRnloTotEPS1 = MLLRnloEPS1 * G
print("1/eps pole:")
print("M(L,L,L)_nlo = ", MLLLnloTotEPS1)
print("M(L,L,R)_nlo = ", MLLRnloTotEPS1)
print()

MLLLnloTotFIN = MLLLnloFIN * G
MLLRnloTotFIN = MLLRnloFIN * G
print("Finite part:")
print("M(L,L,L)_nlo = ", MLLLnloTotFIN)
print("M(L,L,R)_nlo = ", MLLRnloTotFIN)
print()


# NLO squared amplitudes (including color summation Cf*Nc and spin average 1/(2Nc)^2)
print("NLO squared amplitudes")
# 1/eps^2 pole
M2LLLnloEPS2 = MLLLtreeTot*MLLLnloTotEPS2.conjugate()*(Cf*Nc/((2*Nc)**2))
M2LLRnloEPS2 = MLLRtreeTot*MLLRnloTotEPS2.conjugate()*(Cf*Nc/((2*Nc)**2))
# 1/eps pole
M2LLLnloEPS1 = MLLLtreeTot*MLLLnloTotEPS1.conjugate()*(Cf*Nc/((2*Nc)**2))
M2LLRnloEPS1 = MLLRtreeTot*MLLRnloTotEPS1.conjugate()*(Cf*Nc/((2*Nc)**2))
# finite part
M2LLLnloFIN = MLLLtreeTot*MLLLnloTotFIN.conjugate()*(Cf*Nc/((2*Nc)**2))
M2LLRnloFIN = MLLRtreeTot*MLLRnloTotFIN.conjugate()*(Cf*Nc/((2*Nc)**2))

print("1/eps^2 pole:")
print("2Re(M_0 M_1*)(L,L,L) =", 2*M2LLLnloEPS2.real)
print("2Re(M_0 M_1*)(L,L,R) =", 2*M2LLRnloEPS2.real)
print("Sum for left-handed quarks:")
print("2Re(M_0 M_1*)(L,L,L) + 2Re(M_0 M_1*)(L,L,R) =", 2*M2LLLnloEPS2.real + 2*M2LLRnloEPS2.real,"(Dmitrii)")
print("2Re(M_0 M_1*)(L,L,L) + 2Re(M_0 M_1*)(L,L,R) = OPENLOOPS RESULT", "(OpenLoops)")
print()
print("1/eps pole:")
print("2Re(M_0 M_1*)(L,L,L) =", 2*M2LLLnloEPS1.real)
print("2Re(M_0 M_1*)(L,L,R) =", 2*M2LLRnloEPS1.real)
print("Sum for left-handed quarks:")
print("2Re(M_0 M_1*)(L,L,L) + 2Re(M_0 M_1*)(L,L,R) =", 2*M2LLLnloEPS1.real + 2*M2LLRnloEPS1.real,"(Dmitrii)")
print("2Re(M_0 M_1*)(L,L,L) + 2Re(M_0 M_1*)(L,L,R) = OPENLOOPS RESULT", "(OpenLoops)")
print()
print("Finite part:")
print("2Re(M_0 M_1*)(L,L,L) =", 2*M2LLLnloFIN.real)
print("2Re(M_0 M_1*)(L,L,R) =", 2*M2LLRnloFIN.real)
print("Sum for left-handed quarks:")
print("2Re(M_0 M_1*)(L,L,L) + 2Re(M_0 M_1*)(L,L,R) =", 2*M2LLLnloFIN.real + 2*M2LLRnloFIN.real,"(Dmitrii)")
print("2Re(M_0 M_1*)(L,L,L) + 2Re(M_0 M_1*)(L,L,R) = OPENLOOPS RESULT", "(OpenLoops)")


"""














