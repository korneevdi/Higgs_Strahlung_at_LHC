
import math, cmath
import numpy as np
import const
import helicities
import form_factor



# LEADING ORDER, ONE-LOOP AND TWO-LOOP HELICITY AMPLITUDES

def loop_amplitude(number_of_loops):

    s, Ang, Sq, GlobFac_3, GlobFac_4 = helicities.helicities(3)

    loop_factors = {
        0: 1,
        1: const.alpha_s / (2 * math.pi),
        2: (const.alpha_s / (2 * math.pi))**2
    }

    try:
        n_loop_factor = loop_factors[number_of_loops]
    except KeyError:
        raise ValueError("Invalid value for number of loops. Program terminated.")

    # Helicity order: M(quark, antiquark, lepton, antilepton)

    # 3-point amplitudes
    MLRLL_3 = n_loop_factor * (form_factor.B['B1'][number_of_loops] - s[1,2] / 2 * form_factor.B['B2'][number_of_loops]) * Sq[1,2] * (Ang[3,1] * Sq[1,4] - Ang[3,2] * Sq[2,4]) * GlobFac_3 * (const.vev/2 * const.C1)
    MRLLL_3 = n_loop_factor * (form_factor.B['B1'][number_of_loops] - s[1,2] / 2 * form_factor.B['B2'][number_of_loops]) * Ang[1,2] * (Ang[3,1] * Sq[1,4] - Ang[3,2] * Sq[2,4]) * GlobFac_3 * (const.vev/2 * const.C2)
    MLLLL_3 = n_loop_factor * form_factor.B['B3'][number_of_loops] * Ang[2,3] * Sq[4,1] * GlobFac_3 * (const.S3 + const.vev/2 * const.C3)
    MRRLL_3 = n_loop_factor * form_factor.B['B3'][number_of_loops] * Ang[3,1] * Sq[2,4] * GlobFac_3 * (const.vev/2 * const.C4)

    # 4-point amplitudes
    MLRLL_4 = n_loop_factor * ( 2 * form_factor.A['A1'][number_of_loops] * Sq[4,1] * Sq[2,4] * Ang[3,4] + form_factor.A['A2'][number_of_loops] * (s[2,3] + s[2,4]) / 2 * Sq[1,2] * Ang[1,3] * Sq[1,4] + form_factor.A['A2'][number_of_loops] * (- s[1,3] - s[1,4]) / 2 * Sq[1,2] * Ang[2,3] * Sq[2,4]) * GlobFac_4 * const.C1
    MRLLL_4 = n_loop_factor * ( 2 * form_factor.A['A1'][number_of_loops] * Ang[1,3] * Ang[2,3] * Sq[3,4] + form_factor.A['A2'][number_of_loops] * (s[2,3] + s[2,4]) / 2 * Ang[1,2] * Ang[1,3] * Sq[1,4] + form_factor.A['A2'][number_of_loops] * (- s[1,3] - s[1,4]) / 2 * Ang[1,2] * Ang[1,3] * Sq[2,4]) * GlobFac_4 * const.C2
    MLLLL_4 = n_loop_factor * form_factor.A['A3'][number_of_loops] * Ang[2,3] * Sq[4,1] * GlobFac_4 * const.C3
    MRRLL_4 = n_loop_factor * form_factor.A['A3'][number_of_loops] * Ang[3,1] * Sq[2,4] * GlobFac_4 * const.C4

    # Total amplitudes
    MLRLL = MLRLL_3 + MLRLL_4
    MRLLL = MRLLL_3 + MRLLL_4
    MLLLL = MLLLL_3 + MLLLL_4
    MRRLL = MRRLL_3 + MRRLL_4

    return MLRLL, MRLLL, MLLLL, MRRLL





# LEADING ORDER, ONE-LOOP AND TWO-LOOP SQUARED AMPLITUDE

def loop_squared_amplitude(number_of_loops):

    spin_color_factor = const.Nc / (4 * const.Nc**2)

    # Total leading order, one-loop, and two-loop helicity amplitudes
    MLRLL0, MRLLL0, MLLLL0, MRRLL0 = loop_amplitude(0)
    MLRLL1, MRLLL1, MLLLL1, MRRLL1 = loop_amplitude(1)
    MLRLL2, MRLLL2, MLLLL2, MRRLL2 = loop_amplitude(2)

    # Squared helicity amplitudes
    if number_of_loops == 0:
        M2 = MLRLL0 * MLRLL0.conjugate() + MRLLL0 * MRLLL0.conjugate() + MLLLL0 * MLLLL0.conjugate() + MRRLL0 * MRRLL0.conjugate()
    elif number_of_loops == 1:
        M2 = (MLRLL0 * MLRLL1.conjugate()).real + (MRLLL0 * MRLLL1.conjugate()).real + (MLLLL0 * MLLLL1.conjugate()).real + (MRRLL0 * MRRLL1.conjugate()).real
    else:
        M2 = (MLRLL0 * MLRLL2.conjugate()).real + (MRLLL0 * MRLLL2.conjugate()).real + (MLLLL0 * MLLLL2.conjugate()).real + (MRRLL0 * MRRLL2.conjugate()).real
        + MLRLL1 * MLRLL1.conjugate() + MRLLL1 * MRLLL1.conjugate() + MLLLL1 * MLLLL1.conjugate() + MRRLL1 * MRRLL1.conjugate()

    # Multiply with the spin-color factor

    M2 = M2.real * spin_color_factor

    # Print result

    if number_of_loops == 0:
        print("Total squared leading order amplitude:")
    elif number_of_loops == 1:
        print("Total squared one-loop amplitude:")
    else:
        print("Total squared two-loop amplitude:")
    print("|M|^2 =", M2, "\n")





# SINGLE REAL GLUON TREE-LEVEL AND ONE-LOOP (VIRTUAL-REAL) HELICITY AMPLITUDES

def single_real_amplitude(number_of_loops):

    s, Ang, Sq, GlobFac_3, GlobFac_4 = helicities.helicities(4)

    loop_factors = {
        0: (const.alpha_s / (2 * math.pi))**(1/2),
        1: (const.alpha_s / (2 * math.pi))**(3/2)
    }

    try:
        n_loop_factor = loop_factors[number_of_loops]
    except KeyError:
        raise ValueError("Invalid value for number of loops. Program terminated.")


    # HELICITY AMPLITUDES
    # Helicity order: M(quark, antiquark, gluon, lepton, antilepton)

    # 3-point amplitudes
    MLRLLL_3 = n_loop_factor * (2 * form_factor.b['b12'][number_of_loops] * Sq[1,2]**2 * Ang[1,5] * Ang[2,5] * ( Ang[1,3] * Sq[1,4] - Ang[2,3] * Sq[2,4] ) 
+ form_factor.b['b13'][number_of_loops] * s[1,5] * Sq[1,2] * Ang[2,5] * ( Ang[3,1] * Sq[1,4] * Sq[2,1] * Ang[1,5] - s[1,2] * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b14'][number_of_loops] * s[1,5] * Sq[1,2] * Ang[2,5] * ( Ang[3,2] * Sq[2,4] * Sq[2,1] * Ang[1,5] - s[1,2] * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b15'][number_of_loops] * s[1,5] * Sq[1,2] * Ang[2,5] * ( Ang[3,5] * Sq[5,4] * Sq[2,1] * Ang[1,5] - (s[5,3] + s[5,4]) * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b16'][number_of_loops] * Sq[1,2] * Ang[2,5] * ( Ang[1,3] * Sq[1,4] * Ang[1,5] * Sq[2,1] + s[1,2] * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b17'][number_of_loops] * Sq[1,2] * Ang[2,5] * ( Ang[2,3] * Sq[2,4] * Ang[1,5] * Sq[2,1] + s[1,2] * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b18'][number_of_loops] * Sq[1,2] * Ang[2,5] * ( Ang[3,5] * Sq[4,5] * Ang[1,5] * Sq[2,1] + (s[5,3] + s[5,4]) * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b19'][number_of_loops] * Sq[1,2] * Ang[3,5] * ( Ang[1,5] * Sq[1,4] + Ang[2,5] * Sq[2,4] ) 
+ form_factor.b['b20'][number_of_loops] * Sq[1,2]**2 * Sq[1,4] * Ang[2,3] * Ang[1,5]**2 
+ form_factor.b['b21'][number_of_loops] * Sq[1,2]**2 * Sq[2,4] * Ang[2,3] * Ang[2,5]**2 
+ form_factor.b['b22'][number_of_loops] * Sq[1,2]**2 * Sq[1,4] * Ang[2,3] * Ang[2,5]**2 
+ form_factor.b['b23'][number_of_loops] * Sq[1,2]**2 * Sq[2,4] * Ang[2,3] * Ang[2,5]**2 ) * GlobFac_3 * (const.vev/2 * const.C1)

    MLRRLL_3 = - n_loop_factor * (8 * form_factor.b['b8'][number_of_loops] * Sq[1,2] * Ang[1,3] * Sq[1,5] * Sq[4,5] 
+ 8 * form_factor.b['b9'][number_of_loops] * Sq[1,2] * Ang[2,3] * Sq[2,5] * Sq[4,5] 
+ 2 * form_factor.b['b10'][number_of_loops] * Sq[1,5] * Sq[2,5] * (s[1,2] * Ang[3,5] * Sq[4,5] - (s[5,3] + s[5,4]) * Ang[1,3] * Sq[1,4] ) 
+ 2 * form_factor.b['b11'][number_of_loops] * Sq[1,5] * Sq[2,5] * (s[1,2] * Ang[3,5] * Sq[4,5] - (s[5,3] + s[5,4]) * Ang[2,3] * Sq[2,4] ) 
+ 2 * form_factor.b['b12'][number_of_loops] * s[1,2] * Sq[1,5] * Sq[2,5] * ( Ang[2,3] * Sq[2,4] - Ang[1,3] * Sq[1,4] ) 
+ ( s[1,5] * form_factor.b['b13'][number_of_loops] + form_factor.b['b16'][number_of_loops] ) * Sq[2,1] * Sq[2,5] * ( Ang[3,1] * Sq[1,4] * Ang[1,2] * Sq[1,5] + s[1,2] * Ang[2,3] * Sq[4,5] ) 
+ ( s[1,5] * form_factor.b['b14'][number_of_loops] + form_factor.b['b17'][number_of_loops] ) * Sq[2,1] * Sq[2,5] * Ang[2,3] * ( Ang[2,1] * Sq[2,4] * Sq[1,5] + s[1,2] * Sq[4,5] ) 
+ ( s[1,5] * form_factor.b['b15'][number_of_loops] + form_factor.b['b18'][number_of_loops] ) * Sq[2,1] * Sq[2,5] * Sq[4,5] * ( Ang[2,1] * Sq[1,5] * Ang[3,5] + (s[5,3] + s[5,4]) * Ang[2,3] ) 
+ form_factor.b['b19'][number_of_loops] * Sq[2,1] * Ang[3,5] * ( Sq[1,5] * Sq[1,4] + Sq[2,5] * Sq[2,4] ) 
+ ( s[1,5] * form_factor.b['b20'][number_of_loops] + s[2,5] * form_factor.b['b22'][number_of_loops] ) * Sq[1,2]**2 * Sq[1,4] * Ang[2,3] 
+ ( s[2,5] * form_factor.b['b21'][number_of_loops] + s[1,5] * form_factor.b['b23'][number_of_loops] ) * Sq[1,2]**2 * Sq[2,4] * Ang[2,3] ) * GlobFac_3 * (const.vev/2 * const.C1)

    MRLLLL_3 = n_loop_factor * (4 * ( form_factor.b['b8'][number_of_loops] + form_factor.b['b9'][number_of_loops] ) * Ang[1,5] * Ang[2,5] * ( Ang[2,3] * Sq[2,4] + Ang[1,3] * Sq[1,4] ) 
+ 2 *form_factor.b['b10'][number_of_loops] * Ang[1,5] * Ang[2,5] * ( (s[5,3] + s[5,4]) * Ang[3,1] * Sq[1,4] * s[1,2] * Ang[3,5] * Sq[5,4] ) 
+ 2 *form_factor.b['b11'][number_of_loops] * Ang[1,5] * Ang[2,5] * ( (s[5,3] + s[5,4]) * Ang[3,2] * Sq[2,4] * s[1,2] * Ang[3,5] * Sq[5,4] ) 
+ 2 *form_factor.b['b12'][number_of_loops] * s[1,2] * Ang[1,5] * Ang[2,5] * ( Ang[2,3] * Sq[2,4] - Ang[1,3] * Sq[1,4] ) 
+ form_factor.b['b13'][number_of_loops] * s[1,5] * Ang[1,2] * Ang[2,5] * ( Ang[3,1] * Sq[1,4] * Sq[2,1] * Ang[1,5] - s[1,2] * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b14'][number_of_loops] * s[1,5] * Ang[1,2] * Ang[2,5] * ( Ang[3,2] * Sq[2,4] * Sq[2,1] * Ang[1,5] - s[1,2] * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b15'][number_of_loops] * s[1,5] * Ang[1,2] * Ang[2,5] * ( Ang[3,5] * Sq[5,4] * Sq[2,1] * Ang[1,5] - (s[5,3] + s[5,4]) * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b16'][number_of_loops] * Ang[1,2] * Ang[2,5] * ( Ang[1,3] * Sq[1,4] * Ang[1,5] * Sq[2,1] + s[1,2] * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b17'][number_of_loops] * Ang[1,2] * Ang[2,5] * ( Ang[2,3] * Sq[2,4] * Ang[1,5] * Sq[2,1] + s[1,2] * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b18'][number_of_loops] * Ang[1,2] * Ang[2,5] * ( Ang[3,5] * Sq[4,5] * Ang[1,5] * Sq[2,1] + (s[5,3] + s[5,4]) * Sq[2,4] * Ang[3,5] ) 
+ form_factor.b['b19'][number_of_loops] * Ang[1,2] * Ang[3,5] * ( Ang[1,5] * Sq[1,4] + Ang[2,5] * Sq[2,4] ) 
+ form_factor.b['b20'][number_of_loops] * s[1,2] * Sq[1,4] * Ang[3,2] * Ang[1,5]**2 
+ form_factor.b['b21'][number_of_loops] * s[1,2] * Sq[2,4] * Ang[3,2] * Ang[2,5]**2 
+ form_factor.b['b22'][number_of_loops] * s[1,2] * Sq[1,4] * Ang[3,2] * Ang[2,5]**2 
+ form_factor.b['b23'][number_of_loops] * s[1,2] * Sq[2,4] * Ang[3,2] * Ang[1,5]**2 ) * GlobFac_3 * (const.vev/2 * const.C2)

    MRLRLL_3 = - n_loop_factor * (2 * form_factor.b['b12'][number_of_loops] * Ang[1,2]**2 * Sq[1,5] * Sq[2,5] * ( Ang[1,3] * Sq[1,4] - Ang[2,3] * Sq[2,4] ) 
+ ( s[1,5] * form_factor.b['b13'][number_of_loops] + form_factor.b['b16'][number_of_loops] ) * Ang[1,2] * Sq[2,5] * ( Ang[3,1] * Sq[1,4] * Ang[1,2] * Sq[1,5] + s[1,2] * Ang[2,3] * Sq[4,5] ) 
+ ( s[1,5] * form_factor.b['b14'][number_of_loops] + form_factor.b['b17'][number_of_loops] ) * Ang[1,2] * Sq[2,5] * Ang[2,3] * ( Ang[2,1] * Sq[2,4] * Sq[1,5] + s[1,2] * Sq[4,5] ) 
+ ( s[1,5] * form_factor.b['b15'][number_of_loops] + form_factor.b['b18'][number_of_loops] ) * Ang[1,2] * Sq[2,5] * Sq[4,5] * ( Ang[2,1] * Sq[1,5] * Ang[3,5] + (s[5,3] * s[5,4]) * Ang[2,3] ) 
+ form_factor.b['b19'][number_of_loops] * Ang[1,2] * Ang[3,5] * ( Sq[1,5] * Sq[1,4] + Sq[2,5] * Sq[2,4] ) 
+ ( s[1,5] * form_factor.b['b20'][number_of_loops] + s[2,5] * form_factor.b['b22'][number_of_loops] ) * s[1,2] * Sq[1,4] * Ang[2,3] 
+ ( s[2,5] * form_factor.b['b21'][number_of_loops] + s[1,5] * form_factor.b['b23'][number_of_loops] ) * s[1,2] * Sq[2,4] * Ang[2,3] ) * GlobFac_3 * (const.vev/2 * const.C2)

    MLLLLL_3 = n_loop_factor * (( s[1,2] * form_factor.b['b1'][number_of_loops] + s[1,2] * form_factor.b['b2'][number_of_loops] + (s[1,2] + s[1,5] + s[2,5]) * form_factor.b['b3'][number_of_loops] + 2 * s[2,5] * form_factor.b['b7'][number_of_loops] ) * Ang[5,2] * Ang[5,3] * Sq[4,1] 
+ form_factor.b['b4'][number_of_loops] * Ang[3,1] * Sq[1,4] * Ang[2,5]**2 * Sq[1,2] 
+ form_factor.b['b5'][number_of_loops] * Ang[3,2] * Sq[2,4] * Ang[2,5]**2 * Sq[1,2] 
+ form_factor.b['b6'][number_of_loops] * Ang[3,5] * Sq[5,4] * Ang[2,5]**2 * Sq[1,2] 
+ 2 * form_factor.b['b7'][number_of_loops] * Ang[2,5] * Ang[1,5] * Sq[2,1] * Ang[2,3] * Sq[4,1] ) * GlobFac_3 * (const.S3 + const.vev/2 * const.C3)

    MLLRLL_3 = n_loop_factor * (form_factor.b['b1'][number_of_loops] * Ang[3,1] * Sq[1,4] * Sq[1,5]**2 * Ang[1,2] 
+ form_factor.b['b2'][number_of_loops] * Ang[3,2] * Sq[2,4] * Sq[1,5]**2 * Ang[1,2] 
+ form_factor.b['b3'][number_of_loops] * Ang[3,5] * Sq[5,4] * Sq[1,5]**2 * Ang[1,2] 
+ 2 * form_factor.b['b7'][number_of_loops] * Sq[1,5] * Sq[2,5] * Ang[1,2] * Ang[2,3] * Sq[4,1] 
+ ( s[1,2] * form_factor.b['b4'][number_of_loops] + s[1,2] * form_factor.b['b5'][number_of_loops] + (s[1,2] + s[1,5] + s[2,5]) * form_factor.b['b6'][number_of_loops] - 2 * s[1,5] * form_factor.b['b7'][number_of_loops] ) * Sq[1,5] * Ang[2,3] * Sq[4,5] ) * GlobFac_3 * (const.S3 + const.vev/2 * const.C3)

    MRRLLL_3 = n_loop_factor * (form_factor.b['b1'][number_of_loops] * Ang[3,1] * Sq[1,4] * Ang[1,5]**2 * Sq[2,1] 
+ form_factor.b['b2'][number_of_loops] * Ang[3,2] * Sq[2,4] * Ang[1,5]**2 * Sq[2,1] 
+ form_factor.b['b3'][number_of_loops] * Ang[3,5] * Sq[5,4] * Ang[1,5]**2 * Sq[2,1] 
+ 2 * form_factor.b['b7'][number_of_loops] * Ang[1,5] * Ang[2,5] * Sq[2,1] * Sq[2,4] * Ang[3,1] 
+ ( s[1,2] * form_factor.b['b4'][number_of_loops] + s[1,2] * form_factor.b['b5'][number_of_loops] + (s[1,2] + s[1,5] + s[2,5]) * form_factor.b['b6'][number_of_loops] - 2 * s[1,5] * form_factor.b['b7'][number_of_loops] ) * Ang[5,1] * Sq[2,4] * Ang[3,5] ) * GlobFac_3 * (const.vev/2 * const.C4)

    MRRRLL_3 = n_loop_factor * (( s[1,2] * form_factor.b['b1'][number_of_loops] + s[1,2] * form_factor.b['b2'][number_of_loops] + (s[1,2] + s[1,5] + s[2,5]) * form_factor.b['b3'][number_of_loops] + 2 * s[2,5] * form_factor.b['b7'][number_of_loops] ) * Sq[2,5] * Sq[5,4] * Ang[3,1] 
+ form_factor.b['b4'][number_of_loops] * Ang[3,1] * Sq[1,4] * Sq[2,5]**2 * Ang[2,1] 
+ form_factor.b['b5'][number_of_loops] * Ang[3,2] * Sq[2,4] * Sq[2,5]**2 * Ang[2,1] 
+ form_factor.b['b6'][number_of_loops] * Ang[3,5] * Sq[5,4] * Sq[2,5]**2 * Ang[2,1] 
+ 2 * form_factor.b['b7'][number_of_loops] * Sq[1,5] * Sq[2,5] * Ang[2,1] * Sq[2,4] * Ang[3,1] ) * GlobFac_3 * (const.vev/2 * const.C4)

    
    # 4-point amplitudes
    MLRLLL_4 = n_loop_factor * (4 * form_factor.a['a12'][number_of_loops] * Sq[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[1,5] * Ang[2,5] 
+ ( s[1,5] * form_factor.a['a13'][number_of_loops] - form_factor.a['a16'][number_of_loops] ) * Sq[1,2] * Ang[2,5] * (Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,5] + Sq[1,4] * Sq[2,4] * Ang[5,1] * Ang[3,4])
+ ( s[1,5] * form_factor.a['a14'][number_of_loops] - form_factor.a['a17'][number_of_loops] ) * Sq[2,1] * Sq[2,4]**2 * Ang[2,5]**2 * Ang[3,4] 
+ ( s[1,5] * form_factor.a['a15'][number_of_loops] - form_factor.a['a18'][number_of_loops] ) * s[2,5] * Sq[2,1] * Ang[3,5]**2 * Sq[3,4] 
+ form_factor.a['a19'][number_of_loops] * Sq[1,2] * Ang[3,5]**2 * Sq[3,4] 
+ form_factor.a['a20'][number_of_loops] * Sq[1,2] * Sq[1,4]**2 * Ang[1,5]**2 * Ang[3,4] 
+ form_factor.a['a21'][number_of_loops] * Sq[2,1] * Ang[1,5] * ( Sq[1,2] * Ang[3,2] * Ang[3,5] * Sq[3,4] + Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,5] ) 
+ form_factor.a['a22'][number_of_loops] * Sq[2,1] * Sq[1,4] * Sq[2,4] * Ang[1,5] * Ang[2,5] * Ang[3,4] 
+ form_factor.a['a23'][number_of_loops] * Sq[1,2] * Sq[2,4]**2 * Ang[2,5] * Ang[3,4]) * GlobFac_4 * const.C1

    MLRRLL_4 = n_loop_factor * (8 * form_factor.a['a8'][number_of_loops] * Sq[2,3] * Sq[3,4] * Ang[3,5] * Sq[5,1] 
+ 4 * form_factor.a['a9'][number_of_loops] * Sq[3,1] * Sq[2,5] * Sq[3,4] * Ang[3,5] 
+ 2 * form_factor.a['a10'][number_of_loops] * Sq[1,5] * Sq[2,5] * ( (s[5,3] + s[5,4]) * Ang[1,3] * Sq[1,4] - (s[1,3] + s[1,4]) * Ang[3,5] * Sq[4,5] ) 
+ 2 * form_factor.a['a11'][number_of_loops] * Sq[1,5] * Sq[2,5] * ( (s[5,3] + s[5,4]) * Ang[2,3] * Sq[2,4] - (s[2,3] + s[2,4]) * Ang[3,5] * Sq[4,5] ) 
+ 2 * form_factor.a['a12'][number_of_loops] * Sq[1,2] * Sq[1,3] * Sq[2,3] * Sq[4,3] * Ang[1,5] * Ang[2,5] 
+ form_factor.a['a13'][number_of_loops] * Ang[1,5]**2 * Ang[2,5] * Sq[1,2] * (Sq[1,3] * Sq[2,3] * Sq[1,5] * Sq[3,4] + Sq[1,4] * Sq[4,5] * Ang[3,4] * Sq[1,2] ) 
+ form_factor.a['a14'][number_of_loops] * s[2,5] * Sq[1,2] * Sq[2,3]**2 * Sq[3,4] * Ang[1,5]**2 
+ form_factor.a['a15'][number_of_loops] * Sq[1,2] * Ang[1,5]**2 * Ang[2,5]**2 * Sq[3,4] * Sq[4,5]**2 
+ form_factor.a['a16'][number_of_loops] * Sq[1,4] * Sq[2,3] * Sq[1,5] * Sq[2,5] * ( Ang[3,1] * Sq[2,3] + Ang[1,4] * Sq[2,4] ) 
+ form_factor.a['a17'][number_of_loops] * Sq[2,4] * Sq[2,3] * Sq[1,5] * Sq[2,5] * ( Ang[3,2] * Sq[2,3] + Ang[2,4] * Sq[2,4] ) 
+ form_factor.a['a18'][number_of_loops] * Sq[5,4] * Sq[2,3] * Sq[1,5] * Sq[2,5] * ( Ang[3,5] * Sq[2,3] + Ang[5,4] * Sq[2,4] ) 
+ form_factor.a['a19'][number_of_loops] * Sq[2,1] * Sq[3,4] * Ang[3,5]**2 
+ form_factor.a['a20'][number_of_loops] * Sq[2,1] * Sq[1,4]**2 * Ang[1,5]**2 * Ang[3,4] 
+ form_factor.a['a21'][number_of_loops] * Sq[2,1] * Ang[1,5] * ( Sq[1,2] * Ang[3,2] * Ang[3,5] * Sq[3,4] + Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,5] ) 
+ form_factor.a['a22'][number_of_loops] * Sq[2,1] * Sq[1,4] * Sq[2,4] * Ang[1,5] * Ang[2,5] * Ang[3,4] 
+ form_factor.a['a23'][number_of_loops] * Sq[2,1] * Sq[2,4]**2 * Ang[2,5] * Ang[3,4]) * GlobFac_4 * const.C1

    MRLLLL_4 = n_loop_factor * (8 * form_factor.a['a8'][number_of_loops] * Ang[2,3] * Sq[3,4] * Ang[3,5] * Ang[1,5] 
+ 4 * form_factor.a['a9'][number_of_loops] * Ang[1,3] * Ang[2,5] * Sq[3,4] * Ang[3,5] 
+ 2 * form_factor.a['a10'][number_of_loops] * Ang[1,5] * Ang[2,5] * ( (s[1,3] + s[1,4]) * Ang[3,5] * Sq[4,5] * - (s[5,3] + s[5,4]) * Ang[1,3] * Sq[1,4] ) 
+ 2 * form_factor.a['a11'][number_of_loops] * Ang[1,5] * Ang[2,5] * ( (s[2,3] + s[2,4]) * Ang[3,5] * Sq[4,5] - (s[5,3] + s[5,4]) * Ang[2,3] * Sq[2,4] ) 
+ 2 * form_factor.a['a12'][number_of_loops] * Sq[1,2] * Ang[1,3] * Ang[2,3] * Sq[4,3] * Ang[1,5] * Ang[2,5] 
+ form_factor.a['a13'][number_of_loops] * Ang[1,5]**2 * Ang[2,5] * Sq[1,2] * (Ang[3,1] * Ang[2,3] * Sq[1,5] * Sq[3,4] + Sq[1,4] * Sq[4,5] * Ang[4,3] * Ang[1,2] ) 
+ form_factor.a['a14'][number_of_loops] * s[2,5] * Sq[1,2] * Ang[2,3]**2 * Sq[3,4] * Ang[1,5]**2 
+ form_factor.a['a15'][number_of_loops] * Sq[1,2] * Ang[1,5]**2 * Ang[2,5]**2 * Ang[4,3] * Sq[4,5]**2 
+ form_factor.a['a16'][number_of_loops] * Sq[1,4] * Ang[2,3] * Ang[5,1] * Ang[2,5] * ( Ang[3,1] * Sq[2,3] + Ang[1,4] * Sq[2,4] ) 
+ form_factor.a['a17'][number_of_loops] * Sq[2,4] * Ang[2,3] * Ang[5,1] * Ang[2,5] * ( Ang[3,2] * Sq[2,3] + Ang[2,4] * Sq[2,4] ) 
+ form_factor.a['a18'][number_of_loops] * Sq[5,4] * Ang[2,3] * Ang[5,1] * Ang[2,5] * ( Ang[3,5] * Sq[2,3] + Ang[5,4] * Sq[2,4] ) 
+ form_factor.a['a19'][number_of_loops] * Ang[1,2] * Sq[3,4] * Ang[3,5]**2 
+ form_factor.a['a20'][number_of_loops] * Ang[1,2] * Sq[1,4]**2 * Ang[1,5]**2 * Ang[3,4] 
+ form_factor.a['a21'][number_of_loops] * Ang[1,2] * Ang[1,5] * ( Sq[1,2] * Ang[3,2] * Ang[3,5] * Sq[3,4] + Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,5] ) 
+ form_factor.a['a22'][number_of_loops] * Ang[1,2] * Sq[1,4] * Sq[2,4] * Ang[1,5] * Ang[2,5] * Ang[3,4] 
+ form_factor.a['a23'][number_of_loops] * Ang[1,2] * Sq[2,4]**2 * Ang[2,5] * Ang[3,4]) * GlobFac_4 * const.C2

    MRLRLL_4 = n_loop_factor * (4 * form_factor.a['a12'][number_of_loops] * Ang[2,1] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[1,5] * Ang[2,5] 
+ ( s[1,5] * form_factor.a['a13'][number_of_loops] - form_factor.a['a16'][number_of_loops] ) * Ang[2,1] * Ang[2,5] * (Ang[2,1] * Ang[1,3] * Sq[3,4] * Ang[3,5] + Sq[1,4] * Sq[2,4] * Ang[5,1] * Sq[3,4]) 
+ ( s[1,5] * form_factor.a['a14'][number_of_loops] - form_factor.a['a17'][number_of_loops] ) * Ang[1,2] * Sq[2,4]**2 * Ang[2,5]**2 * Ang[3,4] 
+ ( s[1,5] * form_factor.a['a15'][number_of_loops] - form_factor.a['a18'][number_of_loops] ) * s[2,5] * Ang[1,2] * Ang[3,5]**2 * Sq[3,4] 
+ form_factor.a['a19'][number_of_loops] * Ang[2,1] * Ang[3,5]**2 * Sq[3,4] 
+ form_factor.a['a20'][number_of_loops] * Ang[2,1] * Sq[1,4]**2 * Ang[1,5]**2 * Ang[3,4] 
+ form_factor.a['a21'][number_of_loops] * Ang[1,2] * Ang[1,5] * ( Sq[1,2] * Ang[3,2] * Ang[3,5] * Sq[3,4] + Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,5] ) 
+ form_factor.a['a22'][number_of_loops] * Ang[1,2] * Sq[1,4] * Sq[2,4] * Ang[1,5] * Ang[2,5] * Ang[3,4] 
+ form_factor.a['a23'][number_of_loops] * Ang[2,1] * Ang[2,4]**2 * Ang[2,5] * Ang[3,4]) * GlobFac_4 * const.C2

    MLLLLL_4 = n_loop_factor * (( s[1,2] * form_factor.a['a1'][number_of_loops] + s[1,2] * form_factor.a['a2'][number_of_loops] + (s[1,2] + s[1,5] + s[2,5]) * form_factor.a['a3'][number_of_loops] + 2 * s[2,5] * form_factor.a['a7'][number_of_loops] ) * Ang[5,2] * Ang[5,3] * Sq[4,1] 
+ form_factor.a['a4'][number_of_loops] * Ang[3,1] * Sq[1,4] * Ang[2,5]**2 * Sq[1,2] 
+ form_factor.a['a5'][number_of_loops] * Ang[3,2] * Sq[2,4] * Ang[2,5]**2 * Sq[1,2] 
+ form_factor.a['a6'][number_of_loops] * Ang[3,5] * Sq[5,4] * Ang[2,5]**2 * Sq[1,2] 
+ 2 * form_factor.a['a7'][number_of_loops] * Ang[2,5] * Ang[1,5] * Sq[2,1] * Ang[2,3] * Sq[4,1]) * GlobFac_4 * const.C3

    MLLRLL_4 = n_loop_factor * (form_factor.a['a1'][number_of_loops] * Ang[3,1] * Sq[1,4] * Sq[1,5]**2 * Ang[1,2] 
+ form_factor.a['a2'][number_of_loops] * Ang[3,2] * Sq[2,4] * Sq[1,5]**2 * Ang[1,2] 
+ form_factor.a['a3'][number_of_loops] * Ang[3,5] * Sq[5,4] * Sq[1,5]**2 * Ang[1,2] 
+ 2 * form_factor.a['a7'][number_of_loops] * Sq[1,5] * Sq[2,5] * Ang[1,2] * Ang[2,3] * Sq[4,1] 
+ ( s[1,2] * form_factor.a['a4'][number_of_loops] + s[1,2] * form_factor.a['a5'][number_of_loops] + (s[1,2] + s[1,5] + s[2,5]) * form_factor.a['a6'][number_of_loops] - 2 * s[1,5] * form_factor.a['a7'][number_of_loops] ) * Sq[1,5] * Ang[2,3] * Sq[4,5] ) * GlobFac_4 * const.C3

    MRRLLL_4 = n_loop_factor * (form_factor.a['a1'][number_of_loops] * Ang[3,1] * Sq[1,4] * Ang[1,5]**2 * Sq[2,1] 
+ form_factor.a['a2'][number_of_loops] * Ang[3,2] * Sq[2,4] * Ang[1,5]**2 * Sq[2,1] 
+ form_factor.a['a3'][number_of_loops] * Ang[3,5] * Sq[5,4] * Ang[1,5]**2 * Sq[2,1] 
+ 2 * form_factor.a['a7'][number_of_loops] * Ang[1,5] * Ang[2,5] * Sq[2,1] * Sq[2,4] * Ang[3,1] 
+ ( s[1,2] * form_factor.a['a4'][number_of_loops] + s[1,2] * form_factor.a['a5'][number_of_loops] + (s[1,2] + s[1,5] + s[2,5]) * form_factor.a['a6'][number_of_loops] - 2 * s[1,5] * form_factor.a['a7'][number_of_loops] ) * Ang[5,1] * Sq[2,4] * Ang[3,5] ) * GlobFac_4 * const.C4

    MRRRLL_4 = n_loop_factor * (( s[1,2] * form_factor.a['a1'][number_of_loops] + s[1,2] * form_factor.a['a2'][number_of_loops] + (s[1,2] + s[1,5] + s[2,5]) * form_factor.a['a3'][number_of_loops] + 2 * s[2,5] * form_factor.a['a7'][number_of_loops] ) * Sq[2,5] * Sq[5,4] * Ang[3,1] 
+ form_factor.a['a4'][number_of_loops] * Ang[3,1] * Sq[1,4] * Sq[2,5]**2 * Ang[2,1] 
+ form_factor.a['a5'][number_of_loops] * Ang[3,2] * Sq[2,4] * Sq[2,5]**2 * Ang[2,1] 
+ form_factor.a['a6'][number_of_loops] * Ang[3,5] * Sq[5,4] * Sq[2,5]**2 * Ang[2,1] 
+ 2 * form_factor.a['a7'][number_of_loops] * Sq[1,5] * Sq[2,5] * Ang[2,1] * Sq[2,4] * Ang[3,1] ) * GlobFac_4 * const.C4

    # Total amplitudes
    MLRLLL = MLRLLL_3 + MLRLLL_4
    MRLLLL = MRLLLL_3 + MRLLLL_4
    MLLLLL = MLLLLL_3 + MLLLLL_4
    MRRLLL = MRRLLL_3 + MRRLLL_4
    MLRRLL = MLRRLL_3 + MLRRLL_4
    MRLRLL = MRLRLL_3 + MRLRLL_4
    MLLRLL = MLLRLL_3 + MLLRLL_4
    MRRRLL = MRRRLL_3 + MRRRLL_4

    return MLRLLL, MLRRLL, MRLLLL, MRLRLL, MLLLLL, MLLRLL, MRRLLL, MRRRLL





# SINGLE REAL GLUON TREE-LEVEL AND ONE-LOOP (VIRTUAL-REAL) SQUARED AMPLITUDE

def single_real_squared_amplitude(number_of_loops):

    spin_color_factor = const.Cf * const.Nc/((2 * const.Nc)**2)

    # Total single-real tree-level and virtual-real helicity amplitudes
    MLRLLL0, MLRRLL0, MRLLLL0, MRLRLL0, MLLLLL0, MLLRLL0, MRRLLL0, MRRRLL0 = single_real_amplitude(0)
    MLRLLL1, MLRRLL1, MRLLLL1, MRLRLL1, MLLLLL1, MLLRLL1, MRRLLL1, MRRRLL1 = single_real_amplitude(1)

    # Squared helicity amplitudes
    if number_of_loops == 0:
        M2 = MLRLLL0 * MLRLLL0.conjugate() + MRLLLL0 * MRLLLL0.conjugate() + MLLLLL0 * MLLLLL0.conjugate() + MRRLLL0 * MRRLLL0.conjugate()
        + MLRRLL0 * MLRRLL0.conjugate() + MRLRLL0 * MRLRLL0.conjugate() + MLLRLL0 * MLLRLL0.conjugate() + MRRRLL0 * MRRRLL0.conjugate()
    else:
        M2 = (MLRLLL0 * MLRLLL1.conjugate()).real + (MRLLLL0 * MRLLLL1.conjugate()).real + (MLLLLL0 * MLLLLL1.conjugate()).real + (MRRLLL0 * MRRLLL1.conjugate()).real
        + (MLRRLL0 * MLRRLL1.conjugate()).real + (MRLRLL0 * MRLRLL1.conjugate()).real + (MLLRLL0 * MLLRLL1.conjugate()).real + (MRRRLL0 * MRRRLL1.conjugate()).real

    # Multiply with the spin-color factor

    M2 = M2.real * spin_color_factor

    # Print result

    if number_of_loops == 0:
        print("Total squared single real gluon tree-level amplitude:")
    else:
        print("Total squared single real gluon one-loop (virtual-real) amplitude:")
    print("|M|^2 =", M2, "\n")





# DOUBLE REAL GLUON TREE-LEVEL HELICITY AMPLITUDES

def double_real_amplitude():

    s, Ang, Sq, GlobFac_3, GlobFac_4 = helicities.helicities(5)

    n_loop_factor = (const.alpha_s / (2 * math.pi))**2


    # HELICITY AMPLITUDES
    # Helicity order: M(quark, antiquark, gluon5, gluon6, lepton, antilepton)

    # 3-point amplitudes
    MLRLLLL_3 = n_loop_factor * 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( const.Nc * ((Sq[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,6]) / (Sq[1,5] * Sq[5,6]) + (Sq[1,2] * Sq[1,4] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Sq[1,5] * Sq[5,6]) - (Sq[1,2] * Sq[1,4] * Ang[3,4] * Sq[4,6] * Ang[5,6]) / (Sq[5,6] * Sq[1,6])) - 2 * const.Cf * ((Sq[1,2]**2 * Sq[1,4] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Sq[1,5] * Sq[2,5] * Sq[1,6]) - (Sq[1,2]**2 * Sq[1,4] * Ang[3,4] 
* Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2]**2 * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2]**2 * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,6]) / (Sq[1,5] * Sq[2,5] * Sq[1,6]))) * GlobFac_3 * (const.vev/2 * const.C1)

    MLRLRLL_3 = n_loop_factor * 2 * const.Cf * ( 4 * const.Cf * (Sq[1,2] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,4] * Sq[2,4] * Ang[1,5] * Sq[1,6] * Ang[3,4]) / (Sq[1,5] * Ang[1,6]) - (Sq[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Sq[2,4] * Sq[2,6] * Ang[3,4]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (Sq[1,2] * Sq[1,4] * Ang[1,5] * Sq[2,6] * Ang[3,4] * Sq[4,5]) 
/ (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (Sq[1,2] * Sq[1,4] * Sq[2,6] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Sq[2,5])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Sq[2,4] * Ang[2,5] * Ang[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) - (s[1,2] * Sq[1,4] * Ang[3,4] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) - (Sq[1,4] * Sq[1,6] * Sq[2,4] * Ang[2,5] * Ang[3,4]) / (Sq[1,5] * Ang[2,6]) + (Sq[1,4] * Sq[1,6] * Ang[3,4] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[2,6])) + 4 * const.Cf 
* 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,5] * Sq[1,6]**2 * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Sq[1,6]**2 * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Sq[5,6]) - (Ang[1,5] * Sq[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,6] * Sq[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Sq[1,4] * Ang[1,5] * Sq[2,4] * Ang[2,5] * Ang[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] * Sq[1,6] * Sq[2,4] * Sq[2,6] * Ang[3,4]) / (Sq[1,5] 
* Ang[1,6] * Sq[5,6]) - (Sq[1,2] * Sq[1,4] * Ang[1,5] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Ang[1,6]) - (Sq[1,4] * Sq[1,6] * Sq[2,6] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Sq[5,6]) - (Sq[1,4] * Ang[1,5] * Sq[1,6] * Sq[2,6] * Ang[3,4] * Sq[4,5]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) - (Sq[1,4] * Ang[1,5] * Sq[1,6] * Sq[2,5] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6])) - const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Sq[1,4] * Ang[1,5] * Sq[1,6] 
* Sq[2,4] * Ang[3,4]) / (Sq[1,5] * Ang[1,6]) - const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Sq[1,4] * Ang[1,5] * Sq[1,6] * Sq[2,4] * Ang[3,4]) / (Sq[1,5] * Ang[1,6])) * GlobFac_3 * (const.vev/2 * const.C1)

    MLRRLLL_3 = n_loop_factor * 2 * const.Cf * ( - 4 * const.Cf * (Sq[1,2] * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,4] * Sq[1,5] * Ang[1,6] * Sq[2,4] * Ang[3,4]) / (Ang[1,5] * Sq[1,6]) + (Sq[1,5] * Sq[2,4] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Ang[1,5] * Sq[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Sq[2,4] * Ang[2,6] * Ang[3,4]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + (s[1,2] * Sq[1,4] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Ang[1,5] 
* Sq[1,6] * Ang[2,5]) + (s[1,2] * Sq[1,4] * Sq[2,4] * Sq[2,5] * Ang[3,4]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,4] * Sq[1,5] * Sq[2,4] * Ang[2,6] * Ang[3,4]) / (Sq[1,6] * Ang[2,5]) + (Sq[1,4] * Sq[1,5] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Sq[1,6] * Ang[2,5]) - (Sq[1,2] * Sq[1,4] * Sq[2,5] * Ang[3,4] * Sq[4,5]) / (Sq[1,6] * Sq[2,6]) - (Sq[1,2] * Sq[1,4] * Ang[1,6] * Sq[2,5] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,6])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) 
* ((Sq[1,5]**2 * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,5]**2 * Ang[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) - (Sq[1,5]**2 * Ang[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Sq[1,4] * Sq[1,5] * Sq[2,4] * Sq[2,5] * Ang[3,4]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) - (Sq[1,4] * Sq[1,5] * Sq[2,5] * Ang[3,4] * Sq[4,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,2] * Sq[1,4] 
* Ang[1,6] * Sq[2,4] * Ang[2,6] * Ang[3,4]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) + (Sq[1,2] * Sq[1,4] * Ang[1,6] * Ang[3,4] * Sq[4,5]) / (Ang[1,5] * Sq[1,6])) - const.Nc * ((s[1,5] - s[1,6] - s[5,6])) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Sq[1,4] * Sq[1,5] * Ang[1,6] * Sq[2,4] * Ang[3,4]) / (Ang[1,5] * Sq[1,6]) - const.Nc * ((s[2,5] - s[2,6] - s[5,6])) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Sq[1,4] * Sq[1,5] * Ang[1,6] * Sq[2,4] * Ang[3,4]) / (Ang[1,5] * Sq[1,6])) * GlobFac_3 * (const.vev/2 * const.C1)

    MLRRRLL_3 = n_loop_factor * 4 * const.Cf * ( 2 * const.Cf * ((Ang[1,2] * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) + (Ang[3,4] * Sq[4,5] * Sq[4,6]) / (Ang[1,5] * Ang[2,6]) + (Ang[3,4] * Sq[4,5] * Sq[4,6]) / (Ang[1,6] * Ang[2,5])) + 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Ang[1,2]**2 * Sq[1,4] * Sq[2,4] * Sq[2,6] * Ang[3,4]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) - (Ang[1,2]**2 * Sq[1,4] * Sq[2,4] * Sq[2,5] * Ang[3,4]) / (Ang[1,5] 
* Ang[1,6] * Ang[2,6]) - (Ang[1,2] * Sq[1,4] * Sq[2,6] * Ang[3,4] * Sq[4,5]) / (Ang[1,6] * Ang[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[2,5] * Ang[3,4] * Sq[4,5]) / (Ang[1,6] * Ang[2,6]) - (Ang[1,2] * Sq[1,4] * Sq[2,6] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[2,5] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[2,6]) + (Ang[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Sq[5,6]) / (Ang[1,6] * Ang[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Sq[5,6]) / (Ang[1,5] * Ang[2,6]) 
+ (Sq[1,4] * Ang[1,5] * Ang[3,4] * Sq[4,5] * Sq[5,6]) / (Ang[1,6] * Ang[2,5]) - (Sq[1,4] * Ang[1,6] * Ang[3,4] * Sq[4,6] * Sq[5,6]) / (Ang[1,5] * Ang[2,6]) + (Sq[1,4] * Ang[3,4] * Sq[4,6] * Sq[5,6]) / (Ang[2,5]) - (Sq[1,4] * Ang[3,4] * Sq[4,5] * Sq[5,6]) / (Ang[2,6])) + const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Ang[5,6]) + (Sq[1,5] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[5,6]) + (s[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[5,6]) 
+ (s[1,5] * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Ang[1,6] * Ang[5,6])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Sq[1,4] * Sq[2,4] * Sq[2,5] * Ang[3,4]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] * Sq[2,4] * Sq[2,6] * Ang[3,4]) / (Ang[1,5] * Ang[5,6]) + (Sq[1,4] * Sq[2,5] * Ang[3,4] * Sq[4,6]) / (Ang[5,6]) + (Sq[1,4] * Sq[2,6] * Ang[3,4] * Sq[4,5]) / (Ang[5,6]) + (Sq[1,4] * Ang[1,5] * Sq[2,5] * Ang[3,4] * Sq[4,5]) / (Ang[1,6] * Ang[5,6]) + (Sq[1,4] * Ang[1,6] * Sq[2,6] 
* Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[5,6]))) * GlobFac_3 * (const.vev/2 * const.C1)

    MRLLLLL_3 = n_loop_factor * 4 * const.Cf * ( - 2 * const.Cf * ((Sq[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,5]) + (Sq[3,4] * Ang[3,5] * Ang[3,6]) / (Sq[1,5] * Sq[2,6]) + (Sq[3,4] * Ang[3,5] * Ang[3,6]) / (Sq[1,6] * Sq[2,5])) + 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[2,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,5]) + (Sq[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[2,5]) / (Sq[1,5] 
* Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,5] * Ang[2,6]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[2,5] * Ang[3,6]) / (Sq[1,5] * Sq[2,6]) + (Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[2,6] * Ang[3,6]) / (Sq[1,5] * Sq[2,5]) + (Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[2,5] * Ang[3,5]) / (Sq[1,6] * Sq[2,6]) - (Sq[1,2] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[5,6]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,2] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[5,6]) / (Sq[1,5] * Sq[2,6]) 
- (Ang[1,3] * Sq[1,5] * Sq[3,4] * Ang[3,5] * Ang[5,6]) / (Sq[1,6] * Sq[2,5]) - (Ang[1,3] * Sq[1,6] * Sq[3,4] * Ang[3,6] * Ang[5,6]) / (Sq[1,5] * Sq[2,6]) - (Ang[1,3] * Sq[3,4] * Ang[3,6] * Ang[5,6]) / (Sq[2,5]) + (Ang[1,3] * Sq[3,4] * Ang[3,5] * Ang[5,6]) / (Sq[2,6])) - const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[2,3] * Ang[1,6] * Sq[3,4] * Ang[3,5]) / (Sq[5,6]) + (Ang[2,3] * Ang[1,5] * Sq[3,4] * Ang[3,6]) / (Sq[5,6]) + (s[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Sq[5,6]) 
+ (s[1,5] * Ang[2,3] * Sq[3,4] * Ang[3,5]) / (Sq[1,6] * Sq[5,6])) - const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[2,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,2] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[2,6]) / (Sq[1,5] * Sq[5,6]) + (Ang[1,3] * Sq[3,4] * Sq[1,5] * Ang[2,5] * Ang[3,5]) / (Sq[1,6] * Sq[5,6]) + (Ang[1,3] * Sq[3,4] * Sq[1,6] * Ang[2,6] * Ang[3,6]) / (Sq[1,5] * Sq[5,6]) + (Ang[1,3] * Sq[3,4] * Ang[2,5] * Ang[3,6]) / (Sq[5,6]) + (Ang[1,3] 
* Sq[3,4] * Ang[2,6] * Ang[3,5]) / (Sq[5,6]))) * GlobFac_3 * (const.vev/2 * const.C2)

    MRLLRLL_3 = n_loop_factor * 2 * const.Cf * ( - 4 * const.Cf * ((Ang[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,5]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) + (Sq[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (Sq[3,4] * Ang[3,5] * Ang[3,6]) / (Ang[1,6] * Sq[2,5])) - 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,3] * Ang[2,3] * Ang[1,5] * Sq[1,6] * Sq[3,4]) / (Sq[1,5] * Ang[1,6]) + (Ang[1,5] * Ang[2,3] * Sq[3,4] * Ang[3,5] * Sq[5,6]) / (Sq[1,5] * Ang[1,6])) - 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] 
* Ang[1,3] * Ang[2,3] * Sq[3,4] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (s[1,2] * Ang[1,3] * Ang[3,5] * Sq[3,4] * Sq[5,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (s[1,2] * Ang[1,3] * Ang[2,3] * Ang[2,5] * Sq[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) + (s[1,5] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (s[1,5] * Ang[1,3] * Ang[3,5] * Sq[3,4] * Sq[5,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (Ang[1,2] * Ang[2,5] * Ang[1,3] * Ang[3,5] * Sq[3,4]) 
/ (Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Ang[2,5] * Sq[1,6] * Ang[1,3] * Ang[3,6] * Sq[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[2,6])) - 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,5]**2 * Ang[2,3] * Ang[3,5] * Sq[3,4]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,5]**2 * Sq[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) - (Ang[1,5]**2 * Sq[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Ang[5,6])) - 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Ang[1,3] * Ang[1,5] 
* Ang[2,3] * Ang[2,5] * Sq[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Ang[1,3] * Ang[1,5] * Ang[2,5] * Sq[3,4] * Ang[3,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,6] * Ang[2,3] * Sq[2,6] * Sq[3,4]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,6] * Sq[3,4] * Ang[3,5] * Sq[5,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6])) + const.Nc * ((s[1,5] - s[1,6] - s[5,6])) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Ang[1,3] * Ang[1,5] * Sq[1,6] * Ang[2,3] * Sq[3,4]) / (Sq[1,5] 
* Ang[1,6]) + const.Nc * ((s[2,5] - s[2,6] - s[5,6])) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Ang[1,3] * Ang[1,5] * Sq[1,6] * Ang[2,3] * Sq[3,4]) / (Sq[1,5] * Ang[1,6])) * GlobFac_3 * (const.vev/2 * const.C2)

    MRLRLLL_3 = n_loop_factor * 2 * const.Cf * ( - 4 * const.Cf * (Ang[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[1,6]) - (Ang[1,3] * Sq[1,5] * Ang[1,6] * Ang[2,3] * Sq[3,4]) / (Ang[1,5] * Sq[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (s[1,2] * Ang[1,3] * Ang[2,3] * Ang[2,6] * Sq[3,4]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) - (s[1,2] * Ang[1,3] * Ang[2,3] * Sq[2,5] * Sq[3,4]) 
/ (Ang[1,5] * Sq[1,6] * Sq[2,6]) - (s[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,5] * Ang[2,6] * Sq[3,4] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + (Ang[1,2] * Ang[1,3] * Sq[1,6] * Ang[2,6] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) - (Ang[1,3] * Ang[1,6] * Ang[2,3] * Sq[2,5] * Sq[3,4]) / (Ang[1,5] * Sq[2,6]) + (Ang[1,3] * Ang[1,6] * Sq[3,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[2,6])) + 2 * const.Nc * 1 
/ (s[1,5] + s[1,6] + s[5,6]) * ( - (Sq[1,5] * Ang[1,6]**2 * Ang[2,3] * Sq[3,4] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) - (Ang[1,6]**2 * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Ang[5,6]) + (Sq[1,5] * Ang[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,6] * Ang[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Ang[1,2] * Ang[1,3] * Sq[1,5] * Ang[2,3] * Sq[2,5] * Sq[3,4]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) - (Sq[1,2] * Ang[1,3] * Ang[1,6] * Ang[2,3] * Ang[2,6] * Sq[3,4]) / (Ang[1,5] 
* Sq[1,6] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,5] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6]) + (Ang[1,3] * Ang[1,6] * Sq[1,5] * Ang[2,5] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) - (Ang[1,3] * Sq[1,5] * Ang[1,6] * Ang[2,6] * Sq[3,4] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) - (Ang[1,3] * Ang[1,6] * Ang[2,6] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Ang[5,6])) + const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Ang[1,3] * Sq[1,5] * Ang[1,6] 
* Ang[2,3] * Sq[3,4]) / (Ang[1,5] * Sq[1,6]) + const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Ang[1,3] * Sq[1,5] * Ang[1,6] * Ang[2,3] * Sq[3,4]) / (Ang[1,5] * Sq[1,6])) * GlobFac_3 * (const.vev/2 * const.C2)

    MRLRRLL_3 = n_loop_factor * 4 * const.Cf * ( 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[2,6] * Sq[3,4]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) + (Ang[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[2,5] * Sq[3,4]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) + (Ang[1,2]**2 * Ang[1,3] * Sq[3,4] * Ang[3,5] * Sq[5,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) - (Ang[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[2,5] * Sq[3,4]) / (Ang[1,5] * Ang[1,6] * Ang[2,6])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Ang[1,2] * Ang[1,3] * Ang[2,3] 
* Sq[2,5] * Sq[3,4]) / (Ang[1,6] * Ang[5,6]) - (Ang[1,2] * Ang[1,3] * Ang[2,3] * Sq[2,6] * Sq[3,4]) / (Ang[1,5] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,6] * Ang[5,6]) - (Ang[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,5] * Sq[5,6]) / (Ang[1,5] * Ang[5,6]))) * GlobFac_3 * (const.vev/2 * const.C2)

    MLLLLLL_3 = n_loop_factor * 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( 2 * const.Cf * ((Sq[1,2]**2 * Sq[1,4] * Ang[2,3] * Ang[2,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,5]) + (Sq[1,2]**2 * Sq[1,4] * Ang[2,3] * Ang[2,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Sq[1,4] * Ang[2,6] * Ang[3,5]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,2] * Sq[1,4] * Ang[2,5] * Ang[3,5]) / (Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Sq[1,4] * Ang[2,6] * Ang[3,6]) / (Sq[1,5] * Sq[2,5]) + (Sq[1,2] * Sq[1,4] * Ang[2,5] * Ang[3,6]) / (Sq[1,5] * Sq[2,6]) + (Sq[1,2] 
* Ang[2,3] * Sq[1,4] * Ang[5,6]) / (Sq[1,5] * Sq[2,6]) - (Sq[1,2] * Ang[2,3] * Sq[1,4] * Ang[5,6]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,4] * Sq[1,6] * Ang[3,6] * Ang[5,6]) / (Sq[1,5] * Sq[2,6]) - (Sq[1,4] * Sq[1,5] * Ang[3,5] * Ang[5,6]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,4] * Ang[3,5] * Ang[5,6]) / (Sq[2,6]) - (Sq[1,4] * Ang[3,6] * Ang[5,6]) / (Sq[2,5])) + const.Nc * ((Sq[1,2] * Ang[2,3] * Sq[1,4] * Ang[2,5] * Ang[5,6]) / (Sq[1,6] * Sq[5,6]) - (Sq[1,2] * Ang[2,3] * Sq[1,4] * Ang[2,6] * Ang[5,6]) 
/ (Sq[1,5] * Sq[5,6]) + (Sq[1,4] * Sq[1,5] * Ang[2,5] * Ang[3,5] * Ang[5,6]) / (Sq[1,6] * Sq[5,6]) - (Sq[1,4] * Sq[1,6] * Ang[2,6] * Ang[3,6] * Ang[5,6]) / (Sq[1,5] * Sq[5,6]) + (Sq[1,4] * Ang[2,5] * Ang[3,6] * Ang[5,6]) / (Sq[5,6]) - (Sq[1,4] * Ang[2,6] * Ang[3,5] * Ang[5,6]) / (Sq[5,6]))) * GlobFac_3 * (const.S3 + const.vev/2 * const.C3)

    MLLLRLL_3 = n_loop_factor * const.Cf * ( 4 * const.Cf * ((Sq[1,2] * Ang[2,3] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (Ang[3,5] * Sq[4,6]) / (Ang[1,6] * Sq[2,5])) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,4] * Ang[1,5] * Sq[1,6] * Ang[2,3]) / (Sq[1,5] * Ang[1,6]) - (Sq[1,6] * Ang[2,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (s[1,2] * Sq[1,4] * Ang[3,5] * Sq[5,6]) / (Sq[1,5] * Ang[1,6] 
* Sq[2,5]) + (s[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (Sq[1,4] * Ang[1,5] * Ang[2,3] * Sq[2,6]) / (Ang[1,6] * Sq[2,5]) + (Sq[1,4] * Ang[1,5] * Ang[3,5] * Sq[5,6]) / (Ang[1,6] * Sq[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[2,6] * Ang[3,5]) / (Ang[1,6] * Sq[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[1,6] * Sq[2,6] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,5] * Sq[1,6] * Ang[2,3] * Sq[4,6] * Ang[5,6]) / (Ang[1,6] 
* Sq[5,6]) - (Sq[1,6]**2 * Ang[2,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Sq[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Sq[1,4] * Ang[1,5] * Ang[2,3] * Ang[2,5]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Sq[1,4] * Ang[1,5] * Ang[2,5] * Ang[3,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[2,5] * Sq[1,6] * Ang[1,5] * Ang[3,6] * Sq[1,4]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) - (Ang[2,5] * Sq[1,6] * Ang[1,5] * Ang[3,6] * Sq[1,4]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] * Sq[1,6] 
* Sq[2,6] * Ang[2,3]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Ang[1,2] * Sq[1,6] * Ang[3,5] * Sq[1,4]) / (Sq[1,5] * Ang[1,6])) - const.Nc * ((s[1,5] - s[1,6] - s[5,6])) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Sq[1,4] * Ang[1,5] * Sq[1,6] * Ang[2,3]) / (Sq[1,5] * Ang[1,6]) - const.Nc * ((s[2,5] - s[2,6] - s[5,6])) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Sq[1,4] * Ang[1,5] * Sq[1,6] * Ang[2,3]) / (Sq[1,5] * Ang[1,6])) * GlobFac_3 * (const.S3 + const.vev/2 * const.C3)

    MLLRLLL_3 = n_loop_factor * const.Cf * ( 4 * const.Cf * ((Sq[1,2] * Ang[2,3] * Sq[4,5]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + (Ang[3,6] * Sq[4,5]) / (Ang[1,5] * Sq[2,6])) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,3]) / (Ang[1,5] * Sq[1,6]) + (Sq[1,5] * Ang[2,3] * Sq[4,5] * Ang[5,6]) / (Ang[1,5] * Sq[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Ang[2,3] * Ang[2,6]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + (s[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,5]) / (Ang[1,5] * Sq[1,6] 
* Sq[2,6]) - (s[1,2] * Sq[1,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) - (Ang[1,2] * Sq[1,4] * Sq[1,5] * Ang[2,6] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) - (Ang[1,2] * Sq[1,4] * Ang[2,6] * Ang[3,6]) / (Ang[1,5] * Ang[2,5]) + (Sq[1,4] * Ang[1,6] * Ang[2,3] * Sq[2,5]) / (Ang[1,5] * Sq[2,6]) - (Sq[1,4] * Ang[1,6] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[2,6])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,5]**2 * Ang[2,3] * Sq[4,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,5]**2 
* Ang[1,6] * Ang[2,3] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) - (Sq[1,5]**2 * Ang[1,6] * Ang[2,3] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Sq[1,5] * Sq[2,5] * Ang[2,3] * Sq[1,4]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) + (Ang[1,2] * Sq[1,4] * Sq[1,5] * Ang[3,6]) / (Ang[1,5] * Sq[1,6]) + (Sq[1,2] * Sq[1,4] * Ang[1,6] * Ang[2,3] * Ang[2,6]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) + (Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,6] * Ang[3,5]) 
/ (Ang[1,5] * Sq[1,6] * Ang[5,6]) + (Sq[1,4] * Ang[1,6] * Ang[2,6] * Ang[3,6]) / (Ang[1,5] * Ang[5,6]) - (Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,5] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[5,6])) - const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,3]) / (Ang[1,5] * Sq[1,6]) - const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,3]) / (Ang[1,5] * Sq[1,6])) * GlobFac_3 * (const.S3 + const.vev/2 * const.C3)

    MLLRRLL_3 = n_loop_factor * 2 * const.Cf * ( 2 * const.Cf * ((Ang[1,2] * Ang[2,3] * Sq[4,5]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Ang[2,3] * Sq[4,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5])) + 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Ang[1,2]**2 * Sq[1,4] * Ang[2,3] * Sq[2,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) - (Ang[1,2]**2 * Sq[1,4] * Ang[2,3] * Sq[2,5]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) - (Ang[1,2]**2 * Sq[1,4] * Ang[3,5] * Sq[5,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) + (Ang[1,2]**2 * Sq[1,4] * Ang[3,6] * Sq[5,6]) 
/ (Ang[1,5] * Ang[1,6] * Ang[2,6])) + const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,6] * Ang[2,3] * Sq[4,5]) / (Ang[1,6] * Ang[5,6]) + (Sq[1,5] * Ang[2,3] * Sq[4,6]) / (Ang[5,6]) + (s[1,6] * Ang[2,3] * Sq[4,6]) / (Ang[1,5] * Ang[5,6]) + (s[1,5] * Ang[2,3] * Sq[4,5]) / (Ang[1,6] * Ang[5,6])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,6]) / (Ang[1,5] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] 
* Ang[3,5] * Sq[5,6]) / (Ang[1,5] * Ang[5,6]) - (Ang[1,2] * Sq[1,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,6] * Ang[5,6]))) * GlobFac_3 * (const.S3 + const.vev/2 * const.C3)

    MRRLLLL_3 = n_loop_factor * 2 * const.Cf * ( 2 * const.Cf * ((Sq[1,2] * Sq[2,4] * Ang[3,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Sq[2,4] * Ang[3,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,5])) - 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2]**2 * Ang[1,3] * Sq[2,4] * Ang[2,6]) / (Sq[1,5] * Sq[2,5] * Sq[1,6]) + (Sq[1,2]**2 * Ang[1,3] * Sq[2,4] * Ang[2,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2]**2 * Ang[1,3] * Sq[4,5] * Ang[5,6]) / (Sq[1,5] * Sq[2,5] * Sq[1,6]) - (Sq[1,2]**2 * Ang[1,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] 
* Sq[1,6] * Sq[2,6])) + const.Nc * (s[1,5] + s[1,6]) / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[2,4] * Ang[3,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[2,4] * Ang[3,6]) / (Sq[1,5] * Sq[5,6])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Ang[1,3] * Sq[2,4] * Ang[2,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,2] * Ang[1,3] * Sq[2,4] * Ang[2,6]) / (Sq[1,5] * Sq[5,6]) + (Sq[1,2] * Ang[1,3] * Sq[4,5] * Ang[5,6]) / (Sq[1,5] * Sq[5,6]) - (Sq[1,2] * Ang[1,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,6] * Sq[5,6]))) * GlobFac_3 * (const.vev/2 * const.C4)

    MRRLRLL_3 = n_loop_factor * const.Cf * ( 4 * const.Cf * ((Ang[1,2] * Sq[2,4] * Sq[2,6] * Ang[3,5]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) + (Sq[2,6] * Ang[3,5] * Sq[4,6]) / (Sq[1,5] * Ang[2,6])) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,3] * Ang[1,5] * Sq[1,6] * Sq[2,4]) / (Sq[1,5] * Ang[1,6]) + (Ang[1,5] * Sq[2,4] * Ang[3,5] * Sq[5,6]) / (Sq[1,5] * Ang[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Ang[1,3] * Sq[2,4] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (s[1,2] * Ang[1,3] * Sq[2,4] * Ang[2,5]) 
/ (Sq[1,5] * Ang[1,6] * Ang[2,6]) - (s[1,2] * Ang[1,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) - (Sq[1,2] * Ang[1,3] * Ang[1,5] * Sq[2,6] * Sq[4,5]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (Sq[1,2] * Ang[1,3] * Sq[2,6] * Sq[4,6]) / (Sq[1,5] * Sq[2,5]) + (Ang[1,3] * Sq[1,6] * Sq[2,4] * Ang[2,5]) / (Sq[1,5] * Ang[2,6]) - (Ang[1,3] * Sq[1,6] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[2,6])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,5]**2 * Sq[2,4] * Ang[3,5]) / (Ang[1,6] 
* Ang[5,6]) + (Ang[1,5]**2 * Sq[1,6] * Sq[2,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) - (Ang[1,5]**2 * Sq[1,6] * Sq[2,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Ang[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Sq[1,2] * Ang[1,3] * Ang[1,5] * Sq[2,4] * Ang[2,5]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Sq[1,2] * Ang[1,3] * Ang[1,5] * Sq[4,6]) / (Sq[1,5] * Ang[1,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,6] * Sq[2,4] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Ang[1,3] * Ang[1,5] * Sq[1,6] 
* Sq[2,6] * Sq[4,5]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Ang[1,3] * Ang[1,6] * Sq[1,6] * Sq[2,6] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) - (Ang[1,3] * Ang[1,5] * Sq[1,6] * Sq[2,5] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6])) - const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Ang[1,3] * Ang[1,5] * Sq[1,6] * Sq[2,4]) / (Sq[1,5] * Ang[1,6]) - const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Ang[1,3] * Ang[1,5] * Sq[1,6] 
* Sq[2,4]) / (Sq[1,5] * Ang[1,6])) * GlobFac_3 * (const.vev/2 * const.C4)

    MRRRLLL_3 = n_loop_factor * const.Cf * ( 4 * const.Cf * ((Ang[1,2] * Sq[2,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + (Ang[3,6] * Sq[4,5]) / (Sq[1,6] * Ang[2,5])) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,3] * Sq[1,5] * Ang[1,6] * Sq[2,4]) / (Ang[1,5] * Sq[1,6]) - (Ang[1,6] * Sq[2,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Ang[1,3] * Sq[2,4] * Ang[2,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,5]) + (s[1,2] * Ang[1,3] * Sq[4,5] * Ang[5,6]) / (Ang[1,5] * Sq[1,6] 
* Sq[2,5]) + (s[1,2] * Ang[1,3] * Sq[2,4] * Sq[2,5]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + (Ang[1,3] * Sq[1,5] * Sq[2,4] * Ang[2,6]) / (Sq[1,6] * Ang[2,5]) + (Ang[1,3] * Sq[1,5] * Sq[4,5] * Ang[5,6]) / (Sq[1,6] * Ang[2,5]) - (Sq[1,2] * Ang[1,3] * Sq[2,5] * Sq[4,5]) / (Sq[1,6] * Sq[2,6]) - (Sq[1,2] * Ang[1,3] * Ang[1,6] * Sq[2,5] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,6])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,5] * Ang[1,6]**2 * Sq[2,4] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] 
* Ang[5,6]) + (Ang[1,6]**2 * Sq[2,4] * Ang[3,6]) / (Ang[1,5] * Ang[5,6]) - (Sq[1,5] * Ang[1,6] * Sq[2,4] * Ang[3,6]) / (Sq[1,6] * Ang[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Ang[1,3] * Ang[1,6] * Sq[4,5]) / (Ang[1,5] * Sq[1,6]) - (Sq[1,2] * Ang[1,3] * Ang[1,6] * Sq[2,4] * Ang[2,6]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,5] * Sq[2,4] * Sq[2,5]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) + (Ang[1,3] * Sq[1,5] * Sq[2,5] * Sq[4,5]) / (Sq[1,6] * Sq[5,6])) 
- const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Ang[1,3] * Sq[1,5] * Ang[1,6] * Sq[2,4]) / (Ang[1,5] * Sq[1,6]) - const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (2 * s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Ang[1,3] * Sq[1,5] * Ang[1,6] * Sq[2,4]) / (Ang[1,5] * Sq[1,6])) * GlobFac_3 * (const.vev/2 * const.C4)

    MRRRRLL_3 = n_loop_factor * 2 * const.Cf * ( - 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2]**2 * Ang[1,3] * Sq[2,4] * Sq[2,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) + (Ang[1,2]**2 * Ang[1,3] * Sq[2,4] * Sq[2,5]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Ang[1,3] * Sq[2,6] * Sq[4,5]) / (Ang[1,6] * Ang[2,5]) + (Ang[1,2] * Ang[1,3] * Sq[2,5] * Sq[4,5]) / (Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Ang[1,3] * Sq[2,6] * Sq[4,6]) / (Ang[1,5] * Ang[2,5]) + (Ang[1,2] * Ang[1,3] * Sq[2,5] * Sq[4,6]) / (Ang[1,5] * Ang[2,6]) 
+ (Ang[1,2] * Ang[1,3] * Sq[2,4] * Sq[5,6]) / (Ang[1,5] * Ang[2,6]) - (Ang[1,2] * Ang[1,3] * Sq[2,4] * Sq[5,6]) / (Ang[1,6] * Ang[2,5]) + (Ang[1,3] * Sq[4,5] * Sq[5,6]) / (Ang[2,6]) - (Ang[1,3] * Sq[4,6] * Sq[5,6]) / (Ang[2,5]) + (Ang[1,3] * Ang[1,6] * Sq[4,6] * Sq[5,6]) / (Ang[1,5] * Ang[2,6]) - (Ang[1,3] * Ang[1,5] * Sq[4,5] * Sq[5,6]) / (Ang[1,6] * Ang[2,5])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Ang[1,3] * Sq[2,4] * Sq[2,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] 
* Sq[2,4] * Sq[2,6]) / (Ang[1,5] * Ang[5,6]) + (Ang[1,3] * Sq[2,5] * Sq[4,6]) / (Ang[5,6]) + (Ang[1,3] * Sq[2,6] * Sq[4,5]) / (Ang[5,6]) + (Ang[1,3] * Sq[2,5] * Ang[1,5] * Sq[4,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,3] * Ang[1,6] * Sq[2,6] * Sq[4,6]) / (Ang[1,5] * Ang[5,6]))) * GlobFac_3 * (const.vev/2 * const.C4)

    
    # 4-point amplitudes
    MLRLLLL_4 = n_loop_factor * 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( const.Nc * ((Sq[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,6]) / (Sq[1,5] * Sq[5,6]) + (Sq[1,2] * Sq[1,4] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Sq[1,5] * Sq[5,6]) - (Sq[1,2] * Sq[1,4] * Ang[3,4] * Sq[4,6] * Ang[5,6]) / (Sq[5,6] * Sq[1,6])) - 2 * const.Cf * ((Sq[1,2]**2 * Sq[1,4] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Sq[1,5] * Sq[2,5] * Sq[1,6]) - (Sq[1,2]**2 * Sq[1,4] * Ang[3,4] 
* Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2]**2 * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2]**2 * Sq[1,4] * Sq[2,4] * Ang[3,4] * Ang[2,6]) / (Sq[1,5] * Sq[2,5] * Sq[1,6]))) * GlobFac_4 * const.C1

    MLRLRLL_4 = n_loop_factor * 2 * 2 * const.Cf * ( 4 * const.Cf * (Sq[1,2] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,4] * Sq[2,4] * Ang[1,5] * Sq[1,6] * Ang[3,4]) / (Sq[1,5] * Ang[1,6]) - (Sq[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Sq[2,4] * Sq[2,6] * Ang[3,4]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (Sq[1,2] * Sq[1,4] * Ang[1,5] * Sq[2,6] * Ang[3,4] * Sq[4,5]) 
/ (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (Sq[1,2] * Sq[1,4] * Sq[2,6] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Sq[2,5])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Sq[2,4] * Ang[2,5] * Ang[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) - (s[1,2] * Sq[1,4] * Ang[3,4] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) - (Sq[1,4] * Sq[1,6] * Sq[2,4] * Ang[2,5] * Ang[3,4]) / (Sq[1,5] * Ang[2,6]) + (Sq[1,4] * Sq[1,6] * Ang[3,4] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[2,6])) + 4 * const.Cf 
* 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,5] * Sq[1,6]**2 * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Sq[1,6]**2 * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Sq[5,6]) - (Ang[1,5] * Sq[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,6] * Sq[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Sq[1,4] * Ang[1,5] * Sq[2,4] * Ang[2,5] * Ang[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] * Sq[1,6] * Sq[2,4] * Sq[2,6] * Ang[3,4]) / (Sq[1,5] 
* Ang[1,6] * Sq[5,6]) - (Sq[1,2] * Sq[1,4] * Ang[1,5] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Ang[1,6]) - (Sq[1,4] * Sq[1,6] * Sq[2,6] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Sq[5,6]) - (Sq[1,4] * Ang[1,5] * Sq[1,6] * Sq[2,6] * Ang[3,4] * Sq[4,5]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) - (Sq[1,4] * Ang[1,5] * Sq[1,6] * Sq[2,5] * Ang[3,4] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6])) - const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Sq[1,4] * Ang[1,5] * Sq[1,6] 
* Sq[2,4] * Ang[3,4]) / (Sq[1,5] * Ang[1,6]) - const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Sq[1,4] * Ang[1,5] * Sq[1,6] * Sq[2,4] * Ang[3,4]) / (Sq[1,5] * Ang[1,6])) * GlobFac_4 * const.C1

    MLRRLLL_4 = n_loop_factor * 2 * const.Cf * ( - 4 * const.Cf * (Sq[1,2] * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,4] * Sq[1,5] * Ang[1,6] * Sq[2,4] * Ang[3,4]) / (Ang[1,5] * Sq[1,6]) + (Sq[1,5] * Sq[2,4] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Ang[1,5] * Sq[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Sq[2,4] * Ang[2,6] * Ang[3,4]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + (s[1,2] * Sq[1,4] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Ang[1,5] 
* Sq[1,6] * Ang[2,5]) + (s[1,2] * Sq[1,4] * Sq[2,4] * Sq[2,5] * Ang[3,4]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,4] * Sq[1,5] * Sq[2,4] * Ang[2,6] * Ang[3,4]) / (Sq[1,6] * Ang[2,5]) + (Sq[1,4] * Sq[1,5] * Ang[3,4] * Sq[4,5] * Ang[5,6]) / (Sq[1,6] * Ang[2,5]) - (Sq[1,2] * Sq[1,4] * Sq[2,5] * Ang[3,4] * Sq[4,5]) / (Sq[1,6] * Sq[2,6]) - (Sq[1,2] * Sq[1,4] * Ang[1,6] * Sq[2,5] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,6])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) 
* ((Sq[1,5]**2 * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,5]**2 * Ang[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) - (Sq[1,5]**2 * Ang[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Sq[1,4] * Sq[1,5] * Sq[2,4] * Sq[2,5] * Ang[3,4]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) - (Sq[1,4] * Sq[1,5] * Sq[2,5] * Ang[3,4] * Sq[4,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,2] * Sq[1,4] 
* Ang[1,6] * Sq[2,4] * Ang[2,6] * Ang[3,4]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) + (Sq[1,2] * Sq[1,4] * Ang[1,6] * Ang[3,4] * Sq[4,5]) / (Ang[1,5] * Sq[1,6])) - const.Nc * ((s[1,5] - s[1,6] - s[5,6])) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Sq[1,4] * Sq[1,5] * Ang[1,6] * Sq[2,4] * Ang[3,4]) / (Ang[1,5] * Sq[1,6]) - const.Nc * ((s[2,5] - s[2,6] - s[5,6])) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Sq[1,4] * Sq[1,5] * Ang[1,6] * Sq[2,4] * Ang[3,4]) / (Ang[1,5] * Sq[1,6])) * GlobFac_4 * const.C1

    MLRRRLL_4 = n_loop_factor * 4 * const.Cf * ( 2 * const.Cf * ((Ang[1,2] * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) + (Ang[3,4] * Sq[4,5] * Sq[4,6]) / (Ang[1,5] * Ang[2,6]) + (Ang[3,4] * Sq[4,5] * Sq[4,6]) / (Ang[1,6] * Ang[2,5])) + 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Ang[1,2]**2 * Sq[1,4] * Sq[2,4] * Sq[2,6] * Ang[3,4]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) - (Ang[1,2]**2 * Sq[1,4] * Sq[2,4] * Sq[2,5] * Ang[3,4]) / (Ang[1,5] 
* Ang[1,6] * Ang[2,6]) - (Ang[1,2] * Sq[1,4] * Sq[2,6] * Ang[3,4] * Sq[4,5]) / (Ang[1,6] * Ang[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[2,5] * Ang[3,4] * Sq[4,5]) / (Ang[1,6] * Ang[2,6]) - (Ang[1,2] * Sq[1,4] * Sq[2,6] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[2,5] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[2,6]) + (Ang[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Sq[5,6]) / (Ang[1,6] * Ang[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[2,4] * Ang[3,4] * Sq[5,6]) / (Ang[1,5] * Ang[2,6]) 
+ (Sq[1,4] * Ang[1,5] * Ang[3,4] * Sq[4,5] * Sq[5,6]) / (Ang[1,6] * Ang[2,5]) - (Sq[1,4] * Ang[1,6] * Ang[3,4] * Sq[4,6] * Sq[5,6]) / (Ang[1,5] * Ang[2,6]) + (Sq[1,4] * Ang[3,4] * Sq[4,6] * Sq[5,6]) / (Ang[2,5]) - (Sq[1,4] * Ang[3,4] * Sq[4,5] * Sq[5,6]) / (Ang[2,6])) + const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Ang[5,6]) + (Sq[1,5] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[5,6]) + (s[1,6] * Sq[2,4] * Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[5,6]) 
+ (s[1,5] * Sq[2,4] * Ang[3,4] * Sq[4,5]) / (Ang[1,6] * Ang[5,6])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Sq[1,4] * Sq[2,4] * Sq[2,5] * Ang[3,4]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] * Sq[2,4] * Sq[2,6] * Ang[3,4]) / (Ang[1,5] * Ang[5,6]) + (Sq[1,4] * Sq[2,5] * Ang[3,4] * Sq[4,6]) / (Ang[5,6]) + (Sq[1,4] * Sq[2,6] * Ang[3,4] * Sq[4,5]) / (Ang[5,6]) + (Sq[1,4] * Ang[1,5] * Sq[2,5] * Ang[3,4] * Sq[4,5]) / (Ang[1,6] * Ang[5,6]) + (Sq[1,4] * Ang[1,6] * Sq[2,6] 
* Ang[3,4] * Sq[4,6]) / (Ang[1,5] * Ang[5,6]))) * GlobFac_4 * const.C1

    MRLLLLL_4 = n_loop_factor * 4 * const.Cf * ( - 2 * const.Cf * ((Sq[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,5]) + (Sq[3,4] * Ang[3,5] * Ang[3,6]) / (Sq[1,5] * Sq[2,6]) + (Sq[3,4] * Ang[3,5] * Ang[3,6]) / (Sq[1,6] * Sq[2,5])) + 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[2,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,5]) + (Sq[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[2,5]) / (Sq[1,5] 
* Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,5] * Ang[2,6]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[2,5] * Ang[3,6]) / (Sq[1,5] * Sq[2,6]) + (Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[2,6] * Ang[3,6]) / (Sq[1,5] * Sq[2,5]) + (Sq[1,2] * Ang[1,3] * Sq[3,4] * Ang[2,5] * Ang[3,5]) / (Sq[1,6] * Sq[2,6]) - (Sq[1,2] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[5,6]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,2] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[5,6]) / (Sq[1,5] * Sq[2,6]) 
- (Ang[1,3] * Sq[1,5] * Sq[3,4] * Ang[3,5] * Ang[5,6]) / (Sq[1,6] * Sq[2,5]) - (Ang[1,3] * Sq[1,6] * Sq[3,4] * Ang[3,6] * Ang[5,6]) / (Sq[1,5] * Sq[2,6]) - (Ang[1,3] * Sq[3,4] * Ang[3,6] * Ang[5,6]) / (Sq[2,5]) + (Ang[1,3] * Sq[3,4] * Ang[3,5] * Ang[5,6]) / (Sq[2,6])) - const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[2,3] * Ang[1,6] * Sq[3,4] * Ang[3,5]) / (Sq[5,6]) + (Ang[2,3] * Ang[1,5] * Sq[3,4] * Ang[3,6]) / (Sq[5,6]) + (s[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Sq[5,6]) 
+ (s[1,5] * Ang[2,3] * Sq[3,4] * Ang[3,5]) / (Sq[1,6] * Sq[5,6])) - const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[2,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,2] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Ang[2,6]) / (Sq[1,5] * Sq[5,6]) + (Ang[1,3] * Sq[3,4] * Sq[1,5] * Ang[2,5] * Ang[3,5]) / (Sq[1,6] * Sq[5,6]) + (Ang[1,3] * Sq[3,4] * Sq[1,6] * Ang[2,6] * Ang[3,6]) / (Sq[1,5] * Sq[5,6]) + (Ang[1,3] * Sq[3,4] * Ang[2,5] * Ang[3,6]) / (Sq[5,6]) + (Ang[1,3] 
* Sq[3,4] * Ang[2,6] * Ang[3,5]) / (Sq[5,6]))) * GlobFac_4 * const.C2

    MRLLRLL_4 = n_loop_factor * 2 * const.Cf * ( - 4 * const.Cf * ((Ang[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,5]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) + (Sq[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (Sq[3,4] * Ang[3,5] * Ang[3,6]) / (Ang[1,6] * Sq[2,5])) - 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,3] * Ang[2,3] * Ang[1,5] * Sq[1,6] * Sq[3,4]) / (Sq[1,5] * Ang[1,6]) + (Ang[1,5] * Ang[2,3] * Sq[3,4] * Ang[3,5] * Sq[5,6]) / (Sq[1,5] * Ang[1,6])) - 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] 
* Ang[1,3] * Ang[2,3] * Sq[3,4] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (s[1,2] * Ang[1,3] * Ang[3,5] * Sq[3,4] * Sq[5,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (s[1,2] * Ang[1,3] * Ang[2,3] * Ang[2,5] * Sq[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) + (s[1,5] * Ang[1,3] * Ang[2,3] * Sq[3,4] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (s[1,5] * Ang[1,3] * Ang[3,5] * Sq[3,4] * Sq[5,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (Ang[1,2] * Ang[2,5] * Ang[1,3] * Ang[3,5] * Sq[3,4]) 
/ (Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Ang[2,5] * Sq[1,6] * Ang[1,3] * Ang[3,6] * Sq[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[2,6])) - 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,5]**2 * Ang[2,3] * Ang[3,5] * Sq[3,4]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,5]**2 * Sq[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) - (Ang[1,5]**2 * Sq[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Ang[5,6])) - 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Ang[1,3] * Ang[1,5] 
* Ang[2,3] * Ang[2,5] * Sq[3,4]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Ang[1,3] * Ang[1,5] * Ang[2,5] * Sq[3,4] * Ang[3,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,6] * Ang[2,3] * Sq[2,6] * Sq[3,4]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,6] * Sq[3,4] * Ang[3,5] * Sq[5,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6])) + const.Nc * ((s[1,5] - s[1,6] - s[5,6])) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Ang[1,3] * Ang[1,5] * Sq[1,6] * Ang[2,3] * Sq[3,4]) / (Sq[1,5] 
* Ang[1,6]) + const.Nc * ((s[2,5] - s[2,6] - s[5,6])) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Ang[1,3] * Ang[1,5] * Sq[1,6] * Ang[2,3] * Sq[3,4]) / (Sq[1,5] * Ang[1,6])) * GlobFac_4 * const.C2

    MRLRLLL_4 = n_loop_factor * 2 * const.Cf * ( - 4 * const.Cf * (Ang[1,2] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[1,6]) - (Ang[1,3] * Sq[1,5] * Ang[1,6] * Ang[2,3] * Sq[3,4]) / (Ang[1,5] * Sq[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (s[1,2] * Ang[1,3] * Ang[2,3] * Ang[2,6] * Sq[3,4]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) - (s[1,2] * Ang[1,3] * Ang[2,3] * Sq[2,5] * Sq[3,4]) 
/ (Ang[1,5] * Sq[1,6] * Sq[2,6]) - (s[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,5] * Ang[2,6] * Sq[3,4] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + (Ang[1,2] * Ang[1,3] * Sq[1,6] * Ang[2,6] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) - (Ang[1,3] * Ang[1,6] * Ang[2,3] * Sq[2,5] * Sq[3,4]) / (Ang[1,5] * Sq[2,6]) + (Ang[1,3] * Ang[1,6] * Sq[3,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[2,6])) + 2 * const.Nc * 1 
/ (s[1,5] + s[1,6] + s[5,6]) * ( - (Sq[1,5] * Ang[1,6]**2 * Ang[2,3] * Sq[3,4] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) - (Ang[1,6]**2 * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Ang[5,6]) + (Sq[1,5] * Ang[1,6] * Ang[2,3] * Sq[3,4] * Ang[3,6]) / (Sq[1,6] * Ang[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Ang[1,2] * Ang[1,3] * Sq[1,5] * Ang[2,3] * Sq[2,5] * Sq[3,4]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) - (Sq[1,2] * Ang[1,3] * Ang[1,6] * Ang[2,3] * Ang[2,6] * Sq[3,4]) / (Ang[1,5] 
* Sq[1,6] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,5] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6]) + (Ang[1,3] * Ang[1,6] * Sq[1,5] * Ang[2,5] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) - (Ang[1,3] * Sq[1,5] * Ang[1,6] * Ang[2,6] * Sq[3,4] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) - (Ang[1,3] * Ang[1,6] * Ang[2,6] * Sq[3,4] * Ang[3,6]) / (Ang[1,5] * Ang[5,6])) + const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Ang[1,3] * Sq[1,5] * Ang[1,6] 
* Ang[2,3] * Sq[3,4]) / (Ang[1,5] * Sq[1,6]) + const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Ang[1,3] * Sq[1,5] * Ang[1,6] * Ang[2,3] * Sq[3,4]) / (Ang[1,5] * Sq[1,6])) * GlobFac_4 * const.C2

    MRLRRLL_4 = n_loop_factor * 4 * const.Cf * ( 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[2,6] * Sq[3,4]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) + (Ang[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[2,5] * Sq[3,4]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) + (Ang[1,2]**2 * Ang[1,3] * Sq[3,4] * Ang[3,5] * Sq[5,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) - (Ang[1,2]**2 * Ang[1,3] * Ang[2,3] * Sq[2,5] * Sq[3,4]) / (Ang[1,5] * Ang[1,6] * Ang[2,6])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Ang[1,2] * Ang[1,3] * Ang[2,3] 
* Sq[2,5] * Sq[3,4]) / (Ang[1,6] * Ang[5,6]) - (Ang[1,2] * Ang[1,3] * Ang[2,3] * Sq[2,6] * Sq[3,4]) / (Ang[1,5] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,6] * Ang[5,6]) - (Ang[1,2] * Ang[1,3] * Sq[3,4] * Ang[3,5] * Sq[5,6]) / (Ang[1,5] * Ang[5,6]))) * GlobFac_4 * const.C2

    MLLLLLL_4 = n_loop_factor * 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( 2 * const.Cf * ((Sq[1,2]**2 * Sq[1,4] * Ang[2,3] * Ang[2,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,5]) + (Sq[1,2]**2 * Sq[1,4] * Ang[2,3] * Ang[2,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Sq[1,4] * Ang[2,6] * Ang[3,5]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,2] * Sq[1,4] * Ang[2,5] * Ang[3,5]) / (Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Sq[1,4] * Ang[2,6] * Ang[3,6]) / (Sq[1,5] * Sq[2,5]) + (Sq[1,2] * Sq[1,4] * Ang[2,5] * Ang[3,6]) / (Sq[1,5] * Sq[2,6]) + (Sq[1,2] 
* Ang[2,3] * Sq[1,4] * Ang[5,6]) / (Sq[1,5] * Sq[2,6]) - (Sq[1,2] * Ang[2,3] * Sq[1,4] * Ang[5,6]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,4] * Sq[1,6] * Ang[3,6] * Ang[5,6]) / (Sq[1,5] * Sq[2,6]) - (Sq[1,4] * Sq[1,5] * Ang[3,5] * Ang[5,6]) / (Sq[1,6] * Sq[2,5]) + (Sq[1,4] * Ang[3,5] * Ang[5,6]) / (Sq[2,6]) - (Sq[1,4] * Ang[3,6] * Ang[5,6]) / (Sq[2,5])) + const.Nc * ((Sq[1,2] * Ang[2,3] * Sq[1,4] * Ang[2,5] * Ang[5,6]) / (Sq[1,6] * Sq[5,6]) - (Sq[1,2] * Ang[2,3] * Sq[1,4] * Ang[2,6] * Ang[5,6]) 
/ (Sq[1,5] * Sq[5,6]) + (Sq[1,4] * Sq[1,5] * Ang[2,5] * Ang[3,5] * Ang[5,6]) / (Sq[1,6] * Sq[5,6]) - (Sq[1,4] * Sq[1,6] * Ang[2,6] * Ang[3,6] * Ang[5,6]) / (Sq[1,5] * Sq[5,6]) + (Sq[1,4] * Ang[2,5] * Ang[3,6] * Ang[5,6]) / (Sq[5,6]) - (Sq[1,4] * Ang[2,6] * Ang[3,5] * Ang[5,6]) / (Sq[5,6]))) * GlobFac_4 * const.C3

    MLLLRLL_4 = n_loop_factor * const.Cf * ( 4 * const.Cf * ((Sq[1,2] * Ang[2,3] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (Ang[3,5] * Sq[4,6]) / (Ang[1,6] * Sq[2,5])) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,4] * Ang[1,5] * Sq[1,6] * Ang[2,3]) / (Sq[1,5] * Ang[1,6]) - (Sq[1,6] * Ang[2,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (s[1,2] * Sq[1,4] * Ang[3,5] * Sq[5,6]) / (Sq[1,5] * Ang[1,6] 
* Sq[2,5]) + (s[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (Sq[1,4] * Ang[1,5] * Ang[2,3] * Sq[2,6]) / (Ang[1,6] * Sq[2,5]) + (Sq[1,4] * Ang[1,5] * Ang[3,5] * Sq[5,6]) / (Ang[1,6] * Sq[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[2,6] * Ang[3,5]) / (Ang[1,6] * Sq[2,5]) - (Ang[1,2] * Sq[1,4] * Sq[1,6] * Sq[2,6] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,5] * Sq[1,6] * Ang[2,3] * Sq[4,6] * Ang[5,6]) / (Ang[1,6] 
* Sq[5,6]) - (Sq[1,6]**2 * Ang[2,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Sq[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Sq[1,4] * Ang[1,5] * Ang[2,3] * Ang[2,5]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Sq[1,4] * Ang[1,5] * Ang[2,5] * Ang[3,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[2,5] * Sq[1,6] * Ang[1,5] * Ang[3,6] * Sq[1,4]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) - (Ang[2,5] * Sq[1,6] * Ang[1,5] * Ang[3,6] * Sq[1,4]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] * Sq[1,6] 
* Sq[2,6] * Ang[2,3]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Ang[1,2] * Sq[1,6] * Ang[3,5] * Sq[1,4]) / (Sq[1,5] * Ang[1,6])) - const.Nc * ((s[1,5] - s[1,6] - s[5,6])) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Sq[1,4] * Ang[1,5] * Sq[1,6] * Ang[2,3]) / (Sq[1,5] * Ang[1,6]) - const.Nc * ((s[2,5] - s[2,6] - s[5,6])) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Sq[1,4] * Ang[1,5] * Sq[1,6] * Ang[2,3]) / (Sq[1,5] * Ang[1,6])) * GlobFac_4 * const.C3

    MLLRLLL_4 = n_loop_factor * const.Cf * ( 4 * const.Cf * ((Sq[1,2] * Ang[2,3] * Sq[4,5]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + (Ang[3,6] * Sq[4,5]) / (Ang[1,5] * Sq[2,6])) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,3]) / (Ang[1,5] * Sq[1,6]) + (Sq[1,5] * Ang[2,3] * Sq[4,5] * Ang[5,6]) / (Ang[1,5] * Sq[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Sq[1,4] * Ang[2,3] * Ang[2,6]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + (s[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,5]) / (Ang[1,5] * Sq[1,6] 
* Sq[2,6]) - (s[1,2] * Sq[1,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) - (Ang[1,2] * Sq[1,4] * Sq[1,5] * Ang[2,6] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) - (Ang[1,2] * Sq[1,4] * Ang[2,6] * Ang[3,6]) / (Ang[1,5] * Ang[2,5]) + (Sq[1,4] * Ang[1,6] * Ang[2,3] * Sq[2,5]) / (Ang[1,5] * Sq[2,6]) - (Sq[1,4] * Ang[1,6] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[2,6])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,5]**2 * Ang[2,3] * Sq[4,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,5]**2 
* Ang[1,6] * Ang[2,3] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) - (Sq[1,5]**2 * Ang[1,6] * Ang[2,3] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Sq[1,5] * Sq[2,5] * Ang[2,3] * Sq[1,4]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) + (Ang[1,2] * Sq[1,4] * Sq[1,5] * Ang[3,6]) / (Ang[1,5] * Sq[1,6]) + (Sq[1,2] * Sq[1,4] * Ang[1,6] * Ang[2,3] * Ang[2,6]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) + (Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,6] * Ang[3,5]) 
/ (Ang[1,5] * Sq[1,6] * Ang[5,6]) + (Sq[1,4] * Ang[1,6] * Ang[2,6] * Ang[3,6]) / (Ang[1,5] * Ang[5,6]) - (Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,5] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[5,6])) - const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,3]) / (Ang[1,5] * Sq[1,6]) - const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Sq[1,4] * Sq[1,5] * Ang[1,6] * Ang[2,3]) / (Ang[1,5] * Sq[1,6])) * GlobFac_4 * const.C3

    MLLRRLL_4 = n_loop_factor * 2 * const.Cf * ( 2 * const.Cf * ((Ang[1,2] * Ang[2,3] * Sq[4,5]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Ang[2,3] * Sq[4,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5])) + 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Ang[1,2]**2 * Sq[1,4] * Ang[2,3] * Sq[2,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) - (Ang[1,2]**2 * Sq[1,4] * Ang[2,3] * Sq[2,5]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) - (Ang[1,2]**2 * Sq[1,4] * Ang[3,5] * Sq[5,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) + (Ang[1,2]**2 * Sq[1,4] * Ang[3,6] * Sq[5,6]) 
/ (Ang[1,5] * Ang[1,6] * Ang[2,6])) + const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,6] * Ang[2,3] * Sq[4,5]) / (Ang[1,6] * Ang[5,6]) + (Sq[1,5] * Ang[2,3] * Sq[4,6]) / (Ang[5,6]) + (s[1,6] * Ang[2,3] * Sq[4,6]) / (Ang[1,5] * Ang[5,6]) + (s[1,5] * Ang[2,3] * Sq[4,5]) / (Ang[1,6] * Ang[5,6])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] * Ang[2,3] * Sq[2,6]) / (Ang[1,5] * Ang[5,6]) + (Ang[1,2] * Sq[1,4] 
* Ang[3,5] * Sq[5,6]) / (Ang[1,5] * Ang[5,6]) - (Ang[1,2] * Sq[1,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,6] * Ang[5,6]))) * GlobFac_4 * const.C3

    MRRLLLL_4 = n_loop_factor * 2 * const.Cf * ( 2 * const.Cf * ((Sq[1,2] * Sq[2,4] * Ang[3,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2] * Sq[2,4] * Ang[3,6]) / (Sq[1,5] * Sq[1,6] * Sq[2,5])) - 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2]**2 * Ang[1,3] * Sq[2,4] * Ang[2,6]) / (Sq[1,5] * Sq[2,5] * Sq[1,6]) + (Sq[1,2]**2 * Ang[1,3] * Sq[2,4] * Ang[2,5]) / (Sq[1,5] * Sq[1,6] * Sq[2,6]) + (Sq[1,2]**2 * Ang[1,3] * Sq[4,5] * Ang[5,6]) / (Sq[1,5] * Sq[2,5] * Sq[1,6]) - (Sq[1,2]**2 * Ang[1,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] 
* Sq[1,6] * Sq[2,6])) + const.Nc * (s[1,5] + s[1,6]) / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[2,4] * Ang[3,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[2,4] * Ang[3,6]) / (Sq[1,5] * Sq[5,6])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Ang[1,3] * Sq[2,4] * Ang[2,5]) / (Sq[1,6] * Sq[5,6]) + (Sq[1,2] * Ang[1,3] * Sq[2,4] * Ang[2,6]) / (Sq[1,5] * Sq[5,6]) + (Sq[1,2] * Ang[1,3] * Sq[4,5] * Ang[5,6]) / (Sq[1,5] * Sq[5,6]) - (Sq[1,2] * Ang[1,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,6] * Sq[5,6]))) * GlobFac_4 * const.C4

    MRRLRLL_4 = n_loop_factor * const.Cf * ( 4 * const.Cf * ((Ang[1,2] * Sq[2,4] * Sq[2,6] * Ang[3,5]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) + (Sq[2,6] * Ang[3,5] * Sq[4,6]) / (Sq[1,5] * Ang[2,6])) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,3] * Ang[1,5] * Sq[1,6] * Sq[2,4]) / (Sq[1,5] * Ang[1,6]) + (Ang[1,5] * Sq[2,4] * Ang[3,5] * Sq[5,6]) / (Sq[1,5] * Ang[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Ang[1,3] * Sq[2,4] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) + (s[1,2] * Ang[1,3] * Sq[2,4] * Ang[2,5]) 
/ (Sq[1,5] * Ang[1,6] * Ang[2,6]) - (s[1,2] * Ang[1,3] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[1,6] * Ang[2,6]) - (Sq[1,2] * Ang[1,3] * Ang[1,5] * Sq[2,6] * Sq[4,5]) / (Sq[1,5] * Ang[1,6] * Sq[2,5]) - (Sq[1,2] * Ang[1,3] * Sq[2,6] * Sq[4,6]) / (Sq[1,5] * Sq[2,5]) + (Ang[1,3] * Sq[1,6] * Sq[2,4] * Ang[2,5]) / (Sq[1,5] * Ang[2,6]) - (Ang[1,3] * Sq[1,6] * Sq[4,6] * Ang[5,6]) / (Sq[1,5] * Ang[2,6])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,5]**2 * Sq[2,4] * Ang[3,5]) / (Ang[1,6] 
* Ang[5,6]) + (Ang[1,5]**2 * Sq[1,6] * Sq[2,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) - (Ang[1,5]**2 * Sq[1,6] * Sq[2,4] * Ang[3,6]) / (Sq[1,5] * Ang[1,6] * Ang[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ( - (Sq[1,2] * Ang[1,3] * Ang[1,5] * Sq[2,4] * Ang[2,5]) / (Sq[1,5] * Ang[1,6] * Ang[5,6]) + (Sq[1,2] * Ang[1,3] * Ang[1,5] * Sq[4,6]) / (Sq[1,5] * Ang[1,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,6] * Sq[2,4] * Sq[2,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Ang[1,3] * Ang[1,5] * Sq[1,6] 
* Sq[2,6] * Sq[4,5]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) + (Ang[1,3] * Ang[1,6] * Sq[1,6] * Sq[2,6] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6]) - (Ang[1,3] * Ang[1,5] * Sq[1,6] * Sq[2,5] * Sq[4,6]) / (Sq[1,5] * Ang[1,6] * Sq[5,6])) - const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Ang[1,3] * Ang[1,5] * Sq[1,6] * Sq[2,4]) / (Sq[1,5] * Ang[1,6]) - const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Ang[1,3] * Ang[1,5] * Sq[1,6] 
* Sq[2,4]) / (Sq[1,5] * Ang[1,6])) * GlobFac_4 * const.C4

    MRRRLLL_4 = n_loop_factor * const.Cf * ( 4 * const.Cf * ((Ang[1,2] * Sq[2,4] * Ang[3,6]) / (Ang[1,5] * Sq[1,6] * Ang[2,5]) + (Ang[3,6] * Sq[4,5]) / (Sq[1,6] * Ang[2,5])) + 4 * const.Cf * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Ang[1,3] * Sq[1,5] * Ang[1,6] * Sq[2,4]) / (Ang[1,5] * Sq[1,6]) - (Ang[1,6] * Sq[2,4] * Ang[3,6] * Sq[5,6]) / (Ang[1,5] * Sq[1,6])) + 4 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((s[1,2] * Ang[1,3] * Sq[2,4] * Ang[2,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,5]) + (s[1,2] * Ang[1,3] * Sq[4,5] * Ang[5,6]) / (Ang[1,5] * Sq[1,6] 
* Sq[2,5]) + (s[1,2] * Ang[1,3] * Sq[2,4] * Sq[2,5]) / (Ang[1,5] * Sq[1,6] * Sq[2,6]) + (Ang[1,3] * Sq[1,5] * Sq[2,4] * Ang[2,6]) / (Sq[1,6] * Ang[2,5]) + (Ang[1,3] * Sq[1,5] * Sq[4,5] * Ang[5,6]) / (Sq[1,6] * Ang[2,5]) - (Sq[1,2] * Ang[1,3] * Sq[2,5] * Sq[4,5]) / (Sq[1,6] * Sq[2,6]) - (Sq[1,2] * Ang[1,3] * Ang[1,6] * Sq[2,5] * Sq[4,6]) / (Ang[1,5] * Sq[1,6] * Sq[2,6])) + 2 * const.Nc * 1 / (s[1,5] + s[1,6] + s[5,6]) * ((Sq[1,5] * Ang[1,6]**2 * Sq[2,4] * Ang[3,5]) / (Ang[1,5] * Sq[1,6] 
* Ang[5,6]) + (Ang[1,6]**2 * Sq[2,4] * Ang[3,6]) / (Ang[1,5] * Ang[5,6]) - (Sq[1,5] * Ang[1,6] * Sq[2,4] * Ang[3,6]) / (Sq[1,6] * Ang[5,6])) + 2 * const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Sq[1,2] * Ang[1,3] * Ang[1,6] * Sq[4,5]) / (Ang[1,5] * Sq[1,6]) - (Sq[1,2] * Ang[1,3] * Ang[1,6] * Sq[2,4] * Ang[2,6]) / (Ang[1,5] * Sq[1,6] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] * Sq[1,5] * Sq[2,4] * Sq[2,5]) / (Ang[1,5] * Sq[1,6] * Sq[5,6]) + (Ang[1,3] * Sq[1,5] * Sq[2,5] * Sq[4,5]) / (Sq[1,6] * Sq[5,6])) 
- const.Nc * (s[1,5] - s[1,6] - s[5,6]) / (s[5,6] * (s[1,5] + s[1,6] + s[5,6])) * (Ang[1,3] * Sq[1,5] * Ang[1,6] * Sq[2,4]) / (Ang[1,5] * Sq[1,6]) - const.Nc * (s[2,5] - s[2,6] - s[5,6]) / (2 * s[5,6] * (s[2,5] + s[2,6] + s[5,6])) * (Ang[1,3] * Sq[1,5] * Ang[1,6] * Sq[2,4]) / (Ang[1,5] * Sq[1,6])) * GlobFac_4 * const.C4

    MRRRRLL_4 = n_loop_factor * 2 * const.Cf * ( - 2 * const.Cf * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2]**2 * Ang[1,3] * Sq[2,4] * Sq[2,6]) / (Ang[1,5] * Ang[1,6] * Ang[2,5]) + (Ang[1,2]**2 * Ang[1,3] * Sq[2,4] * Sq[2,5]) / (Ang[1,5] * Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Ang[1,3] * Sq[2,6] * Sq[4,5]) / (Ang[1,6] * Ang[2,5]) + (Ang[1,2] * Ang[1,3] * Sq[2,5] * Sq[4,5]) / (Ang[1,6] * Ang[2,6]) + (Ang[1,2] * Ang[1,3] * Sq[2,6] * Sq[4,6]) / (Ang[1,5] * Ang[2,5]) + (Ang[1,2] * Ang[1,3] * Sq[2,5] * Sq[4,6]) / (Ang[1,5] * Ang[2,6]) 
+ (Ang[1,2] * Ang[1,3] * Sq[2,4] * Sq[5,6]) / (Ang[1,5] * Ang[2,6]) - (Ang[1,2] * Ang[1,3] * Sq[2,4] * Sq[5,6]) / (Ang[1,6] * Ang[2,5]) + (Ang[1,3] * Sq[4,5] * Sq[5,6]) / (Ang[2,6]) - (Ang[1,3] * Sq[4,6] * Sq[5,6]) / (Ang[2,5]) + (Ang[1,3] * Ang[1,6] * Sq[4,6] * Sq[5,6]) / (Ang[1,5] * Ang[2,6]) - (Ang[1,3] * Ang[1,5] * Sq[4,5] * Sq[5,6]) / (Ang[1,6] * Ang[2,5])) + const.Nc * 1 / (s[2,5] + s[2,6] + s[5,6]) * ((Ang[1,2] * Ang[1,3] * Sq[2,4] * Sq[2,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,2] * Ang[1,3] 
* Sq[2,4] * Sq[2,6]) / (Ang[1,5] * Ang[5,6]) + (Ang[1,3] * Sq[2,5] * Sq[4,6]) / (Ang[5,6]) + (Ang[1,3] * Sq[2,6] * Sq[4,5]) / (Ang[5,6]) + (Ang[1,3] * Sq[2,5] * Ang[1,5] * Sq[4,5]) / (Ang[1,6] * Ang[5,6]) + (Ang[1,3] * Ang[1,6] * Sq[2,6] * Sq[4,6]) / (Ang[1,5] * Ang[5,6]))) * GlobFac_4 * const.C4

    # Total amplitudes
    MLRLLLL = MLRLLLL_3 + MLRLLLL_4
    MLRLRLL = MLRLRLL_3 + MLRLRLL_4
    MLRRLLL = MLRRLLL_3 + MLRRLLL_4
    MLRRRLL = MLRRRLL_3 + MLRRRLL_4
    MRLLLLL = MRLLLLL_3 + MRLLLLL_4
    MRLLRLL = MRLLRLL_3 + MRLLRLL_4
    MRLRLLL = MRLRLLL_3 + MRLRLLL_4
    MRLRRLL = MRLRRLL_3 + MRLRRLL_4    
    MLLLLLL = MLLLLLL_3 + MLLLLLL_4
    MLLLRLL = MLLLRLL_3 + MLLLRLL_4
    MLLRLLL = MLLRLLL_3 + MLLRLLL_4
    MLLRRLL = MLLRRLL_3 + MLLRRLL_4
    MRRLLLL = MRRLLLL_3 + MRRLLLL_4
    MRRLRLL = MRRLRLL_3 + MRRLRLL_4
    MRRRLLL = MRRRLLL_3 + MRRRLLL_4
    MRRRRLL = MRRRRLL_3 + MRRRRLL_4

    return MLRLLLL, MLRLRLL, MLRRLLL, MLRRRLL, MRLLLLL, MRLLRLL, MRLRLLL, MRLRRLL, MLLLLLL, MLLLRLL, MLLRLLL, MLLRRLL, MRRLLLL, MRRLRLL, MRRRLLL, MRRRRLL





# DOUBLE REAL GLUON TREE-LEVEL SQUARED AMPLITUDE

def double_real_squared_amplitude():

    spin_color_factor1 = 4 * const.Nc * const.Cf**2
    spin_color_factor2 = const.Nc * const.Cf

    # Total double-real helicity amplitudes
    MLRLLLL, MLRLRLL, MLRRLLL, MLRRRLL, MRLLLLL, MRLLRLL, MRLRLLL, MRLRRLL, MLLLLLL, MLLLRLL, MLLRLLL, MLLRRLL, MRRLLLL, MRRLRLL, MRRRLLL, MRRRRLL = double_real_amplitude()

    # Squared helicity amplitudes, including spin-color factors
    M2 = ((MLRLLLL * MLRLLLL.conjugate() + MRLRRLL * MRLRRLL.conjugate() + MLLLRLL * MLLLRLL.conjugate() + MRRRLLL * MRRRLLL.conjugate()) * (const.Nc / (4 * const.Nc - 1) * spin_color_factor1 - (1 - const.Cf**2) * spin_color_factor2)
    + (MLRRRLL * MLRRRLL.conjugate() + MRLLLLL * MRLLLLL.conjugate() + MLLRLLL * MLLRLLL.conjugate() + MRRLRLL * MRRLRLL.conjugate()) * (const.Nc / (4 * const.Nc - 1) * spin_color_factor2 - (1 - const.Cf**2) * spin_color_factor1)
    + (MLRLRLL * MLRLRLL.conjugate() + MRLRLLL * MRLRLLL.conjugate() + MLLLLLL * MLLLLLL.conjugate() + MRRRRLL * MRRRRLL.conjugate()) * (const.CA / (2 * const.Nc) * spin_color_factor1 + const.Nc * spin_color_factor2)
    + (MLRRLLL * MLRRLLL.conjugate() + MRLLRLL * MRLLRLL.conjugate() + MLLRRLL * MLLRRLL.conjugate() + MRRLLLL * MRRLLLL.conjugate()) * (const.Nc * spin_color_factor1 + const.CA / (2 * const.Nc) * spin_color_factor2)).real

    # Print result

    print("Total squared double real amplitude:")
    print("|M|^2 =", M2, "\n")





