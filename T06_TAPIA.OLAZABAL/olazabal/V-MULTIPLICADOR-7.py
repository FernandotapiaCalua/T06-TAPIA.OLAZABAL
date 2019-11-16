import os

#INPUT
area_lateral= float(os.sys.argv[1])
area_base_menor= float(os.sys.argv[2])
area_base_mayor= float(os.sys.argv[3])

#PROCESSING
area_total=(area_lateral+area_base_menor+area_base_mayor)

#OUTPUT
print("#############################################################################################")
print("########################### AREA TRONCO DEL TRONCO PIRAMIDE #################################")
print("#############################################################################################")
print("######## area lateral:",    area_lateral,            "#######################################")
print("######## area base menor:", area_base_menor,         "#######################################")
print("######## area base mayor:", area_base_mayor,         "#######################################")
print("######## area total:"     , area_total,              "#######################################")
print("#############################################################################################")

#CONDICION DOBLE
if (area_total>690):
    print("el area total del tronco piramide es la maxima")
if (area_total<15):
    print("el area total del tronco piramide es el minimo")
else:
    print("el area total del tronco piramide es la minima")
