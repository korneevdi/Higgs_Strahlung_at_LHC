(* Created with the Wolfram Language : www.wolfram.com *)
(Wprop*(H[angle, 3, 1]*H[angle, 5, 2]*H[square, 1, 4]*
    (2*FF[3]*H[square, 1, R] + H[square, 1, 5]*
      (FF[6]*H[angle, 1, 5]*H[square, R, 1] + FF[7]*H[angle, 2, 5]*
        H[square, R, 2])) + H[angle, 3, 2]*
    (2*H[square, 1, 4]*(FF[1]*H[angle, 1, 5]*H[square, R, 1] + 
       FF[2]*H[angle, 2, 5]*H[square, R, 2]) + H[angle, 5, 2]*H[square, 2, 4]*
      (2*FF[4]*H[square, 1, R] + H[square, 1, 5]*
        (FF[8]*H[angle, 1, 5]*H[square, R, 1] + FF[9]*H[angle, 2, 5]*
          H[square, R, 2]))) + H[angle, 5, 2]*
    (4*FF[13]*H[angle, 5, 3]*H[square, 1, 5]*H[square, 4, 5] + 
     H[angle, 3, 5]*(2*FF[5]*H[square, 1, R]*H[square, 5, 4] + 
       H[square, 1, 5]*(FF[10]*H[angle, 1, 5]*H[square, 5, 4]*
          H[square, R, 1] + FF[11]*H[angle, 2, 5]*H[square, 5, 4]*
          H[square, R, 2] + 2*FF[12]*H[square, R, 4])))))/
 (Sqrt[2]*H[square, 5, R])
