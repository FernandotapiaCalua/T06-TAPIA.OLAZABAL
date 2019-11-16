import os

#INPUT
Base= float(os.sys.argv[1])
Altura= float(os.sys.argv[2])

#PROCESSING
area= (Base*Altura)/2

#OUTPUT
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%% AREA DEL TRIANGULO %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%% Base:", Base,"%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%% Altura:", Altura, "%%%%%%%%%%%%%%%%")
print("%%%%%%%%% Area:", area, "%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion simple
if (area>12):
    print("el area es incorrecta")
#fin_si
