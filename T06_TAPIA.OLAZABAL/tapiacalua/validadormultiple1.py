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
if (area==10.2):
    print("el area es incorrecta")
elif (area<22.4):
    print("el area esta en el intervalo")
else :
    print("el area esta fuera del intervalo")

