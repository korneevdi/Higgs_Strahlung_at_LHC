
import math
import numpy as np
import random
from decimal import Decimal, getcontext, ROUND_DOWN
from scipy.optimize import root

import const



precise = const.precise                     # Number of digits after the point for momenta
precise_sq = const.precise_sq               # Number of digits after the point for squared momenta

mH = Decimal(const.mH)                      # Higgs mass
mW = Decimal(const.mW)                      # W boson mass
sqrt_s_min = Decimal(const.sqrt_s_min)      # Center-of-mass energy minimum
sqrt_s_max = Decimal(const.sqrt_s_max)      # Center-of-mass energy maximum



def generate_random(a, b):
    # Set precision to precise + 5 digits to ensure accuracy of calculations
    getcontext().prec = precise + 5  

    # Convert input values ​​to Decimal
    a = Decimal(a)
    b = Decimal(b)

    # Generate a random number in the range [0, 1] and scale it to [a, b]
    random_fraction = Decimal(random.random())
    random_decimal = a + (b - a) * random_fraction

    # Trim to "precise" digits with rounding down
    result = random_decimal.quantize(Decimal('1.' + '0' * precise), rounding=ROUND_DOWN)

    return result



def check_sqrt_s_validity(sqrt_s):
    if sqrt_s < sqrt_s_min or sqrt_s > sqrt_s_max:
        # If the center-of-mass energy is too low, throw an exception
        raise ValueError("Invalid center-of-mass energy. It must be between mW + mH and 20.000 GeV.")



def phase_space_generate_3(sqrt_s):

    # Check validity of sqrt_s
    check_sqrt_s_validity(sqrt_s)

    print("\n\nPHASE-SPACE GENERATION: 3 outgoing particles\n")
    
    iteration = 1

    while True:

        # Generate 0-th momenta components
        PH0 = generate_random(mH, sqrt_s)
        P40 = generate_random(0, sqrt_s - PH0)
        P30 = sqrt_s - PH0 - P40

        # Generate 1-st momenta components
        PH1 = generate_random(-math.sqrt(PH0**2 - mH**2), math.sqrt(PH0**2 - mH**2))
        P41 = generate_random(-P40, P40)
        P31 = - PH1 - P41

        # Check compatibility of the 0-th and the 1-st components
        if P31**2 < P30**2 and P41**2 < P40**2 and PH1**2 < (PH0**2 - mH**2):

            # Generate all Higgs momentum components
            PH2 = generate_random(-math.sqrt(PH0**2 - PH1**2 - mH**2), math.sqrt(PH0**2 - PH1**2 - mH**2))
            PH3 = (PH0**2 - PH1**2 - PH2**2 - mH**2).sqrt() * Decimal(random.choice([-1, 1]))
            PH3 = PH3.quantize(Decimal('1.' + '0' * precise))

            # Generate all the rest components of lepton and antilepton
            # Define a set of equations working with float type
            def equations(variables):
                P32, P42, P33, P43 = variables  # Unknown variavles
                return [
                    P32 + P42 + float(PH2),  # Equation 1
                    P33 + P43 + float(PH3),  # Equation 2
                    P32**2 + P33**2 - (float(P30**2) - float(P31**2)),  # Equation 3
                    P42**2 + P43**2 - (float(P40**2) - float(P41**2))   # Equation 4
                ]

            # Initial approximation for finding a solution
            initial_guess = [1.0, 1.0, 1.0, 1.0]

            # Solving the system
            solution = root(equations, initial_guess, method='hybr')

            # Check the result
            if solution.success:
                # Convert the solution back to Decimal with rounding to "precise" digits
                P32, P42, P33, P43 = [Decimal(x).quantize(Decimal('1.' + '0' * precise)) for x in solution.x]

                P3_square = P30**2 - P31**2 - P32**2 - P33**2
                P3_square = P3_square.quantize(Decimal('1.' + '0' * precise_sq))
                P4_square = P40**2 - P41**2 - P42**2 - P43**2
                P4_square = P4_square.quantize(Decimal('1.' + '0' * precise_sq))

                if P3_square == 0 and P4_square == 0:
                    print("Iteration:", iteration)
                    print("SUCCESS!")
                    break
                else:
                    iteration += 1
            else:
                iteration += 1
        else:
            iteration += 1

    # Generate the incoming particle momenta as numpy arrays
    p1 = np.array([Decimal(sqrt_s / 2), Decimal(0.0), Decimal(0.0), Decimal(sqrt_s / 2)]) # quark
    p2 = np.array([Decimal(sqrt_s / 2), Decimal(0.0), Decimal(0.0), Decimal(-sqrt_s / 2)]) # antiquark
    p3 = np.array([P30, P31, P32, P33]) # lepton
    p4 = np.array([P40, P41, P42, P43]) # antilepton
    pH = np.array([PH0, PH1, PH2, PH3]) # Higgs

    # Check the momentum conservation law: p1 + p2 = p3 + p4 + pH
    P0 = p1[0] + p2[0] - p3[0] - p4[0] - pH[0]
    P0 = P0.quantize(Decimal('1.' + '0' * precise_sq))
    P1 = p1[1] + p2[1] - p3[1] - p4[1] - pH[1]
    P1 = P1.quantize(Decimal('1.' + '0' * precise_sq))
    P2 = p1[2] + p2[2] - p3[2] - p4[2] - pH[2]
    P2 = P2.quantize(Decimal('1.' + '0' * precise_sq))
    P3 = p1[3] + p2[3] - p3[3] - p4[3] - pH[3]
    P3 = P3.quantize(Decimal('1.' + '0' * precise_sq))

    print("\nMomentum conservation law:")
    print("p1[0] + p2[0] - p3[0] - p4[0] - pH[0] =", P0)
    print("p1[1] + p2[1] - p3[1] - p4[1] - pH[1] =", P1)
    print("p1[2] + p2[2] - p3[2] - p4[2] - pH[2] =", P2)
    print("p1[3] + p2[3] - p3[3] - p4[3] - pH[3] =", P3)

    # Check squared momenta: p1^2 = 0, p2^2 = 0, p3^2 = 0, p4^2 = 0, pH^2 = mH^2
    p1sq = p1[0]**2 - p1[1]**2 - p1[2]**2 - p1[3]**2
    p1sq = p1sq.quantize(Decimal('1.' + '0' * precise_sq))
    p2sq = p2[0]**2 - p2[1]**2 - p2[2]**2 - p2[3]**2
    p2sq = p2sq.quantize(Decimal('1.' + '0' * precise_sq))
    p3sq = p3[0]**2 - p3[1]**2 - p3[2]**2 - p3[3]**2
    p3sq = p3sq.quantize(Decimal('1.' + '0' * precise_sq))
    p4sq = p4[0]**2 - p4[1]**2 - p4[2]**2 - p4[3]**2
    p4sq = p4sq.quantize(Decimal('1.' + '0' * precise_sq))
    pHsq = pH[0]**2 - pH[1]**2 - pH[2]**2 - pH[3]**2
    pHsq = pHsq.quantize(Decimal('1.' + '0' * precise_sq))

    print("\nSquared momenta:")
    print("p1^2 = ", p1sq)
    print("p2^2 = ", p2sq)
    print("p3^2 = ", p3sq)
    print("p4^2 = ", p4sq)
    print("pH^2 = ", pHsq)
    print("mH^2 = ", mH**2)

    # Convert to a float array for simpler work
    p1 = p1.astype(float)
    p2 = p2.astype(float)
    p3 = p3.astype(float)
    p4 = p4.astype(float)
    pH = pH.astype(float)

    print("\nPhase-space:")
    print(f"p1 = [{p1[0]}, {p1[1]}, {p1[2]}, {p1[3]}] (quark)")
    print(f"p2 = [{p2[0]}, {p2[1]}, {p2[2]}, {p2[3]}] (antiquark)")
    print(f"p3 = [{p3[0]}, {p3[1]}, {p3[2]}, {p3[3]}] (lepton)")
    print(f"p4 = [{p4[0]}, {p4[1]}, {p4[2]}, {p4[3]}] (antilepton)")
    print(f"pH = [{pH[0]}, {pH[1]}, {pH[2]}, {pH[3]}] (Higgs)")

    # Create a matrix of momenta
    p = np.column_stack((np.zeros(4), p1, p2, p3, p4))

    return p



def phase_space_generate_4(sqrt_s):

    # Check validity of sqrt_s
    check_sqrt_s_validity(sqrt_s)

    print("\n\n\nPHASE-SPACE GENERATION: 4 outgoing particles\n")
    
    iteration = 1

    while True:

        # Generate 0-th momenta components
        PH0 = generate_random(mH, sqrt_s)
        P50 = generate_random(0, sqrt_s - PH0)
        P40 = generate_random(0, sqrt_s - PH0 - P50)
        P30 = sqrt_s - PH0 - P50 - P40

        # Generate 1-st momenta components
        PH1 = generate_random(-math.sqrt(PH0**2 - mH**2), math.sqrt(PH0**2 - mH**2))
        P51 = generate_random(-P50, P50)
        P41 = generate_random(-P40, P40)
        P31 = - PH1 - P51 - P41

        # Check compatibility of the 0-th and the 1-st components
        if P31**2 < P30**2 and P41**2 < P40**2 and P51**2 < P50**2 and PH1**2 < (PH0**2 - mH**2):

            # Generate all Higgs momentum components
            PH2 = generate_random(-math.sqrt(PH0**2 - PH1**2 - mH**2), math.sqrt(PH0**2 - PH1**2 - mH**2))
            PH3 = (PH0**2 - PH1**2 - PH2**2 - mH**2).sqrt() * Decimal(random.choice([-1, 1]))
            PH3 = PH3.quantize(Decimal('1.' + '0' * precise))

            # Generate all gluon momentum components
            P52 = generate_random(-math.sqrt(P50**2 - P51**2), math.sqrt(P50**2 - P51**2))
            P53 = (P50**2 - P51**2 - P52**2).sqrt() * Decimal(random.choice([-1, 1]))
            P53 = P53.quantize(Decimal('1.' + '0' * precise))

            # Generate all the rest components of lepton and antilepton
            # Define a set of equations working with float type
            def equations(variables):
                P32, P42, P33, P43 = variables  # Unknown variavles
                return [
                    P32 + P42 + float(PH2) + float(P52),  # Equation 1
                    P33 + P43 + float(PH3) + float(P53),  # Equation 2
                    P32**2 + P33**2 - (float(P30**2) - float(P31**2)),  # Equation 3
                    P42**2 + P43**2 - (float(P40**2) - float(P41**2))   # Equation 4
                ]

            # Initial approximation for finding a solution
            initial_guess = [1.0, 1.0, 1.0, 1.0]

            # Solving the system
            solution = root(equations, initial_guess, method='hybr')

            # Check the result
            if solution.success:
                # Convert the solution back to Decimal with rounding to "precise" digits
                P32, P42, P33, P43 = [Decimal(x).quantize(Decimal('1.' + '0' * precise)) for x in solution.x]

                P3_square = P30**2 - P31**2 - P32**2 - P33**2
                P3_square = P3_square.quantize(Decimal('1.' + '0' * precise_sq))
                P4_square = P40**2 - P41**2 - P42**2 - P43**2
                P4_square = P4_square.quantize(Decimal('1.' + '0' * precise_sq))
                P5_square = P50**2 - P51**2 - P52**2 - P53**2
                P5_square = P5_square.quantize(Decimal('1.' + '0' * precise_sq))

                if P3_square == 0 and P4_square == 0 and P5_square == 0:
                    print("Iteration:", iteration)
                    print("SUCCESS!")
                    break
                else:
                    iteration += 1
            else:
                iteration += 1
        else:
            iteration += 1

    # Generate the incoming particle momenta as numpy arrays
    p1 = np.array([Decimal(sqrt_s / 2), Decimal(0.0), Decimal(0.0), Decimal(sqrt_s / 2)]) # quark
    p2 = np.array([Decimal(sqrt_s / 2), Decimal(0.0), Decimal(0.0), Decimal(-sqrt_s / 2)]) # antiquark
    p3 = np.array([P30, P31, P32, P33]) # lepton
    p4 = np.array([P40, P41, P42, P43]) # antilepton
    p5 = np.array([P50, P51, P52, P53]) # gluon
    pH = np.array([PH0, PH1, PH2, PH3]) # Higgs

    # Check the momentum conservation law: p1 + p2 = p3 + p4 + p5 + pH
    P0 = p1[0] + p2[0] - p3[0] - p4[0] - p5[0] - pH[0]
    P0 = P0.quantize(Decimal('1.' + '0' * precise_sq))
    P1 = p1[1] + p2[1] - p3[1] - p4[1] - p5[1] - pH[1]
    P1 = P1.quantize(Decimal('1.' + '0' * precise_sq))
    P2 = p1[2] + p2[2] - p3[2] - p4[2] - p5[2] - pH[2]
    P2 = P2.quantize(Decimal('1.' + '0' * precise_sq))
    P3 = p1[3] + p2[3] - p3[3] - p4[3] - p5[3] - pH[3]
    P3 = P3.quantize(Decimal('1.' + '0' * precise_sq))

    print("\nMomentum conservation law:")
    print("p1[0] + p2[0] - p3[0] - p4[0] - p5[0] - pH[0] =", P0)
    print("p1[1] + p2[1] - p3[1] - p4[1] - p5[1] - pH[1] =", P1)
    print("p1[2] + p2[2] - p3[2] - p4[2] - p5[2] - pH[2] =", P2)
    print("p1[3] + p2[3] - p3[3] - p4[3] - p5[3] - pH[3] =", P3)

    # Check squared momenta: p1^2 = 0, p2^2 = 0, p3^2 = 0, p4^2 = 0, p5^2 = 0, pH^2 = mH^2
    p1sq = p1[0]**2 - p1[1]**2 - p1[2]**2 - p1[3]**2
    p1sq = p1sq.quantize(Decimal('1.' + '0' * precise_sq))
    p2sq = p2[0]**2 - p2[1]**2 - p2[2]**2 - p2[3]**2
    p2sq = p2sq.quantize(Decimal('1.' + '0' * precise_sq))
    p3sq = p3[0]**2 - p3[1]**2 - p3[2]**2 - p3[3]**2
    p3sq = p3sq.quantize(Decimal('1.' + '0' * precise_sq))
    p4sq = p4[0]**2 - p4[1]**2 - p4[2]**2 - p4[3]**2
    p4sq = p4sq.quantize(Decimal('1.' + '0' * precise_sq))
    p5sq = p5[0]**2 - p5[1]**2 - p5[2]**2 - p5[3]**2
    p5sq = p5sq.quantize(Decimal('1.' + '0' * precise_sq))
    pHsq = pH[0]**2 - pH[1]**2 - pH[2]**2 - pH[3]**2
    pHsq = pHsq.quantize(Decimal('1.' + '0' * precise_sq))

    print("\nSquared momenta:")
    print("p1^2 = ", p1sq)
    print("p2^2 = ", p2sq)
    print("p3^2 = ", p3sq)
    print("p4^2 = ", p4sq)
    print("p5^2 = ", p5sq)
    print("pH^2 = ", pHsq)
    print("mH^2 = ", mH**2)

    # Convert to a float array for simpler work
    p1 = p1.astype(float)
    p2 = p2.astype(float)
    p3 = p3.astype(float)
    p4 = p4.astype(float)
    p5 = p5.astype(float)
    pH = pH.astype(float)

    print("\nPhase-space:")
    print(f"p1 = [{p1[0]}, {p1[1]}, {p1[2]}, {p1[3]}] (quark)")
    print(f"p2 = [{p2[0]}, {p2[1]}, {p2[2]}, {p2[3]}] (antiquark)")
    print(f"p3 = [{p3[0]}, {p3[1]}, {p3[2]}, {p3[3]}] (lepton)")
    print(f"p4 = [{p4[0]}, {p4[1]}, {p4[2]}, {p4[3]}] (antilepton)")
    print(f"p5 = [{p5[0]}, {p5[1]}, {p5[2]}, {p5[3]}] (gluon)")
    print(f"pH = [{pH[0]}, {pH[1]}, {pH[2]}, {pH[3]}] (Higgs)")

    # Create a matrix of momenta
    p = np.column_stack((np.zeros(4), p1, p2, p3, p4, p5))

    return p



def phase_space_generate_5(sqrt_s):

    # Check validity of sqrt_s
    check_sqrt_s_validity(sqrt_s)

    print("\n\n\nPHASE-SPACE GENERATION: 5 outgoing particles\n")
    
    iteration = 1

    while True:

        # Generate 0-th momenta components
        PH0 = generate_random(mH, sqrt_s)
        P60 = generate_random(0, sqrt_s - PH0)
        P50 = generate_random(0, sqrt_s - PH0 - P60)
        P40 = generate_random(0, sqrt_s - PH0 - P60 - P50)
        P30 = sqrt_s - PH0 - P60 - P50 - P40

        # Generate 1-st momenta components
        PH1 = generate_random(-math.sqrt(PH0**2 - mH**2), math.sqrt(PH0**2 - mH**2))
        P61 = generate_random(-P60, P60)
        P51 = generate_random(-P50, P50)
        P41 = generate_random(-P40, P40)
        P31 = - PH1 - P61 - P51 - P41

        # Check compatibility of the 0-th and the 1-st components
        if P31**2 < P30**2 and P41**2 < P40**2 and P51**2 < P50**2 and P61**2 < P60**2 and PH1**2 < (PH0**2 - mH**2):

            # Generate all Higgs momentum components
            PH2 = generate_random(-math.sqrt(PH0**2 - PH1**2 - mH**2), math.sqrt(PH0**2 - PH1**2 - mH**2))
            PH3 = (PH0**2 - PH1**2 - PH2**2 - mH**2).sqrt() * Decimal(random.choice([-1, 1]))
            PH3 = PH3.quantize(Decimal('1.' + '0' * precise))

            # Generate all gluon_6 momentum components
            P62 = generate_random(-math.sqrt(P60**2 - P61**2), math.sqrt(P60**2 - P61**2))
            P63 = (P60**2 - P61**2 - P62**2).sqrt() * Decimal(random.choice([-1, 1]))
            P63 = P63.quantize(Decimal('1.' + '0' * precise))

            # Generate all gluon_5 momentum components
            P52 = generate_random(-math.sqrt(P50**2 - P51**2), math.sqrt(P50**2 - P51**2))
            P53 = (P50**2 - P51**2 - P52**2).sqrt() * Decimal(random.choice([-1, 1]))
            P53 = P53.quantize(Decimal('1.' + '0' * precise))

            # Generate all the rest components of lepton and antilepton
            # Define a set of equations working with float type
            def equations(variables):
                P32, P42, P33, P43 = variables  # Unknown variavles
                return [
                    P32 + P42 + float(PH2) + float(P52) + float(P62),  # Equation 1
                    P33 + P43 + float(PH3) + float(P53) + float(P63),  # Equation 2
                    P32**2 + P33**2 - (float(P30**2) - float(P31**2)),  # Equation 3
                    P42**2 + P43**2 - (float(P40**2) - float(P41**2))   # Equation 4
                ]

            # Initial approximation for finding a solution
            initial_guess = [1.0, 1.0, 1.0, 1.0]

            # Solving the system
            solution = root(equations, initial_guess, method='hybr')

            # Check the result
            if solution.success:
                # Convert the solution back to Decimal with rounding to "precise" digits
                P32, P42, P33, P43 = [Decimal(x).quantize(Decimal('1.' + '0' * precise)) for x in solution.x]

                P3_square = P30**2 - P31**2 - P32**2 - P33**2
                P3_square = P3_square.quantize(Decimal('1.' + '0' * precise_sq))
                P4_square = P40**2 - P41**2 - P42**2 - P43**2
                P4_square = P4_square.quantize(Decimal('1.' + '0' * precise_sq))
                P5_square = P50**2 - P51**2 - P52**2 - P53**2
                P5_square = P5_square.quantize(Decimal('1.' + '0' * precise_sq))
                P6_square = P60**2 - P61**2 - P62**2 - P63**2
                P6_square = P6_square.quantize(Decimal('1.' + '0' * precise_sq))

                if P3_square == 0 and P4_square == 0 and P5_square == 0 and P6_square == 0:
                    print("Iteration:", iteration)
                    print("SUCCESS!")
                    break
                else:
                    iteration += 1
            else:
                iteration += 1
        else:
            iteration += 1

    # Generate the incoming particle momenta as numpy arrays
    p1 = np.array([Decimal(sqrt_s / 2), Decimal(0.0), Decimal(0.0), Decimal(sqrt_s / 2)]) # quark
    p2 = np.array([Decimal(sqrt_s / 2), Decimal(0.0), Decimal(0.0), Decimal(-sqrt_s / 2)]) # antiquark
    p3 = np.array([P30, P31, P32, P33]) # lepton
    p4 = np.array([P40, P41, P42, P43]) # antilepton
    p5 = np.array([P50, P51, P52, P53]) # gluon_5
    p6 = np.array([P60, P61, P62, P63]) # gluon_5
    pH = np.array([PH0, PH1, PH2, PH3]) # Higgs

    # Check the momentum conservation law: p1 + p2 = p3 + p4 + p5 + p6 + pH
    P0 = p1[0] + p2[0] - p3[0] - p4[0] - p5[0] - p6[0] - pH[0]
    P0 = P0.quantize(Decimal('1.' + '0' * precise_sq))
    P1 = p1[1] + p2[1] - p3[1] - p4[1] - p5[1] - p6[1] - pH[1]
    P1 = P1.quantize(Decimal('1.' + '0' * precise_sq))
    P2 = p1[2] + p2[2] - p3[2] - p4[2] - p5[2] - p6[2] - pH[2]
    P2 = P2.quantize(Decimal('1.' + '0' * precise_sq))
    P3 = p1[3] + p2[3] - p3[3] - p4[3] - p5[3] - p6[3] - pH[3]
    P3 = P3.quantize(Decimal('1.' + '0' * precise_sq))

    print("\nMomentum conservation law:")
    print("p1[0] + p2[0] - p3[0] - p4[0] - p5[0] - p6[0] - pH[0] =", P0)
    print("p1[1] + p2[1] - p3[1] - p4[1] - p5[1] - p6[1] - pH[1] =", P1)
    print("p1[2] + p2[2] - p3[2] - p4[2] - p5[2] - p6[2] - pH[2] =", P2)
    print("p1[3] + p2[3] - p3[3] - p4[3] - p5[3] - p6[3] - pH[3] =", P3)

    # Check squared momenta: p1^2 = 0, p2^2 = 0, p3^2 = 0, p4^2 = 0, p5^2 = 0, p6^2 = 0, pH^2 = mH^2
    p1sq = p1[0]**2 - p1[1]**2 - p1[2]**2 - p1[3]**2
    p1sq = p1sq.quantize(Decimal('1.' + '0' * precise_sq))
    p2sq = p2[0]**2 - p2[1]**2 - p2[2]**2 - p2[3]**2
    p2sq = p2sq.quantize(Decimal('1.' + '0' * precise_sq))
    p3sq = p3[0]**2 - p3[1]**2 - p3[2]**2 - p3[3]**2
    p3sq = p3sq.quantize(Decimal('1.' + '0' * precise_sq))
    p4sq = p4[0]**2 - p4[1]**2 - p4[2]**2 - p4[3]**2
    p4sq = p4sq.quantize(Decimal('1.' + '0' * precise_sq))
    p5sq = p5[0]**2 - p5[1]**2 - p5[2]**2 - p5[3]**2
    p5sq = p5sq.quantize(Decimal('1.' + '0' * precise_sq))
    p6sq = p6[0]**2 - p6[1]**2 - p6[2]**2 - p6[3]**2
    p6sq = p6sq.quantize(Decimal('1.' + '0' * precise_sq))
    pHsq = pH[0]**2 - pH[1]**2 - pH[2]**2 - pH[3]**2
    pHsq = pHsq.quantize(Decimal('1.' + '0' * precise_sq))

    print("\nSquared momenta:")
    print("p1^2 = ", p1sq)
    print("p2^2 = ", p2sq)
    print("p3^2 = ", p3sq)
    print("p4^2 = ", p4sq)
    print("p5^2 = ", p5sq)
    print("p6^2 = ", p6sq)
    print("pH^2 = ", pHsq)
    print("mH^2 = ", mH**2)

    # Convert to a float array for simpler work
    p1 = p1.astype(float)
    p2 = p2.astype(float)
    p3 = p3.astype(float)
    p4 = p4.astype(float)
    p5 = p5.astype(float)
    p6 = p6.astype(float)
    pH = pH.astype(float)

    print("\nPhase-space:")
    print(f"p1 = [{p1[0]}, {p1[1]}, {p1[2]}, {p1[3]}] (quark)")
    print(f"p2 = [{p2[0]}, {p2[1]}, {p2[2]}, {p2[3]}] (antiquark)")
    print(f"p3 = [{p3[0]}, {p3[1]}, {p3[2]}, {p3[3]}] (lepton)")
    print(f"p4 = [{p4[0]}, {p4[1]}, {p4[2]}, {p4[3]}] (antilepton)")
    print(f"p5 = [{p5[0]}, {p5[1]}, {p5[2]}, {p5[3]}] (gluon)")
    print(f"p6 = [{p6[0]}, {p6[1]}, {p6[2]}, {p6[3]}] (gluon)")
    print(f"pH = [{pH[0]}, {pH[1]}, {pH[2]}, {pH[3]}] (Higgs)")

    # Create a matrix of momenta
    p = np.column_stack((np.zeros(4), p1, p2, p3, p4, p5, p6))

    return p




















