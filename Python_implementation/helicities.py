
import math, cmath
import numpy as np

import const


def helicities(number_of_outgoing_particles, p):

    if number_of_outgoing_particles not in {3, 4, 5}:
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











