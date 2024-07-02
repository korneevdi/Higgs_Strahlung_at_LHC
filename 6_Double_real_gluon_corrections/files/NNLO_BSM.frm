*** Spinor helicity amplitudes for 0->qb(j1) q(j2) W(->l(j3) lb(j4)) H  ***
*** NNLO_BSM

f  LepCurr, WqqbVertex, Q2prop, Q3prop, gqqbarVertex, gqqbarLeftVertex, gqqbarRightVertex, gammaGluonL, gammaGluonR, BSMcoupl, gggVertexLL, gggVertexLR, gggVertexRL, gggVertexRR, gamma, Bra, Ket, Ket1, Bra2;        *** Non-commuting functions
cf Wprop, g, WHVertex za(antisymmetric), zb(antisymmetric), [za^-1](antisymmetric), [zb^-1](antisymmetric), zab, [denWprop^-1], [denQ3prop^-1], [gL.p], [gR.p], [gL.gL], [gL.gR], [gR.gR], PL1, PL2, PR1, PR2;         *** Commuting functions
V  j1, j2, j3, j4, j5, j6, q, k, r3, r4;                                						                                                 							                                           *** Vectors
S  Mw, gw, [v^-1], gs, Vud, Tg3, Tg4, A, B, C, D, sqrt2;                        				                                           					  		                                                   *** Symbols (scalars)
I  mu, nu, rho, sigma;                          						                                                              											                                       *** Indices


*** EXPRESSION FROM FEYNMAN DIAGRAMS (Helicity order: quark, antiquark, gluon)

*** Helicity g3 = L, Helicity g4 = L

G [iM1.LLLL] = + Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarLeftVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexLL(j3,r3,j4,r4) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gggVertexLL(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
                           
G [iM1.LRLL] = + Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarLeftVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexLL(j3,r3,j4,r4) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gggVertexLL(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
G [iM1.RLLL] = + Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarLeftVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexLL(j3,r3,j4,r4) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gggVertexLL(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
G [iM1.RRLL] = + Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarLeftVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexLL(j3,r3,j4,r4) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gggVertexLL(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);        
               
               
               
               
               
*** Helicity g3 = L, Helicity g4 = R               
               
G [iM1.LLLR] = + Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarLeftVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexLR(j3,r3,j4,r4) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gggVertexLR(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
G [iM1.LRLR] = + Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarLeftVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexLR(j3,r3,j4,r4) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gggVertexLR(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
G [iM1.RLLR] = + Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarLeftVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexLR(j3,r3,j4,r4) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gggVertexLR(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
G [iM1.RRLR] = + Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarLeftVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarLeftVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexLR(j3,r3,j4,r4) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gggVertexLR(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
               
               
               
               
*** Helicity g3 = R, Helicity g4 = L

G [iM1.LLRL] = + Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarRightVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexRL(j3,r3,j4,r4) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gggVertexRL(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
G [iM1.LRRL] = + Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarRightVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexRL(j3,r3,j4,r4) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gggVertexRL(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
              
G [iM1.RLRL] = + Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarRightVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexRL(j3,r3,j4,r4) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gggVertexRL(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu); 
               
G [iM1.RRRL] = + Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarRightVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * gqqbarLeftVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexRL(j3,r3,j4,r4) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gggVertexRL(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu); 

               
               
               
                              
*** Helicity g3 = R, Helicity g4 = R

G [iM1.LLRR] = + Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarRightVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexRR(j3,r3,j4,r4) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gggVertexRR(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
G [iM1.LRRR] = + Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarRightVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexRR(j3,r3,j4,r4) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gggVertexRR(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,-1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
G [iM1.LRRR] = + Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarRightVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,-1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexRR(j3,r3,j4,r4) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,-1) * gggVertexRR(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               
G [iM1.RRRR] = + Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * gqqbarRightVertex(j3,r3,Tg3) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * gqqbarRightVertex(j4,r4,Tg4) * Q2prop(j2,j4) * BSMcoupl(mu,k) * Q2prop(j1,j3) * gqqbarRightVertex(j3,r3,Tg3) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               - Bra2(j2,+1) * BSMcoupl(mu,k) * Q3prop(j1,j3,j4) * gggVertexRR(j3,r3,j4,r4) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu)
               + Bra2(j2,+1) * gggVertexRR(j3,r3,j4,r4) * Q3prop(j2,j3,j4) * BSMcoupl(mu,k) * Ket1(j1,+1) * Wprop(k,mu,nu) * LepCurr(j5,j6,nu);
               


            
             
*** BSM WH-COUPLING to qqb LINE 
id BSMcoupl(mu?,k?) = A*PL2*(gamma(mu)*gamma(k) - gamma(k)*gamma(mu))*PL1 + B*PR2*(gamma(mu)*gamma(k) - gamma(k)*gamma(mu))*PR1 + C*PR2*gamma(mu)*PL1 + D*PL2*gamma(mu)*PR1;


*** QUARK-ANTIQUARK-W VERTEX
id WqqbVertex(mu?) = i_* gw/sqrt2 * Vud * PR2 * gamma(mu) * PL1; 


*** W PROPAGATOR
**id Wprop(q?,mu?,nu?)= - i_ * (g(mu,nu) - q(mu) * q(nu)/Mw^2) * [denWprop^-1](q);		*** [denWprop^-1](q) = [q^2 - Mw^2]^-1;
**id Wprop(q?,mu?,nu?) = + i_ * q(mu) * q(nu)/Mw^2 * [denWprop^-1](q);
id Wprop(q?,mu?,nu?) = - i_ * g(mu,nu) * [denWprop^-1](q);


*** QUARK-ANTIQUARK-GLUON LEFT/RIGHT VERTEX
id gqqbarLeftVertex(j3?,r3?,Tg3?) = + i_* gs * Tg3 * gammaGluonL(j3,r3);      *** j1 = gluon momentum, r = gluon polarization
id gqqbarRightVertex(j3?,r3?,Tg3?) = + i_* gs * Tg3 * gammaGluonR(j3,r3);     *** j1 = gluon momentum, r = gluon polarization


*** TRIPLE GLUON VERTEX
id gggVertexLL(j3?,r3?,j4?,r4?) = i_ * gs^2 * Tg4 * Tg3 * [za^-1](j3,j4) * [zb^-1](j4,j3) * (+2 * gammaGluonL(j3,r3) * [gL.p](j4,r4,j3) - 2 * gammaGluonL(j4,r4) * [gL.p](j3,r3,j4) - [gL.gL](j3,r3,j4,r4) * (gamma(j3) - gamma(j4)));
id gggVertexLR(j3?,r3?,j4?,r4?) = i_ * gs^2 * Tg4 * Tg3 * [za^-1](j3,j4) * [zb^-1](j4,j3) * (+2 * gammaGluonL(j3,r3) * [gR.p](j4,r4,j3) - 2 * gammaGluonR(j4,r4) * [gL.p](j3,r3,j4) - [gL.gR](j3,r3,j4,r4) * (gamma(j3) - gamma(j4)));
id gggVertexRL(j3?,r3?,j4?,r4?) = i_ * gs^2 * Tg4 * Tg3 * [za^-1](j3,j4) * [zb^-1](j4,j3) * (+2 * gammaGluonR(j3,r3) * [gL.p](j4,r4,j3) - 2 * gammaGluonL(j4,r4) * [gR.p](j3,r3,j4) - [gL.gR](j4,r4,j3,r3) * (gamma(j3) - gamma(j4)));
id gggVertexRR(j3?,r3?,j4?,r4?) = i_ * gs^2 * Tg4 * Tg3 * [za^-1](j3,j4) * [zb^-1](j4,j3) * (+2 * gammaGluonR(j3,r3) * [gR.p](j4,r4,j3) - 2 * gammaGluonR(j4,r4) * [gR.p](j3,r3,j4) - [gR.gR](j3,r3,j4,r4) * (gamma(j3) - gamma(j4)));


id [gL.p](j3?,r3?,j4?) = - 1/sqrt2 * za(j4,j3) * zb(r3,j4) * [zb^-1](r3,j3);			       *** (Left-gluon vector polarization)(j3) x j4 
id [gR.p](j3?,r3?,j4?) = 1/sqrt2 * za(r3,j4) * zb(j4,j3) * [za^-1](r3,j3);                     *** (Right-gluon vector polarization)(j3) x j4 
id [gL.gL](j3?,r3?,j4?,r4?) = za(j4,j3) * zb(r3,r4) * [zb^-1](r3,j3) * [zb^-1](r4,j4);         *** (Left-gluon vector polarization)(j3) x (Left-gluon vector polarization)(j4)
id [gL.gR](j3?,r3?,j4?,r4?) = - za(r4,j3) * zb(r3,j4) * [za^-1](r4,j4) * [zb^-1](r3,j3);       *** (Left-gluon vector polarization)(j3) x (Right-gluon vector polarization)(j4)
id [gR.gR](j3?,r3?,j4?,r4?) = za(r3,r4) * zb(j4,j3) * [za^-1](r3,j3) * [za^-1](r4,j4);         *** (Right-gluon vector polarization)(j3) x (Right-gluon vector polarization)(j4)

id gammaGluonL(j3?,r3?) = - sqrt2 * (Ket(r3,-1) * Bra(j3,-1) + Ket(j3,+1) * Bra(r3,+1)) * [zb^-1](r3,j3);      *** - sqrt2 * (|r3]<j3| + |j3>[r3|) / [r3 j3]
id gammaGluonR(j3?,r3?) = + sqrt2 * (Ket(j3,-1) * Bra(r3,-1) + Ket(r3,+1) * Bra(j3,+1)) * [za^-1](r3,j3);	   *** + sqrt2 * (|j3]<r3| + |r3>[j3|) / <r3 j3>


*** QUARK PROPAGATORS
id Q2prop(j1?,j2?) = i_ * (gamma(j1) + gamma(j2)) * [za^-1](j1,j2) * [zb^-1](j2,j1);
id Q3prop(j1?,j2?,j3?) = i_ * (gamma(j1) + gamma(j2) + gamma(j3)) * [denQ3prop^-1](j1,j2,j3);		*** [denQ3prop^-1](j1,j2,j3) = [j1 + j2 + j3]^-2;


*** W-HIGGS VERTEX
id WHVertex(mu?,nu?) = i_ * 2 * Mw^2*[v^-1] * g(mu,nu);


*** LEPTONIC CURRENT W->l(j5) lb(j6) 
id LepCurr(j1?,j2?,nu?) = i_*gw/sqrt2 * Bra(j1,-1) * gamma(nu) * Ket(j2,-1);


*** LEFT and RIGHT PROJECTORS (PL/PR) rules
id PL1 * Ket1(j1,+1) = 0;
id PL1 * Ket1(j1,-1) = Ket(j1,-1);
id PR1 * Ket1(j1,+1) = Ket(j1,+1);
id PR1 * Ket1(j1,-1) = 0;
id Bra2(j2,+1) * PL2 = Bra(j2,+1);
id Bra2(j2,-1) * PL2 = 0;
id Bra2(j2,+1) * PR2 = 0;
id Bra2(j2,-1) * PR2 = Bra(j2,-1);


*** USE g^{mu,nu} gamma_nu = gamma^{mu}
repeat;
id g(mu?,rho?) * g(rho?,nu?) = g(mu,nu);
id g(mu?,nu?) * gamma(nu?) = gamma(mu);
id q?(mu?) * gamma(mu?) = gamma(q);
endrepeat;
id gamma(q) = - gamma(j1) - gamma(j2) - gamma(j3) - gamma(j4);
id gamma(k) = + gamma(j5) + gamma(j6);


*** DIRAC EQUATION
id gamma(j1?) * Ket(j1?,+1) = 0;
id gamma(j1?) * Ket(j1?,-1) = 0;
id Bra(j1?,+1) * gamma(j1?) = 0;
id Bra(j1?,-1) * gamma(j1?) = 0;


*** GAMMA BRAKET WRITING and CONDITIONS
repeat;
id gamma(j1?) = Ket(j1,-1) * Bra(j1,-1) + Ket(j1,+1) * Bra(j1,+1);
endrepeat;


*** CREATION OF <1|mu|2] and [1|mu|2>
id Bra(j1?,-1) * gamma(mu?) * Ket(j2?,-1) = zab(j1,mu,j2);		*** <1|mu|2]
id Bra(j1?,+1) * gamma(mu?) * Ket(j2?,+1) = zab(j2,mu,j1);		*** [1|mu|2> = <2|mu|1]
id Bra(j1?,-1) * gamma(mu?) * Ket(j2?,+1) = 0;
id Bra(j1?,+1) * gamma(mu?) * Ket(j2?,-1) = 0;


*** CONDITIONS ON Bra-Ket
id Bra(j1?,-1) * Ket(j2?,-1) = 0;				*** <12] = 0
id Bra(j1?,+1) * Ket(j2?,+1) = 0;				*** [12> = 0
id Bra(j1?,+1) * Ket(j1?,-1) = 0;	    		*** [11] = 0
id Bra(j1?,-1) * Ket(j1?,+1) = 0;	    		*** <11> = 0	
id Bra(j1?,-1) * Ket(j2?,+1) = za(j1,j2);		*** <12> 
id Bra(j1?,+1) * Ket(j2?,-1) = zb(j1,j2);		*** [12] 


*** FIERZ 
id zab(j1?,mu?,j2?) * zab(j3?,mu?,j4?) = 2 * za(j1,j3) * zb(j4,j2); 	*** <1|mu|2] <3|mu|4] = 2 <13> [42]


*** FIX THE DENOMINATORS AND SIMPLIFICATIONS
id [za^-1](j1?,j2?) * za(j1?,j2?) = 1;
id [zb^-1](j1?,j2?) * zb(j1?,j2?) = 1;
id 1/sqrt2 = sqrt2/2;
id sqrt2 * sqrt2 = 2;

id [za^-1](j1?,j2?) = 1/za(j1,j2);
id [zb^-1](j1?,j2?) = 1/zb(j1,j2);


Bracket i_, Mw, [v^-1], gw, gs, Vud, Tg3, Tg4, sqrt2, [denWprop^-1], [denQ3prop^-1], A, B, C, D;


print +s;


.end



