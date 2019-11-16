import os

#INPUT
velocidad_angular= float(os.sys.argv[1])
radio_de_la_curvatura_de_la_trayectoria= float(os.sys.argv[2])

#PROCESSING
velocidad= velocidad_angular*radio_de_la_curvatura_de_la_trayectoria

#OUTPUT
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&&& MOVIMIENTO CIRCULAR UNIFORME &&&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("&&&&&&&&& velocidad angular:", velocidad_angular,"&&&&&&&&&&&&&")
print("&&&&&&&&& radio de la curvatura de la trayectoria:", radio_de_la_curvatura_de_la_trayectoria,"&&&&&&")
print("&&&&&&&&& velocidad:", velocidad,"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

#condicion simple
if (velocidad > 15.3):
    print("la velocidad es aceptable")
#fin_si
