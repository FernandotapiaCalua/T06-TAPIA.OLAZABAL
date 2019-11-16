import os

#INPUT
pi= float(os.sys.argv[1])
semiperimetro= float(os.sys.argv[2])
altura= float(os.sys.argv[3])

#PROCESSING
area=(semiperimetro*(altura+altura))

#OUTPUT
print("#############################################################################################")
print("############################### AREA DEL PRISMA RECTO #######################################")
print("#############################################################################################")
print("######## pi:", pi,                       "###################################################")
print("######## semiperimetro:", semiperimetro, "###################################################")
print("######## altura:"       , altura,        "###################################################")
print("######## area:"         , area,          "###################################################")
print("#############################################################################################")

#CONDICION DOBLE
if (area>100):
    print("el volumen del tronco conico es la maxima")
if  (area<1):
    print("el volumen del tronco conico es el minimo")
else:
    print("volumen del tronco conico es la minima")
