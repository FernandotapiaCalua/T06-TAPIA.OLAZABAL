import os
#INPUT
base= float(os.sys.argv[1])
radio= float(os.sys.argv[2])
pi= float(os.sys.argv[3])
altura= float(os.sys.argv[4])
#PROCESSING
area=(pi*(radio**2)*altura)

#OUTPUT
print("##############################################")
print("############### AREA DEL CONO ##############")
print("##############################################")
print("########### base:", base, "###############")
print("########### radio:", radio, "#################")
print("############### pi:", pi, "###################")
print("######## area del cono:", area, "###########")
print("##############################################")

#CONDICION SIMPLE
if (area==600):
    print("El area del cono es aceptable")

else:
    print("La variación no es la correcta")
