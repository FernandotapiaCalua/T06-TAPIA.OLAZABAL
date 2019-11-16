import os

#INPUT
cantidad_de_calor=  float(os.sys.argv[1])
trabajo=  float(os.sys.argv[2])

#PROCESSING
variacion_de_energia_interna= cantidad_de_calor*trabajo

#OUTPUT
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%% VARIACION DE LA ENERGIA INTERNA %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("cantidad de calor:", cantidad_de_calor,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("trabajo:", trabajo,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("variacion de energia interna:", variacion_de_energia_interna,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion doble
if (variacion_de_energia_interna<13):
    print("la variacion es la correcta")
else:
    print("la variacion no es la correcta")
