*** Spinor helicity amplitudes for virtual-real process q(p1) + qb(p2) -> g(p5) + W( -> l(p3) + lb(p4)) + H(pH)



*** DECLARATION

*** functions
f U, Ubar, eps, Wprop, LeptonCurrent, DenWprop, epsL, epsR, Bra, Ket, angle(antisymmetric), square(antisymmetric), current;

*** constants
S AlphaOverTwoPi, s12, s15, s25, s1v, s2v, s5v, Mw2, gw, sqrt2, DenWprop, C1, C2, C3, C4;

*** form factors (constants)
S A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23;

*** vectors
V A, p1, p2, pV, p3, p4, p5, r5;

*** tensor structures (vectors)
V T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23;

*** indices
I mu, nu;




*** AMPLITUDE
L M_gamma = AlphaOverTwoPi^(3/2) * Ubar(p2) * (A1*T1(mu) + A2*T2(mu) + A3*T3(mu) + A4*T4(mu) + A5*T5(mu) + A6*T6(mu) + A7*T7(mu)) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);
L M_commutator = AlphaOverTwoPi^(3/2) * Ubar(p2) * (A8*T8(mu) + A9*T9(mu) + A10*T10(mu) + A11*T11(mu) + A12*T12(mu) + A13*T13(mu) + A14*T14(mu) + A15*T15(mu) + A16*T16(mu) + A17*T17(mu) + A18*T18(mu) + A19*T19(mu) + A20*T20(mu) + A21*T21(mu) + A22*T22(mu) + A23*T23(mu)) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);


*** REPLACE TENSOR STRUCTURES
id T1(mu) = (g_(1, p5)*eps.p1*p1(mu) - s15/2*g_(1, eps)*p1(mu) + s12/4*g_(1, eps, p5, mu));
id T2(mu) = (g_(1, p5)*eps.p1*p2(mu) - s15/2*g_(1, eps)*p2(mu) + s12/4*g_(1, eps, p5, mu));
id T3(mu) = (g_(1, p5)*eps.p1*p5(mu) - s15/2*g_(1, eps)*p5(mu) + (s12 - s15 - s25)/4*g_(1, eps, p5, mu));
id T4(mu) = (g_(1, p5)*eps.p2*p1(mu) - s25/2*g_(1, eps)*p1(mu) + s12/4*g_(1, mu, p5, eps));
id T5(mu) = (g_(1, p5)*eps.p2*p2(mu) - s25/2*g_(1, eps)*p2(mu) + s12/4*g_(1, mu, p5, eps));
id T6(mu) = (g_(1, p5)*eps.p2*p5(mu) - s25/2*g_(1, eps)*p5(mu) + (s12 - s15 - s25)/4*g_(1, mu, p5, eps));
id T7(mu) = (s25*(g_(1, mu)*eps.p1 + 1/2*g_(1, eps, p5, mu)) - s12*(g_(1, mu)*eps.p2 + 1/2*g_(1, mu, p5, eps)));

id T8(mu) = (g_(1, mu, pV, p5, eps) - g_(1, pV, mu, p5, eps));
id T9(mu) = (g_(1, p5, eps) * (g_(1, mu, pV, p5, eps) - g_(1, pV, mu, p5, eps)));
id T10(mu) = ((s1v*p5(mu) - s5v*p1(mu))*g_(1, p5, eps));
id T11(mu) = ((s2v*p5(mu) - s5v*p2(mu))*g_(1, p5, eps));
id T12(mu) = ((g_(1, mu, pV, p5, eps) - g_(1, pV, mu, p5, eps)) * (s25*eps.p1 - s15*eps.p2));
id T13(mu) = ((p1(mu)*g_(1, pV, p5) - 1/2*s1v*g_(1, mu, p5)) * (s25*eps.p1 - s15*eps.p2));
id T14(mu) = ((p2(mu)*g_(1, pV, p5) - 1/2*s2v*g_(1, mu, p5)) * (s25*eps.p1 - s15*eps.p2));
id T15(mu) = ((p5(mu)*g_(1, pV, p5) - 1/2*s5v*g_(1, mu, p5)) * (s25*eps.p1 - s15*eps.p2));
id T16(mu) = (1/2*s25*p1(mu)*g_(1, pV, eps) + 1/2*s1v*eps.p2*g_(1, mu, p5) - p1(mu)*eps.p2*g_(1, pV, p5) - 1/4*s25*s1v*g_(1, mu, eps));
id T17(mu) = (1/2*s25*p2(mu)*g_(1, pV, eps) + 1/2*s2v*eps.p2*g_(1, mu, p5) - p2(mu)*eps.p2*g_(1, pV, p5) - 1/4*s25*s2v*g_(1, mu, eps));
id T18(mu) = (1/2*s25*p5(mu)*g_(1, pV, eps) + 1/2*s5v*eps.p2*g_(1, mu, p5) - p5(mu)*eps.p2*g_(1, pV, p5) - 1/4*s25*s5v*g_(1, mu, eps));
id T19(mu) = (p5(mu)*eps.pV - 1/4*s5v*g_(1, mu, eps) - 1/4*s5v*g_(1, eps, mu));
id T20(mu) = ((p1(mu)*(s15*eps.pV - s5v*eps.p1) + s1v*p5(mu)*eps.p1) - 1/4*s15*s1v*g_(1, mu, eps) - 1/4*s15*s1v*g_(1, eps, mu));
id T21(mu) = ((p2(mu)*(s15*eps.pV - s5v*eps.p1) + s2v*p5(mu)*eps.p1) - 1/4*s15*s2v*g_(1, mu, eps) - 1/4*s15*s2v*g_(1, eps, mu));
id T22(mu) = ((p1(mu)*(s25*eps.pV - s5v*eps.p2) + s1v*p5(mu)*eps.p2) - 1/4*s25*s1v*g_(1, mu, eps) - 1/4*s25*s1v*g_(1, eps, mu));
id T23(mu) = ((p2(mu)*(s25*eps.pV - s5v*eps.p2) + s2v*p5(mu)*eps.p2) - 1/4*s25*s2v*g_(1, mu, eps) - 1/4*s25*s2v*g_(1, eps, mu));



*** HELICITY AMPLITUDES
L M_LLLLL = C3 * M_gamma(Ubar(p2) = Bra(p2, -1), U(p1) = Ket(p1, -1), eps(mu?) = epsL(mu));
L M_LRLLL = C1 * M_commutator(Ubar(p2) = Bra(p2, +1), U(p1) = Ket(p1, -1), eps(mu?) = epsL(mu));
L M_RLLLL = C2 * M_commutator(Ubar(p2) = Bra(p2, -1), U(p1) = Ket(p1, +1), eps(mu?) = epsL(mu));
L M_RRLLL = C4 * M_gamma(Ubar(p2) = Bra(p2, +1), U(p1) = Ket(p1, +1), eps(mu?) = epsL(mu));
L M_LLRLL = C3 * M_gamma(Ubar(p2) = Bra(p2, -1), U(p1) = Ket(p1, -1), eps(mu?) = epsR(mu));
L M_LRRLL = C1 * M_commutator(Ubar(p2) = Bra(p2, +1), U(p1) = Ket(p1, -1), eps(mu?) = epsR(mu));
L M_RLRLL = C2 * M_commutator(Ubar(p2) = Bra(p2, -1), U(p1) = Ket(p1, +1), eps(mu?) = epsR(mu));
L M_RRRLL = C4 * M_gamma(Ubar(p2) = Bra(p2, +1), U(p1) = Ket(p1, +1), eps(mu?) = epsR(mu));



*** W PROPAGATOR
id Wprop(pV?,mu?,nu?) = - i_ * g(mu,nu) / DenWprop; 			*** DenWprop = [pV^2 - Mw2]



*** LEPTON CURRENT W -> l(p3) lb(p4) 
id LeptonCurrent(p1?,p2?,nu?) = i_*gw / sqrt2 * Bra(p1,-1) * g_(1, nu) * Ket(p2,-1);



*** REPLACE WEAK BOSON MOMUNTUM
id pV(mu?) = p3(mu) + p4(mu);

contract;


*** DIRAC EQUATION
id g_(1, p1?) * Ket(p1?,+1) = 0;
id g_(1, p1?) * Ket(p1?,-1) = 0;
id Bra(p1?,+1) * g_(1, p1?) = 0;
id Bra(p1?,-1) * g_(1, p1?) = 0;
.sort


*** REPLACE GLUON POLARIZATION VECTOR
id epsL.p1? = Bra(r5, +1) * g_(1, p1) * Ket(p5, +1) / (sqrt2 * square(p5, r5));
id g_(1, epsL) = sqrt2 * (Ket(p5, -1 * Bra(r5, -1) + Ket(r5, +1 * Bra(p5, +1)))) / square(p5, r5);
id epsR.p1? = - Bra(r5, -1) * g_(1, p1) * Ket(p5, -1) / (sqrt2 * angle(p5, r5));
id g_(1, epsR) = - sqrt2 * (Ket(r5, -1 * Bra(p5, -1) + Ket(p5, +1 * Bra(r5, +1)))) / angle(p5, r5);



*** GAMMA BRAKET WRITING and CONDITIONS
repeat;
id gamma(p1?) = Ket(p1,-1) * Bra(p1,-1) + Ket(p1,+1) * Bra(p1,+1);
endrepeat;


*** CREATION OF <1|mu|2] and [1|mu|2>
id Bra(p1?,-1) * g_(1, mu?) * Ket(p2?,-1) = current(p1,mu,p2);		*** <1|mu|2]
id Bra(p1?,+1) * g_(1, mu?) * Ket(p2?,+1) = current(p2,mu,p1);		*** [1|mu|2> = <2|mu|1]
id Bra(p1?,-1) * g_(1, mu?) * Ket(p2?,+1) = 0;				*** <1|mu|2> = 0
id Bra(p1?,+1) * g_(1, mu?) * Ket(p2?,-1) = 0;				*** [1|mu|2] = 0
.sort


*** CONDITIONS ON Bra-Ket
id Bra(p1?,-1) * Ket(p2?,-1) = 0;					*** <12] = 0
id Bra(p1?,+1) * Ket(p2?,+1) = 0;					*** [12> = 0
id Bra(p1?,+1) * Ket(p1?,-1) = 0;	    				*** [11] = 0
id Bra(p1?,-1) * Ket(p1?,+1) = 0;	    				*** <11> = 0	
id Bra(p1?,-1) * Ket(p2?,+1) = angle(p1,p2);				*** <12> 
id Bra(p1?,+1) * Ket(p2?,-1) = square(p1,p2);				*** [12] 
.sort


*** FIERZ IDENTITY
id current(p1?,mu?,p2?) * current(p3?,mu?,p4?) = 2 * angle(p1,p3) * square(p4,p2); 	*** <1|mu|2] <3|mu|4] = 2 <13> [42]
.sort


*** SIMPLIFICATIONS
id sqrt2 * sqrt2 = 2;
.sort


Bracket i_, Mw2, gw, sqrt2, DenWprop, C1, C2, C3, C4;

print +s;


.end
















