
"""
In this project, I compute radiative 2-loop QCD corrections to the process q qb -> g W H -> g l nub H
After quark-antiquark (q and qb) collision a gluon (g), a vector boson (W) and a Higgs (H) appear with subsequent decay of the vector boson into a lepton-antinuetrino (l and nub) pair)
As a result I obtain 2-loop squared amplitude for this process, which allows to compute the cross section measured in CERN (at the Long Hanron Collider)

THE OPENLOOPS RESULT IS GIVEN FOR THE CASE OF W-BOSON WITHIN THE STANDARD MODEL


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
"""


import math, cmath
import numpy as np
import const


def helicities(number_of_outgoing_particles):

    # PHASE SPACE GENERATION
    if number_of_outgoing_particles == 3:
        p1 = np.array([500.0, 0.0, 0.0, 500.0]) # quark
        p2 = np.array([500.0, 0.0, 0.0, -500.0]) # antiquark
        p3 = np.array([349.14239937112842, -17.578471028824460, -333.45082223855940, 101.99000707591840]) # lepton
        p4 = np.array([439.78021928785591, 162.50680658487221, 364.09047948353401, -185.57020730686239]) # antinuetrino
        pH = np.array([2, 2, 2, 2]) # Higgs

        # Define the external momenta matrix (with zero values in the first line for convinient notation)
        p = np.column_stack((np.zeros(4), p1, p2, p3, p4))
    elif number_of_outgoing_particles == 4:
        p1 = np.array([500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]) # quark
        p2 = np.array([500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]) # antiquark
        p3 = np.array([322.3919309874294800, -101.97160213731860, -296.47360464823691,  75.111592116216357]) # lepton
        p4 = np.array([149.6028751502909100, -103.96621515693120, -95.942663470338033,  48.652355394098521]) # antinuetrino
        p5 = np.array([86.94997640526997900, -21.701022816585411,  39.355542645382108, -74.434570386874427]) # gluon
        pH = np.array([441.0552174570096900,  227.63884011083519,  353.06072547319292, -49.329377123440487]) # Higgs

        # Define the external momenta matrix (with zero values in the first line for convinient notation)
        p = np.column_stack((np.zeros(4), p1, p2, p3, p4, p5))
    elif number_of_outgoing_particles == 5:
        p1 = np.array([500.0000000000000000,  0.0000000000000000,  0.0000000000000000, 500.00000000000000]) # quark
        p2 = np.array([500.0000000000000000,  0.0000000000000000,  0.0000000000000000, -500.00000000000000]) # antiquark
        p3 = np.array([322.3919309874294800, -101.97160213731860, -296.47360464823691,  75.111592116216357]) # lepton
        p4 = np.array([149.6028751502909100, -103.96621515693120, -95.942663470338033,  48.652355394098521]) # antinuetrino
        p5 = np.array([86.94997640526997900, -21.701022816585411,  39.355542645382108, -74.434570386874427]) # gluon 5
        p6 = np.array([19.94997640526997900, -21.701022816585411,  59.355542645382108, -84.434570386874427]) # gluon 6
        pH = np.array([441.0552174570096900,  227.63884011083519,  353.06072547319292, -49.329377123440487]) # Higgs

        # Define the external momenta matrix (with zero values in the first line for convinient notation)
        p = np.column_stack((np.zeros(4), p1, p2, p3, p4, p5, p6))
    else:
        # If the number of outgoing particles is incorrect, throw an exception
        raise ValueError("Invalid number of outgoing particles. Expected 3, 4, or 5.")


    # AUXILIARY MATRICES TO BUILD SPINOR PRODUCTS

    # Define the matrix of spinors U_+(pi)
    Uplus = np.zeros((4, number_of_outgoing_particles + 2), dtype=complex)
    Uplus[0,1] = 1j*math.sqrt(2*abs(p[0,1]))
    Uplus[1,2] = 1j*math.sqrt(2*abs(p[0,2]))
    j = 3
    while j < number_of_outgoing_particles + 2:
        Uplus[0,j] = cmath.sqrt(p[0,j] + p[3,j])
        Uplus[1,j] = (p[1,j] + 1j*p[2,j])/cmath.sqrt(p[0,j] + p[3,j])
        j += 1

    # Define the matrix of spinors U_-(pi)
    Uminus = np.zeros((4, number_of_outgoing_particles + 2), dtype=complex)
    Uminus[3,1] = -1j*math.sqrt(2*abs(p[0,1]))
    Uminus[2,2] = 1j*math.sqrt(2*abs(p[0,2]))
    j = 3
    while j < number_of_outgoing_particles + 2:
        Uminus[2,j] = (p[1,j] - 1j*p[2,j])/cmath.sqrt(p[0,j] + p[3,j])
        Uminus[3,j] = - cmath.sqrt(p[0,j] + p[3,j])
        j += 1

    # Define the matrix of spinors [U_+]bar(pi)
    Uplusbar = np.zeros((number_of_outgoing_particles + 2, 4), dtype=complex)
    Uplusbar[1,2] = 1j*cmath.sqrt(2*abs(p[0,1]))
    Uplusbar[2,3] = 1j*cmath.sqrt(2*abs(p[0,2]))
    i = 3
    while i < number_of_outgoing_particles + 2:
        Uplusbar[i,2] = cmath.sqrt(p[0,i] + p[3,i])
        Uplusbar[i,3] = (p[1,i] - 1j*p[2,i])/cmath.sqrt(p[0,i] + p[3,i])
        i += 1

    # Define the matrix of spinors [U_-]bar(pi)
    Uminusbar = np.zeros((number_of_outgoing_particles + 2, 4), dtype=complex)
    Uminusbar[1,1] = -1j*cmath.sqrt(2*abs(p[0,1]))
    Uminusbar[2,0] = 1j*cmath.sqrt(2*abs(p[0,2]))
    i = 3
    while i < number_of_outgoing_particles + 2:
        Uminusbar[i,0] = (p[1,i] + 1j*p[2,i])/cmath.sqrt(p[0,i] + p[3,i])
        Uminusbar[i,1] = - cmath.sqrt(p[0,i] + p[3,i])
        i += 1


    # KINEMATIC OBJECTS

    # Define scalar products of momenta as a matrix s[i,j] = 2(pi*pj)
    s = np.zeros((number_of_outgoing_particles + 2,number_of_outgoing_particles + 2)) # create a 6x6 matrix of zeros
    i = 1
    j = 1
    while i < number_of_outgoing_particles + 2:
        while j < number_of_outgoing_particles + 2:
            if i != j:
                s[i,j] = 2*(p[0,i]*p[0,j] - p[1,i]*p[1,j] - p[2,i]*p[2,j] - p[3,i]*p[3,j]) # fill in the elements of the matrix
                #print("s",i,j, "=", s[i,j]) # print the elements of the matrix
            j += 1
        i += 1
        j = 1

    # Define the matrix of spinor products Ang[i,j] = <pipj>
    Ang = np.zeros((number_of_outgoing_particles + 2, number_of_outgoing_particles + 2), dtype=complex)
    i = 1;
    j = 1;
    while i < number_of_outgoing_particles + 2:
        while j < number_of_outgoing_particles + 2:
            if i != j:
                Ang[i,j] = Uminusbar[i,0] * Uplus[0,j] + Uminusbar[i,1] * Uplus[1,j] + Uminusbar[i,2] * Uplus[2,j] + Uminusbar[i,3] * Uplus[3,j]
                #print("< p", i, "p", j, "> = ", Ang[i,j])
            j += 1
        i += 1
        j = 1

    # Define a matrix of spinor products Sq[i,j] = [pipj]
    Sq = np.zeros((number_of_outgoing_particles + 2, number_of_outgoing_particles + 2), dtype=complex)
    i = 1;
    j = 1;
    while i < number_of_outgoing_particles + 2:
        while j < number_of_outgoing_particles + 2:
            if i != j:
                Sq[i,j] = Uplusbar[i,0] * Uminus[0,j] + Uplusbar[i,1] * Uminus[1,j] + Uplusbar[i,2] * Uminus[2,j] + Uplusbar[i,3] * Uminus[3,j]
                #print("[ p", i, "p", j, "] = ", Sq[i,j])
            j += 1
        i += 1
        j = 1


    # GLOBAL FACTORS

    prop1 = 1 / (s[1,2] - const.mW**2 + 1j*const.mW*const.Gamma_W) # W*-boson propagator
    prop2 = 1 / (s[3,4] - const.mW**2 + 1j*const.mW*const.Gamma_W) # W-boson propagator

    GlobFac_3 = const.gW**2 * const.mW * math.sqrt(2) * prop1 * prop2 # Global factor for the 3-point amplitudes
    GlobFac_4 = const.gW * math.sqrt(2) * prop2 # Global factor for the 4-point amplitudes

    return s, Ang, Sq, GlobFac_3, GlobFac_4












