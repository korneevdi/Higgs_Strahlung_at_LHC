
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
mW = 80.419                         # W-boson mass
mZ = 91.188                         # Z-boson mass
mH = 125.0                          # Higgs boson mass 
Gamma_W = 2.085                     # W-boson decay width
Gamma_Z = 2.4952                    # Z-boson decay width
cosW = mW/mZ                        # cosine of the Weinberg angle
sinW = math.sqrt(1 - cosW**2)       # sine of the Weinberg angle
gW = 0.6530704531238141             # electroweak coupling
vev = 246.21845810181634            # vacuum expectation value
mu = 91.188                         # energy scale
musq = mu**2                        # square of the energy scale
alpha_s = 1                         # strong coupling
gs = math.sqrt(4*math.pi*alpha_s)
Cf = 4/3                            # Casimir operator of SU(3)
Nc = 3                              # number of colors


# GENERAL SETTINGS (SM/SMEFT and W/Z)

# for (u db -> W) and (d ub -> W) BosonType = 1, for (u ub -> Z) and (d db -> Z) BosonType = 2
BosonType = 1

# for SM TheoryType = 1, for SMEFT TheoryType = 2
TheoryType = 1

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
p3 = [322.3919309874294800, -101.97160213731860, -296.47360464823691,  75.111592116216357]     # lepton
p4 = [149.6028751502909100, -103.96621515693120, -95.942663470338033,  48.652355394098521]    # gluon
pH = [441.0552174570096900,  227.63884011083519,  353.06072547319292, -49.329377123440487]      # Higgs boson

# P2
"""
p1 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]      # antiquark
p5 = [408.09769343864940, -151.58297471069091,  -43.368211642550193, 376.41138052233600]        # gluon
p3 = [212.02666673552400, -13.563737621454340, -112.81797905507730,  -179.00680442553411]       # lepton
p4 = [158.79955431793871, 73.137815818506667, 9.3452151582977017,  -140.64432197042041]         # antinuetrino
pH = [221.07608550788780,  92.008896513638575,  146.84097553932980, -56.760254126381483]        # Higgs boson
"""
# P3
"""
p1 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]      # antiquark
p5 = [126.73811290152260, -52.928374081215331,  -114.69266617062870, 10.330963441554880]        # gluon
p3 = [238.95222743344240, 79.194657038630680, 156.04889313946359,  162.71175815498250]          # lepton
p4 = [248.58168823997181, 224.93890423006121, 88.906550096696662,  57.366980414846893]          # antinuetrino
pH = [385.72797142506317,  -251.20518718747661,  -130.26277706553159, -230.40970201138421]      # Higgs boson
"""
# P4
"""
p1 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]      # antiquark
p5 = [310.35315896914290, -117.26507889220611,  59.048532186395803, -281.21389617364753]        # gluon
p3 = [388.47079492070651, 137.32825127124690, -29.745269084920960,  362.16809477944417]         # lepton
p4 = [154.91390425372319, -79.638013102257247, -51.554274920237070,  -122.46738887436540]       # antinuetrino
pH = [146.26214185642741,  59.574840723216461,  22.251011818762301, 41.513190268568692]         # Higgs boson
"""
# P5
"""
p1 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]      # antiquark
p5 = [220.03700633242369, 0.99363779976526345,  -152.19811499639630, 158.90572875513860]        # gluon
p3 = [188.78346963490571, 107.91748016461140, 129.40073588915860,  85.137920068899206]          # lepton
p4 = [360.47585489718779, -136.55878256587721, 214.37213991341781,  -255.61519222637381]        # antinuetrino
pH = [230.70366913548281,  27.647664601500480,  -191.57476080618011, 11.571543402335960]        # Higgs boson
"""
# P6
"""
p1 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]      # antiquark
p5 = [155.19073733016361, 145.78284658400921,  -24.261543200581919, 47.359308657003801]         # gluon
p3 = [150.75757498121041, -136.94027814085209, 32.878065122911543,  -53.798136312468252]        # lepton
p4 = [334.95178538657410, -235.79992017475479, 197.45014544560070,  -132.68208712084649]        # antinuetrino
pH = [359.09990230205182,  226.95735173159781,  -206.06666736793039, 139.12091477631100]        # Higgs boson
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
print("Scalar products of momenta: sij = 2(pi*pj)")
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
MLLLLLtreeSM = gs * 2 * math.sqrt(2) * (vq + aq) * (a + b) * (1/s[1,5] * Ang[2,1] * Sq[1,5] * Ang[1,3] * Sq[4,2] / Ang[2,5] + 1/s[2,5] * Ang[1,5] * Sq[5,2] * Ang[3,2] * Sq[5,4] / Ang[2,5] + 1/s[2,5] * Ang[1,2] * Sq[2,5] * Ang[3,5] * Sq[5,4] / Ang[2,5]) * GlobFac_SM
MLLRLLtreeSM = gs * 2 * math.sqrt(2) * (vq + aq) * (a + b) * (1/s[1,5] * Ang[5,1] * Sq[1,2] * Ang[1,3] * Sq[4,2] / Sq[2,5] + 1/s[2,5] * Ang[1,5] * Sq[5,2] * Ang[3,5] * Sq[2,4] / Sq[2,5] + (s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Ang[1,5] * Ang[5,3] * Sq[4,2]) * GlobFac_SM
MRRLLLtreeSM = gs * 2 * math.sqrt(2) * (vq - aq) * (a + b) * (1/s[1,5] * Ang[2,1] * Sq[1,5] * Sq[1,4] * Ang[3,2] / Ang[2,5] + 1/s[2,5] * Sq[1,5] * Ang[5,2] * Ang[3,2] * Sq[5,4] / Ang[2,5] + (s[1,5] + s[2,5])/(s[1,5] * s[2,5]) * Sq[1,5] * Sq[5,4] * Ang[3,2] + 1/s[2,5] * Ang[1,2] * Sq[2,5] * Ang[3,5] * Sq[5,4] / Ang[2,5]) * GlobFac_SM
MRRRLLtreeSM = gs * 2 * math.sqrt(2) * (vq - aq) * (a + b) * (1/s[1,5] * Ang[5,1] * Sq[1,2] * Sq[1,4] * Ang[3,2] / Sq[2,5] + 1/s[2,5] * Sq[1,5] * Ang[5,2] * Ang[3,5] * Sq[2,4] / Sq[2,5]) * GlobFac_SM

MLRLRRtreeSM = 0 * GlobFac_SM
MLRRRRtreeSM = 0 * GlobFac_SM
MRLLRRtreeSM = 0 * GlobFac_SM
MRLRRRtreeSM = 0 * GlobFac_SM
MLLLRRtreeSM = gs * 2 * math.sqrt(2) * (vq + aq) * b * (1/s[1,5] * Sq[5,1] * Ang[1,2] * Ang[1,4] * Sq[3,2] / Ang[2,5] + 1/s[2,5] * Ang[1,5] * Sq[5,2] * Sq[3,5] * Ang[2,4] / Ang[2,5]) * GlobFac_SM
MLLRRRtreeSM = gs * 2 * math.sqrt(2) * (vq + aq) * b * (1/s[1,5] * Sq[2,1] * Ang[1,5] * Ang[1,4] * Sq[3,2] / Sq[2,5] + 1/s[2,5] * Ang[1,5] * Sq[5,2] * Sq[3,2] * Ang[5,4] / Sq[2,5] + (s[1,5] + s[2,5])/(s[1,5] * s[2,5]) * Ang[1,5] * Ang[5,4] * Sq[3,2] + 1/s[2,5] * Sq[1,2] * Ang[2,5] * Sq[3,5] * Ang[5,4] / Sq[2,5]) * GlobFac_SM
MRRLRRtreeSM = gs * 2 * math.sqrt(2) * (vq - aq) * b * (1/s[1,5] * Sq[5,1] * Ang[1,2] * Sq[1,3] * Ang[4,2] / Ang[2,5] + 1/s[2,5] * Sq[1,5] * Ang[5,2] * Sq[3,5] * Ang[2,4] / Ang[2,5] + (s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Sq[1,5] * Sq[5,3] * Ang[4,2]) * GlobFac_SM
MRRRRRtreeSM = gs * 2 * math.sqrt(2) * (vq - aq) * b * (1/s[1,5] * Sq[2,1] * Ang[1,5] * Sq[1,3] * Ang[4,2] / Sq[2,5] + 1/s[2,5] * Sq[1,5] * Ang[5,2] * Sq[3,2] * Ang[5,4] / Sq[2,5] + 1/s[2,5] * Sq[1,2] * Ang[2,5] * Sq[3,5] * Ang[5,4] / Sq[2,5]) * GlobFac_SM

# SMEFT tree-level helicity amplitudes iM(quark, antiquark, gluon, lepton, antilepton)
MLRLLLtreeSMEFT = gs * 4 * math.sqrt(2) * B * (a + b) * ((s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Ang[1,3] * Sq[3,5] * Sq[5,4] * Ang[2,3] + (s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Ang[1,4] * Sq[4,5] * Sq[5,4] * Ang[2,3] + (s[3,5] + s[4,5])/s[1,5] * Ang[1,2] * Sq[5,4] * Ang[2,3] / Ang[2,5] + 1/s[1,5] * Ang[2,3] * Sq[3,5] * Ang[1,5] * Sq[5,4] * Ang[3,2] / Ang[2,5] + 1/s[1,5] * Ang[2,4] * Sq[4,5] * Ang[1,5] * Sq[5,4] * Ang[3,2] / Ang[2,5] + 1/s[1,5] * Ang[1,2] * Sq[1,5] * Ang[1,3] * Sq[3,4] * Ang[3,2] / Ang[2,5] + 1/s[2,5] * Ang[1,3] * Sq[3,5] * Ang[2,5] * Sq[5,4] * Ang[3,2] / Ang[2,5] + 1/s[2,5] * Ang[1,4] * Sq[4,5] * Ang[2,5] * Sq[5,4] * Ang[3,2] / Ang[2,5]) * GlobFac_SMEFT
MLRRLLtreeSMEFT = gs * 4 * math.sqrt(2) * B * (a + b) * ((s[3,5] + s[4,5])/s[1,5] * Ang[1,5] * Sq[2,4] * Ang[2,3] / Sq[2,5] + 1/s[1,5] * Ang[5,3] * Sq[3,2] * Ang[1,5] * Sq[5,4] * Ang[3,2] / Sq[2,5] + 1/s[1,5] * Ang[5,4] * Sq[4,2] * Ang[1,5] * Sq[5,4] * Ang[3,2] / Sq[2,5] + 1/s[1,5] * Ang[1,5] * Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,2] / Sq[2,5] + 1/s[2,5] * Ang[1,3] * Sq[3,5] * Ang[2,5] * Sq[2,4] * Ang[3,5] / Sq[2,5] + 1/s[2,5] * Ang[1,4] * Sq[4,5] * Ang[2,5] * Sq[2,4] * Ang[3,5] / Sq[2,5] + 1/s[2,5] * Ang[1,3] * Sq[3,2] * Ang[5,2] * Sq[5,4] * Ang[3,5] / Sq[2,5] + 1/s[2,5] * Ang[1,4] * Sq[4,2] * Ang[5,2] * Sq[5,4] * Ang[3,5] / Sq[2,5]) * GlobFac_SMEFT
MRLLLLtreeSMEFT = gs * 4 * math.sqrt(2) * A * (a + b) * ((s[3,5] + s[4,5])/s[1,5] * Sq[1,5] * Ang[2,3] * Sq[2,4] / Ang[2,5] + 1/s[1,5] * Ang[2,3] * Sq[3,5] * Sq[1,5] * Ang[5,3] * Sq[4,2] / Ang[2,5] + 1/s[1,5] * Ang[2,4] * Sq[4,5] * Sq[1,5] * Ang[5,3] * Sq[4,2] / Ang[2,5] + 1/s[1,5] * Ang[1,2] * Sq[1,5] * Sq[1,4] * Ang[4,3] * Sq[4,2] / Ang[2,5] + 1/s[2,5] * Sq[1,3] * Ang[3,5] * Sq[2,5] * Ang[3,2] * Sq[5,4] / Ang[2,5] + 1/s[2,5] * Sq[1,4] * Ang[4,5] * Sq[2,5] * Ang[3,2] * Sq[5,4] / Ang[2,5] + 1/s[2,5] * Sq[1,3] * Ang[3,2] * Sq[5,2] * Ang[3,5] * Sq[5,4] / Ang[2,5] + 1/s[2,5] * Sq[1,4] * Ang[4,2] * Sq[5,2] * Ang[3,5] * Sq[5,4] / Ang[2,5]) * GlobFac_SMEFT
MRLRLLtreeSMEFT = gs * 4 * math.sqrt(2) * A * (a + b) * ((s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Sq[1,3] * Ang[3,5] * Ang[5,3] * Sq[2,4] + (s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Sq[1,4] * Ang[4,5] * Ang[5,3] * Sq[2,4] + (s[3,5] + s[4,5])/s[1,5] * Sq[1,2] * Ang[5,3] * Sq[2,4] / Sq[2,5] + 1/s[1,5] * Ang[5,3] * Sq[3,2] * Sq[1,5] * Ang[5,3] * Sq[4,2] / Sq[2,5] + 1/s[1,5] * Ang[5,4] * Sq[4,2] * Sq[1,5] * Ang[5,3] * Sq[4,2] / Sq[2,5] + 1/s[1,5] * Ang[1,5] * Sq[1,2] * Sq[1,4] * Ang[4,3] * Sq[4,5] / Sq[2,5] + 1/s[2,5] * Ang[3,5] * Sq[1,3] * Sq[2,5] * Ang[3,5] * Sq[2,4] / Sq[2,5] + 1/s[2,5] * Ang[4,5] * Sq[1,4] * Sq[2,5] * Ang[3,5] * Sq[2,4] / Sq[2,5]) * GlobFac_SMEFT
MLLLLLtreeSMEFT = gs * 2 * math.sqrt(2) * C * (a + b) * (1/s[1,5] * Ang[2,1] * Sq[1,5] * Ang[1,3] * Sq[4,2] / Ang[2,5] + 1/s[2,5] * Ang[1,5] * Sq[5,2] * Ang[3,2] * Sq[5,4] / Ang[2,5] + 1/s[2,5] * Ang[1,2] * Sq[2,5] * Ang[3,5] * Sq[5,4] / Ang[2,5]) * GlobFac_SMEFT
MLLRLLtreeSMEFT = gs * 2 * math.sqrt(2) * C * (a + b) * (1/s[1,5] * Ang[5,1] * Sq[1,2] * Ang[1,3] * Sq[4,2] / Sq[2,5] + 1/s[2,5] * Ang[1,5] * Sq[5,2] * Ang[3,5] * Sq[2,4] / Sq[2,5] + (s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Ang[1,5] * Ang[5,3] * Sq[4,2]) * GlobFac_SMEFT
MRRLLLtreeSMEFT = gs * 2 * math.sqrt(2) * D * (a + b) * (1/s[1,5] * Ang[2,1] * Sq[1,5] * Sq[1,4] * Ang[3,2] / Ang[2,5] + 1/s[2,5] * Sq[1,5] * Ang[5,2] * Ang[3,2] * Sq[5,4] / Ang[2,5] + (s[1,5] + s[2,5])/(s[1,5] * s[2,5]) * Sq[1,5] * Sq[5,4] * Ang[3,2] + 1/s[2,5] * Ang[1,2] * Sq[2,5] * Ang[3,5] * Sq[5,4] / Ang[2,5]) * GlobFac_SMEFT
MRRRLLtreeSMEFT = gs * 2 * math.sqrt(2) * D * (a + b) * (1/s[1,5] * Ang[5,1] * Sq[1,2] * Sq[1,4] * Ang[3,2] / Sq[2,5] + 1/s[2,5] * Sq[1,5] * Ang[5,2] * Ang[3,5] * Sq[2,4] / Sq[2,5]) * GlobFac_SMEFT

MLRLRRtreeSMEFT = gs * 4 * math.sqrt(2) * B * b * ((s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Ang[1,3] * Sq[3,5] * Sq[5,3] * Ang[2,4] + (s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Ang[1,4] * Sq[4,5] * Sq[5,3] * Ang[2,4] + (s[3,5] + s[4,5])/s[1,5] * Ang[1,2] * Sq[5,3] * Ang[2,4] / Ang[2,5] + 1/s[1,5] * Sq[5,3] * Ang[3,2] * Ang[1,5] * Sq[5,3] * Ang[4,2] / Ang[2,5] + 1/s[1,5] * Sq[5,4] * Ang[4,2] * Ang[1,5] * Sq[5,3] * Ang[4,2] / Ang[2,5] + 1/s[1,5] * Sq[1,5] * Ang[1,2] * Ang[1,4] * Sq[4,3] * Ang[4,5] / Ang[2,5] + 1/s[2,5] * Sq[3,5] * Ang[1,3] * Ang[2,5] * Sq[3,5] * Ang[2,4] / Ang[2,5] + 1/s[2,5] * Sq[4,5] * Ang[1,4] * Ang[2,5] * Sq[3,5] * Ang[2,4] / Ang[2,5]) * GlobFac_SMEFT
MLRRRRtreeSMEFT = gs * 4 * math.sqrt(2) * B * b * ((s[3,5] + s[4,5])/s[1,5] * Ang[1,5] * Sq[2,3] * Ang[2,4] / Sq[2,5] + 1/s[1,5] * Sq[2,3] * Ang[3,5] * Ang[1,5] * Sq[5,3] * Ang[4,2] / Sq[2,5] + 1/s[1,5] * Sq[2,4] * Ang[4,5] * Ang[1,5] * Sq[5,3] * Ang[4,2] / Sq[2,5] + 1/s[1,5] * Sq[1,2] * Ang[1,5] * Ang[1,4] * Sq[4,3] * Ang[4,2] / Sq[2,5] + 1/s[2,5] * Ang[1,3] * Sq[3,5] * Ang[2,5] * Sq[3,2] * Ang[5,4] / Sq[2,5] + 1/s[2,5] * Ang[1,4] * Sq[4,5] * Ang[2,5] * Sq[3,2] * Ang[5,4] / Sq[2,5] + 1/s[2,5] * Ang[1,3] * Sq[3,2] * Ang[5,2] * Sq[3,5] * Ang[5,4] / Sq[2,5] + 1/s[2,5] * Ang[1,4] * Sq[4,2] * Ang[5,2] * Sq[3,5] * Ang[5,4] / Sq[2,5]) * GlobFac_SMEFT
MRLLRRtreeSMEFT = gs * 4 * math.sqrt(2) * A * b * ((s[3,5] + s[4,5])/s[1,5] * Sq[1,5] * Ang[2,4] * Sq[2,3] / Ang[2,5] + 1/s[1,5] * Sq[5,3] * Ang[3,2] * Sq[1,5] * Ang[5,4] * Sq[3,2] / Ang[2,5] + 1/s[1,5] * Sq[5,4] * Ang[4,2] * Sq[1,5] * Ang[5,4] * Sq[3,2] / Ang[2,5] + 1/s[1,5] * Sq[1,5] * Ang[1,2] * Sq[1,3] * Ang[3,4] * Sq[3,2] / Ang[2,5] + 1/s[2,5] * Sq[1,3] * Ang[3,5] * Sq[2,5] * Ang[2,4] * Sq[3,5] / Ang[2,5] + 1/s[2,5] * Sq[1,4] * Ang[4,5] * Sq[2,5] * Ang[2,4] * Sq[3,5] / Ang[2,5] + 1/s[2,5] * Sq[1,3] * Ang[3,2] * Sq[5,2] * Ang[5,4] * Sq[3,5] / Ang[2,5] + 1/s[2,5] * Sq[1,4] * Ang[4,2] * Sq[5,2] * Ang[5,4] * Sq[3,5] / Ang[2,5]) * GlobFac_SMEFT
MRLRRRtreeSMEFT = gs * 4 * math.sqrt(2) * A * b * ((s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Sq[1,3] * Ang[3,5] * Ang[5,4] * Sq[2,3] + (s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Sq[1,4] * Ang[4,5] * Ang[5,4] * Sq[2,3] + (s[3,5] + s[4,5])/s[1,5] * Sq[1,2] * Ang[5,4] * Sq[2,3] / Sq[2,5] + 1/s[1,5] * Sq[2,3] * Ang[3,5] * Sq[1,5] * Ang[5,4] * Sq[3,2] / Sq[2,5] + 1/s[1,5] * Sq[2,4] * Ang[4,5] * Sq[1,5] * Ang[5,4] * Sq[3,2] / Sq[2,5] + 1/s[1,5] * Sq[1,2] * Ang[1,5] * Sq[1,3] * Ang[3,4] * Sq[3,2] / Sq[2,5] + 1/s[2,5] * Sq[1,3] * Ang[3,5] * Sq[2,5] * Ang[5,4] * Sq[3,2] / Sq[2,5] + 1/s[2,5] * Sq[1,4] * Ang[4,5] * Sq[2,5] * Ang[5,4] * Sq[3,2] / Sq[2,5]) * GlobFac_SMEFT
MLLLRRtreeSMEFT = gs * 2 * math.sqrt(2) * C * b * (1/s[1,5] * Sq[5,1] * Ang[1,2] * Ang[1,4] * Sq[3,2] / Ang[2,5] + 1/s[2,5] * Ang[1,5] * Sq[5,2] * Sq[3,5] * Ang[2,4] / Ang[2,5]) * GlobFac_SMEFT
MLLRRRtreeSMEFT = gs * 2 * math.sqrt(2) * C * b * (1/s[1,5] * Sq[2,1] * Ang[1,5] * Ang[1,4] * Sq[3,2] / Sq[2,5] + 1/s[2,5] * Ang[1,5] * Sq[5,2] * Sq[3,2] * Ang[5,4] / Sq[2,5] + (s[1,5] + s[2,5])/(s[1,5] * s[2,5]) * Ang[1,5] * Ang[5,4] * Sq[3,2] + 1/s[2,5] * Sq[1,2] * Ang[2,5] * Sq[3,5] * Ang[5,4] / Sq[2,5]) * GlobFac_SMEFT
MRRLRRtreeSMEFT = gs * 2 * math.sqrt(2) * D * b * (1/s[1,5] * Sq[5,1] * Ang[1,2] * Sq[1,3] * Ang[4,2] / Ang[2,5] + 1/s[2,5] * Sq[1,5] * Ang[5,2] * Sq[3,5] * Ang[2,4] / Ang[2,5] + (s[1,5] + s[2,5])/(s[1,5]*s[2,5]) * Sq[1,5] * Sq[5,3] * Ang[4,2]) * GlobFac_SMEFT
MRRRRRtreeSMEFT = gs * 2 * math.sqrt(2) * D * b * (1/s[1,5] * Sq[2,1] * Ang[1,5] * Sq[1,3] * Ang[4,2] / Sq[2,5] + 1/s[2,5] * Sq[1,5] * Ang[5,2] * Sq[3,2] * Ang[5,4] / Sq[2,5] + 1/s[2,5] * Sq[1,2] * Ang[2,5] * Sq[3,5] * Ang[5,4] / Sq[2,5]) * GlobFac_SMEFT


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
print()

print("Total tree-level squared amplitude:")
print("|M_tree|^2 = ", M2tree)
print()


# OpenLoops & MadGraph results
OpenLoopsRes = 3.8305580356531853E-009 # P1
#OpenLoopsRes = 1.0622265520776929E-011 # P2
#OpenLoopsRes = 4.0491032338858650E-012 # P3
#OpenLoopsRes = 6.0017562493391458E-015 # P4
#OpenLoopsRes = 6.3822481554852740E-014 # P5
#OpenLoopsRes = 7.7837429299369005E-010 # P6


print("OpenLoops & MadGraph result:")
print("|M_tree|^2 = ", OpenLoopsRes)
print()
print("ratio Dmitrii/OpenLoops: ", M2tree / OpenLoopsRes)





