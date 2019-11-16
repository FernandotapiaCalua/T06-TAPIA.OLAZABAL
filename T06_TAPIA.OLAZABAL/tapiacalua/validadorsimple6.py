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
if (periodo<10):
    print("el periodo es incorrecto")
#fin_si
