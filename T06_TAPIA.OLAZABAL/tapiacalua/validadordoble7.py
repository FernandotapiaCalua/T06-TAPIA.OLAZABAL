import os

#INPUT
coeficiente_de_roce= float(os.sys.argv[1])
fuerza_normal= float(os.sys.argv[1])

#PROCESSING
fuerza_de_friccion= coeficiente_de_roce*fuerza_normal

#OUTPUT
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%% FUERZA DE FRICCION %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("coeficiente de roce:", coeficiente_de_roce)
print("fuerza normal:", fuerza_normal)
print("fuerza de friccion:", fuerza_de_friccion)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion doble
if (fuerza_de_friccion>45.8):
    print("la fuerza es la maxima")
else:
    print("la fuerza es la minima")
