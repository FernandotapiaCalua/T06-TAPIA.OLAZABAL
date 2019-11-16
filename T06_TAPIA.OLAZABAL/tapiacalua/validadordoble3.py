import os

#INPUT
velocidad= float(os.sys.argv[1])
radio= float(os.sys.argv[2])

#PROCESSING
aceleracion_centripeta= (velocidad**2)/radio

#OUTPUT
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%% ACELERACION CENTRIPETA %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("velocidad:", velocidad,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("radio:", radio,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("aceleracion centripeta:", aceleracion_centripeta,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion doble
if (aceleracion_centripeta>80):
    print("la aceleracion es la correcta")
else:
    print(" la aceleracion no es la correcta")
