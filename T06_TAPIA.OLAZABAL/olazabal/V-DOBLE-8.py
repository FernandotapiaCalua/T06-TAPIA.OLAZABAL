import os

#INPUT
pi= float(os.sys.argv[1])
radio= float(os.sys.argv[2])
angulo= float(os.sys.argv[3])

#PROCESSING
area=(radio*angulo)

#OUTPUT
print("#############################################################################################")
print("##################################### HUSO ESFERICO #########################################")
print("#############################################################################################")
print("######## pi:", pi,                       "###################################################")
print("######## radio:"        , radio,         "###################################################")
print("######## angulo:"       , angulo,        "###################################################")
print("######## area:"         , area,          "###################################################")
print("#############################################################################################")

#CONDICION DOBLE
if (area>129):
    print("el area del huso esferico es la maxima")
else:
    print("el area del huso esferico es la minima")
