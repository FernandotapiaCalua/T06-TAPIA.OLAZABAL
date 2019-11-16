import os

#INPUT
Frecuencia=float(os.sys.argv[1])

#PROCESSING
periodo= 1/Frecuencia

#OUTPUT
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$ PERIODO $$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$ frecuencia:", Frecuencia,"$$$$$$$$$$$")
print("$$$$$$$$$$$$$ periodo:", periodo,"$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#condicion simple
if (periodo<2 and periodo>1.5):
    print("el periodo es minimo")
elif (periodo>1):
    print("el periodo esta dentro de lo permitido")
else :
    print("el periodo es no permitido")

#fin_si
