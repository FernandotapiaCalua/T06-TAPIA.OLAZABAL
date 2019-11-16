import os
#INPUT
base= float(os.sys.argv[1])
espesor= float(os.sys.argv[2])
altura= float(os.sys.argv[3])

#PROCESSING
volumen_paralelepipedo= (base*altura*espesor)

#OUTPUT
print("##############################################")
print("############### VOLUMEN DEL PARALELEPIPEDO ##############")
print("##############################################")
print("########### base:", base, "###############")
print("########### espesor:", espesor, "#################")
print("############### altura:", altura, "###################")
print("######## volumen del paralelepipedo:", volumen_paralelepipedo, "###########")
print("##############################################")

#CONDICION SIMPLE
if (volumen_paralelepipedo>200) :
    print("El volumen del paralelepipedo es aceptable")

else:
    print("La variación no es la correcta")
