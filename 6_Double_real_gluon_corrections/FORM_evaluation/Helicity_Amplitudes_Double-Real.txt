*** Spinor helicity amplitudes for double-real process q(p1) + qb(p2) -> g(p5) + g(p6) + W( -> l(p3) + lb(p4)) + H(pH)



*** DECLARATION

*** functions
f U, Ubar, Qprop, gqqbVertex, eps, gggVertex, Gprop, Wprop, LeptonCurrent, DenWprop, gamma, g, epsL, epsR, Bra, Ket, angle(antisymmetric), square(antisymmetric), current, PL1, PL2, PR1, PR2;

*** constants
S Mw2, gw, gs, Tg5, Tg6, sqrt2, DenWprop, C1, C2, C3, C4;

*** vectors
V A, p1, p2, pV, p3, p4, p5, p6, r5, r6;

*** indices
I mu, nu, rho, sigma, lambda, alpha;




*** AMPLITUDE LORENTZ EXPRESSION FROM QGRAF
L diag1 = Ubar(p2) * gqqbVertex(sigma, Tg6) * eps(p6, r6, sigma) * Qprop(p2-p6) * A(mu) * Qprop(p1-p5) * gqqbVertex(rho, Tg5) * eps(p5, r5, rho) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);
L diag2 = Ubar(p2) * gqqbVertex(sigma, Tg5) * eps(p5, r5, sigma) * Qprop(p2-p5) * A(mu) * Qprop(p1-p6) * gqqbVertex(rho, Tg6) * eps(p6, r6, rho) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);
L diag3 = Ubar(p2) * A(mu) * Qprop(p1-p5-p6) * gqqbVertex(rho, Tg6) * eps(p6, r6, rho) * Qprop(p1-p5) * gqqbVertex(sigma, Tg5) * eps(p5, r5, sigma) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);
L diag4 = Ubar(p2) * A(mu) * Qprop(p1-p5-p6) * gqqbVertex(rho, Tg5) * eps(p5, r5, rho) * Qprop(p1-p6) * gqqbVertex(sigma, Tg6) * eps(p6, r6, sigma) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);
L diag5 = Ubar(p2) * gqqbVertex(rho, Tg5) * eps(p5, r5, rho) * Qprop(p2-p5) * gqqbVertex(sigma, Tg6) * eps(p6, r6, sigma) * Qprop(p2-p5-p6) * A(mu) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);
L diag6 = Ubar(p2) * gqqbVertex(rho, Tg6) * eps(p6, r6, rho) * Qprop(p2-p6) * gqqbVertex(sigma, Tg5) * eps(p5, r5, sigma) * Qprop(p2-p5-p6) * A(mu) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);
L diag7 = Ubar(p2) * A(mu) * Qprop(p1-p5-p6) * gqqbVertex(sigma, Tg56) * Gprop(p5+p6, sigma, rho) * gggVertex(rho, lambda, alpha) * eps(p5, r5, alpha) * eps(p6, r6, lambda) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);
L diag8 = Ubar(p2) * gqqbVertex(sigma, Tg56) * Gprop(p5+p6, sigma, rho) * gggVertex(rho, lambda, alpha) * eps(p5, r5, alpha) * eps(p6, r6, lambda) * Qprop(p1-p5-p6) * A(mu) * U(p1) * Wprop(pV, mu, nu) * LeptonCurrent(p3, p4, nu);


*** TOTAL AMPLITUDE
L Ampl = diag1 + diag2 + diag3 + diag4 + diag5 + diag6 + diag7 + diag8;


*** HELICITY AMPLITUDES, helicity order: quark, anti-quark, gluon p5, gluon p6, lepton (always L), anti-lepton (always L)
L M_LLLLLL = Ampl(Ubar(p2?) = Bra(p2, -1), U(p1?) = Ket(p1, -1), eps(p5, r5, sigma?) = epsL(p5, sigma), eps(p6,sigma?) = epsL(p6, sigma));
L M_LLLRLL = Ampl(Ubar(p2?) = Bra(p2, -1), U(p1?) = Ket(p1, -1), eps(p5, r5, sigma?) = epsL(p5, sigma), eps(p6,sigma?) = epsR(p6, sigma));
L M_LLRLLL = Ampl(Ubar(p2?) = Bra(p2, -1), U(p1?) = Ket(p1, -1), eps(p5, r5, sigma?) = epsR(p5, sigma), eps(p6,sigma?) = epsL(p6, sigma));
L M_LLRRLL = Ampl(Ubar(p2?) = Bra(p2, -1), U(p1?) = Ket(p1, -1), eps(p5, r5, sigma?) = epsR(p5, sigma), eps(p6,sigma?) = epsR(p6, sigma));
L M_LRLLLL = Ampl(Ubar(p2?) = Bra(p2, +1), U(p1?) = Ket(p1, -1), eps(p5, r5, sigma?) = epsL(p5, sigma), eps(p6,sigma?) = epsL(p6, sigma));
L M_LRLRLL = Ampl(Ubar(p2?) = Bra(p2, +1), U(p1?) = Ket(p1, -1), eps(p5, r5, sigma?) = epsL(p5, sigma), eps(p6,sigma?) = epsR(p6, sigma));
L M_LRRLLL = Ampl(Ubar(p2?) = Bra(p2, +1), U(p1?) = Ket(p1, -1), eps(p5, r5, sigma?) = epsR(p5, sigma), eps(p6,sigma?) = epsL(p6, sigma));
L M_LRRRLL = Ampl(Ubar(p2?) = Bra(p2, +1), U(p1?) = Ket(p1, -1), eps(p5, r5, sigma?) = epsR(p5, sigma), eps(p6,sigma?) = epsR(p6, sigma));
L M_RLLLLL = Ampl(Ubar(p2?) = Bra(p2, -1), U(p1?) = Ket(p1, +1), eps(p5, r5, sigma?) = epsL(p5, sigma), eps(p6,sigma?) = epsL(p6, sigma));
L M_RLLRLL = Ampl(Ubar(p2?) = Bra(p2, -1), U(p1?) = Ket(p1, +1), eps(p5, r5, sigma?) = epsL(p5, sigma), eps(p6,sigma?) = epsR(p6, sigma));
L M_RLRLLL = Ampl(Ubar(p2?) = Bra(p2, -1), U(p1?) = Ket(p1, +1), eps(p5, r5, sigma?) = epsR(p5, sigma), eps(p6,sigma?) = epsL(p6, sigma));
L M_RLRRLL = Ampl(Ubar(p2?) = Bra(p2, -1), U(p1?) = Ket(p1, +1), eps(p5, r5, sigma?) = epsR(p5, sigma), eps(p6,sigma?) = epsR(p6, sigma));
L M_RRLLLL = Ampl(Ubar(p2?) = Bra(p2, +1), U(p1?) = Ket(p1, +1), eps(p5, r5, sigma?) = epsL(p5, sigma), eps(p6,sigma?) = epsL(p6, sigma));
L M_RRLRLL = Ampl(Ubar(p2?) = Bra(p2, +1), U(p1?) = Ket(p1, +1), eps(p5, r5, sigma?) = epsL(p5, sigma), eps(p6,sigma?) = epsR(p6, sigma));
L M_RRRLLL = Ampl(Ubar(p2?) = Bra(p2, +1), U(p1?) = Ket(p1, +1), eps(p5, r5, sigma?) = epsR(p5, sigma), eps(p6,sigma?) = epsL(p6, sigma));
L M_RRRRLL = Ampl(Ubar(p2?) = Bra(p2, +1), U(p1?) = Ket(p1, +1), eps(p5, r5, sigma?) = epsR(p5, sigma), eps(p6,sigma?) = epsR(p6, sigma));


*** 4-POINT VERTEX 
id A(mu?) = C1*PL2*(gamma(mu)*gamma(pV) - gamma(pV)*gamma(mu))*PL1 + C2*PR2*(gamma(mu)*gamma(pV) - gamma(pV)*gamma(mu))*PR1 + C3*PR2*gamma(mu)*PL1 + C4*PL2*gamma(mu)*PR1;
.sort


*** TOTAL GLUON-QUARK-ANTIQUARK VERTEX LEFT/RIGHT
id gqqbVertex(sigma?, Tg6?) * epsL(p6?, r6?, sigma?) = + i_ * gs * Tg6 * sqrt2 * (Ket(r6, -1) * Bra(p6, -1) + Ket(p6, +1) * Bra(r6, +1)) / square(p6, r6);
id gqqbVertex(sigma?, Tg6?) * epsR(p6?, r6?, sigma?) = - i_ * gs * Tg6 * sqrt2 * (Ket(p6, -1) * Bra(r6, -1) + Ket(r6, +1) * Bra(p6, +1)) / angle(p6, r6);
.sort


*** QUARK PROPAGATOR
id Qprop(p1?) = i_ * gamma(p1) / (p1^2);
.sort


*** GLUON-QUARK-ANTIQUARK VERTEX + GLUON PROPAGATOR
id gqqbVertex(sigma?, Tg56?) * Gprop(p5?, sigma?, rho?) = gs * Tg5 * Tg6 * gamma(rho) / (p5^2);
.sort


*** TRIPLE GLUON VERTEX + GLUONS
id gggVertex(rho?, lambda?, alpha?) * epsL(p5?, r5?, alpha?) * epsR(p6?, r6?, lambda?) = - gs / (2 * square(p5,r5) * angle(p6,r6)) * (Bra(r5,+1) * (gamma(p5) + 2*gamma(p6)) * Ket(p5,+1) * current(r6, p6, rho) + current(r5, lambda, p5) * current(r6, lambda, p6) * (p5(rho) - p6(rho)) - current(r5, rho, p5) * Bra(r6,-1) * (2*gamma(p5) + gamma(p6)) * Ket(p6, -1));
id gggVertex(rho?, lambda?, alpha?) * epsR(p5?, r5?, alpha?) * epsL(p6?, r6?, lambda?) = - gs / (2 * square(p6,r6) * angle(p5,r5)) * (Bra(r6,+1) * (gamma(p6) + 2*gamma(p5)) * Ket(p6,+1) * current(r5, p5, rho) + current(r6, lambda, p6) * current(r5, lambda, p5) * (p6(rho) - p6(rho)) - current(r6, rho, p6) * Bra(r5,-1) * (2*gamma(p6) + gamma(p5)) * Ket(p5, -1));
id gggVertex(rho?, lambda?, alpha?) * epsL(p5?, r5?, alpha?) * epsL(p6?, r6?, lambda?) = + gs / (2 * square(p5,r5) * square(p6,r6)) * (Bra(r5,+1) * (gamma(p5) + 2*gamma(p6)) * Ket(p5,+1) * current(r6, p6, rho) + current(r5, lambda, p5) * current(r6, lambda, p6) * (p5(rho) - p6(rho)) - current(r5, rho, p5) * Bra(r6,+1) * (2*gamma(p5) + gamma(p6)) * Ket(p6, +1));
id gggVertex(rho?, lambda?, alpha?) * epsR(p5?, r5?, alpha?) * epsR(p6?, r6?, lambda?) = + gs / (2 * angle(p5,r5) * angle(p6,r6)) * (Bra(r5,-1) * (gamma(p5) + 2*gamma(p6)) * Ket(p5,-1) * current(r6, p6, rho) + current(r5, lambda, p5) * current(r6, lambda, p6) * (p5(rho) - p6(rho)) - current(r5, rho, p5) * Bra(r6,-1) * (2*gamma(p5) + gamma(p6)) * Ket(p6, -1));
.sort


*** CONTRACT INDICES
#procedure ReplaceGamma
  #do i = 5,6
    id gamma(rho?) p`i`(rho?) = gamma(p`i`);
  #enddo
#endprocedure

#call ReplaceGamma

id gamma(rho?) * current(r5, rho, p5) = sqrt2 * (Ket(r5,-1) * Bra(p5,-1) + Ket(p5,+1) * Bra(r5,+1));
.sort


*** W PROPAGATOR
id Wprop(pV?,mu?,nu?) = - i_ * g(mu,nu) / DenWprop; 			*** DenWprop = [pV^2 - Mw2]


*** LEPTON CURRENT W -> l(p3) lb(p4) 
id LeptonCurrent(p1?,p2?,nu?) = i_*gw / sqrt2 * Bra(p1,-1) * gamma(nu) * Ket(p2,-1);


*** LEFT and RIGHT PROJECTORS (PL/PR) rules
id PL1 * Ket(p1,+1) = 0;
id PL1 * Ket(p1,-1) = Ket(p1,-1);
id PR1 * Ket(p1,+1) = Ket(p1,+1);
id PR1 * Ket(p1,-1) = 0;
id Bra(p2,+1) * PL2 = Bra(p2,+1);
id Bra(p2,-1) * PL2 = 0;
id Bra(p2,+1) * PR2 = 0;
id Bra(p2,-1) * PR2 = Bra(p2,-1);
.sort


*** USE g^{mu,nu} gamma_nu = gamma^{mu}
repeat;
id g(mu?,rho?) * g(rho?,nu?) = g(mu,nu);
id g(mu?,nu?) * gamma(nu?) = gamma(mu);
id p1?(mu?) * gamma(mu?) = gamma(p1);
endrepeat;
id gamma(pV) = gamma(p3) + gamma(p4);
.sort


*** DIRAC EQUATION
id gamma(p1?) * Ket(p1?,+1) = 0;
id gamma(p1?) * Ket(p1?,-1) = 0;
id Bra(p1?,+1) * gamma(p1?) = 0;
id Bra(p1?,-1) * gamma(p1?) = 0;
.sort


*** GAMMA BRAKET WRITING and CONDITIONS
repeat;
id gamma(p1?) = Ket(p1,-1) * Bra(p1,-1) + Ket(p1,+1) * Bra(p1,+1);
endrepeat;


*** CREATION OF <1|mu|2] and [1|mu|2>
id Bra(p1?,-1) * gamma(mu?) * Ket(p2?,-1) = current(p1,mu,p2);		*** <1|mu|2]
id Bra(p1?,+1) * gamma(mu?) * Ket(p2?,+1) = current(p2,mu,p1);		*** [1|mu|2> = <2|mu|1]
id Bra(p1?,-1) * gamma(mu?) * Ket(p2?,+1) = 0;				*** <1|mu|2> = 0
id Bra(p1?,+1) * gamma(mu?) * Ket(p2?,-1) = 0;				*** [1|mu|2] = 0
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
id current(p1?,mu?,p2?) * current(p5?,mu?,p6?) = 2 * angle(p1,p5) * square(p6,p2); 	*** <1|mu|2] <3|mu|4] = 2 <13> [42]
.sort


*** SIMPLIFICATIONS
id sqrt2 * sqrt2 = 2;
.sort


Bracket i_, Mw2, gw, gs, Tg5, Tg6, sqrt2, DenWprop, C1, C2, C3, C4;

print +s;


.end
















