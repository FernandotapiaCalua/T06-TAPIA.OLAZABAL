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

#condicion simple
if (fuerza_resultante<20):
    print("la fuerza resultante es la correcta")
#fin_si
