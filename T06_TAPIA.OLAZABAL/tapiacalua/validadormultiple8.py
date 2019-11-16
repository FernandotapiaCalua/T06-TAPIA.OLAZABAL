import os

#INPUT
masa= float(os.sys.argv[1])
aceleración= float(os.sys.argv[2])

#PROCESSING
fuerza_resultante= masa*aceleración

#OUTPUT
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!! FUERZA RESULTANTE !!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!! masa:", masa,"!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!! aceleracion:", aceleración,"!!!!!!!!!")
print("!!!!!!!!!!! fuerza resultante:", fuerza_resultante,"!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#condicion multiple
if (fuerza_resultante>20 and fuerza_resultante<49.3):
    print("la fuerza resultante es la correcta")
elif (fuerza_resultante>10 and fuerza_resultante<20):
    print("la fuerza resultante esta dentro de lo permitido")
else :
    print("la fuerza resultante no esta dentro del intervalo")
#fin_si
