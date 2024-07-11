Dimension d;

* Definition of vectors
V p1, p2, pV, k1, k2;

* Definition of the vertex
V A;

* Definition of scalar quantities
S C12, C34, mu02, mV2, pi, e, CF, CA, Nf;
S A1, A2, A3;

* Definition of indices
Index mu, num rho, sigma, alpha, beta;

* Definition of spinors
C Up1, Ubarp1, Up2, Ubarp2;

* Additional trace
L tr = g_(1, nu, k1 - k2, rho, k2);

Trace, tr;

* Propagators Topology 1
L D1 = k1^2;
L D2 = (p1 + k1)^2;
L D3 = (p2 - k1)^2;
L D4 = k2^2;
L D5 = (p1 + k2)^2;
L D6 = (p2 - k2)^2;
L D7 = (k1 - k2)^2;

* Propagators Topology 2
L Dt1 = k1^2;
L Dt2 = (p1 + k1)^2;
L Dt3 = (p2 - k2)^2;
L Dt4 = k2^2;
L Dt5 = (p1 + k1 + k2)^2;
L Dt6 = (p2 - k1 - k2)^2;
L Dt7 = (k1 + k2)^2;

* Diagrams
L M1(mu) = 64*pi^4*CF*CA*mu02^(2*e)*Ubarp2*g_(1, nu, p2 - k1)*A(mu)*g_(1, rho)*(d_(alpha, nu)*(k1(beta) + k2(beta)) + d_(alpha, beta)*(k1(nu) - 2*k2(nu)) + d_(beta, nu)*(-2*k1(alpha) + k2(alpha)))*(d_(alpha, beta)*(k1(rho) + k2(rho)) + d_(alpha, rho)*(k1(beta) - 2*k2(beta)) + d_(beta, rho)*(-2*k1(alpha) + k2(alpha)))*Up1/(D1^2*D2*D3*D4*D7);
L M2(mu) = 64*pi^4*CF*Nf*mu02^(2*e)*Ubarp2*g_(1, nu, p2 - k1)*A(mu)*g_(1, p1 + k1, rho)*tr*Up1/(D1^2*D2*D3*D4*D7);
L M3(mu) = 64*pi^4*CF*CA*mu02^(2*e)*Ubarp2*g_(1, k1, p2 - k1)*A(mu)*g_(1, p1 + k1, k1)*Up1/(D1^2*D2*D3*D4*D7);
L M4(mu) = -64*pi^4*CF^2*mu02^(2*e)*Ubarp2*g_(1, nu, p2 - k1, sigma, p2 - k1 - k2)*A(mu)*g_(1, p1 + k1 + k2, sigma, p1 + k1, nu)*Up1/(D1*D2*D3*D4*D5*D6);
L M5(mu) = 64*pi^4*CF/(2*CA)*mu02^(2*e)*Ubarp2*g_(1, nu, p2 - k2, sigma, p2 - k1 - k2)*A(mu)*g_(1, p1 + k1 + k2, nu, p1 + k1, sigma)*Up1/(Dt1*Dt2*Dt3*Dt4*Dt5*Dt6);
L M6(mu) = 64*pi^4*CF^2*mu02^(2*e)*Ubarp2*g_(1, nu, p2 - k1, sigma, p2 - k1 - k2, sigma, p2 - k1)*A(mu)*g_(1, p1 + k1, nu)*Up1/(D1*D2*D3^3*D4*D6);
L M7(mu) = 64*pi^4*CF^2*mu02^(2*e)*Ubarp2*g_(1, nu, p2 - k1)*A(mu)*g_(1, p1 + k1, sigma, p1 + k1 + k2, sigma, p1 + k1, nu)*Up1/(D1*D2^2*D3*D4*D5);
L M8(mu) = 64*pi^4*CF*CA/2*mu02^(2*e)*Ubarp2*g_(1, nu, p2 - k2, rho, p2 - k1 - k2)*A(mu)*g_(1, p1 + k1 + k2, sigma)*(d_(nu, rho)*(-k1(sigma) + k2(sigma)) + d_(rho, sigma)*(2*k1(nu) + k2(nu)) + d_(nu, sigma)*(-k1(rho) - 2*k2(rho)))*Up1/(Dt1*Dt3*Dt4*Dt5*Dt6*Dt7);
L M9(mu) = -64*pi^4*CF*CA/2*mu02^(2*e)*Ubarp2*g_(1, nu, p2 - k1 - k2)*A(mu)*g_(1, p1 + k1 + k2, rho, p1 + k1, sigma)*(d_(nu, rho)*(k1(sigma) + 2*k2(sigma)) + d_(rho, sigma)*(k1(nu) - k2(nu)) + d_(nu, sigma)*(-2*k1(rho) - 2*k2(rho)))*Up1/(Dt1*Dt2*Dt4*Dt5*Dt6*Dt7);
L M10(mu) = 64*pi^4*CF/(2*CA)*mu02^(2*e)*Ubarp2*g_(1, nu, k2, sigma, k1, nu, p2 - k1 - k2)*A(mu)*g_(1, p1 + k1 + k2, sigma)*Up1/(Dt1*Dt3*Dt4*Dt5*Dt6*Dt7);
L M11(mu) = 64*pi^4*CF/(2*CA)*mu02^(2*e)*Ubarp2*g_(1, nu, p2 - k1 - k2)*A(mu)*g_(1, p1 + k1 + k2, sigma, k2, nu, k1, sigma)*Up1/(Dt1*Dt2*Dt4*Dt5*Dt6*Dt7);

* Total amplitude
L M(mu) = M1(mu) + M2(mu) + M3(mu) + M4(mu) + M5(mu) + M6(mu) + M7(mu) + M8(mu) + M9(mu) + M10(mu) + M11(mu);

* Substituting the vertex
id A(mu) = C12*(g_(1, mu)*g_(1, pV) - g_(1, pV)*g_(1, mu)) + C34*g_(1, mu);

.sort

* Contracted amplitudes
L Ampl1 = M(mu)*Ubarp1*p1(mu)*Up2;
L Ampl2 = M(mu)*Ubarp1*g_(1, mu)*g_(1, pV)*Up2;
L Ampl3 = M(mu)*Up2*g_(1, mu)*Ubarp1;

* Substitute spinors with gamma matrices
id Ubarp1 = g_(1, p1)/Up1;
id Ubarp2 = 1;
id Up2 = 1;
Ampl1 = g_(1, p2) * Ampl1;
Ampl2 = g_(1, p2) * Ampl2;
Ampl3 = g_(1, p2) * Ampl3;

* Compute traces
Trace, Ampl1;
Trace, Ampl2;
Trace, Ampl3;

* Substitute scalar products
id p1.p1 = 0;
id p2.p2 = 0;
id p1.p2 = s12/2;

.sort

L eq1 = Ampl1 - p1.pV*s12*(s12*A2 - 2*A1);
L eq2 = Ampl2 - A1*(8*(d-2)*p1.pV*p2.pV + 2*(3-d)*s12*mV2) - 8*A2*s12*p1.pV*p2.pV;

* Express equations in terms of A1 and A2
collect A1, A2;

.sort

* Solve the system of equations
Solve eq1, eq2 for A1, A2;

L A3 = Ampl3 / (2*(2-d)*s12);

* Output form factors
print A1, A2, A3;
.end
