import os
#INPUT
altura= float(os.sys.argv[1])
radio= float(os.sys.argv[2])
pi= float(os.sys.argv[3])

#PROCESSING
area=2*(pi*radio*altura)

#OUTPUT
print("##############################################")
print("############### AREA LATERAL DEL CILINDRO ##############")
print("##############################################")
print("########### altura:", altura, "###############")
print("########### radio:", radio, "#################")
print("############### pi:", pi, "###################")
print("######## area lateral del cilindro:", area, "###########")
print("##############################################")

#CONDICION SIMPLE
if (area==400) :
    print("El area lateral del cilindro es aceptable")

else:
    print("La variación no es la correcta")
