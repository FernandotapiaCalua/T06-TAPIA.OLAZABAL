import os

#INPUT
base= float(os.sys.argv[1])
altura= float(os.sys.argv[2])
pi= float(os.sys.argv[3])

#PROCESSING
area_del_elipse= base*altura*pi

#OUTPUT
print("##############################################")
print("############### AREA DEL ELIPSE ##############")
print("##############################################")
print("########### base:", base, "###############")
print("########### altura:", altura, "#################")
print("############### pi:", pi, "###################")
print("######## area del elipse:", area_del_elipse, "###########")
print("##############################################")

#CONDICION SIMPLE
if (area_del_elipse == 150):
    print("El area del elipse es aceptable")

else:
    print("La variación no es la correcta")
