import os
#INPUT
generatriz= float(os.sys.argv[1])
radio= float(os.sys.argv[2])
pi= float(os.sys.argv[3])

#PROCESSING
area_lateral=(pi*radio*generatriz)

#OUTPUT
print("##############################################")
print("############### AREA LATERAL DEL CONO ##############")
print("##############################################")
print("########### generatriz:", generatriz, "###############")
print("########### radio:", radio, "#################")
print("############### pi:", pi, "###################")
print("######## area lateral del cono:", area_lateral, "###########")
print("##############################################")

#CONDICION SIMPLE
if (area_lateral==73519) :
    print("El area lateral del cono es aceptable")

else:
    print("La variación no es la correcta")
