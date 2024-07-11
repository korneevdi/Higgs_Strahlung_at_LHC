Dimension d;

* Definition of vectors
V p1, p2, pV, pg, k, eps;

* Definition of the vertex
V A;

* Definition of scalar quantities
S C12, C34, mu02, mV2, s1g, s2g, s1v, s2v, sgv, pi, e, CF, CA, Nf;
S A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23;

* Definition of indices
Index mu, num rho, sigma, alpha, beta;

* Definition of spinors
C Up1, Ubarp1, Up2, Ubarp2;

* Additional trace
L tr = g_(1, nu, k1 - k2, rho, k2);

Trace, tr;

* Propagators
L D1 = k^2;
L D2 = (p1 + k)^2;
L D3 = (p2 - k)^2;
L D4 = (p1 - pg + k)^2;
L D5 = (p2 - pg - k)^2;
L D6 = (pg + k)^2;

* Diagrams
L M1(mu) = i_*CF/(s1g^2)*mu02^e*Ubarp2*A(mu)*g_(1, p1 - pg, rho, p1 - pg + k, rho, p1 - pg, eps)*Up1/(D1*D4);
L M2(mu) = -i_*CF/(s2g^2)*mu02^e*Ubarp2*g_(1, eps, p2 - pg, rho, p2 - pg + k, rho, p2 - pg)*A(mu)*Up1/(D1*D5);
L M3(mu) = -i_*CF/(s1g)*mu02^e*Ubarp2*g_(1, rho, p2 - k)*A(mu)*g(1, p1 - pg + k, rho, p1 - pg, eps)*Up1/(D1*D3*D4);
L M4(mu) = i_*CF/(s2g)*mu02^e*Ubarp2*g_(1, eps, p2 - pg, rho, p2 - pg - k)*A(mu)*g(1, p1 + k, rho)*Up1/(D1*D2*D5);
L M5(mu) = -i_/(2*CA*s1g)*mu02^e*Ubarp2*A(mu)*g_(1, p1 - pg, rho, p1 - pg + k, eps, p1 + k, rho)*Up1/(D1*D2*D4);
L M6(mu) = i_/(2*CA*s2g)*mu02^e*Ubarp2*g_(1, rho, p2 - k, eps, p2 - pg - k, rho, p2 - pg)*A(mu)*Up1/(D1*D3*D5);
L M7(mu) = i_*CA/(2*s1g)*mu02^e*Ubarp2*A(mu)*g_(1, p1 - pg, rho, p1 + k, nu)*(d_(sigma, rho)*(2*pg(nu) + k(nu)) + d_(sigma, nu)*(-pg(rho) + k(rho)) + d_(rho, nu)*(-pg(sigma) - 2*k(sigma)))*Up1/(D1*D2*D6);
L M8(mu) = i_*CA/(2*s2g)*mu02^e*Ubarp2*g_(1, p2 - pg - k, nu, p2 - pg)*A(mu)*(d_(sigma, rho)*(2*pg(nu) + k(nu)) + d_(sigma, nu)*(-pg(rho) + k(rho)) + d_(rho, nu)*(-pg(sigma) - 2*k(sigma)))*Up1/(D1*D5*D6);
L M9(mu) = i_/(2*CA)*mu02^e*Ubarp2*g_(1, rho, p2 - k)*A(mu)*g_(1, p1 - pg + k, eps, p1 + k, rho)*Up1/(D1*D2*D3*D4);
L M10(mu) = -i_/(2*CA)*mu02^e*Ubarp2*g_(1, rho, p2 - k, eps, p2 - pg - k)*A(mu)*g_(1, p1 + k, rho)*Up1/(D1*D2*D3*D5);
L M11(mu) = -i_*CA/2*mu02^e*Ubarp2*g_(1, rho, p2 - pg - k)*A(mu)*g_(1, p1 + k, nu)*(d_(sigma, rho)*(2*pg(nu) + k(nu)) + d_(sigma, nu)*(-pg(rho) + k(rho)) + d_(rho, nu)*(-pg(sigma) - 2*k(sigma)))*Up1/(D1*D2*D5*D6);

* Total amplitude
L M(mu) = M1(mu) + M2(mu) + M3(mu) + M4(mu) + M5(mu) + M6(mu) + M7(mu) + M8(mu) + M9(mu) + M10(mu) + M11(mu);

* Substituting the vertex
id A(mu) = C12*(g_(1, mu)*g_(1, pV) - g_(1, pV)*g_(1, mu)) + C34*g_(1, mu);

.sort

* Tensor structures
L T1(mu) = Ubarp1*(g_(1, pg)*eps.p1*p1(mu) - s1g/2*g_(1, eps)*p1(mu) + s12/4*g_(1, eps, pg, mu))*Up2;
L T2(mu) = Ubarp1*(g_(1, pg)*eps.p1*p2(mu) - s1g/2*g_(1, eps)*p2(mu) + s12/4*g_(1, eps, pg, mu))*Up2;
L T3(mu) = Ubarp1*(g_(1, pg)*eps.p1*pg(mu) - s1g/2*g_(1, eps)*pg(mu) + (s12 - s1g - s2g)/4*g_(1, eps, pg, mu))*Up2;
L T4(mu) = Ubarp1*(g_(1, pg)*eps.p2*p1(mu) - s2g/2*g_(1, eps)*p1(mu) + s12/4*g_(1, mu, pg, eps))*Up2;
L T5(mu) = Ubarp1*(g_(1, pg)*eps.p2*p2(mu) - s2g/2*g_(1, eps)*p2(mu) + s12/4*g_(1, mu, pg, eps))*Up2;
L T6(mu) = Ubarp1*(g_(1, pg)*eps.p2*pg(mu) - s2g/2*g_(1, eps)*pg(mu) + (s12 - s1g - s2g)/4*g_(1, mu, pg, eps))*Up2;
L T7(mu) = Ubarp1*(s2g*(g_(1, mu)*eps.p1 + 1/2*g_(1, eps, pg, mu)) - s12*(g_(1, mu)*eps.p2 + 1/2*g_(1, mu, pg, eps)))*Up2;

L T8(mu) = Ubarp1*(g_(1, mu, pV, pg, eps) - g_(1, pV, mu, pg, eps))*Up2;
L T9(mu) = Ubarp1*(g_(1, pg, eps) * (g_(1, mu, pV, pg, eps) - g_(1, pV, mu, pg, eps)))*Up2;
L T10(mu) = Ubarp1*((s1v*pg(mu) - sgv*p1(mu))*g_(1, pg, eps))*Up2;
L T11(mu) = Ubarp1*((s2v*pg(mu) - sgv*p2(mu))*g_(1, pg, eps))*Up2;
L T12(mu) = Ubarp1*((g_(1, mu, pV, pg, eps) - g_(1, pV, mu, pg, eps)) * (s2g*eps.p1 - s1g*eps.p2))*Up2;
L T13(mu) = Ubarp1*((p1(mu)*g_(1, pV, pg) - 1/2*s1v*g_(1, mu, pg)) * (s2g*eps.p1 - s1g*eps.p2))*Up2;
L T14(mu) = Ubarp1*((p2(mu)*g_(1, pV, pg) - 1/2*s2v*g_(1, mu, pg)) * (s2g*eps.p1 - s1g*eps.p2))*Up2;
L T15(mu) = Ubarp1*((pg(mu)*g_(1, pV, pg) - 1/2*sgv*g_(1, mu, pg)) * (s2g*eps.p1 - s1g*eps.p2))*Up2;
L T16(mu) = Ubarp1*(1/2*s2g*p1(mu)*g_(1, pV, eps) + 1/2*s1v*eps.p2*g_(1, mu, pg) - p1(mu)*eps.p2*g_(1, pV, pg) - 1/4*s2g*s1v*g_(1, mu, eps))*Up2;
L T17(mu) = Ubarp1*(1/2*s2g*p2(mu)*g_(1, pV, eps) + 1/2*s2v*eps.p2*g_(1, mu, pg) - p2(mu)*eps.p2*g_(1, pV, pg) - 1/4*s2g*s2v*g_(1, mu, eps))*Up2;
L T18(mu) = Ubarp1*(1/2*s2g*pg(mu)*g_(1, pV, eps) + 1/2*sgv*eps.p2*g_(1, mu, pg) - pg(mu)*eps.p2*g_(1, pV, pg) - 1/4*s2g*sgv*g_(1, mu, eps))*Up2;
L T19(mu) = Ubarp1*(pg(mu)*eps.pV - 1/4*sgv*g_(1, mu, eps) - 1/4*sgv*g_(1, eps, mu))*Up2;
L T20(mu) = Ubarp1*((p1(mu)*(s1g*eps.pV - sgv*eps.p1) + s1v*pg(mu)*eps.p1) - 1/4*s1g*s1v*g_(1, mu, eps) - 1/4*s1g*s1v*g_(1, eps, mu))*Up2;
L T21(mu) = Ubarp1*((p2(mu)*(s1g*eps.pV - sgv*eps.p1) + s2v*pg(mu)*eps.p1) - 1/4*s1g*s2v*g_(1, mu, eps) - 1/4*s1g*s2v*g_(1, eps, mu))*Up2;
L T22(mu) = Ubarp1*((p1(mu)*(s2g*eps.pV - sgv*eps.p2) + s1v*pg(mu)*eps.p2) - 1/4*s2g*s1v*g_(1, mu, eps) - 1/4*s2g*s1v*g_(1, eps, mu))*Up2;
L T23(mu) = Ubarp1*((p2(mu)*(s2g*eps.pV - sgv*eps.p2) + s2v*pg(mu)*eps.p2) - 1/4*s2g*s2v*g_(1, mu, eps) - 1/4*s2g*s2v*g_(1, eps, mu))*Up2;

* Total amplitude through form factors
L Mff1 = A1*T1(mu) + A2*T2(mu) + A3*T3(mu) + A4*T4(mu) + A5*T5(mu) + A6*T6(mu) + A7*T7(mu);
L Mff2 = A8*T8(mu) + A9*T9(mu) + A10*T10(mu) + A11*T11(mu) + A12*T12(mu) + A13*T13(mu) + A14*T14(mu) + A15*T15(mu) + A16*T16(mu) + A17*T17(mu) + A18*T18(mu) + A19*T19(mu) + A20*T20(mu) + A21*T21(mu) + A22*T22(mu) + A23*T23(mu);

* Contracted amplitudes expressed through form factors
L R1 = Mff1*T1(mu);
L R2 = Mff1*T2(mu);
L R3 = Mff1*T3(mu);
L R4 = Mff1*T4(mu);
L R5 = Mff1*T5(mu);
L R6 = Mff1*T6(mu);
L R7 = Mff1*T7(mu);
L R8 = Mff2*T8(mu);
L R9 = Mff2*T9(mu);
L R10 = Mff2*T10(mu);
L R11 = Mff2*T11(mu);
L R12 = Mff2*T12(mu);
L R13 = Mff2*T13(mu);
L R14 = Mff2*T14(mu);
L R15 = Mff2*T15(mu);
L R16 = Mff2*T16(mu);
L R17 = Mff2*T17(mu);
L R18 = Mff2*T18(mu);
L R19 = Mff2*T19(mu);
L R20 = Mff2*T20(mu);
L R21 = Mff2*T21(mu);
L R22 = Mff2*T22(mu);
L R23 = Mff2*T23(mu);

* Contracted amplitudes
L Ampl1 = M(mu)*Ubarp1*T1(mu)*Up2;
L Ampl2 = M(mu)*Ubarp1*T2(mu)*Up2;
L Ampl3 = M(mu)*Ubarp1*T3(mu)*Up2;
L Ampl4 = M(mu)*Ubarp1*T4(mu)*Up2;
L Ampl5 = M(mu)*Ubarp1*T5(mu)*Up2;
L Ampl6 = M(mu)*Ubarp1*T6(mu)*Up2;
L Ampl7 = M(mu)*Ubarp1*T7(mu)*Up2;
L Ampl8 = M(mu)*Ubarp1*T8(mu)*Up2;
L Ampl9 = M(mu)*Ubarp1*T9(mu)*Up2;
L Ampl10 = M(mu)*Ubarp1*T10(mu)*Up2;
L Ampl11 = M(mu)*Ubarp1*T11(mu)*Up2;
L Ampl12 = M(mu)*Ubarp1*T12(mu)*Up2;
L Ampl13 = M(mu)*Ubarp1*T13(mu)*Up2;
L Ampl14 = M(mu)*Ubarp1*T14(mu)*Up2;
L Ampl15 = M(mu)*Ubarp1*T15(mu)*Up2;
L Ampl16 = M(mu)*Ubarp1*T16(mu)*Up2;
L Ampl17 = M(mu)*Ubarp1*T17(mu)*Up2;
L Ampl18 = M(mu)*Ubarp1*T18(mu)*Up2;
L Ampl19 = M(mu)*Ubarp1*T19(mu)*Up2;
L Ampl20 = M(mu)*Ubarp1*T20(mu)*Up2;
L Ampl21 = M(mu)*Ubarp1*T21(mu)*Up2;
L Ampl22 = M(mu)*Ubarp1*T22(mu)*Up2;
L Ampl23 = M(mu)*Ubarp1*T23(mu)*Up2;

* REPLACE spinors with gamma matrices
id Ubarp1 * Up1 = g_(1, p1);
id Ubarp2 = 1;
id Up2 = 1;

Ampl1 = g_(1, p2) * Ampl1;
Ampl2 = g_(1, p2) * Ampl2;
Ampl3 = g_(1, p2) * Ampl3;
Ampl4 = g_(1, p2) * Ampl4;
Ampl5 = g_(1, p2) * Ampl5;
Ampl6 = g_(1, p2) * Ampl6;
Ampl7 = g_(1, p2) * Ampl7;
Ampl8 = g_(1, p2) * Ampl8;
Ampl9 = g_(1, p2) * Ampl9;
Ampl10 = g_(1, p2) * Ampl10;
Ampl11 = g_(1, p2) * Ampl11;
Ampl12 = g_(1, p2) * Ampl12;
Ampl13 = g_(1, p2) * Ampl13;
Ampl14 = g_(1, p2) * Ampl14;
Ampl15 = g_(1, p2) * Ampl15;
Ampl16 = g_(1, p2) * Ampl16;
Ampl17 = g_(1, p2) * Ampl17;
Ampl18 = g_(1, p2) * Ampl18;
Ampl19 = g_(1, p2) * Ampl19;
Ampl20 = g_(1, p2) * Ampl20;
Ampl21 = g_(1, p2) * Ampl21;
Ampl22 = g_(1, p2) * Ampl22;
Ampl23 = g_(1, p2) * Ampl23;

R1 = g_(1, p2) * R1;
R2 = g_(1, p2) * R2;
R3 = g_(1, p2) * R3;
R4 = g_(1, p2) * R4;
R5 = g_(1, p2) * R5;
R6 = g_(1, p2) * R6;
R7 = g_(1, p2) * R7;
R8 = g_(1, p2) * R8;
R9 = g_(1, p2) * R9;
R10 = g_(1, p2) * R10;
R11 = g_(1, p2) * R11;
R12 = g_(1, p2) * R12;
R13 = g_(1, p2) * R13;
R14 = g_(1, p2) * R14;
R15 = g_(1, p2) * R15;
R16 = g_(1, p2) * R16;
R17 = g_(1, p2) * R17;
R18 = g_(1, p2) * R18;
R19 = g_(1, p2) * R19;
R20 = g_(1, p2) * R20;
R21 = g_(1, p2) * R21;
R22 = g_(1, p2) * R22;
R23 = g_(1, p2) * R23;

* Compute traces
Trace, Ampl1;
Trace, Ampl2;
Trace, Ampl3;
Trace, Ampl4;
Trace, Ampl5;
Trace, Ampl6;
Trace, Ampl7;
Trace, Ampl8;
Trace, Ampl9;
Trace, Ampl10;
Trace, Ampl11;
Trace, Ampl12;
Trace, Ampl13;
Trace, Ampl14;
Trace, Ampl15;
Trace, Ampl16;
Trace, Ampl17;
Trace, Ampl18;
Trace, Ampl19;
Trace, Ampl20;
Trace, Ampl21;
Trace, Ampl22;
Trace, Ampl23;

Trace, R1;
Trace, R2;
Trace, R3;
Trace, R4;
Trace, R5;
Trace, R6;
Trace, R7;
Trace, R8;
Trace, R9;
Trace, R10;
Trace, R11;
Trace, R12;
Trace, R13;
Trace, R14;
Trace, R15;
Trace, R16;
Trace, R17;
Trace, R18;
Trace, R19;
Trace, R20;
Trace, R21;
Trace, R22;
Trace, R23;

* Substitute scalar products
id p1.p1 = 0;
id p2.p2 = 0;
id pg.pg = 0;
id p1.p2 = s12/2;
id p1.pg = -s1g/2;
id p2.pg = -s2g/2;

.sort

* Equations for the form factors
L eq1 = Ampl1 - R1;
L eq2 = Ampl2 - R2;
L eq3 = Ampl3 - R3;
L eq4 = Ampl4 - R4;
L eq5 = Ampl5 - R5;
L eq6 = Ampl6 - R6;
L eq7 = Ampl7 - R7;
L eq8 = Ampl8 - R8;
L eq9 = Ampl9 - R9;
L eq10 = Ampl10 - R10;
L eq11 = Ampl11 - R11;
L eq12 = Ampl12 - R12;
L eq13 = Ampl13 - R13;
L eq14 = Ampl14 - R14;
L eq15 = Ampl15 - R15;
L eq16 = Ampl16 - R16;
L eq17 = Ampl17 - R17;
L eq18 = Ampl18 - R18;
L eq19 = Ampl19 - R19;
L eq20 = Ampl20 - R20;
L eq21 = Ampl21 - R21;
L eq22 = Ampl22 - R22;
L eq23 = Ampl23 - R23;

* Express equations in terms of form factors
collect A1, A2, A3, A4, A5, A6, A7;
collect A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23; 

.sort

* Solve the system of equations
Solve eq1, eq2 , eq3 , eq4 , eq5 , eq6 , eq7 for A1, A2, A3, A4, A5, A6, A7;
Solve eq8, eq9 , eq10 , eq11 , eq12 , eq13 , eq14, eq15 , eq16 , eq17 , eq18 , eq19 , eq20, eq21, eq22, eq23 for A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23;

* Output form factors to the file
write form_factors.txt, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23;
.end
