import os

#INPUT
pi= float(os.sys.argv[1])
radio_menor= float(os.sys.argv[2])
radio_mayor= float(os.sys.argv[3])
altura= float(os.sys.argv[4])

#PROCESSING
volumen=(1/3*pi*altura*(radio_mayor**2+radio_menor**2+radio_mayor+radio_menor))

#OUTPUT
print("#############################################################################################")
print("############################# VOLUMEN DEL TRONCO CONICO #####################################")
print("#############################################################################################")
print("######## pi:", pi,                       "###################################################")
print("######## radio menor:", radio_menor,     "###################################################")
print("######## radio mayor:", radio_mayor,     "###################################################")
print("######## altura:"     , altura,          "###################################################")
print("######## volumen:"    , volumen,         "###################################################")
print("#############################################################################################")

#CONDICION DOBLE
if (volumen>63):
    print("el volumen del tronco conico es la maxima")
else:
    print("volumen del tronco conico es la minima")
