
import math

# CONSTANTS
mW = 80.419                         # W-boson mass
mH = 125.0                          # Higgs boson mass 
Gamma_W = 2.085                     # W-boson decay width
gW = 0.6530704531238141             # electroweak coupling
vev = 246.21845810181634            # vacuum expectation value
Cf = 4/3                            # quadratic Casimir operator in the fundamental representation of SU(3)
Nc = 3                              # number of colors
Nf = 4                              # number of flavors
CA = 3                              # quadratic Casimir operator in the adjoint representation of SU(3)
beta0 = (33 - 2 * Nf)/12            # beta-function zero coefficient
S3 = gW/math.sqrt(2)                # Standard Model coefficient
C1 = 0                              # Wilson coefficients
C2 = 0
C3 = 0
C4 = 0


# PARAMETERS
mu = 91.188                         # energy scale
mu2 = mu**2                         # square of the energy scale
alpha_s = 0.1                       # strong coupling constant
gs = math.sqrt(4*math.pi*alpha_s)   # gluon coupling constant


# PROGRAM SETTINGS
sqrt_s_min = mW + mH                # Center-of-mass energy minimum
sqrt_s_max = 20000                  # Center-of-mass energy maximum
precise = 17                        # Number of digits after the point for momenta
precise_sq = 8                      # Number of digits after the point for squared momenta
