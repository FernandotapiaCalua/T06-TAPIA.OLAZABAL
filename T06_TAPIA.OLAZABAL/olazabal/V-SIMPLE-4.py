import os
#INPUT
pi= float(os.sys.argv[1])
area_base= float(os.sys.argv[2])
altura= float(os.sys.argv[3])

#PROCESSING
volumen_del_cilindro=(pi*area_base*altura)

#OUTPUT
print("##############################################")
print("############### VOLUMEN DEL CILINDRO ##############")
print("##############################################")
print("########### pi:", pi, "###############")
print("########### area de la base:", area_base, "#################")
print("############### altura:", altura, "###################")
print("######## volumen del cilindro:", volumen_del_cilindro, "###########")
print("##############################################")

#CONDICION SIMPLE
if (volumen_del_cilindro==789) :
    print("El volumen del paralelepipedo es aceptable")

else:
    print("La variación no es la correcta")
