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

#condicion multiple
if (velocidad_angular>10 and velocidad_angular<18.7):
    print("la velocidad angular es minima")
elif (velocidad_angular<7.3):
    print("la velocidad angular es muy baja")
else :
    print("la velocidad angular es maxima")
#fin_si
