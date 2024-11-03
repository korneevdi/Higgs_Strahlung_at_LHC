
import const
import helicities
import math, cmath
import numpy as np
from mpmath import *


# LEADING ORDER FORM FACTORS

A_leading_order_1 = 2
A_leading_order_2 = 0
A_leading_order_3 = 1

B_leading_order_1 = A_leading_order_1
B_leading_order_2 = A_leading_order_2
B_leading_order_3 = A_leading_order_3


# ONE-LOOP FORM FACTORS

A_one_loop_1 = - const.Cf * (8 + cmath.log( - const.mu2 / helicities.s[1,2]))
A_one_loop_2 = 0
A_one_loop_3 = - 4 * const.Cf

B_one_loop_1 = A_one_loop_1
B_one_loop_2 = A_one_loop_2
B_one_loop_3 = A_one_loop_3


# TWO-LOOP FORM FACTORS

A_two_loop_1 = const.Cf / 51840 * (20 * (24907 * const.CA - 43956 * const.Cf - 3862 * const.Nf - 4536 * const.beta0) + 15 * (403 * const.CA + 432 * const.Cf - 58 * const.Nf + 36 * (4 + 3 * math.pi) * const.beta0) * math.pi**2 + 9 * (-83 * const.CA + 184 * const.Cf) * math.pi**4 + 360 * (-593 * const.CA + 1002 * const.Cf + 26 * const.Nf + 6 * (14 + 3 * math.pi) * const.beta0) * zetazero(3) - 60 * (-5245 * const.CA + 12879 * const.Cf + 802 * const.Nf + 2 * (432 - 635 * math.pi) * const.beta0 + 3 * (-55 * const.CA + 54 * const.Cf + 10 * const.Nf + 18 * (-1 + 4 * math.pi) * const.beta0) * math.pi**2 + 216 * (13 * const.CA - 20 * const.Cf) * zetazero(3)) * cmath.log( - const.mu2 / helicities.s[1,2]) -180 * (-532 * const.CA + 1341  * const.Cf + 88 * const.Nf + 36 * (2 - 3 * math.pi) * const.beta0 + 12 * const.CA * math.pi**2)  * (cmath.log( - const.mu2 / helicities.s[1,2]))**2 - 720 * (-11 * const.CA + 21 * const.Cf + 2 * const.Nf + 3 * const.beta0 * (1 - 2 * math.pi)) * (cmath.log( - const.mu2 / helicities.s[1,2]))**3)
A_two_loop_2 = 0
A_two_loop_3 = const.Cf / 103680 * (5 * (134581 * const.CA - 20655 * const.Cf - 23338 * const.Nf - 20736 * const.beta0) + 45 * (49 * const.CA + 48 * const.Cf + 2 * const.Nf - 20 * (-1 + math.pi) * const.beta0) * math.pi**2 + 9 * (-93 * const.CA + 76 * const.Cf) * math.pi**4 - 360 * (467 * const.CA - 342 * const.Cf - 26 * const.Nf  + 6 * (-14 + 3 * math.pi) * const.beta0) * zetazero(3) + 6 * (- 16 * (9 + 7 * math.pi) * const.beta0 + 3 * (1 + 4 * math.pi) * math.pi**2 * const.beta0 + 48 * const.Cf * zetazero(3)) * cmath.log( - const.mu2 / helicities.s[1,2]) - 1080 * (-33  * const.CA + 54 * const.Cf + 6 * const.Nf + 9 * const.beta0 * (1 + 2 * math.pi) - 4 * const.Cf * math.pi**2) * (cmath.log( - const.mu2 / helicities.s[1,2]))**2 -720 * (-11 * const.CA + 72 * const.Cf + 2 * const.Nf + const.beta0 * (3 + 6 * math.pi)) * (cmath.log( - const.mu2 / helicities.s[1,2]))**3 - 8640 * const.Cf * (cmath.log( - const.mu2 / helicities.s[1,2]))**4)

B_two_loop_1 = A_two_loop_1
B_two_loop_2 = A_two_loop_2
B_two_loop_3 = A_two_loop_3


# SINGLE REAL GLUON TREE LEVEL FORM FACTORS

# SINGLE REAL GLUON ONE-LOOP (VIRTUAL-REAL) FORM FACTORS
