import os
#INPUT
pi= float(os.sys.argv[1])
radio_menor= float(os.sys.argv[2])
radio_mayor= float(os.sys.argv[3])
generatriz= float(os.sys.argv[4])

#PROCESSING
area_lateral=(pi*(radio_menor+radio_mayor)*generatriz)

#OUTPUT
print("##############################################")
print("############### AREA LATERAL ##############")
print("##############################################")
print("########### pi:", pi, "###############")
print("########### radio menor:", radio_menor, "#################")
print("########### radio mayor:", radio_mayor, "###################")
print("######## generatriz:", generatriz, "###########")
print("########## area lateral:", area_lateral, "###############")
print("##############################################")

#CONDICION SIMPLE
if (area_lateral<123):
    print("El area lateral es aceptable")

else:
    print("La variación no es la correcta")
