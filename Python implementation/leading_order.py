
import math, cmath
import numpy as np
import const
import helicities
import form_factor



# HELICITY AMPLITUDES

# Helicity order: M(quark, antiquark, lepton, antilepton)

# 3-point amplitudes
MLRLL_3 = (form_factor.B_leading_order_1 - helicities.s[1,2] / 2 * form_factor.B_leading_order_2) * helicities.Sq[1,2] * (helicities.Ang[3,1] * helicities.Sq[1,4] - helicities.Ang[3,2] * helicities.Sq[2,4]) * helicities.GlobFac_3 * (const.vev/2 * const.C1)
MRLLL_3 = (form_factor.B_leading_order_1 - helicities.s[1,2] / 2 * form_factor.B_leading_order_2) * helicities.Ang[1,2] * (helicities.Ang[3,1] * helicities.Sq[1,4] - helicities.Ang[3,2] * helicities.Sq[2,4]) * helicities.GlobFac_3 * (const.vev/2 * const.C2)
MLLLL_3 = form_factor.B_leading_order_3 * helicities.Ang[2,3] * helicities.Sq[4,1] * helicities.GlobFac_3 * (const.S3 + const.vev/2 * const.C3)
MRRLL_3 = form_factor.B_leading_order_3 * helicities.Ang[3,1] * helicities.Sq[2,4] * helicities.GlobFac_3 * (const.vev/2 * const.C4)

# 4-point amplitudes
MLRLL_4 = ( 2 * form_factor.A_leading_order_1 * helicities.Sq[4,1] * helicities.Sq[2,4] * helicities.Ang[3,4] + form_factor.A_leading_order_2 * (helicities.s[2,3] + helicities.s[2,4]) / 2 * helicities.Sq[1,2] * helicities.Ang[1,3] * helicities.Sq[1,4] + form_factor.A_leading_order_2 * (- helicities.s[1,3] - helicities.s[1,4]) / 2 * helicities.Sq[1,2] * helicities.Ang[2,3] * helicities.Sq[2,4]) * helicities.GlobFac_4 * const.C1
MRLLL_4 = ( 2 * form_factor.A_leading_order_1 * helicities.Ang[1,3] * helicities.Ang[2,3] * helicities.Sq[3,4] + form_factor.A_leading_order_2 * (helicities.s[2,3] + helicities.s[2,4]) / 2 * helicities.Ang[1,2] * helicities.Ang[1,3] * helicities.Sq[1,4] + form_factor.A_leading_order_2 * (- helicities.s[1,3] - helicities.s[1,4]) / 2 * helicities.Ang[1,2] * helicities.Ang[1,3] * helicities.Sq[2,4]) * helicities.GlobFac_4 * const.C2
MLLLL_4 = form_factor.A_leading_order_3 * helicities.Ang[2,3] * helicities.Sq[4,1] * helicities.GlobFac_4 * const.C3
MRRLL_4 = form_factor.A_leading_order_3 * helicities.Ang[3,1] * helicities.Sq[2,4] * helicities.GlobFac_4 * const.C4



# SQUARED HELICITY AMPLITUDES

spin_color_factor = const.Nc / (4 * const.Nc**2)

M2LRLL = (MLRLL_3 * MLRLL_3.conjugate() + MLRLL_4 * MLRLL_4.conjugate() + (2 * MLRLL_3 * MLRLL_4).real) * spin_color_factor
M2RLLL = (MRLLL_3 * MRLLL_3.conjugate() + MRLLL_4 * MRLLL_4.conjugate() + (2 * MRLLL_3 * MRLLL_4).real) * spin_color_factor
M2LLLL = (MLLLL_3 * MLLLL_3.conjugate() + MLLLL_4 * MLLLL_4.conjugate() + (2 * MLLLL_3 * MLLLL_4).real) * spin_color_factor
M2RRLL = (MRRLL_3 * MRRLL_3.conjugate() + MRRLL_4 * MRRLL_4.conjugate() + (2 * MRRLL_3 * MRRLL_4).real) * spin_color_factor



# TOTAL HELICITY AMPLITUDE

M2 = M2LRLL.real + M2RLLL.real + M2LLLL.real + M2RRLL.real



# COMPARISON AGAINST OpenLoops

# OpenLoops results for squared amplitude
OpenLoopsResTree = 3.4729976354737612E-011

print("Total tree-level squared amplitude:")
print("|M_tree|^2 = ", M2, " (Dmitrii)")
print("|M_tree|^2 = ", OpenLoopsResTree, " (OpenLoops & MadGraph)")
print("ratio Dmitrii/OpenLoops: ", M2 / OpenLoopsResTree)




