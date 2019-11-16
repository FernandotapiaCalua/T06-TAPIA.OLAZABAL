import os
#INPUT
base= float(os.sys.argv[1])
radio= float(os.sys.argv[2])
pi= float(os.sys.argv[3])
altura= float(os.sys.argv[4])
#PROCESSING
area_total=(2*pi*radio*(altura+radio))

#VALIDADOR
validador_area_total=(area_total==700)

#OUTPUT
print("##############################################")
print("############### AREA TOTAL DEL CILINDRO ##############")
print("##############################################")
print("########### base:", base, "###############")
print("########### radio:", radio, "#################")
print("############### pi:", pi, "###################")
print("######## area total del cilindro:", area_total, "###########")
print("##############################################")

#CONDICION SIMPLE
if (validador_area_total==True) :
    print("El area total del cilindro es aceptable")

else:
    print("La variación no es la correcta")
