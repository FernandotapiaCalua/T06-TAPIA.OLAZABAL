import os

#INPUT
diagonal_mayor=  float(os.sys.argv[1])
diagonal_menor=  float(os.sys.argv[2])

#PROCESSING
area= (diagonal_mayor*diagonal_menor)/2

#OUTPUT
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%% AREA %%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%% DIAGONAL MAYOR:", diagonal_mayor)
print("%%%%%%%% DIAGONAL MENOR:", diagonal_menor)
print("%%%%%%%% AREA:", area)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion doble
if (area==45):
    print("el area es la correcta")
else:
    print("el area es la incorrecta")

