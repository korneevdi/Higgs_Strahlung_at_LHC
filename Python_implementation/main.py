
import amplitudes
import phase_space



def main():

    # Request for input and convert it to a number
    sqrt_s = int(input("\nEnter the center-of-mass energy between mW + mH and 20.000 GeV: "))

    print("\nCenter-of-mass energy:", sqrt_s, " GeV")

    # Generate phase-space
    PS3 = phase_space.phase_space_generate_3(sqrt_s)
    PS4 = phase_space.phase_space_generate_4(sqrt_s)
    PS5 = phase_space.phase_space_generate_5(sqrt_s)

    # Calculate squared amplitudes
    print("\n\n\nSQUARED AMPLITUDES CALCULATION\n")

    # Leading order amplitude
    amplitudes.loop_squared_amplitude(0, PS3)

    # One-loop amplitude
    amplitudes.loop_squared_amplitude(1, PS3)

    # Two-loop amplitude
    amplitudes.loop_squared_amplitude(2, PS3)

    # Single real gluon tree-level amplitude
    amplitudes.single_real_squared_amplitude(0, PS4)

    # Virtual-real amplitude
    amplitudes.single_real_squared_amplitude(1, PS4)

    # Double-real amplitude
    amplitudes.double_real_squared_amplitude(PS5)



if __name__ == "__main__":
    main()


