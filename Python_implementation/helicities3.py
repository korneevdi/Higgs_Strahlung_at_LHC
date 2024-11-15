
import math, cmath
import numpy as np
import const

# PHASE SPACE

# Momenta initialization

p1 = np.array([500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000])       # quark
p2 = np.array([500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000])     # antiquark
p5 = np.array([86.94997640526997900, -21.701022816585411,  39.355542645382108, -74.434570386874427])       # antinuetrino
p6 = np.array([19.94997640526997900, -21.701022816585411,  59.355542645382108, -84.434570386874427])    # gluon 6
p3 = np.array([322.3919309874294800, -101.97160213731860, -296.47360464823691,  75.111592116216357])     # lepton 5
p4 = np.array([149.6028751502909100, -103.96621515693120, -95.942663470338033,  48.652355394098521])    # gluon
pH = np.array([441.0552174570096900,  227.63884011083519,  353.06072547319292, -49.329377123440487])      # Higgs boson

# Define the external momenta matrix (with zero values in the first line for convinient notation)
p = np.column_stack((np.zeros(4), p1, p2, p3, p4, p5, p6))


# AUXILIARY MATRICES TO BUILD SPINOR PRODUCTS

# Define a matrix of spinors U_+(pi)
Uplus = np.zeros((4, 7), dtype=complex)
#print(Uplus)
Uplus[0,1] = 1j*math.sqrt(2*abs(p[0,1]))
Uplus[1,2] = 1j*math.sqrt(2*abs(p[0,2]))
j = 3
while j < 7:
    Uplus[0,j] = cmath.sqrt(p[0,j] + p[3,j])
    Uplus[1,j] = (p[1,j] + 1j*p[2,j])/cmath.sqrt(p[0,j] + p[3,j])
    j += 1
#print("Matrix of spinors U_+(pi)")
#print(Uplus)


# Define a matrix of spinors U_-(pi)
Uminus = np.zeros((4, 7), dtype=complex)
#print(Uminus)
Uminus[3,1] = -1j*math.sqrt(2*abs(p[0,1]))
Uminus[2,2] = 1j*math.sqrt(2*abs(p[0,2]))
j = 3
while j < 7:
    Uminus[2,j] = (p[1,j] - 1j*p[2,j])/cmath.sqrt(p[0,j] + p[3,j])
    Uminus[3,j] = - cmath.sqrt(p[0,j] + p[3,j])
    j += 1
#print("Matrix of spinors U_-(pi)")
#print(Uminus)


# Define a matrix of spinors [U_+]bar(pi)
Uplusbar = np.zeros((7, 4), dtype=complex)
#print(Uplusbar)
Uplusbar[1,2] = 1j*cmath.sqrt(2*abs(p[0,1]))
Uplusbar[2,3] = 1j*cmath.sqrt(2*abs(p[0,2]))
i = 3
while i < 7:
    Uplusbar[i,2] = cmath.sqrt(p[0,i] + p[3,i])
    Uplusbar[i,3] = (p[1,i] - 1j*p[2,i])/cmath.sqrt(p[0,i] + p[3,i])
    i += 1
#print("Matrix of spinors [U_+]bar(pi)")
#print(Uplusbar)


# Define a matrix of spinors [U_-]bar(pi)
Uminusbar = np.zeros((7, 4), dtype=complex)
#print(Uminusbar)
Uminusbar[1,1] = -1j*cmath.sqrt(2*abs(p[0,1]))
Uminusbar[2,0] = 1j*cmath.sqrt(2*abs(p[0,2]))
i = 3
while i < 7:
    Uminusbar[i,0] = (p[1,i] + 1j*p[2,i])/cmath.sqrt(p[0,i] + p[3,i])
    Uminusbar[i,1] = - cmath.sqrt(p[0,i] + p[3,i])
    i += 1
#print("Matrix of spinors [U_-]bar(pi)")
#print(Uminusbar)


# KINEMATIC OBJECTS

# Define scalar products of momenta as a matrix sij = 2(pi*pj)
#print("Scalar products of momenta: sij = 2(pi*pj)")
s = np.zeros((7,7)) # create a 6x6 matrix of zeros
i = 1
j = 1
while i < 7:
    while j < 7:
        if i != j:
            s[i,j] = 2*(p[0,i]*p[0,j] - p[1,i]*p[1,j] - p[2,i]*p[2,j] - p[3,i]*p[3,j]) # fill in the elements of the matrix
            #print("s",i,j, "=", s[i,j]) # print the elements of the matrix
        j += 1
    i += 1
    j = 1
print()


# Define a matrix of spinor products A_(ij) = <pipj>
#print("Spinor products <pipj>:")
Ang = np.zeros((7, 7), dtype=complex)
i = 1;
j = 1;
while i < 7:
    while j < 7:
        if i != j:
            Ang[i,j] = Uminusbar[i,0] * Uplus[0,j] + Uminusbar[i,1] * Uplus[1,j] + Uminusbar[i,2] * Uplus[2,j] + Uminusbar[i,3] * Uplus[3,j]
            #print("< p", i, "p", j, "> = ", Ang[i,j])
        j += 1
    i += 1
    j = 1
print()


# Define a matrix of spinor products S_(ij) = [pipj]
#print("Spinor products [pipj]:")
Sq = np.zeros((7, 7), dtype=complex)
i = 1;
j = 1;
while i < 7:
    while j < 7:
        if i != j:
            Sq[i,j] = Uplusbar[i,0] * Uminus[0,j] + Uplusbar[i,1] * Uminus[1,j] + Uplusbar[i,2] * Uminus[2,j] + Uplusbar[i,3] * Uminus[3,j]
            #print("[ p", i, "p", j, "] = ", Sq[i,j])
        j += 1
    i += 1
    j = 1
print()


# Global factor
prop1 = 1 / (s[1,2] - const.mW**2 + 1j*const.mW*const.Gamma_W)
prop2 = 1 / (s[3,4] - const.mW**2 + 1j*const.mW*const.Gamma_W)

GlobFac_3 = const.gW**2 * const.mW * math.sqrt(2) * prop1 * prop2
GlobFac_4 = const.gW * math.sqrt(2) * prop2
