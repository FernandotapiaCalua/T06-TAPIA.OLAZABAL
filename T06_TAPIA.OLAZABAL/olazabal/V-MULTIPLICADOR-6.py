import os

#INPUT
semiperimetro_menor= float(os.sys.argv[1])
semiperimetro_mayor= float(os.sys.argv[2])
altura= float(os.sys.argv[3])

#PROCESSING
area_lateral=(altura*(semiperimetro_menor+semiperimetro_mayor)/2)

#OUTPUT
print("#############################################################################################")
print("########################## AREA LATERAL DEL TRONCO PIRAMIDE #################################")
print("#############################################################################################")
print("######## semiperimetro menor:", semiperimetro_menor, "#######################################")
print("######## semiperimetro mayor:", semiperimetro_mayor, "#######################################")
print("######## altura:"             , altura,              "#######################################")
print("######## area lateral:"       , area_lateral,        "#######################################")
print("#############################################################################################")

#CONDICION DOBLE
if (area_lateral>80):
    print("el area lateral del tronco piramide es la maxima")
if (area_lateral<1):
    print("el area lateral del tronco piramide es el minimo")
else:
    print("el area lateral del tronco piramide es la minima")
