
import math, cmath
import numpy as np
from mpmath import *
from mpmath import zetazero, mp

# Setting the accuracy for zeta-function calculations
#mp.dps = 15

"""
In this project, I compute radiative 2-loop QCD corrections to the process q qb -> g W H -> g l nub H
After quark-antiquark (q and qb) collision a gluon (g), a vector boson (W) and a Higgs (H) appear with subsequent decay of the vector boson into a lepton-antinuetrino (l and nub) pair)
As a result I obtain 2-loop squared amplitude for this process, which allows to compute the cross section measured in CERN (at the Long Hanron Collider)

THE OPENLOOPS RESULT IS GIVEN FOR THE CASE OF W-BOSON WITHIN THE STANDARD MODEL
"""

# PROCESS
# q(p1) + qb(p2) -> VH + jets -> e(p3) + nub(p4) + H(pH) + jets
print("Considered process: q(p1) + qb(p2) -> VH + jets -> e(p3) + nub(p4) + H(pH) + jets")
print()

# LEADING ORDER, ONE-LOOP, TWO-LOOP
# q(p1) + qb(p2) -> e(p3) + nub(p4) + H(pH)

print("Tree-level, one-loop and two-loop process without real emission: q(p1) + qb(p2) -> gVH -> l(p3) + nub(p4) + H(pH)")
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
Nf = 4                              # number of flavors


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



# External Momenta and OpenLoops results

# T1

p1 = [500.00000000000000, 0.0000000000000000, 0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.00000000000000,  0.0000000000000000, 0.0000000000000000, -500.00000000000000]     # antiquark
p4 = [439.78021928785591, 162.50680658487221, 364.09047948353401, -185.57020730686239]      # antinuetrino
p3 = [349.14239937112842, -17.578471028824460, -333.45082223855940, 101.99000707591840]     # lepton
pH = [211.07738134101581, -144.92833555604770, -30.639657244974519, 83.580200230944016]     # Higgs boson
# OpenLoops results for squared amplitude
OpenLoopsResTree = 3.4729976354737612E-011          # tree level
OpenLoopsResOneLoopEps2 = -1.4739859760856361E-011  # one-loop 1/eps^2 pole
OpenLoopsResOneLoopEps1 = 4.8489185121397621E-011   # one-loop 1/eps pole
OpenLoopsResOneLoopFin = -4.9395366291861276E-011   # one-loop finite part
OpenLoopsResTwoLoopEps2 = 1 # two-loop 1/eps^2 pole
OpenLoopsResTwoLoopEps1 = 1 # two-loop 1/eps pole
OpenLoopsResTwoLoopFin = 1 # two-loop finite part


# T2
"""
p1 = [500.00000000000000, 0.0000000000000000, 0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.00000000000000,  0.0000000000000000, 0.0000000000000000, -500.00000000000000]     # antiquark
p4 = [422.08957321198892, -126.50552822371320, -399.42574168565420, 51.137422911046571]     # antinuetrino
p3 = [180.70100467419249, 177.01798495038040, 32.064088390317352, 17.011182500560881]       # lepton
pH = [397.20942211381850, -50.512456726667111, 367.36165329533691, -68.148605411607434]     # Higgs boson
# OpenLoops results for squared amplitude
OpenLoopsResTree = 6.7466380038976574E-011          # tree level
OpenLoopsResOneLoopEps2 = -2.8633621001918670E-011  # one-loop 1/eps^2 pole
OpenLoopsResOneLoopEps1 = 9.4194990453376490E-011   # one-loop 1/eps pole
OpenLoopsResOneLoopFin = -9.5955336115757703E-011   # one-loop finite part
"""

# T3
"""
p1 = [500.00000000000000, 0.0000000000000000, 0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.00000000000000,  0.0000000000000000, 0.0000000000000000, -500.00000000000000]     # antiquark
p4 = [362.19939027519791, 244.30626335943609, 153.49919119423609, -218.95398215558970]      # antinuetrino
p3 = [451.73431596931482, -246.55144057953359, -288.90577126990979, 244.56028847578659]     # lepton
pH = [186.06629375548721, 2.2451772200975202, 135.40658007567370, -25.606306320196850]      # Higgs boson
# OpenLoops results for squared amplitude
OpenLoopsResTree = 4.2298820425566844E-011          # tree level
OpenLoopsResOneLoopEps2 = -1.7952176953827712E-011  # one-loop 1/eps^2 pole
OpenLoopsResOneLoopEps1 = 5.9056629151786867E-011   # one-loop 1/eps pole
OpenLoopsResOneLoopFin = -6.0160298046086038E-011   # one-loop finite part
"""

# T4
"""
p1 = [500.00000000000000, 0.0000000000000000, 0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.00000000000000,  0.0000000000000000, 0.0000000000000000, -500.00000000000000]     # antiquark
p4 = [330.53969568768753, -33.008723457689108, -303.71353193985487, -126.19431491799300]    # antinuetrino
p3 = [212.92384630012540, 167.02867017961910, -110.86379342176120, 71.744037866602881]      # lepton
pH = [456.53645801218698, -134.01994672192990, 414.57732536161609, 54.450277051390032]      # Higgs boson
# OpenLoops results for squared amplitude
OpenLoopsResTree = 5.9737839579143591E-010          # tree level
OpenLoopsResOneLoopEps2 = -2.5353526556403661E-010  # one-loop 1/eps^2 pole
OpenLoopsResOneLoopEps1 = 8.3404582039409006E-010   # one-loop 1/eps pole
OpenLoopsResOneLoopFin = -8.4963273149298393E-010   # one-loop finite part
"""

# T5
"""
p1 = [500.00000000000000, 0.0000000000000000, 0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.00000000000000,  0.0000000000000000, 0.0000000000000000, -500.00000000000000]     # antiquark
p4 = [452.43514519062069, -360.30712670107181, 273.29434984302782, 13.657722941712629]      # antinuetrino
p3 = [166.74787661340551, 136.45200948428351, -3.9533202721630261, -95.760507108130113]     # lepton
pH = [380.81697819597377, 223.85511721678819, -269.34102957086469, 82.102784166417536]      # Higgs boson
# OpenLoops results for squared amplitude
OpenLoopsResTree = 2.1564977816288064E-011          # tree level
OpenLoopsResOneLoopEps2 = -9.1524608456781679E-012  # one-loop 1/eps^2 pole
OpenLoopsResOneLoopEps1 = 3.0108520397255691E-011   # one-loop 1/eps pole
OpenLoopsResOneLoopFin = -3.0671197913617454E-011   # one-loop finite part
"""

# T6
"""
p1 = [500.00000000000000, 0.0000000000000000, 0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.00000000000000,  0.0000000000000000, 0.0000000000000000, -500.00000000000000]     # antiquark
p4 = [437.54043701755631, -97.116824717561357, 24.273872530803061, -425.93513061809170]     # antinuetrino
p3 = [155.34397295089261, 76.271838801236925, 118.04809928637390, 66.174034129106673]       # lepton
pH = [407.11559003155111, 20.844985916324440, -142.32197181717689, 359.76109648898500]      # Higgs boson
# OpenLoops results for squared amplitude
OpenLoopsResTree = 2.1353768988401058E-010          # tree level
OpenLoopsResOneLoopEps2 = -9.0628210350572019E-011  # one-loop 1/eps^2 pole
OpenLoopsResOneLoopEps1 = 2.9813635544755937E-010   # one-loop 1/eps pole
OpenLoopsResOneLoopFin = -3.0370802160076132E-010   # one-loop finite part
"""


print("External Momenta:")
print("p1 = [", p1[0], ",", p1[1], ",", p1[2], ",", p1[3], "] (quark)")
print("p2 = [", p2[0], ",", p2[1], ",", p2[2], ",", p2[3], "] (antiquark)")
print("p3 = [", p3[0], ",", p3[1], ",", p3[2], ",", p3[3], "] (lepton)")
print("p4 = [", p4[0], ",", p4[1], ",", p4[2], ",", p4[3], "] (antilepton)")
print("pH = [", pH[0], ",", pH[1], ",", pH[2], ",", pH[3], "] (Higgs)")
print()


# check of the momentum conservation law: p1 + p2 = p3 + p4 + pH

sumP = []
i = 0
while i < 4:
    sumP.append(p1[i] + p2[i] - p3[i] - p4[i] - pH[i])
    i += 1
sumPround = []
for i in sumP:
    sumPround.append(round(i, 12))

print("Momentum conservation law:")
print("p1 + p2 - p3 - p4 - pH = ", sumPround)
print()


# check of squared momenta: p1^2 = 0, p2^2 = 0, p3^2 = 0, p4^2 = 0, pH^2 = mH^2 (all particles are massless except for the Higgs boson)
# to obtain squared momenta I use the Minkowski metrics (1, -1, -1, -1)

p1sq = p1[0]**2 - p1[1]**2 - p1[2]**2 - p1[3]**2
p2sq = p2[0]**2 - p2[1]**2 - p2[2]**2 - p2[3]**2
p3sq = p3[0]**2 - p3[1]**2 - p3[2]**2 - p3[3]**2
p4sq = p4[0]**2 - p4[1]**2 - p4[2]**2 - p4[3]**2
pHsq = pH[0]**2 - pH[1]**2 - pH[2]**2 - pH[3]**2

print("Squared momenta:")
print("p1^2 = ", round(p1sq, 10))
print("p2^2 = ", round(p2sq, 10))
print("p3^2 = ", round(p3sq, 10))
print("p4^2 = ", round(p4sq, 10))
print("pH^2 = ", round(pHsq, 10))
print("mH^2 = ", round(mH**2, 10))
print()


O = np.array([[0], [0], [0], [0]])  # just a zero-vector for comfort notation
p1 = np.array([[p1[0]], [p1[1]], [p1[2]], [p1[3]]]) # quark
p2 = np.array([[p2[0]], [p2[1]], [p2[2]], [p2[3]]]) # antiquark
p3 = np.array([[p3[0]], [p3[1]], [p3[2]], [p3[3]]]) # electron
p4 = np.array([[p4[0]], [p4[1]], [p4[2]], [p4[3]]]) # electron antinuetrino


# Define external momenta as a matrix 4x6, where the 0-th line consists of zeros (just for convenience of notation)
p = np.hstack((O, p1, p2, p3, p4))
#print(p)
#print()


# Define scalar products of momenta as a matrix sij = 2(pi*pj)
print("Scalar products of momenta: sij = 2(pi*pj)")
s = np.zeros((5,5)) # create a 5x5 matrix of zeros
i = 1
j = 1
while i < 5:
    while j < 5:
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
while j < 5:
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
while j < 5:
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
while i < 5:
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
while i < 5:
    Uminusbar[i,0] = (p[1,i] + 1j*p[2,i])/math.sqrt(p[0,i] + p[3,i])
    Uminusbar[i,1] = -math.sqrt(p[0,i] + p[3,i])
    i += 1
#print("Matrix of spinors [U_-]bar(pi)")
#print(Uminusbar)



# Define a matrix of spinor products A_(ij) = <pipj>
print("Spinor products <pipj>:")
Ang = np.array([[0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j]])
#print(A)
i = 1;
j = 1;
while i < 5:
    while j < 5:
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
#print(S)
i = 1;
j = 1;
while i < 5:
    while j < 5:
        if i != j:
            Sq[i,j] = Uplusbar[i,0] * Uminus[0,j] + Uplusbar[i,1] * Uminus[1,j] + Uplusbar[i,2] * Uminus[2,j] + Uplusbar[i,3] * Uminus[3,j]
            print("[ p", i, "p", j, "] = ", Sq[i,j])
        j += 1
    i += 1
    j = 1
print()


# Global factor settings
prop1 = 1 / (s[1,2] - mV**2 + 1j*mV*Gamma_V)
prop2 = 1 / (s[3,4] - mV**2 + 1j*mV*Gamma_V)

GlobFac_SM = 1j * gW**3 * mV**3/(mW**2) * prop1 * prop2
GlobFac_SMEFT = gW * prop2

print("Global factors:")
print("G = ", GlobFac_SM, " (Standard Model)")
print("G = ", GlobFac_SMEFT, " (SMEFT)")
print()
print()


                                                                                        # LEADING ORDER (TREE LEVEL)
                                                                                        
                # Particle order: quark(p1), antiquark(p2), lepton(p3), antinuetrino(p4)

print("-----------------------------------------")
print("LEADING ORDER (TREE LEVEL)")
print("-----------------------------------------")
print()
# Tree-level form factors
FFtree1 = 1
FFtree2 = 0
FFtree3 = 1
print("Tree-level form factors:")
print("FFtree1 =", FFtree1)
print("FFtree2 =", FFtree2)
print("FFtree3 =", FFtree3)
print()

# SM Tree-level helicity amplitudes iM(quark, antiquark, lepton, antilepton)
MLRLLtreeSM = 0 * GlobFac_SM
MRLLLtreeSM = 0 * GlobFac_SM
MLLLLtreeSM = -2 * (vq + aq) * (a + b) * FFtree3 * Ang[2,3] * Sq[1,4] * GlobFac_SM
MRRLLtreeSM = -2 * (vq - aq) * (a + b) * FFtree3 * Ang[1,3] * Sq[2,4] * GlobFac_SM
MLRRRtreeSM = 0 * GlobFac_SM
MRLRRtreeSM = 0 * GlobFac_SM
MLLRRtreeSM = -2 * (vq + aq) * b * FFtree3 * Sq[1,3] * Ang[2,4] * GlobFac_SM
MRRRRtreeSM = -2 * (vq - aq) * b * FFtree3 * Ang[1,4] * Sq[2,3] * GlobFac_SM

# SMEFT Tree-level helicity amplitudes
MLRLLtreeSMEFT = A * (a + b) * (-4 * FFtree1 * Sq[1,4] * Sq[2,4] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtree2 * Sq[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtree2 * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MRLLLtreeSMEFT = B * (a + b) * (4 * FFtree1 * Ang[1,3] * Ang[2,3] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtree2 * Ang[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtree2 * Ang[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MLLLLtreeSMEFT = -2 * C * (a + b) * FFtree3 * Ang[2,3] * Sq[1,4] * GlobFac_SMEFT
MRRLLtreeSMEFT = -2 * D * (a + b) * FFtree3 * Ang[1,3] * Sq[2,4] * GlobFac_SMEFT
MLRRRtreeSMEFT = A * b * (4 * FFtree1 * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtree2 * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtree2 * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MRLRRtreeSMEFT = B * b * (-4 * FFtree1 * Ang[1,4] * Ang[2,4] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtree2 * Ang[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtree2 * Ang[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MLLRRtreeSMEFT = -2 * C * b * FFtree3 * Sq[1,3] * Ang[2,4] * GlobFac_SMEFT
MRRRRtreeSMEFT = -2 * D * b * FFtree3 * Ang[1,4] * Sq[2,3] * GlobFac_SMEFT


print("Standard Model tree-level helicity amplitudes iM(quark, antiquark, lepton, antilepton):")
print("M(L,R,L,L)_tree = ", MLRLLtreeSM)
print("M(R,L,L,L)_tree = ", MRLLLtreeSM)
print("M(L,L,L,L)_tree = ", MLLLLtreeSM)
print("M(R,R,L,L)_tree = ", MRRLLtreeSM)
print("M(L,R,R,R)_tree = ", MLRRRtreeSM)
print("M(R,L,R,R)_tree = ", MRLRRtreeSM)
print("M(L,L,R,R)_tree = ", MLLRRtreeSM)
print("M(R,R,R,R)_tree = ", MRRRRtreeSM)
print()
print("SMEFT tree-level helicity amplitudes:")
print("M(L,R,L,L)_tree = ", MLRLLtreeSMEFT)
print("M(R,L,L,L)_tree = ", MRLLLtreeSMEFT)
print("M(L,L,L,L)_tree = ", MLLLLtreeSMEFT)
print("M(R,R,L,L)_tree = ", MRRLLtreeSMEFT)
print("M(L,R,R,R)_tree = ", MLRRRtreeSMEFT)
print("M(R,L,R,R)_tree = ", MRLRRtreeSMEFT)
print("M(L,L,R,R)_tree = ", MLLRRtreeSMEFT)
print("M(R,R,R,R)_tree = ", MRRRRtreeSMEFT)
print()

# Tree-level squared amplitudes (including color summation Nc and spin average 1/(2Nc)^2)
# neglect terms of the order Wilson**2
M2LRLLtree = (MLRLLtreeSM * MLRLLtreeSM.conjugate() + (2 * MLRLLtreeSM * MLRLLtreeSMEFT).real) * (Nc/((2*Nc)**2))
M2RLLLtree = (MRLLLtreeSM * MRLLLtreeSM.conjugate() + (2 * MRLLLtreeSM * MRLLLtreeSMEFT).real) * (Nc/((2*Nc)**2))
M2LLLLtree = (MLLLLtreeSM * MLLLLtreeSM.conjugate() + (2 * MLLLLtreeSM * MLLLLtreeSMEFT).real) * (Nc/((2*Nc)**2))
M2RRLLtree = (MRRLLtreeSM * MRRLLtreeSM.conjugate() + (2 * MRRLLtreeSM * MRRLLtreeSMEFT).real) * (Nc/((2*Nc)**2))
M2LRRRtree = (MLRRRtreeSM * MLRRRtreeSM.conjugate() + (2 * MLRRRtreeSM * MLRRRtreeSMEFT).real) * (Nc/((2*Nc)**2))
M2RLRRtree = (MRLRRtreeSM * MRLRRtreeSM.conjugate() + (2 * MRLRRtreeSM * MRLRRtreeSMEFT).real) * (Nc/((2*Nc)**2))
M2LLRRtree = (MLLRRtreeSM * MLLRRtreeSM.conjugate() + (2 * MLLRRtreeSM * MLLRRtreeSMEFT).real) * (Nc/((2*Nc)**2))
M2RRRRtree = (MRRRRtreeSM * MRRRRtreeSM.conjugate() + (2 * MRRRRtreeSM * MRRRRtreeSMEFT).real) * (Nc/((2*Nc)**2))

print("Squared tree-level helicity amplitudes:")
print("|M(L,R,L,L)_tree|^2 = ", M2LRLLtree.real)
print("|M(R,L,L,L)_tree|^2 = ", M2RLLLtree.real)
print("|M(L,L,L,L)_tree|^2 = ", M2LLLLtree.real)
print("|M(R,R,L,L)_tree|^2 = ", M2RRLLtree.real)
print("|M(L,R,R,R)_tree|^2 = ", M2LRRRtree.real)
print("|M(R,L,R,R)_tree|^2 = ", M2RLRRtree.real)
print("|M(L,L,R,R)_tree|^2 = ", M2LLRRtree.real)
print("|M(R,R,R,R)_tree|^2 = ", M2RRRRtree.real)
print()

# Total tree-level squared amplitude
M2tree = M2LRLLtree.real + M2RLLLtree.real + M2LLLLtree.real + M2RRLLtree.real + M2LRRRtree.real + M2RLRRtree.real + M2LLRRtree.real + M2RRRRtree.real

print("Total tree-level squared amplitude:")
print("|M_tree|^2 = ", M2tree, " (Dmitrii)")
print("|M_tree|^2 = ", OpenLoopsResTree, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2tree / OpenLoopsResTree)
print()
print()



                                                                                        # NEXT-TO-LEADING ORDER (ONE LOOP)
                                                                                        
                # Particle order: quark(p1), antiquark(p2), lepton(p3), antinuetrino(p4)

print("-----------------------------------------")
print("NEXT-TO-LEADING ORDER (ONE LOOP)")
print("-----------------------------------------")
print()

# One-loop form factors: FFoneloop[1/eps^0, 1/eps^1, 1/eps^2]
Log = cmath.log(mu**2 / -s[1,2])
OneLoopFactor = gs**2 / (8 * (math.pi)**2)
FFoneloop1 = [(-4 - 2 * Log - 1/2 * Log**2) * Cf * OneLoopFactor, (-2 - Log) * Cf * OneLoopFactor, (-1) * Cf * OneLoopFactor]
FFoneloop2 = [0, 0, 0]
FFoneloop3 = [(-4 - 3/2 * Log - 1/2 * Log**2) * Cf * OneLoopFactor, (-3/2 - Log) * Cf * OneLoopFactor, (-1) * Cf * OneLoopFactor]
print("One-loop form factors [1/eps^0, 1/eps^1, 1/eps^2]:")
print("FFoneloop1 =", FFoneloop1)
print("FFoneloop2 =", FFoneloop2)
print("FFoneloop3 =", FFoneloop3)
print()


# SM one-loop helicity amplitudes iM(quark, antiquark, lepton, antilepton)
# 1/eps^2 poles
MLRLLoneloopEps2SM = 0 * GlobFac_SM
MRLLLoneloopEps2SM = 0 * GlobFac_SM
MLLLLoneloopEps2SM = -2 * (vq + aq) * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SM * FFoneloop3[2]
MRRLLoneloopEps2SM = -2 * (vq - aq) * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SM * FFoneloop3[2]
MLRRRoneloopEps2SM = 0 * GlobFac_SM
MRLRRoneloopEps2SM = 0 * GlobFac_SM
MLLRRoneloopEps2SM = -2 * (vq + aq) * b * Sq[1,3] * Ang[2,4] * GlobFac_SM * FFoneloop3[2]
MRRRRoneloopEps2SM = -2 * (vq - aq) * b * Ang[1,4] * Sq[2,3] * GlobFac_SM * FFoneloop3[2]
# 1/eps poles
MLRLLoneloopEps1SM = 0 * GlobFac_SM
MRLLLoneloopEps1SM = 0 * GlobFac_SM
MLLLLoneloopEps1SM = -2 * (vq + aq) * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SM * FFoneloop3[1]
MRRLLoneloopEps1SM = -2 * (vq - aq) * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SM * FFoneloop3[1]
MLRRRoneloopEps1SM = 0 * GlobFac_SM
MRLRRoneloopEps1SM = 0 * GlobFac_SM
MLLRRoneloopEps1SM = -2 * (vq + aq) * b * Sq[1,3] * Ang[2,4] * GlobFac_SM * FFoneloop3[1]
MRRRRoneloopEps1SM = -2 * (vq - aq) * b * Ang[1,4] * Sq[2,3] * GlobFac_SM * FFoneloop3[1]
# finite parts
MLRLLoneloopFinSM = 0 * GlobFac_SM
MRLLLoneloopFinSM = 0 * GlobFac_SM
MLLLLoneloopFinSM = -2 * (vq + aq) * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SM * FFoneloop3[0]
MRRLLoneloopFinSM = -2 * (vq - aq) * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SM * FFoneloop3[0]
MLRRRoneloopFinSM = 0 * GlobFac_SM
MRLRRoneloopFinSM = 0 * GlobFac_SM
MLLRRoneloopFinSM = -2 * (vq + aq) * b * Sq[1,3] * Ang[2,4] * GlobFac_SM * FFoneloop3[0]
MRRRRoneloopFinSM = -2 * (vq - aq) * b * Ang[1,4] * Sq[2,3] * GlobFac_SM * FFoneloop3[0]

# SMEFT one-loop helicity amplitudes
# 1/eps^2 poles
MLRLLoneloopEps2SMEFT = B * (a + b) * (-4 * FFoneloop1[2] * Sq[1,4] * Sq[2,4] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[2] * Sq[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[2] * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MRLLLoneloopEps2SMEFT = A * (a + b) * (4 * FFoneloop1[2] * Ang[1,3] * Ang[2,3] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[2] * Ang[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[2] * Ang[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MLLLLoneloopEps2SMEFT = -2 * C * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SMEFT * FFoneloop3[2]
MRRLLoneloopEps2SMEFT = -2 * D * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SMEFT * FFoneloop3[2]
MLRRRoneloopEps2SMEFT = B * b * (4 * FFoneloop1[2] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[2] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[2] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MRLRRoneloopEps2SMEFT = A * b * (-4 * FFoneloop1[2] * Ang[1,4] * Ang[2,4] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[2] * Ang[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[2] * Ang[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MLLRRoneloopEps2SMEFT = -2 * C * b * Sq[1,3] * Ang[2,4] * GlobFac_SMEFT * FFoneloop3[2]
MRRRRoneloopEps2SMEFT = -2 * D * b * Ang[1,4] * Sq[2,3] * GlobFac_SMEFT * FFoneloop3[2]
# 1/eps poles
MLRLLoneloopEps1SMEFT = B * (a + b) * (-4 * FFoneloop1[1] * Sq[1,4] * Sq[2,4] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[1] * Sq[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[1] * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MRLLLoneloopEps1SMEFT = A * (a + b) * (4 * FFoneloop1[1] * Ang[1,3] * Ang[2,3] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[1] * Ang[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[1] * Ang[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MLLLLoneloopEps1SMEFT = -2 * C * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SMEFT * FFoneloop3[1]
MRRLLoneloopEps1SMEFT = -2 * D * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SMEFT * FFoneloop3[1]
MLRRRoneloopEps1SMEFT = B * b * (4 * FFoneloop1[1] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[1] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[1] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MRLRRoneloopEps1SMEFT = B * b * (4 * FFoneloop1[1] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[1] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[1] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MLLRRoneloopEps1SMEFT = -2 * C * b * Sq[1,3] * Ang[2,4] * GlobFac_SMEFT * FFoneloop3[1]
MRRRRoneloopEps1SMEFT = -2 * D * b * Ang[1,4] * Sq[2,3] * GlobFac_SMEFT * FFoneloop3[1]
# finite parts
MLRLLoneloopFinSMEFT = B * (a + b) * (-4 * FFoneloop1[0] * Sq[1,4] * Sq[2,4] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[0] * Sq[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[0] * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MRLLLoneloopFinSMEFT = A * (a + b) * (4 * FFoneloop1[0] * Ang[1,3] * Ang[2,3] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[0] * Ang[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[0] * Ang[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MLLLLoneloopFinSMEFT = -2 * C * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SMEFT * FFoneloop3[0]
MRRLLoneloopFinSMEFT = -2 * D * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SMEFT * FFoneloop3[0]
MLRRRoneloopFinSMEFT = B * b * (4 * FFoneloop1[0] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[0] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[0] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MRLRRoneloopFinSMEFT = B * b * (4 * FFoneloop1[0] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFoneloop2[0] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFoneloop2[0] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MLLRRoneloopFinSMEFT = -2 * C * b * Sq[1,3] * Ang[2,4] * GlobFac_SMEFT * FFoneloop3[0]
MRRRRoneloopFinSMEFT = -2 * D * b * Ang[1,4] * Sq[2,3] * GlobFac_SMEFT * FFoneloop3[0]

print("Standard Model one-loop helicity amplitudes iM(quark, antiquark, lepton, antilepton)")
print("1/eps^2 poles:")
print("M(L,R,L,L)_oneloop = ", MLRLLoneloopEps2SM)
print("M(R,L,L,L)_oneloop = ", MRLLLoneloopEps2SM)
print("M(L,L,L,L)_oneloop = ", MLLLLoneloopEps2SM)
print("M(R,R,L,L)_oneloop = ", MRRLLoneloopEps2SM)
print("M(L,R,R,R)_oneloop = ", MLRRRoneloopEps2SM)
print("M(R,L,R,R)_oneloop = ", MRLRRoneloopEps2SM)
print("M(L,L,R,R)_oneloop = ", MLLRRoneloopEps2SM)
print("M(R,R,R,R)_oneloop = ", MRRRRoneloopEps2SM)
print()
print("1/eps poles:")
print("M(L,R,L,L)_oneloop = ", MLRLLoneloopEps1SM)
print("M(R,L,L,L)_oneloop = ", MRLLLoneloopEps1SM)
print("M(L,L,L,L)_oneloop = ", MLLLLoneloopEps1SM)
print("M(R,R,L,L)_oneloop = ", MRRLLoneloopEps1SM)
print("M(L,R,R,R)_oneloop = ", MLRRRoneloopEps1SM)
print("M(R,L,R,R)_oneloop = ", MRLRRoneloopEps1SM)
print("M(L,L,R,R)_oneloop = ", MLLRRoneloopEps1SM)
print("M(R,R,R,R)_oneloop = ", MRRRRoneloopEps1SM)
print()
print("finite parts:")
print("M(L,R,L,L)_oneloop = ", MLRLLoneloopFinSM)
print("M(R,L,L,L)_oneloop = ", MRLLLoneloopFinSM)
print("M(L,L,L,L)_oneloop = ", MLLLLoneloopFinSM)
print("M(R,R,L,L)_oneloop = ", MRRLLoneloopFinSM)
print("M(L,R,R,R)_oneloop = ", MLRRRoneloopFinSM)
print("M(R,L,R,R)_oneloop = ", MRLRRoneloopFinSM)
print("M(L,L,R,R)_oneloop = ", MLLRRoneloopFinSM)
print("M(R,R,R,R)_oneloop = ", MRRRRoneloopFinSM)
print()
print("SMEFT one-loop helicity amplitudes")
print("1/eps^2 poles:")
print("M(L,R,L,L)_oneloop = ", MLRLLoneloopEps2SMEFT)
print("M(R,L,L,L)_oneloop = ", MRLLLoneloopEps2SMEFT)
print("M(L,L,L,L)_oneloop = ", MLLLLoneloopEps2SMEFT)
print("M(R,R,L,L)_oneloop = ", MRRLLoneloopEps2SMEFT)
print("M(L,R,R,R)_oneloop = ", MLRRRoneloopEps2SMEFT)
print("M(R,L,R,R)_oneloop = ", MRLRRoneloopEps2SMEFT)
print("M(L,L,R,R)_oneloop = ", MLLRRoneloopEps2SMEFT)
print("M(R,R,R,R)_oneloop = ", MRRRRoneloopEps2SMEFT)
print()
print("1/eps poles:")
print("M(L,R,L,L)_oneloop = ", MLRLLoneloopEps1SMEFT)
print("M(R,L,L,L)_oneloop = ", MRLLLoneloopEps1SMEFT)
print("M(L,L,L,L)_oneloop = ", MLLLLoneloopEps1SMEFT)
print("M(R,R,L,L)_oneloop = ", MRRLLoneloopEps1SMEFT)
print("M(L,R,R,R)_oneloop = ", MLRRRoneloopEps1SMEFT)
print("M(R,L,R,R)_oneloop = ", MRLRRoneloopEps1SMEFT)
print("M(L,L,R,R)_oneloop = ", MLLRRoneloopEps1SMEFT)
print("M(R,R,R,R)_oneloop = ", MRRRRoneloopEps1SMEFT)
print()
print("finite parts:")
print("M(L,R,L,L)_oneloop = ", MLRLLoneloopFinSMEFT)
print("M(R,L,L,L)_oneloop = ", MRLLLoneloopFinSMEFT)
print("M(L,L,L,L)_oneloop = ", MLLLLoneloopFinSMEFT)
print("M(R,R,L,L)_oneloop = ", MRRLLoneloopFinSMEFT)
print("M(L,R,R,R)_oneloop = ", MLRRRoneloopFinSMEFT)
print("M(R,L,R,R)_oneloop = ", MRLRRoneloopFinSMEFT)
print("M(L,L,R,R)_oneloop = ", MLLRRoneloopFinSMEFT)
print("M(R,R,R,R)_oneloop = ", MRRRRoneloopFinSMEFT)
print()


# Squared amplitudes of order (alpha_s)^1 (including color summation Nc and spin average 1/(2Nc)^2)
# neglect terms of the order Wilson**2
# 1/eps^2 poles
M2LRLLalphas1Eps2 = (2 * (MLRLLtreeSM * MLRLLoneloopEps2SMEFT.conjugate()).real + 2 * (MLRLLoneloopEps2SM * MLRLLtreeSMEFT.conjugate()).real + 2 * (MLRLLtreeSM * MLRLLoneloopEps2SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLLLalphas1Eps2 = (2 * (MRLLLtreeSM * MRLLLoneloopEps2SMEFT.conjugate()).real + 2 * (MRLLLoneloopEps2SM * MRLLLtreeSMEFT.conjugate()).real + 2 * (MRLLLtreeSM * MRLLLoneloopEps2SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLLLalphas1Eps2 = (2 * (MLLLLtreeSM * MLLLLoneloopEps2SMEFT.conjugate()).real + 2 * (MLLLLoneloopEps2SM * MLLLLtreeSMEFT.conjugate()).real + 2 * (MLLLLtreeSM * MLLLLoneloopEps2SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRLLalphas1Eps2 = (2 * (MRRLLtreeSM * MRRLLoneloopEps2SMEFT.conjugate()).real + 2 * (MRRLLoneloopEps2SM * MRRLLtreeSMEFT.conjugate()).real + 2 * (MRRLLtreeSM * MRRLLoneloopEps2SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LRRRalphas1Eps2 = (2 * (MLRRRtreeSM * MLRRRoneloopEps2SMEFT.conjugate()).real + 2 * (MLRRRoneloopEps2SM * MLRRRtreeSMEFT.conjugate()).real + 2 * (MLRRRtreeSM * MLRRRoneloopEps2SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLRRalphas1Eps2 = (2 * (MRLRRtreeSM * MRLRRoneloopEps2SMEFT.conjugate()).real + 2 * (MRLRRoneloopEps2SM * MRLRRtreeSMEFT.conjugate()).real + 2 * (MRLRRtreeSM * MRLRRoneloopEps2SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLRRalphas1Eps2 = (2 * (MLLRRtreeSM * MLLRRoneloopEps2SMEFT.conjugate()).real + 2 * (MLLRRoneloopEps2SM * MLLRRtreeSMEFT.conjugate()).real + 2 * (MLLRRtreeSM * MLLRRoneloopEps2SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRRRalphas1Eps2 = (2 * (MRRRRtreeSM * MRRRRoneloopEps2SMEFT.conjugate()).real + 2 * (MRRRRoneloopEps2SM * MRRRRtreeSMEFT.conjugate()).real + 2 * (MRRRRtreeSM * MRRRRoneloopEps2SM.conjugate()).real) * (Nc/((2*Nc)**2))

# 1/eps^1 poles
M2LRLLalphas1Eps1 = (2 * (MLRLLtreeSM * MLRLLoneloopEps1SMEFT.conjugate()).real + 2 * (MLRLLoneloopEps1SM * MLRLLtreeSMEFT.conjugate()).real + 2 * (MLRLLtreeSM * MLRLLoneloopEps1SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLLLalphas1Eps1 = (2 * (MRLLLtreeSM * MRLLLoneloopEps1SMEFT.conjugate()).real + 2 * (MRLLLoneloopEps1SM * MRLLLtreeSMEFT.conjugate()).real + 2 * (MRLLLtreeSM * MRLLLoneloopEps1SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLLLalphas1Eps1 = (2 * (MLLLLtreeSM * MLLLLoneloopEps1SMEFT.conjugate()).real + 2 * (MLLLLoneloopEps1SM * MLLLLtreeSMEFT.conjugate()).real + 2 * (MLLLLtreeSM * MLLLLoneloopEps1SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRLLalphas1Eps1 = (2 * (MRRLLtreeSM * MRRLLoneloopEps1SMEFT.conjugate()).real + 2 * (MRRLLoneloopEps1SM * MRRLLtreeSMEFT.conjugate()).real + 2 * (MRRLLtreeSM * MRRLLoneloopEps1SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LRRRalphas1Eps1 = (2 * (MLRRRtreeSM * MLRRRoneloopEps1SMEFT.conjugate()).real + 2 * (MLRRRoneloopEps1SM * MLRRRtreeSMEFT.conjugate()).real + 2 * (MLRRRtreeSM * MLRRRoneloopEps1SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLRRalphas1Eps1 = (2 * (MRLRRtreeSM * MRLRRoneloopEps1SMEFT.conjugate()).real + 2 * (MRLRRoneloopEps1SM * MRLRRtreeSMEFT.conjugate()).real + 2 * (MRLRRtreeSM * MRLRRoneloopEps1SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLRRalphas1Eps1 = (2 * (MLLRRtreeSM * MLLRRoneloopEps1SMEFT.conjugate()).real + 2 * (MLLRRoneloopEps1SM * MLLRRtreeSMEFT.conjugate()).real + 2 * (MLLRRtreeSM * MLLRRoneloopEps1SM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRRRalphas1Eps1 = (2 * (MRRRRtreeSM * MRRRRoneloopEps1SMEFT.conjugate()).real + 2 * (MRRRRoneloopEps1SM * MRRRRtreeSMEFT.conjugate()).real + 2 * (MRRRRtreeSM * MRRRRoneloopEps1SM.conjugate()).real) * (Nc/((2*Nc)**2))

# finite parts
M2LRLLalphas1Fin = (2 * (MLRLLtreeSM * MLRLLoneloopFinSMEFT.conjugate()).real + 2 * (MLRLLoneloopFinSM * MLRLLtreeSMEFT.conjugate()).real + 2 * (MLRLLtreeSM * MLRLLoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLLLalphas1Fin = (2 * (MRLLLtreeSM * MRLLLoneloopFinSMEFT.conjugate()).real + 2 * (MRLLLoneloopFinSM * MRLLLtreeSMEFT.conjugate()).real + 2 * (MRLLLtreeSM * MRLLLoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLLLalphas1Fin = (2 * (MLLLLtreeSM * MLLLLoneloopFinSMEFT.conjugate()).real + 2 * (MLLLLoneloopFinSM * MLLLLtreeSMEFT.conjugate()).real + 2 * (MLLLLtreeSM * MLLLLoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRLLalphas1Fin = (2 * (MRRLLtreeSM * MRRLLoneloopFinSMEFT.conjugate()).real + 2 * (MRRLLoneloopFinSM * MRRLLtreeSMEFT.conjugate()).real + 2 * (MRRLLtreeSM * MRRLLoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LRRRalphas1Fin = (2 * (MLRRRtreeSM * MLRRRoneloopFinSMEFT.conjugate()).real + 2 * (MLRRRoneloopFinSM * MLRRRtreeSMEFT.conjugate()).real + 2 * (MLRRRtreeSM * MLRRRoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLRRalphas1Fin = (2 * (MRLRRtreeSM * MRLRRoneloopFinSMEFT.conjugate()).real + 2 * (MRLRRoneloopFinSM * MRLRRtreeSMEFT.conjugate()).real + 2 * (MRLRRtreeSM * MRLRRoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLRRalphas1Fin = (2 * (MLLRRtreeSM * MLLRRoneloopFinSMEFT.conjugate()).real + 2 * (MLLRRoneloopFinSM * MLLRRtreeSMEFT.conjugate()).real + 2 * (MLLRRtreeSM * MLLRRoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRRRalphas1Fin = (2 * (MRRRRtreeSM * MRRRRoneloopFinSMEFT.conjugate()).real + 2 * (MRRRRoneloopFinSM * MRRRRtreeSMEFT.conjugate()).real + 2 * (MRRRRtreeSM * MRRRRoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))

print("Squared helicity amplitudes of order (alpha_s)^1")
print("1/eps^2 poles:")
print("|M(L,R,L,L)_alphas1|^2 = ", M2LRLLalphas1Eps2.real)
print("|M(R,L,L,L)_alphas1|^2 = ", M2RLLLalphas1Eps2.real)
print("|M(L,L,L,L)_alphas1|^2 = ", M2LLLLalphas1Eps2.real)
print("|M(R,R,L,L)_alphas1|^2 = ", M2RRLLalphas1Eps2.real)
print("|M(L,R,R,R)_alphas1|^2 = ", M2LRRRalphas1Eps2.real)
print("|M(R,L,R,R)_alphas1|^2 = ", M2RLRRalphas1Eps2.real)
print("|M(L,L,R,R)_alphas1|^2 = ", M2LLRRalphas1Eps2.real)
print("|M(R,R,R,R)_alphas1|^2 = ", M2RRRRalphas1Eps2.real)
print()
print("1/eps^1 poles:")
print("|M(L,R,L,L)_alphas1|^2 = ", M2LRLLalphas1Eps1.real)
print("|M(R,L,L,L)_alphas1|^2 = ", M2RLLLalphas1Eps1.real)
print("|M(L,L,L,L)_alphas1|^2 = ", M2LLLLalphas1Eps1.real)
print("|M(R,R,L,L)_alphas1|^2 = ", M2RRLLalphas1Eps1.real)
print("|M(L,R,R,R)_alphas1|^2 = ", M2LRRRalphas1Eps1.real)
print("|M(R,L,R,R)_alphas1|^2 = ", M2RLRRalphas1Eps1.real)
print("|M(L,L,R,R)_alphas1|^2 = ", M2LLRRalphas1Eps1.real)
print("|M(R,R,R,R)_alphas1|^2 = ", M2RRRRalphas1Eps1.real)
print()
print("finite parts:")
print("|M(L,R,L,L)_alphas1|^2 = ", M2LRLLalphas1Fin.real)
print("|M(R,L,L,L)_alphas1|^2 = ", M2RLLLalphas1Fin.real)
print("|M(L,L,L,L)_alphas1|^2 = ", M2LLLLalphas1Fin.real)
print("|M(R,R,L,L)_alphas1|^2 = ", M2RRLLalphas1Fin.real)
print("|M(L,R,R,R)_alphas1|^2 = ", M2LRRRalphas1Fin.real)
print("|M(R,L,R,R)_alphas1|^2 = ", M2RLRRalphas1Fin.real)
print("|M(L,L,R,R)_alphas1|^2 = ", M2LLRRalphas1Fin.real)
print("|M(R,R,R,R)_alphas1|^2 = ", M2RRRRalphas1Fin.real)
print()

# Total squared amplitude of order (alphas)^1
M2alphas1Eps2 = M2LRLLalphas1Eps2.real + M2RLLLalphas1Eps2.real + M2LLLLalphas1Eps2.real + M2RRLLalphas1Eps2.real + M2LRRRalphas1Eps2.real + M2RLRRalphas1Eps2.real + M2LLRRalphas1Eps2.real + M2RRRRalphas1Eps2.real
M2alphas1Eps1 = M2LRLLalphas1Eps1.real + M2RLLLalphas1Eps1.real + M2LLLLalphas1Eps1.real + M2RRLLalphas1Eps1.real + M2LRRRalphas1Eps1.real + M2RLRRalphas1Eps1.real + M2LLRRalphas1Eps1.real + M2RRRRalphas1Eps1.real
M2alphas1Fin = M2LRLLalphas1Fin.real + M2RLLLalphas1Fin.real + M2LLLLalphas1Fin.real + M2RRLLalphas1Fin.real + M2LRRRalphas1Fin.real + M2RLRRalphas1Fin.real + M2LLRRalphas1Fin.real + M2RRRRalphas1Fin.real

print("Total tree-level squared amplitude")
print("|M_tree|^2 = ", M2tree, " (Dmitrii)")
print("|M_tree|^2 = ", OpenLoopsResTree, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2tree / OpenLoopsResTree)
print()

print("Total squared amplitude of order (alpha_s)^1")
print("1/eps^2 pole:")
print("|M_alphas1|^2 =", M2alphas1Eps2, " (Dmitrii)")
print("|M_alphas1|^2 =", OpenLoopsResOneLoopEps2, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2alphas1Eps2 / OpenLoopsResOneLoopEps2)
print()
print("1/eps^1 pole:")
print("|M_alphas1|^2 =", M2alphas1Eps1, " (Dmitrii)")
print("|M_alphas1|^2 =", OpenLoopsResOneLoopEps1, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2alphas1Eps1 / OpenLoopsResOneLoopEps1)
print()
print("finite part:")
print("|M_alphas1|^2 =", M2alphas1Fin, " (Dmitrii)")
print("|M_alphas1|^2 =", OpenLoopsResOneLoopFin, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2alphas1Fin / OpenLoopsResOneLoopFin)
print()
print()


                                                                            # NEXT-TO-NEXT-TO-LEADING ORDER (TWO LOOPS)
                                                                                        
                # Particle order: quark(p1), antiquark(p2), lepton(p3), antinuetrino(p4)

print("-----------------------------------------")
print("NEXT-TO-NEXT-TO-LEADING ORDER (TWO LOOPS)")
print("-----------------------------------------")
print()
# Two-loop form factors: FFtwoloop[1/eps^0, 1/eps^1, 1/eps^2, 1/eps^3, 1/eps^4]
TwoLoopFactor = gs**4 / (64 * (math.pi)**4)
FFtwoloop1 = [0, 0, 0, 0, 0]
FFtwoloop2 = [0, 0, 0, 0, 0]
FFtwoloop3 = [0, 0, 0, 0, 0]
# Initialization
FFtwoloop1[4] = (Nc**2 - 1)/(2*Nc) * (Cf - (Nc**2 - 1)/(4*Nc)) * TwoLoopFactor
FFtwoloop1[3] = (Nc**2 - 1)/(2*Nc) * (7/2*Cf + 5/8*Nc - Nf/4 + 3/(4*Nc) + (Cf + Nc/2 - 1/(2*Nc))*Log) * TwoLoopFactor
FFtwoloop1[2] = (Nc**2 - 1)/(2*Nc) * (7*Cf - 17*Nc/144 - Nf/9 + 9/(16*Nc) + (-Cf + Nc/2 - 1/(4*Nc)) * ((math.pi)**2)/6 + (-Nf/6 + 3/(2*Nc) + 7*Nc/12 + 7*Cf/2)*Log + 1/2*(Cf + 1/Nc - Nc)*Log**2) * TwoLoopFactor + (2*Nf - 33)/24 * TwoLoopFactor
FFtwoloop1[1] = (Nc**2 - 1)/(2*Nc) * (7*Cf + 3/(32*Nc) - 2003*Nc/864 + 65*Nf/216 + (9*Nc/43 + 18*Nf/43 - 7*Cf/12 - 1/(4*Nc)) * (math.pi)**2 + Log * (3*Cf + 9/(8*Nc) + 5*Nf/18 - 215*Nc/72 + (Nc - Cf - 1/(2*Nc)) * ((math.pi)**2)/6) + Log**2 * 3/2 * (- Nc + 1/Nc) + Log**3 * 1/3 * (Nc - 1/Nc) - zetazero(3)/12 * (16/Nc - 23*Nc)) * TwoLoopFactor - (51/16*Cf**2 + 13*Cf*Nf/72 + 257*Cf*Nc/144) * TwoLoopFactor
FFtwoloop1[0] = (- ((-1 + Nc**2)*(-5*(-81 + 49*Nc**2 + 8*Nc*Nf)*(math.pi)**2 + 3*(-3 + 8*Nc**2)*(math.pi)**4 - 10*Log*(81 - 2003*Nc**2 + 260*Nc*Nf + 12*(-18 + 7*Nc**2 + 2*Nc*Nf)*(math.pi)**2 - 6*Log*(-81 - 38*Nc*Nf + 6*(math.pi)**2 + Nc**2*(314 - 12*(math.pi)**2) - 2*Log*(36 - 47*Nc**2 + 2*Nc*Nf - 6*(-1 + Nc**2)*Log))) + 180*(12 - Nc*(Nc + 2*Nf) - (64 + 92*Nc**2)*Log)*zetazero(3)))/(8640*Nc**2)) * TwoLoopFactor + (-7*Cf/2 + Cf*((math.pi)**2)/48 + Cf * zetazero(3)) * TwoLoopFactor + ((Nc**2 - 1)/(2*Nc) * (-1j) * (-12109*Nc/648 + 1175*Nf/324 - 83/(12*Nc) + (-5*Nc/4 + Nf/2 - 2/Nc) * ((math.pi)**2)/4 + (49*Nc + 44/Nc) * ((math.pi)**4)/1440  + (61*Nf/36 - 1255*Nc/144 - 35/(16*Nc)) * Log - 1/4 * (19*Nc/12 - Nf/3 + 1/(4*Nc)) * Log**2 + zetazero(3) * (497*Nc/6480 - Nf/(3240*Nc) + 23/(4*Nc)))) * TwoLoopFactor + Cf * (Nc**2 - 1)/(2*Nc) * (-5/2 - ((math.pi)**2)/8 + 29*((math.pi)**4)/720 + Log * (13 - 7*((math.pi)**2)/12) + 1/2 * Log**2 * (7 - ((math.pi)**2)/6) + 7/12 * Log**3 + 1/24*Log**4 + zetazero(3) - 2*zetazero(3)*Log) * TwoLoopFactor
FFtwoloop3[4] = (Nc**2 - 1)/(2*Nc) * (Cf - (Nc**2 - 1)/(4*Nc)) * TwoLoopFactor
FFtwoloop3[3] = (Nc**2 - 1)/(4*Nc) * (6 + 6*Cf + 5*Nc**2 - 2*Nc*Nf + 2*(2 + Cf - 2*Nc**2)*Log) * TwoLoopFactor
FFtwoloop3[2] = (Nc**2 - 1)/(2*Nc) * (27/46 + 25*Cf/4 - Nc*Nf/9 - (17*Nc**2)/144 + ((Nc**2)/2 - 1/4 - Cf) * ((math.pi)**2)/6 + (3/2 - 7/12*Nc**2 - 1/6*Nc*Nf + 3*Cf)*Log + 1/2*(Cf + 1 - Nc**2)*Log**2) * TwoLoopFactor
FFtwoloop3[1] = (Nc**2 - 1)/(2*Nc) * (3/(32*Nc) + 14*Cf - 2003*Nc/864 + 65*Nf/216 + (Nc/24 + Nf/12 - Cf - 1/(2*Nc)) * ((math.pi)**2)/2 + Log * (25*Cf/4 + 9/(8*Nc) + 5/18*Nf/Nc - 215*Nc/72 + (Nc - Cf - 1/(2*Nc)) * ((math.pi)**2)/6) + Log**2 * 3/2 * (Cf - Nc + 1/Nc) + Log**3 * 1/3 * (Cf/2 - Nc + 1/Nc) + zetazero(3)/3 * (-8*Cf + 4/Nc + 23*Nc/4)) * TwoLoopFactor
FFtwoloop3[0] = (Nc**2 - 1)/(2*Nc) * ((-1j) * (-81659*Nc/5184 + 4085*Nf/1296 - 255/(64*Nc) + (-151*Nc/20 + 7*Nf - 413/(10*Nc)) * ((math.pi)**2)/72 - 2/3 * Log * (11*Nc - 2*Nf) + zetazero(3) * (389*Nc/18)/4 - Nf/9 + 45/(8*Nc)) + 28*Cf - (25*Cf/6 + 3/(8*Nc) - 49*Nc/216 - Nc/27) * ((math.pi)**2)/4 + (Cf/8 + 1/(120*Nc) - Nc/45) * ((math.pi)**4)/4 + Log * (14*Cf + 3/(16*Nc) - 2003*Nc/432 + 65*Nf/180 + (7*Nc + 2*Nf - 18/Nc - 18*Cf) * ((math.pi)**2)/36) + Log**2 * (25*Cf/8 + 9/(8*Nc) + 19*Nf/36 - 157*Nc - (Cf/2 + 1/(2*Nc) + Nc) * ((math.pi)**2)/6) + Log**3 * (Cf/2 + 1/Nc - 47*Nc/36 - Nf/18) + Log**4 * (Cf/4 - Nc + 1/Nc)/6 - zetazero(3) * (8*Cf - Nc/24 + 1/(2*Nc) + Nf/12) - Log * zetazero(3) * (8*Cf - 8/Nc - 23*Nc)/3) * TwoLoopFactor


print("Two-loop form factors [1/eps^0, 1/eps^1, 1/eps^2, 1/eps^3, 1/eps^4]:")
print("FFtwoloop1 =", FFtwoloop1)
print("FFtwoloop2 =", FFtwoloop2)
print("FFtwoloop3 =", FFtwoloop3)
print()


# SM two-loop helicity amplitudes iM(quark, antiquark, lepton, antilepton)
# 1/eps^4 poles
MLRLLtwoloopEps4SM = 0 * GlobFac_SM
MRLLLtwoloopEps4SM = 0 * GlobFac_SM
MLLLLtwoloopEps4SM = -2 * (vq + aq) * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SM * FFtwoloop3[4]
MRRLLtwoloopEps4SM = -2 * (vq - aq) * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SM * FFtwoloop3[4]
MLRRRtwoloopEps4SM = 0 * GlobFac_SM
MRLRRtwoloopEps4SM = 0 * GlobFac_SM
MLLRRtwoloopEps4SM = -2 * (vq + aq) * b * Sq[1,3] * Ang[2,4] * GlobFac_SM * FFtwoloop3[4]
MRRRRtwoloopEps4SM = -2 * (vq - aq) * b * Ang[1,4] * Sq[2,3] * GlobFac_SM * FFtwoloop3[4]
# 1/eps^3 poles
MLRLLtwoloopEps3SM = 0 * GlobFac_SM
MRLLLtwoloopEps3SM = 0 * GlobFac_SM
MLLLLtwoloopEps3SM = -2 * (vq + aq) * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SM * FFtwoloop3[3]
MRRLLtwoloopEps3SM = -2 * (vq - aq) * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SM * FFtwoloop3[3]
MLRRRtwoloopEps3SM = 0 * GlobFac_SM
MRLRRtwoloopEps3SM = 0 * GlobFac_SM
MLLRRtwoloopEps3SM = -2 * (vq + aq) * b * Sq[1,3] * Ang[2,4] * GlobFac_SM * FFtwoloop3[3]
MRRRRtwoloopEps3SM = -2 * (vq - aq) * b * Ang[1,4] * Sq[2,3] * GlobFac_SM * FFtwoloop3[3]
# 1/eps^2 poles
MLRLLtwoloopEps2SM = 0 * GlobFac_SM
MRLLLtwoloopEps2SM = 0 * GlobFac_SM
MLLLLtwoloopEps2SM = -2 * (vq + aq) * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SM * FFtwoloop3[2]
MRRLLtwoloopEps2SM = -2 * (vq - aq) * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SM * FFtwoloop3[2]
MLRRRtwoloopEps2SM = 0 * GlobFac_SM
MRLRRtwoloopEps2SM = 0 * GlobFac_SM
MLLRRtwoloopEps2SM = -2 * (vq + aq) * b * Sq[1,3] * Ang[2,4] * GlobFac_SM * FFtwoloop3[2]
MRRRRtwoloopEps2SM = -2 * (vq - aq) * b * Ang[1,4] * Sq[2,3] * GlobFac_SM * FFtwoloop3[2]
# 1/eps poles
MLRLLtwoloopEps1SM = 0 * GlobFac_SM
MRLLLtwoloopEps1SM = 0 * GlobFac_SM
MLLLLtwoloopEps1SM = -2 * (vq + aq) * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SM * FFtwoloop3[1]
MRRLLtwoloopEps1SM = -2 * (vq - aq) * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SM * FFtwoloop3[1]
MLRRRtwoloopEps1SM = 0 * GlobFac_SM
MRLRRtwoloopEps1SM = 0 * GlobFac_SM
MLLRRtwoloopEps1SM = -2 * (vq + aq) * b * Sq[1,3] * Ang[2,4] * GlobFac_SM * FFtwoloop3[1]
MRRRRtwoloopEps1SM = -2 * (vq - aq) * b * Ang[1,4] * Sq[2,3] * GlobFac_SM * FFtwoloop3[1]
# finite parts
MLRLLtwoloopFinSM = 0 * GlobFac_SM
MRLLLtwoloopFinSM = 0 * GlobFac_SM
MLLLLtwoloopFinSM = -2 * (vq + aq) * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SM * FFtwoloop3[0]
MRRLLtwoloopFinSM = -2 * (vq - aq) * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SM * FFtwoloop3[0]
MLRRRtwoloopFinSM = 0 * GlobFac_SM
MRLRRtwoloopFinSM = 0 * GlobFac_SM
MLLRRtwoloopFinSM = -2 * (vq + aq) * b * Sq[1,3] * Ang[2,4] * GlobFac_SM * FFtwoloop3[0]
MRRRRtwoloopFinSM = -2 * (vq - aq) * b * Ang[1,4] * Sq[2,3] * GlobFac_SM * FFtwoloop3[0]

# SMEFT two-loop helicity amplitudes
# 1/eps^4 poles
MLRLLtwoloopEps4SMEFT = B * (a + b) * (-4 * FFtwoloop1[4] * Sq[1,4] * Sq[2,4] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[4] * Sq[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[4] * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MRLLLtwoloopEps4SMEFT = A * (a + b) * (4 * FFtwoloop1[4] * Ang[1,3] * Ang[2,3] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[4] * Ang[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[4] * Ang[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MLLLLtwoloopEps4SMEFT = -2 * C * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SMEFT * FFtwoloop3[4]
MRRLLtwoloopEps4SMEFT = -2 * D * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SMEFT * FFtwoloop3[4]
MLRRRtwoloopEps4SMEFT = B * b * (4 * FFtwoloop1[4] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[4] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[4] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MRLRRtwoloopEps4SMEFT = A * b * (-4 * FFtwoloop1[4] * Ang[1,4] * Ang[2,4] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[4] * Ang[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[4] * Ang[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MLLRRtwoloopEps4SMEFT = -2 * C * b * Sq[1,3] * Ang[2,4] * GlobFac_SMEFT * FFtwoloop3[4]
MRRRRtwoloopEps4SMEFT = -2 * D * b * Ang[1,4] * Sq[2,3] * GlobFac_SMEFT * FFtwoloop3[4]
# 1/eps^3 poles
MLRLLtwoloopEps3SMEFT = B * (a + b) * (-4 * FFtwoloop1[3] * Sq[1,4] * Sq[2,4] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[3] * Sq[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[3] * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MRLLLtwoloopEps3SMEFT = A * (a + b) * (4 * FFtwoloop1[3] * Ang[1,3] * Ang[2,3] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[3] * Ang[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[3] * Ang[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MLLLLtwoloopEps3SMEFT = -2 * C * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SMEFT * FFtwoloop3[3]
MRRLLtwoloopEps3SMEFT = -2 * D * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SMEFT * FFtwoloop3[3]
MLRRRtwoloopEps3SMEFT = B * b * (4 * FFtwoloop1[3] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[3] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[3] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MRLRRtwoloopEps3SMEFT = A * b * (-4 * FFtwoloop1[3] * Ang[1,4] * Ang[2,4] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[3] * Ang[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[3] * Ang[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MLLRRtwoloopEps3SMEFT = -2 * C * b * Sq[1,3] * Ang[2,4] * GlobFac_SMEFT * FFtwoloop3[3]
MRRRRtwoloopEps3SMEFT = -2 * D * b * Ang[1,4] * Sq[2,3] * GlobFac_SMEFT * FFtwoloop3[3]
# 1/eps^2 poles
MLRLLtwoloopEps2SMEFT = B * (a + b) * (-4 * FFtwoloop1[2] * Sq[1,4] * Sq[2,4] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[2] * Sq[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[2] * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MRLLLtwoloopEps2SMEFT = A * (a + b) * (4 * FFtwoloop1[2] * Ang[1,3] * Ang[2,3] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[2] * Ang[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[2] * Ang[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MLLLLtwoloopEps2SMEFT = -2 * C * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SMEFT * FFtwoloop3[2]
MRRLLtwoloopEps2SMEFT = -2 * D * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SMEFT * FFtwoloop3[2]
MLRRRtwoloopEps2SMEFT = B * b * (4 * FFtwoloop1[2] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[2] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[2] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MRLRRtwoloopEps2SMEFT = A * b * (-4 * FFtwoloop1[2] * Ang[1,4] * Ang[2,4] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[2] * Ang[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[2] * Ang[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MLLRRtwoloopEps2SMEFT = -2 * C * b * Sq[1,3] * Ang[2,4] * GlobFac_SMEFT * FFtwoloop3[2]
MRRRRtwoloopEps2SMEFT = -2 * D * b * Ang[1,4] * Sq[2,3] * GlobFac_SMEFT * FFtwoloop3[2]
# 1/eps poles
MLRLLtwoloopEps1SMEFT = B * (a + b) * (-4 * FFtwoloop1[1] * Sq[1,4] * Sq[2,4] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[1] * Sq[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[1] * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MRLLLtwoloopEps1SMEFT = A * (a + b) * (4 * FFtwoloop1[1] * Ang[1,3] * Ang[2,3] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[1] * Ang[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[1] * Ang[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MLLLLtwoloopEps1SMEFT = -2 * C * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SMEFT * FFtwoloop3[1]
MRRLLtwoloopEps1SMEFT = -2 * D * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SMEFT * FFtwoloop3[1]
MLRRRtwoloopEps1SMEFT = B * b * (4 * FFtwoloop1[1] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[1] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[1] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MRLRRtwoloopEps1SMEFT = B * b * (4 * FFtwoloop1[1] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[1] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[1] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MLLRRtwoloopEps1SMEFT = -2 * C * b * Sq[1,3] * Ang[2,4] * GlobFac_SMEFT * FFtwoloop3[1]
MRRRRtwoloopEps1SMEFT = -2 * D * b * Ang[1,4] * Sq[2,3] * GlobFac_SMEFT * FFtwoloop3[1]
# finite parts
MLRLLtwoloopFinSMEFT = B * (a + b) * (-4 * FFtwoloop1[0] * Sq[1,4] * Sq[2,4] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[0] * Sq[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[0] * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MRLLLtwoloopFinSMEFT = A * (a + b) * (4 * FFtwoloop1[0] * Ang[1,3] * Ang[2,3] * Sq[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[0] * Ang[1,2] * Ang[1,3] * Sq[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[0] * Ang[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_SMEFT
MLLLLtwoloopFinSMEFT = -2 * C * (a + b) * Ang[2,3] * Sq[1,4] * GlobFac_SMEFT * FFtwoloop3[0]
MRRLLtwoloopFinSMEFT = -2 * D * (a + b) * Ang[1,3] * Sq[2,4] * GlobFac_SMEFT * FFtwoloop3[0]
MLRRRtwoloopFinSMEFT = B * b * (4 * FFtwoloop1[0] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[0] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[0] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MRLRRtwoloopFinSMEFT = B * b * (4 * FFtwoloop1[0] * Sq[1,3] * Sq[2,3] * Ang[3,4] + (s[2,3]/2 + s[2,4]/2) * FFtwoloop2[0] * Sq[1,2] * Sq[1,3] * Ang[1,4] - (s[1,3]/2 + s[1,4]/2) * FFtwoloop2[0] * Sq[1,2] * Sq[2,3] * Ang[2,4]) * GlobFac_SMEFT
MLLRRtwoloopFinSMEFT = -2 * C * b * Sq[1,3] * Ang[2,4] * GlobFac_SMEFT * FFtwoloop3[0]
MRRRRtwoloopFinSMEFT = -2 * D * b * Ang[1,4] * Sq[2,3] * GlobFac_SMEFT * FFtwoloop3[0]

print("Standard Model two-loop helicity amplitudes iM(quark, antiquark, lepton, antilepton)")
print("1/eps^4 poles:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopEps4SM)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopEps4SM)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopEps4SM)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopEps4SM)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopEps4SM)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopEps4SM)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopEps4SM)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopEps4SM)
print()
print("1/eps^3 poles:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopEps3SM)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopEps3SM)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopEps3SM)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopEps3SM)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopEps3SM)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopEps3SM)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopEps3SM)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopEps3SM)
print()
print("1/eps^2 poles:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopEps2SM)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopEps2SM)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopEps2SM)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopEps2SM)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopEps2SM)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopEps2SM)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopEps2SM)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopEps2SM)
print()
print("1/eps poles:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopEps1SM)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopEps1SM)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopEps1SM)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopEps1SM)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopEps1SM)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopEps1SM)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopEps1SM)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopEps1SM)
print()
print("finite parts:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopFinSM)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopFinSM)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopFinSM)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopFinSM)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopFinSM)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopFinSM)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopFinSM)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopFinSM)
print()
print("SMEFT two-loop helicity amplitudes")
print("1/eps^4 poles:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopEps4SMEFT)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopEps4SMEFT)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopEps4SMEFT)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopEps4SMEFT)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopEps4SMEFT)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopEps4SMEFT)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopEps4SMEFT)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopEps4SMEFT)
print()
print("1/eps^3 poles:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopEps3SMEFT)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopEps3SMEFT)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopEps3SMEFT)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopEps3SMEFT)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopEps3SMEFT)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopEps3SMEFT)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopEps3SMEFT)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopEps3SMEFT)
print()
print("1/eps^2 poles:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopEps2SMEFT)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopEps2SMEFT)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopEps2SMEFT)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopEps2SMEFT)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopEps2SMEFT)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopEps2SMEFT)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopEps2SMEFT)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopEps2SMEFT)
print()
print("1/eps poles:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopEps1SMEFT)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopEps1SMEFT)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopEps1SMEFT)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopEps1SMEFT)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopEps1SMEFT)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopEps1SMEFT)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopEps1SMEFT)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopEps1SMEFT)
print()
print("finite parts:")
print("M(L,R,L,L)_twoloop = ", MLRLLtwoloopFinSMEFT)
print("M(R,L,L,L)_twoloop = ", MRLLLtwoloopFinSMEFT)
print("M(L,L,L,L)_twoloop = ", MLLLLtwoloopFinSMEFT)
print("M(R,R,L,L)_twoloop = ", MRRLLtwoloopFinSMEFT)
print("M(L,R,R,R)_twoloop = ", MLRRRtwoloopFinSMEFT)
print("M(R,L,R,R)_twoloop = ", MRLRRtwoloopFinSMEFT)
print("M(L,L,R,R)_twoloop = ", MLLRRtwoloopFinSMEFT)
print("M(R,R,R,R)_twoloop = ", MRRRRtwoloopFinSMEFT)
print()


# Squared amplitudes of order (alpha_s)^2 (including color summation Nc and spin average 1/(2Nc)^2)
# neglect terms of the order Wilson**2
# 1/eps^4 poles
M2LRLLalphas2Eps4 = (2 * (MLRLLtreeSM * MLRLLtwoloopEps4SM.conjugate()).real + 2 * (MLRLLtreeSMEFT * MLRLLtwoloopEps4SM.conjugate()).real + 2 * (MLRLLtreeSM * MLRLLtwoloopEps4SMEFT.conjugate()).real + MLRLLoneloopEps2SM * MLRLLoneloopEps2SM.conjugate() + MLRLLoneloopEps2SMEFT * MLRLLoneloopEps2SM.conjugate() + MLRLLoneloopEps2SM * MLRLLoneloopEps2SMEFT.conjugate()) * (Nc/((2*Nc)**2))
M2RLLLalphas2Eps4 = (2 * (MRLLLtreeSM * MRLLLtwoloopEps4SM.conjugate()).real + 2 * (MRLLLtreeSMEFT * MRLLLtwoloopEps4SM.conjugate()).real + 2 * (MRLLLtreeSM * MRLLLtwoloopEps4SMEFT.conjugate()).real + MRLLLoneloopEps2SM * MRLLLoneloopEps2SM.conjugate() + MRLLLoneloopEps2SMEFT * MRLLLoneloopEps2SM.conjugate() + MRLLLoneloopEps2SM * MRLLLoneloopEps2SMEFT.conjugate()) * (Nc/((2*Nc)**2))
M2LLLLalphas2Eps4 = (2 * (MLLLLtreeSM * MLLLLtwoloopEps4SM.conjugate()).real + 2 * (MLLLLtreeSMEFT * MLLLLtwoloopEps4SM.conjugate()).real + 2 * (MLLLLtreeSM * MLLLLtwoloopEps4SMEFT.conjugate()).real + MLLLLoneloopEps2SM * MLLLLoneloopEps2SM.conjugate() + MLLLLoneloopEps2SMEFT * MLLLLoneloopEps2SM.conjugate() + MLLLLoneloopEps2SM * MLLLLoneloopEps2SMEFT.conjugate()) * (Nc/((2*Nc)**2))
M2RRLLalphas2Eps4 = (2 * (MRRLLtreeSM * MRRLLtwoloopEps4SM.conjugate()).real + 2 * (MRRLLtreeSMEFT * MRRLLtwoloopEps4SM.conjugate()).real + 2 * (MRRLLtreeSM * MRRLLtwoloopEps4SMEFT.conjugate()).real + MRRLLoneloopEps2SM * MRRLLoneloopEps2SM.conjugate() + MRRLLoneloopEps2SMEFT * MRRLLoneloopEps2SM.conjugate() + MRRLLoneloopEps2SM * MRRLLoneloopEps2SMEFT.conjugate()) * (Nc/((2*Nc)**2))
M2LRRRalphas2Eps4 = (2 * (MLRRRtreeSM * MLRRRtwoloopEps4SM.conjugate()).real + 2 * (MLRRRtreeSMEFT * MLRRRtwoloopEps4SM.conjugate()).real + 2 * (MLRRRtreeSM * MLRRRtwoloopEps4SMEFT.conjugate()).real + MLRRRoneloopEps2SM * MLRRRoneloopEps2SM.conjugate() + MLRRRoneloopEps2SMEFT * MLRRRoneloopEps2SM.conjugate() + MLRRRoneloopEps2SM * MLRRRoneloopEps2SMEFT.conjugate()) * (Nc/((2*Nc)**2))
M2RLRRalphas2Eps4 = (2 * (MRLRRtreeSM * MRLRRtwoloopEps4SM.conjugate()).real + 2 * (MRLRRtreeSMEFT * MRLRRtwoloopEps4SM.conjugate()).real + 2 * (MRLRRtreeSM * MRLRRtwoloopEps4SMEFT.conjugate()).real + MRLRRoneloopEps2SM * MRLRRoneloopEps2SM.conjugate() + MRLRRoneloopEps2SMEFT * MRLRRoneloopEps2SM.conjugate() + MRLRRoneloopEps2SM * MRLRRoneloopEps2SMEFT.conjugate()) * (Nc/((2*Nc)**2))
M2LLRRalphas2Eps4 = (2 * (MLLRRtreeSM * MLLRRtwoloopEps4SM.conjugate()).real + 2 * (MLLRRtreeSMEFT * MLLRRtwoloopEps4SM.conjugate()).real + 2 * (MLLRRtreeSM * MLLRRtwoloopEps4SMEFT.conjugate()).real + MLLRRoneloopEps2SM * MLLRRoneloopEps2SM.conjugate() + MLLRRoneloopEps2SMEFT * MLLRRoneloopEps2SM.conjugate() + MLLRRoneloopEps2SM * MLLRRoneloopEps2SMEFT.conjugate()) * (Nc/((2*Nc)**2))
M2RRRRalphas2Eps4 = (2 * (MRRRRtreeSM * MRRRRtwoloopEps4SM.conjugate()).real + 2 * (MRRRRtreeSMEFT * MRRRRtwoloopEps4SM.conjugate()).real + 2 * (MRRRRtreeSM * MRRRRtwoloopEps4SMEFT.conjugate()).real + MRRRRoneloopEps2SM * MRRRRoneloopEps2SM.conjugate() + MRRRRoneloopEps2SMEFT * MRRRRoneloopEps2SM.conjugate() + MRRRRoneloopEps2SM * MRRRRoneloopEps2SMEFT.conjugate()) * (Nc/((2*Nc)**2))
# 1/eps^3 poles
M2LRLLalphas2Eps3 = (2 * (MLRLLtreeSM * MLRLLtwoloopEps3SM.conjugate()).real + 2 * (MLRLLtreeSMEFT * MLRLLtwoloopEps3SM.conjugate()).real + 2 * (MLRLLtreeSM * MLRLLtwoloopEps3SMEFT.conjugate()).real + 2 * (MLRLLoneloopEps1SM * MLRLLoneloopEps2SM.conjugate()).real + 2 * (MLRLLoneloopEps1SMEFT * MLRLLoneloopEps2SM.conjugate()).real + 2 * (MLRLLoneloopEps1SM * MLRLLoneloopEps2SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLLLalphas2Eps3 = (2 * (MRLLLtreeSM * MRLLLtwoloopEps3SM.conjugate()).real + 2 * (MRLLLtreeSMEFT * MRLLLtwoloopEps3SM.conjugate()).real + 2 * (MRLLLtreeSM * MRLLLtwoloopEps3SMEFT.conjugate()).real + 2 * (MRLLLoneloopEps1SM * MRLLLoneloopEps2SM.conjugate()).real + 2 * (MRLLLoneloopEps1SMEFT * MRLLLoneloopEps2SM.conjugate()).real + 2 * (MRLLLoneloopEps1SM * MRLLLoneloopEps2SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLLLalphas2Eps3 = (2 * (MLLLLtreeSM * MLLLLtwoloopEps3SM.conjugate()).real + 2 * (MLLLLtreeSMEFT * MLLLLtwoloopEps3SM.conjugate()).real + 2 * (MLLLLtreeSM * MLLLLtwoloopEps3SMEFT.conjugate()).real + 2 * (MLLLLoneloopEps1SM * MLLLLoneloopEps2SM.conjugate()).real + 2 * (MLLLLoneloopEps1SMEFT * MLLLLoneloopEps2SM.conjugate()).real + 2 * (MLLLLoneloopEps1SM * MLLLLoneloopEps2SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRLLalphas2Eps3 = (2 * (MRRLLtreeSM * MRRLLtwoloopEps3SM.conjugate()).real + 2 * (MRRLLtreeSMEFT * MRRLLtwoloopEps3SM.conjugate()).real + 2 * (MRRLLtreeSM * MRRLLtwoloopEps3SMEFT.conjugate()).real + 2 * (MRRLLoneloopEps1SM * MRRLLoneloopEps2SM.conjugate()).real + 2 * (MRRLLoneloopEps1SMEFT * MRRLLoneloopEps2SM.conjugate()).real + 2 * (MRRLLoneloopEps1SM * MRRLLoneloopEps2SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2LRRRalphas2Eps3 = (2 * (MLRRRtreeSM * MLRRRtwoloopEps3SM.conjugate()).real + 2 * (MLRRRtreeSMEFT * MLRRRtwoloopEps3SM.conjugate()).real + 2 * (MLRRRtreeSM * MLRRRtwoloopEps3SMEFT.conjugate()).real + 2 * (MLRRRoneloopEps1SM * MLRRRoneloopEps2SM.conjugate()).real + 2 * (MLRRRoneloopEps1SMEFT * MLRRRoneloopEps2SM.conjugate()).real + 2 * (MLRRRoneloopEps1SM * MLRRRoneloopEps2SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLRRalphas2Eps3 = (2 * (MRLRRtreeSM * MRLRRtwoloopEps3SM.conjugate()).real + 2 * (MRLRRtreeSMEFT * MRLRRtwoloopEps3SM.conjugate()).real + 2 * (MRLRRtreeSM * MRLRRtwoloopEps3SMEFT.conjugate()).real + 2 * (MRLRRoneloopEps1SM * MRLRRoneloopEps2SM.conjugate()).real + 2 * (MRLRRoneloopEps1SMEFT * MRLRRoneloopEps2SM.conjugate()).real + 2 * (MRLRRoneloopEps1SM * MRLRRoneloopEps2SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLRRalphas2Eps3 = (2 * (MLLRRtreeSM * MLLRRtwoloopEps3SM.conjugate()).real + 2 * (MLLRRtreeSMEFT * MLLRRtwoloopEps3SM.conjugate()).real + 2 * (MLLRRtreeSM * MLLRRtwoloopEps3SMEFT.conjugate()).real + 2 * (MLLRRoneloopEps1SM * MLLRRoneloopEps2SM.conjugate()).real + 2 * (MLLRRoneloopEps1SMEFT * MLLRRoneloopEps2SM.conjugate()).real + 2 * (MLLRRoneloopEps1SM * MLLRRoneloopEps2SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRRRalphas2Eps3 = (2 * (MRRRRtreeSM * MRRRRtwoloopEps3SM.conjugate()).real + 2 * (MRRRRtreeSMEFT * MRRRRtwoloopEps3SM.conjugate()).real + 2 * (MRRRRtreeSM * MRRRRtwoloopEps3SMEFT.conjugate()).real + 2 * (MRRRRoneloopEps1SM * MRRRRoneloopEps2SM.conjugate()).real + 2 * (MRRRRoneloopEps1SMEFT * MRRRRoneloopEps2SM.conjugate()).real + 2 * (MRRRRoneloopEps1SM * MRRRRoneloopEps2SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
# 1/eps^2 poles
M2LRLLalphas2Eps2 = (2 * (MLRLLtreeSM * MLRLLtwoloopEps2SM.conjugate()).real + 2 * (MLRLLtreeSMEFT * MLRLLtwoloopEps2SM.conjugate()).real + 2 * (MLRLLtreeSM * MLRLLtwoloopEps2SMEFT.conjugate()).real + 2 * (MLRLLoneloopEps2SM * MLRLLoneloopFinSM.conjugate()).real + 2 * (MLRLLoneloopEps2SMEFT * MLRLLoneloopFinSM.conjugate()).real + 2 * (MLRLLoneloopEps2SM * MLRLLoneloopFinSMEFT.conjugate()).real + (MLRLLoneloopEps1SM * MLRLLoneloopEps1SM.conjugate()).real + 2 * (MLRLLoneloopEps1SM * MLRLLoneloopEps1SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLLLalphas2Eps2 = (2 * (MRLLLtreeSM * MRLLLtwoloopEps2SM.conjugate()).real + 2 * (MRLLLtreeSMEFT * MRLLLtwoloopEps2SM.conjugate()).real + 2 * (MRLLLtreeSM * MRLLLtwoloopEps2SMEFT.conjugate()).real + 2 * (MRLLLoneloopEps2SM * MRLLLoneloopFinSM.conjugate()).real + 2 * (MRLLLoneloopEps2SMEFT * MRLLLoneloopFinSM.conjugate()).real + 2 * (MRLLLoneloopEps2SM * MRLLLoneloopFinSMEFT.conjugate()).real + (MRLLLoneloopEps1SM * MRLLLoneloopEps1SM.conjugate()).real + 2 * (MRLLLoneloopEps1SM * MRLLLoneloopEps1SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLLLalphas2Eps2 = (2 * (MLLLLtreeSM * MLLLLtwoloopEps2SM.conjugate()).real + 2 * (MLLLLtreeSMEFT * MLLLLtwoloopEps2SM.conjugate()).real + 2 * (MLLLLtreeSM * MLLLLtwoloopEps2SMEFT.conjugate()).real + 2 * (MLLLLoneloopEps2SM * MLLLLoneloopFinSM.conjugate()).real + 2 * (MLLLLoneloopEps2SMEFT * MLLLLoneloopFinSM.conjugate()).real + 2 * (MLLLLoneloopEps2SM * MLLLLoneloopFinSMEFT.conjugate()).real + (MLLLLoneloopEps1SM * MLLLLoneloopEps1SM.conjugate()).real + 2 * (MLLLLoneloopEps1SM * MLLLLoneloopEps1SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRLLalphas2Eps2 = (2 * (MRRLLtreeSM * MRRLLtwoloopEps2SM.conjugate()).real + 2 * (MRRLLtreeSMEFT * MRRLLtwoloopEps2SM.conjugate()).real + 2 * (MRRLLtreeSM * MRRLLtwoloopEps2SMEFT.conjugate()).real + 2 * (MRRLLoneloopEps2SM * MRRLLoneloopFinSM.conjugate()).real + 2 * (MRRLLoneloopEps2SMEFT * MRRLLoneloopFinSM.conjugate()).real + 2 * (MRRLLoneloopEps2SM * MRRLLoneloopFinSMEFT.conjugate()).real + (MRRLLoneloopEps1SM * MRRLLoneloopEps1SM.conjugate()).real + 2 * (MRRLLoneloopEps1SM * MRRLLoneloopEps1SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2LRRRalphas2Eps2 = (2 * (MLRRRtreeSM * MLRRRtwoloopEps2SM.conjugate()).real + 2 * (MLRRRtreeSMEFT * MLRRRtwoloopEps2SM.conjugate()).real + 2 * (MLRRRtreeSM * MLRRRtwoloopEps2SMEFT.conjugate()).real + 2 * (MLRRRoneloopEps2SM * MLRRRoneloopFinSM.conjugate()).real + 2 * (MLRRRoneloopEps2SMEFT * MLRRRoneloopFinSM.conjugate()).real + 2 * (MLRRRoneloopEps2SM * MLRRRoneloopFinSMEFT.conjugate()).real + (MLRRRoneloopEps1SM * MLRRRoneloopEps1SM.conjugate()).real + 2 * (MLRRRoneloopEps1SM * MLRRRoneloopEps1SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLRRalphas2Eps2 = (2 * (MRLRRtreeSM * MRLRRtwoloopEps2SM.conjugate()).real + 2 * (MRLRRtreeSMEFT * MRLRRtwoloopEps2SM.conjugate()).real + 2 * (MRLRRtreeSM * MRLRRtwoloopEps2SMEFT.conjugate()).real + 2 * (MRLRRoneloopEps2SM * MRLRRoneloopFinSM.conjugate()).real + 2 * (MRLRRoneloopEps2SMEFT * MRLRRoneloopFinSM.conjugate()).real + 2 * (MRLRRoneloopEps2SM * MRLRRoneloopFinSMEFT.conjugate()).real + (MRLRRoneloopEps1SM * MRLRRoneloopEps1SM.conjugate()).real + 2 * (MRLRRoneloopEps1SM * MRLRRoneloopEps1SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLRRalphas2Eps2 = (2 * (MLLRRtreeSM * MLLRRtwoloopEps2SM.conjugate()).real + 2 * (MLLRRtreeSMEFT * MLLRRtwoloopEps2SM.conjugate()).real + 2 * (MLLRRtreeSM * MLLRRtwoloopEps2SMEFT.conjugate()).real + 2 * (MLLRRoneloopEps2SM * MLLRRoneloopFinSM.conjugate()).real + 2 * (MLLRRoneloopEps2SMEFT * MLLRRoneloopFinSM.conjugate()).real + 2 * (MLLRRoneloopEps2SM * MLLRRoneloopFinSMEFT.conjugate()).real + (MLLRRoneloopEps1SM * MLLRRoneloopEps1SM.conjugate()).real + 2 * (MLLRRoneloopEps1SM * MLLRRoneloopEps1SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRRRalphas2Eps2 = (2 * (MRRRRtreeSM * MRRRRtwoloopEps2SM.conjugate()).real + 2 * (MRRRRtreeSMEFT * MRRRRtwoloopEps2SM.conjugate()).real + 2 * (MRRRRtreeSM * MRRRRtwoloopEps2SMEFT.conjugate()).real + 2 * (MRRRRoneloopEps2SM * MRRRRoneloopFinSM.conjugate()).real + 2 * (MRRRRoneloopEps2SMEFT * MRRRRoneloopFinSM.conjugate()).real + 2 * (MRRRRoneloopEps2SM * MRRRRoneloopFinSMEFT.conjugate()).real + (MRRRRoneloopEps1SM * MRRRRoneloopEps1SM.conjugate()).real + 2 * (MRRRRoneloopEps1SM * MRRRRoneloopEps1SMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
# 1/eps^1 poles
M2LRLLalphas2Eps1 = (2 * (MLRLLtreeSM * MLRLLtwoloopEps1SM.conjugate()).real + 2 * (MLRLLtreeSMEFT * MLRLLtwoloopEps1SM.conjugate()).real + 2 * (MLRLLtreeSM * MLRLLtwoloopEps1SMEFT.conjugate()).real + 2 * (MLRLLoneloopEps1SM * MLRLLoneloopFinSM.conjugate()).real + 2 * (MLRLLoneloopEps1SMEFT * MLRLLoneloopFinSM.conjugate()).real + 2 * (MLRLLoneloopEps1SM * MLRLLoneloopFinSMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLLLalphas2Eps1 = (2 * (MRLLLtreeSM * MRLLLtwoloopEps1SM.conjugate()).real + 2 * (MRLLLtreeSMEFT * MRLLLtwoloopEps1SM.conjugate()).real + 2 * (MRLLLtreeSM * MRLLLtwoloopEps1SMEFT.conjugate()).real + 2 * (MRLLLoneloopEps1SM * MRLLLoneloopFinSM.conjugate()).real + 2 * (MRLLLoneloopEps1SMEFT * MRLLLoneloopFinSM.conjugate()).real + 2 * (MRLLLoneloopEps1SM * MRLLLoneloopFinSMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLLLalphas2Eps1 = (2 * (MLLLLtreeSM * MLLLLtwoloopEps1SM.conjugate()).real + 2 * (MLLLLtreeSMEFT * MLLLLtwoloopEps1SM.conjugate()).real + 2 * (MLLLLtreeSM * MLLLLtwoloopEps1SMEFT.conjugate()).real + 2 * (MLLLLoneloopEps1SM * MLLLLoneloopFinSM.conjugate()).real + 2 * (MLLLLoneloopEps1SMEFT * MLLLLoneloopFinSM.conjugate()).real + 2 * (MLLLLoneloopEps1SM * MLLLLoneloopFinSMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRLLalphas2Eps1 = (2 * (MRRLLtreeSM * MRRLLtwoloopEps1SM.conjugate()).real + 2 * (MRRLLtreeSMEFT * MRRLLtwoloopEps1SM.conjugate()).real + 2 * (MRRLLtreeSM * MRRLLtwoloopEps1SMEFT.conjugate()).real + 2 * (MRRLLoneloopEps1SM * MRRLLoneloopFinSM.conjugate()).real + 2 * (MRRLLoneloopEps1SMEFT * MRRLLoneloopFinSM.conjugate()).real + 2 * (MRRLLoneloopEps1SM * MRRLLoneloopFinSMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2LRRRalphas2Eps1 = (2 * (MLRRRtreeSM * MLRRRtwoloopEps1SM.conjugate()).real + 2 * (MLRRRtreeSMEFT * MLRRRtwoloopEps1SM.conjugate()).real + 2 * (MLRRRtreeSM * MLRRRtwoloopEps1SMEFT.conjugate()).real + 2 * (MLRRRoneloopEps1SM * MLRRRoneloopFinSM.conjugate()).real + 2 * (MLRRRoneloopEps1SMEFT * MLRRRoneloopFinSM.conjugate()).real + 2 * (MLRRRoneloopEps1SM * MLRRRoneloopFinSMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLRRalphas2Eps1 = (2 * (MRLRRtreeSM * MRLRRtwoloopEps1SM.conjugate()).real + 2 * (MRLRRtreeSMEFT * MRLRRtwoloopEps1SM.conjugate()).real + 2 * (MRLRRtreeSM * MRLRRtwoloopEps1SMEFT.conjugate()).real + 2 * (MRLRRoneloopEps1SM * MRLRRoneloopFinSM.conjugate()).real + 2 * (MRLRRoneloopEps1SMEFT * MRLRRoneloopFinSM.conjugate()).real + 2 * (MRLRRoneloopEps1SM * MRLRRoneloopFinSMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLRRalphas2Eps1 = (2 * (MLLRRtreeSM * MLLRRtwoloopEps1SM.conjugate()).real + 2 * (MLLRRtreeSMEFT * MLLRRtwoloopEps1SM.conjugate()).real + 2 * (MLLRRtreeSM * MLLRRtwoloopEps1SMEFT.conjugate()).real + 2 * (MLLRRoneloopEps1SM * MLLRRoneloopFinSM.conjugate()).real + 2 * (MLLRRoneloopEps1SMEFT * MLLRRoneloopFinSM.conjugate()).real + 2 * (MLLRRoneloopEps1SM * MLLRRoneloopFinSMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRRRalphas2Eps1 = (2 * (MRRRRtreeSM * MRRRRtwoloopEps1SM.conjugate()).real + 2 * (MRRRRtreeSMEFT * MRRRRtwoloopEps1SM.conjugate()).real + 2 * (MRRRRtreeSM * MRRRRtwoloopEps1SMEFT.conjugate()).real + 2 * (MRRRRoneloopEps1SM * MRRRRoneloopFinSM.conjugate()).real + 2 * (MRRRRoneloopEps1SMEFT * MRRRRoneloopFinSM.conjugate()).real + 2 * (MRRRRoneloopEps1SM * MRRRRoneloopFinSMEFT.conjugate()).real) * (Nc/((2*Nc)**2))
# finite parts
M2LRLLalphas2Fin = (2 * (MLRLLtreeSM * MLRLLtwoloopFinSM.conjugate()).real + 2 * (MLRLLtreeSMEFT * MLRLLtwoloopFinSM.conjugate()).real + 2 * (MLRLLtreeSM * MLRLLtwoloopFinSMEFT.conjugate()).real + (MLRLLoneloopFinSM * MLRLLoneloopFinSM.conjugate()).real + 2 * (MLRLLoneloopFinSMEFT * MLRLLoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLLLalphas2Fin = (2 * (MRLLLtreeSM * MRLLLtwoloopFinSM.conjugate()).real + 2 * (MRLLLtreeSMEFT * MRLLLtwoloopFinSM.conjugate()).real + 2 * (MRLLLtreeSM * MRLLLtwoloopFinSMEFT.conjugate()).real + (MRLLLoneloopFinSM * MRLLLoneloopFinSM.conjugate()).real + 2 * (MRLLLoneloopFinSMEFT * MRLLLoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLLLalphas2Fin = (2 * (MLLLLtreeSM * MLLLLtwoloopFinSM.conjugate()).real + 2 * (MLLLLtreeSMEFT * MLLLLtwoloopFinSM.conjugate()).real + 2 * (MLLLLtreeSM * MLLLLtwoloopFinSMEFT.conjugate()).real + (MLLLLoneloopFinSM * MLLLLoneloopFinSM.conjugate()).real + 2 * (MLLLLoneloopFinSMEFT * MLLLLoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRLLalphas2Fin = (2 * (MRRLLtreeSM * MRRLLtwoloopFinSM.conjugate()).real + 2 * (MRRLLtreeSMEFT * MRRLLtwoloopFinSM.conjugate()).real + 2 * (MRRLLtreeSM * MRRLLtwoloopFinSMEFT.conjugate()).real + (MRRLLoneloopFinSM * MRRLLoneloopFinSM.conjugate()).real + 2 * (MRRLLoneloopFinSMEFT * MRRLLoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LRRRalphas2Fin = (2 * (MLRRRtreeSM * MLRRRtwoloopFinSM.conjugate()).real + 2 * (MLRRRtreeSMEFT * MLRRRtwoloopFinSM.conjugate()).real + 2 * (MLRRRtreeSM * MLRRRtwoloopFinSMEFT.conjugate()).real + (MLRRRoneloopFinSM * MLRRRoneloopFinSM.conjugate()).real + 2 * (MLRRRoneloopFinSMEFT * MLRRRoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RLRRalphas2Fin = (2 * (MRLRRtreeSM * MRLRRtwoloopFinSM.conjugate()).real + 2 * (MRLRRtreeSMEFT * MRLRRtwoloopFinSM.conjugate()).real + 2 * (MRLRRtreeSM * MRLRRtwoloopFinSMEFT.conjugate()).real + (MRLRRoneloopFinSM * MRLRRoneloopFinSM.conjugate()).real + 2 * (MRLRRoneloopFinSMEFT * MRLRRoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2LLRRalphas2Fin = (2 * (MLLRRtreeSM * MLLRRtwoloopFinSM.conjugate()).real + 2 * (MLLRRtreeSMEFT * MLLRRtwoloopFinSM.conjugate()).real + 2 * (MLLRRtreeSM * MLLRRtwoloopFinSMEFT.conjugate()).real + (MLLRRoneloopFinSM * MLLRRoneloopFinSM.conjugate()).real + 2 * (MLLRRoneloopFinSMEFT * MLLRRoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))
M2RRRRalphas2Fin = (2 * (MRRRRtreeSM * MRRRRtwoloopFinSM.conjugate()).real + 2 * (MRRRRtreeSMEFT * MRRRRtwoloopFinSM.conjugate()).real + 2 * (MRRRRtreeSM * MRRRRtwoloopFinSMEFT.conjugate()).real + (MRRRRoneloopFinSM * MRRRRoneloopFinSM.conjugate()).real + 2 * (MRRRRoneloopFinSMEFT * MRRRRoneloopFinSM.conjugate()).real) * (Nc/((2*Nc)**2))


print("Squared helicity amplitudes of order (alpha_s)^2")
print("1/eps^4 poles:")
print("|M(L,R,L,L)_alphas1|^2 = ", M2LRLLalphas2Eps4.real)
print("|M(R,L,L,L)_alphas1|^2 = ", M2RLLLalphas2Eps4.real)
print("|M(L,L,L,L)_alphas1|^2 = ", M2LLLLalphas2Eps4.real)
print("|M(R,R,L,L)_alphas1|^2 = ", M2RRLLalphas2Eps4.real)
print("|M(L,R,R,R)_alphas1|^2 = ", M2LRRRalphas2Eps4.real)
print("|M(R,L,R,R)_alphas1|^2 = ", M2RLRRalphas2Eps4.real)
print("|M(L,L,R,R)_alphas1|^2 = ", M2LLRRalphas2Eps4.real)
print("|M(R,R,R,R)_alphas1|^2 = ", M2RRRRalphas2Eps4.real)
print()
print("1/eps^3 poles:")
print("|M(L,R,L,L)_alphas1|^2 = ", M2LRLLalphas2Eps3.real)
print("|M(R,L,L,L)_alphas1|^2 = ", M2RLLLalphas2Eps3.real)
print("|M(L,L,L,L)_alphas1|^2 = ", M2LLLLalphas2Eps3.real)
print("|M(R,R,L,L)_alphas1|^2 = ", M2RRLLalphas2Eps3.real)
print("|M(L,R,R,R)_alphas1|^2 = ", M2LRRRalphas2Eps3.real)
print("|M(R,L,R,R)_alphas1|^2 = ", M2RLRRalphas2Eps3.real)
print("|M(L,L,R,R)_alphas1|^2 = ", M2LLRRalphas2Eps3.real)
print("|M(R,R,R,R)_alphas1|^2 = ", M2RRRRalphas2Eps3.real)
print()
print("1/eps^2 poles:")
print("|M(L,R,L,L)_alphas1|^2 = ", M2LRLLalphas2Eps2.real)
print("|M(R,L,L,L)_alphas1|^2 = ", M2RLLLalphas2Eps2.real)
print("|M(L,L,L,L)_alphas1|^2 = ", M2LLLLalphas2Eps2.real)
print("|M(R,R,L,L)_alphas1|^2 = ", M2RRLLalphas2Eps2.real)
print("|M(L,R,R,R)_alphas1|^2 = ", M2LRRRalphas2Eps2.real)
print("|M(R,L,R,R)_alphas1|^2 = ", M2RLRRalphas2Eps2.real)
print("|M(L,L,R,R)_alphas1|^2 = ", M2LLRRalphas2Eps2.real)
print("|M(R,R,R,R)_alphas1|^2 = ", M2RRRRalphas2Eps2.real)
print()
print("1/eps^1 poles:")
print("|M(L,R,L,L)_alphas1|^2 = ", M2LRLLalphas2Eps1.real)
print("|M(R,L,L,L)_alphas1|^2 = ", M2RLLLalphas2Eps1.real)
print("|M(L,L,L,L)_alphas1|^2 = ", M2LLLLalphas2Eps1.real)
print("|M(R,R,L,L)_alphas1|^2 = ", M2RRLLalphas2Eps1.real)
print("|M(L,R,R,R)_alphas1|^2 = ", M2LRRRalphas2Eps1.real)
print("|M(R,L,R,R)_alphas1|^2 = ", M2RLRRalphas2Eps1.real)
print("|M(L,L,R,R)_alphas1|^2 = ", M2LLRRalphas2Eps1.real)
print("|M(R,R,R,R)_alphas1|^2 = ", M2RRRRalphas2Eps1.real)
print()
print("finite parts:")
print("|M(L,R,L,L)_alphas1|^2 = ", M2LRLLalphas2Fin.real)
print("|M(R,L,L,L)_alphas1|^2 = ", M2RLLLalphas2Fin.real)
print("|M(L,L,L,L)_alphas1|^2 = ", M2LLLLalphas2Fin.real)
print("|M(R,R,L,L)_alphas1|^2 = ", M2RRLLalphas2Fin.real)
print("|M(L,R,R,R)_alphas1|^2 = ", M2LRRRalphas2Fin.real)
print("|M(R,L,R,R)_alphas1|^2 = ", M2RLRRalphas2Fin.real)
print("|M(L,L,R,R)_alphas1|^2 = ", M2LLRRalphas2Fin.real)
print("|M(R,R,R,R)_alphas1|^2 = ", M2RRRRalphas2Fin.real)
print()

# Total squared amplitude of order (alphas)^2
M2alphas2Eps4 = (M2LRLLalphas2Eps4 + M2RLLLalphas2Eps4 + M2LLLLalphas2Eps4 + M2RRRRalphas2Eps4 + M2LRRRalphas2Eps4 + M2RLRRalphas2Eps4 + M2LLRRalphas2Eps4 + M2RRRRalphas2Eps4).real
M2alphas2Eps3 = (M2LRLLalphas2Eps3 + M2RLLLalphas2Eps3 + M2LLLLalphas2Eps3 + M2RRRRalphas2Eps3 + M2LRRRalphas2Eps3 + M2RLRRalphas2Eps3 + M2LLRRalphas2Eps3 + M2RRRRalphas2Eps3).real
M2alphas2Eps2 = (M2LRLLalphas2Eps2 + M2RLLLalphas2Eps2 + M2LLLLalphas2Eps2 + M2RRRRalphas2Eps2 + M2LRRRalphas2Eps2 + M2RLRRalphas2Eps2 + M2LLRRalphas2Eps2 + M2RRRRalphas2Eps2).real
M2alphas2Eps1 = (M2LRLLalphas2Eps1 + M2RLLLalphas2Eps1 + M2LLLLalphas2Eps1 + M2RRRRalphas2Eps1 + M2LRRRalphas2Eps1 + M2RLRRalphas2Eps1 + M2LLRRalphas2Eps1 + M2RRRRalphas2Eps1).real
M2alphas2Fin = (M2LRLLalphas2Fin + M2RLLLalphas2Fin + M2LLLLalphas2Fin + M2RRRRalphas2Fin + M2LRRRalphas2Fin + M2RLRRalphas2Fin + M2LLRRalphas2Fin + M2RRRRalphas2Fin).real


print("Total tree-level squared amplitude")
print("|M_tree|^2 = ", M2tree, " (Dmitrii)")
print("|M_tree|^2 = ", OpenLoopsResTree, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2tree / OpenLoopsResTree)
print()

print("Total squared amplitude of order (alpha_s)^1")
print("1/eps^2 pole:")
print("|M_alphas1|^2 =", M2alphas1Eps2, " (Dmitrii)")
print("|M_alphas1|^2 =", OpenLoopsResOneLoopEps2, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2alphas1Eps2 / OpenLoopsResOneLoopEps2)
print()
print("1/eps^1 pole:")
print("|M_alphas1|^2 =", M2alphas1Eps1, " (Dmitrii)")
print("|M_alphas1|^2 =", OpenLoopsResOneLoopEps1, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2alphas1Eps1 / OpenLoopsResOneLoopEps1)
print()
print("finite part:")
print("|M_alphas1|^2 =", M2alphas1Fin, " (Dmitrii)")
print("|M_alphas1|^2 =", OpenLoopsResOneLoopFin, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2alphas1Fin / OpenLoopsResOneLoopFin)
print()

print("Total squared amplitude of order (alpha_s)^2")
print("1/eps^4 pole:")
print("|M_alphas2|^2 =", M2alphas2Eps4, " (Dmitrii)")
print()
print("1/eps^3 pole:")
print("|M_alphas2|^2 =", M2alphas2Eps3, " (Dmitrii)")
print()
print("1/eps^2 pole:")
print("|M_alphas2|^2 =", M2alphas2Eps2, " (Dmitrii)")
print()
print("1/eps^1 pole:")
print("|M_alphas2|^2 =", M2alphas2Eps1, " (Dmitrii)")
print()
print("finite part:")
print("|M_alphas2|^2 =", M2alphas2Fin, " (Dmitrii)")




