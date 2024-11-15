
import math
import const

# PHASE SPACE

p1 = [500.00000000000000, 0.0000000000000000, 0.0000000000000000, 500.00000000000000]       # quark
p2 = [500.00000000000000,  0.0000000000000000, 0.0000000000000000, -500.00000000000000]     # antiquark
p4 = [439.78021928785591, 162.50680658487221, 364.09047948353401, -185.57020730686239]      # antinuetrino
p3 = [349.14239937112842, -17.578471028824460, -333.45082223855940, 101.99000707591840]     # lepton
pH = [211.07738134101581, -144.92833555604770, -30.639657244974519, 83.580200230944016]     # Higgs boson



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
print("mH^2 = ", round(const.mH**2, 10))
print()
