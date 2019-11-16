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

#condicion simple
if (area>10.2):
    print("el area es incorrecta")

#fin_si
