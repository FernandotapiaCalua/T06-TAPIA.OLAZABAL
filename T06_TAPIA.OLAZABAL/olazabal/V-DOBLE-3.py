import os

#INPUT
coef_de_rozamiento= float(os.sys.argv[1])
la_normal= float(os.sys.argv[2])

#PROCESSING
fuerza_de_rozamiento= coef_de_rozamiento*la_normal

#OUTPUT
print("#############################################################################################")
print("############################### FUERZA DE ROZAMIENTNO #######################################")
print("###############################################")
print("######## coeficiente de rozamiento:", coef_de_rozamiento, "##################################")
print("######## fuerza normal:",             la_normal,      "##################################")
print("######## fuerza de rozamiento:", fuerza_de_rozamiento,      "##################################")
print("#############################################################################################")

#CONDICION DOBLE
if (fuerza_de_rozamiento>7463):
    print("la fuerza es la maxima")
else:
    print("la fuerza es la minima")
