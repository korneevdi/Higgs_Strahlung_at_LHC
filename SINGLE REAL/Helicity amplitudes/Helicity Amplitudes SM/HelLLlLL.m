(* Created with the Wolfram Language : www.wolfram.com *)
(Wprop*(2*H[angle, 1, 3]*H[square, 4, 2]*
    (FF[1]*H[angle, 1, 5]*H[square, R, 1] + FF[2]*H[angle, 2, 5]*
      H[square, R, 2]) + H[angle, 1, 5]*
    (H[angle, 1, 5]*H[square, 5, 2]*(FF[6]*H[angle, 3, 1]*H[square, 1, 4] + 
       FF[8]*H[angle, 3, 2]*H[square, 2, 4] + FF[10]*H[angle, 3, 5]*
        H[square, 5, 4])*H[square, R, 1] + 2*FF[4]*H[angle, 3, 2]*
      H[square, 2, 4]*H[square, R, 2] + FF[9]*H[angle, 2, 5]*H[angle, 3, 2]*
      H[square, 2, 4]*H[square, 5, 2]*H[square, R, 2] + 
     H[angle, 3, 1]*H[square, 1, 4]*(2*FF[3] + FF[7]*H[angle, 2, 5]*
        H[square, 5, 2])*H[square, R, 2] + 2*FF[5]*H[angle, 3, 5]*
      H[square, 5, 4]*H[square, R, 2] + 4*FF[13]*H[angle, 3, 5]*
      H[square, 5, 4]*H[square, R, 2] + FF[11]*H[angle, 2, 5]*H[angle, 3, 5]*
      H[square, 5, 2]*H[square, 5, 4]*H[square, R, 2] + 
     2*FF[12]*H[angle, 3, 5]*H[square, 5, 2]*H[square, R, 4])))/
 (Sqrt[2]*H[square, 5, R])
