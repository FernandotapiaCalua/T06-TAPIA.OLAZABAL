import os

#INPUT
pi= float(os.sys.argv[1])
radio= float(os.sys.argv[2])
angulo= float(os.sys.argv[3])

#PROCESSING
volumen_cuña_esferica=(4/3*((pi*radio**3)/360)*angulo)

#OUTPUT
print("#############################################################################################")
print("############################ VOLUMEN DE LA CUÑA ESFERICA ####################################")
print("#############################################################################################")
print("######## pi:", pi,                       "###################################################")
print("######## radio:"        , radio,         "###################################################")
print("######## angulo:"       , angulo,        "###################################################")
print("######## volumen:"      , volumen_cuña_esferica,          "##################################")
print("#############################################################################################")

#CONDICION DOBLE
if (volumen_cuña_esferica>129):
    print("el volumen de la cuña esferica es la maxima")
else:
    print("el volumen de la cuña esferica es la minima")
