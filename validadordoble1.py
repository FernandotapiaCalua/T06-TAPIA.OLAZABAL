import os

#INPUT
masa=  float(os.sys.argv[1])
velocidad=  float(os.sys.argv[2])

#PROCESSING
cantidad_de_movimiento= masa*velocidad

#OUPUT
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%% CANTIDAD DE MOVIMIENTO %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%% MASA:", masa,"%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%% VELOCIDAD:", velocidad, "%%%%%%%%%%%%%%%%")
print("%%%%%%%%% C. DE MOVIMIENTO:", cantidad_de_movimiento, "%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion doble
if (cantidad_de_movimiento>20):
    print("la cantidad de movimiento es aceptable")
else:
    print("la cantidad de movimiento no es aceptable")
