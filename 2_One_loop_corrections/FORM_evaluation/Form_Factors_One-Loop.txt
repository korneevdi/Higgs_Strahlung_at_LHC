Dimension d;

* Definition of vectors
V p1, p2, pV, k;

* Definition of the vertex
V A;

* Definition of scalar quantities
S C12, C34, mu02, mV2, pi, e, CF;
S A1, A2, A3;

* Definition of indices
Index mu, nu;

* Definition of spinors
C Up1, Ubarp1, Up2, Ubarp2;

* Amplitude
L M(mu) = 8*pi^2*CF*mu02^e*Ubarp2*g_(1, nu)*g_(1, p2 - k)*A(mu)*g_(1, p1 + k)*g_(1, nu)*Up1 / (k^2*(p1 + k)^2*(p2 - k)^2);

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
