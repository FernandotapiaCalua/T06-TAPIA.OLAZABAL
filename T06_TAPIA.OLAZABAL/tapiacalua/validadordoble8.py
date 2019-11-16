import os

#INPUT
fuerza= float(os.sys.argv[1])
variacion_del_tiempo= float(os.sys.argv[2])

#PROCESSING
impulso= fuerza*variacion_del_tiempo

#OUTPUT
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%% IMPULSO %%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("fuerza:", fuerza)
print("variacion de tiempo:", variacion_del_tiempo)
print("impulso:", impulso)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion doble
if (impulso<36.8):
    print("el impulso es el aceptable")
else:
    print("el impulso no es el aceptable")
