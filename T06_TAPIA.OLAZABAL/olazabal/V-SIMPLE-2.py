#INPUT
base_menor= float(os.sys.argv[1])
base_mayor= float(os.sys.argv[2])
altura= float(os.sys.argv[3])

#PROCESSING
area_del_trapecio= ((base_menor+base_mayor)/2*altura)

#OUTPUT
print("##############################################")
print("############### AREA DEL ELIPSE ##############")
print("##############################################")
print("########### base menor:", base_menor, "###############")
print("########### base mayor:", base_mayor, "#################")
print("############### altura:", altura, "###################")
print("######## area del trapecio:", area_del_trapecio, "###########")
print("##############################################")

#CONDICION SIMPLE
if (area_del_trapecio<800):
    print("El area del trapecio es aceptable")

else:
    print("La variación no es la correcta")
