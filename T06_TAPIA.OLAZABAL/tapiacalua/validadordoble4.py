import os

#INPUT
fuerza= float(os.sys.argv[1])
area= float(os.sys.argv[2])

#PROCESSING
presion= fuerza/area

#OUTPUT
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%% ACELERACION CENTRIPETA %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("fuerza:", fuerza)
print("area:", area)
print("presion:", presion)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion doble
if (presion<2.3):
    print("la presion es la correcta")
else:
    print(" la presion no es la correcta")

