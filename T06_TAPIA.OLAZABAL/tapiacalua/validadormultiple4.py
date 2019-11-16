import os

#INPUT
diagonal_mayor= float(os.sys.argv[1])
diagonal_menor= float(os.sys.argv[2])

#PROCESSING
area= (diagonal_mayor*diagonal_menor)/2

#OUTPUT
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print("°°°°°°°°°°°°°°°°°° AREA DEL ROMBO °°°°°°°°°°°°°°°")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print("°°°°°°°°° diagonal mayor:", diagonal_mayor,"°°°°°°°°°")
print("°°°°°°°°° diagonal menor:", diagonal_menor,"°°°°°°°°°")
print("°°°°°°°°° area:", area,"°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

#condicion multiple
if (area<120):
    print("el area es incorrecta")
elif (area>216):
    print("el area es la correcta")
else :
    print("el area no es la requerida")

#fin_si
