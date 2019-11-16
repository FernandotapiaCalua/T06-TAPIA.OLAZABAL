import os
#INPUT
lado_uno= float(os.sys.argv[1])
lado_dos= float(os.sys.argv[2])
lado_tres= float(os.sys.argv[3])

#PROCESSING
volumen_del_cubo=(lado_uno*lado_dos*lado_tres)

#OUTPUT
print("##############################################")
print("############### VOLUMEN DEL CUBO ##############")
print("##############################################")
print("########### lado uno:", lado_uno, "###############")
print("########### lado dos:", lado_dos, "#################")
print("########## lado tres:", lado_tres, "###################")
print("######## volumen del cubo:", volumen_del_cubo, "###########")
print("##############################################")

#CONDICION SIMPLE
if (volumen_del_cubo==456) :
    print("El volumen del cubo es aceptable")

else:
    print("La variación no es la correcta")
