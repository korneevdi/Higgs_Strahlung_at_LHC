!
! This driver can be simply executed in the following way
! 
! 1) run "./scons auto=ppvj" in OpenLoops' main directory to install the process library 
! 2) copy this driver file into the "examples" folder of OpenLoops
! 3) add "env.Program('OL_pphllj', ['OL_pphllj.f90'], LIBS = ['openloops'])" at the end of the "SConstruct" file in the "examples" directory
! 4) run "../scons" in the "examples" directory to compile the driver
! 5) execute the program "./OL_pphllj"
!

! Example  program how to use the native interface of OpenLoops.
! It calculates the Tree and loop matrix element of the process
! d ubar -> W- g for a random phase-space point.

program main
  use openloops
  implicit none
  integer :: id, error, k
  real(8) :: m2_tree, m2_loop(0:2), m2_bare(0:2),m2_ct(0:2),m2_ir(0:2),m2_sum(0:2), acc, r2
  real(8) :: p_ex(0:3,6)
  real(8) :: mZ = 9.11876D1
  real(8) :: mW = 8.03990000D1
  real(8) :: mH = 1.25000000D2
  real(8) :: alpha_s = 1.D0
  real(8) :: mu = 1.D2

  ! Increase verbosity level to list loaded libraries
  call set_parameter("verbose", 0)
  call set_parameter("no_splash", 1)

  ! scheme for electromagnetic couplings
  call set_parameter("ew_scheme", 2)
  call set_parameter("alpha_qed_mz", 7.55591556146232963D-3)
  
  ! set strong coupling
  call set_parameter("alpha_s", alpha_s)

  ! set Z mass
  call set_parameter("mass(23)", mz)
  call set_parameter("mass(24)", mw)
  call set_parameter("mass(25)", mh)
  call set_parameter("width(24)", 2.1053999999999999D0)

  ! set renormalisation scale
  call set_parameter("mu", mu)

  ! second argument of register_process:
  ! 1 for tree-like matrix elements (tree, color and spin correlations),
  ! 11 for loop, 12 for loop^2
  call set_parameter("nf", 6)
  id = register_process("1 -2 -> 21 11 -12 25", 11)

  ! start
  call start()

  if (id > 0) then
    p_ex(:,1)=(/334.79722981844668d0,  0.0000000000000000d0,   0.0000000000000000d0,        334.79722981844668d0/)
    p_ex(:,2)=(/334.79722981844668d0,  0.0000000000000000d0,   0.0000000000000000d0,       -334.79722981844668d0/)
    p_ex(:,3)=(/105.15993839229942d0,  41.202758892167196d0,   17.997624021261228d0,        95.063299079799819d0/) 
    p_ex(:,4)=(/261.27855458005598d0, -127.36649084356779d0,   9.8778094075176863d0,       -227.91816288954988d0/) 
    p_ex(:,5)=(/58.691931688911218d0, -52.071500451549717d0,  -11.528633405809016d0,       -24.502903866573526d0/)
    p_ex(:,6)=(/244.46403497562682d0,  138.23523240295037d0,  -16.346800022969902d0,        157.35776767632362d0/) 

    print *
    print *, "Tree and loop matrix element of the process"
    print *, "1 2               3 4  5  6"
    print *, "d u~ -> g W- H -> g e- nu H"
    print *, "for the phase-space point"
    do k = 1, size(p_ex,2)
      print *, 'P', int(k,1), ' = {', p_ex(0,k), ',', p_ex(1,k), ',', p_ex(2,k), ',', p_ex(3,k), '}'
    end do
    print *, "mu",mu

    ! evaluate tree matrix element
    call evaluate_tree(id, p_ex, m2_tree)
    ! print tree result
    print *
    print *, "evaluate_tree"
    print *, "Tree:       ", m2_tree
    print *

    ! evaluate tree and loop matrix elements
    call evaluate_r2(id, p_ex, m2_tree, r2)

    ! evaluate tree and loop matrix elements
    call evaluate_loopbare(id, p_ex, m2_tree, m2_loop(0:2), acc)
    print *, "evaluate_loopbare"
    ! print *, "Tree:       ", m2_tree
    print *, "Loop ep^-2: ", m2_loop(2)
    print *, "Loop ep^-1: ", m2_loop(1)
    print *, "Loop ep^0:  ", m2_loop(0)+r2
    ! print *, "accuracy:   ", acc
    print *

    ! evaluate tree and loop matrix elements
    call evaluate_loop(id, p_ex, m2_tree, m2_loop(0:2), acc)
    print *, "evaluate_loop"
    ! print *, "Tree:       ", m2_tree
    print *, "Loop ep^-2: ", m2_loop(2)
    print *, "Loop ep^-1: ", m2_loop(1)
    print *, "Loop ep^0:  ", m2_loop(0)
    ! print *, "accuracy:   ", acc
    print *
    print*, "(UV renormalized) Finite Remainder: ", m2_loop(0)-m2_loop(2)*(4.D0*ATAN(1.D0))**2/12.D0
    print *

  end if

  ! finish
  call finish()

end program main
