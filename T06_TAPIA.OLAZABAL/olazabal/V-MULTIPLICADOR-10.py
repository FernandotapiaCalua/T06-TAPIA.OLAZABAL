import os

#INPUT
pi= float(os.sys.argv[1])
radio= float(os.sys.argv[2])
altura= float(os.sys.argv[3])

#PROCESSING
area_zona_esferica=(4/3*((pi*radio**3)/360)*altura)

#OUTPUT
print("#############################################################################################")
print("############################## AREA DE LA ZONA ESFERICA #####################################")
print("#############################################################################################")
print("######## pi:", pi,                       "###################################################")
print("######## radio:"        , radio,         "###################################################")
print("######## altura:"       , altura,        "###################################################")
print("######## volumen:"      , area_zona_esferica,          "#####################################")
print("#############################################################################################")

#CONDICION DOBLE
if (area_zona_esferica>1301):
    print("el area de la zona esferica es la maxima")
if (area_zona_esferica<1):
    print("el area de la zona esferica el la minima")
else:
    print("el area de la zona esderica es la minima")
