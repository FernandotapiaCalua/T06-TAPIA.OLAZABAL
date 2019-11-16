import os

#INPUT
frecuencia= float(os.sys.argv[1])

#PROCESSING
velocidad_angular= 2*frecuencia

#OUTPUT
print("#################################################")
print("################## VELOCIDAD ANGULAR ############")
print("#################################################")
print("############# frecuencia:", frecuencia,"############")
print("############ velocidad angular:", velocidad_angular,"###########")
print("#################################################")

#condicion simple
if (velocidad_angular>10):
    print("la velocidad angular es minima")
#fin_si
