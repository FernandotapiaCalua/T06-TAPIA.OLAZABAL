import os

#INPUT
base_mayor= float(os.sys.argv[1])
base_menor= float(os.sys.argv[2])
altura= float(os.sys.argv[3])

#PROCESSING
area= (base_mayor + base_menor)/2 * altura

#OUTPUT
print("****************************************************")
print("***********Calculamos el area del trapecio**********")
print("****************************************************")
print("***********base mayor:", base_mayor,"***************")
print("***********base menor:", base_menor,"***************")
print("***********altura:", altura,"***********************")
print("***********area:", area,"***************************")
print("****************************************************")

#condicion simple
if (area<12 and area>9):
    print("el area es la correcta")

#fin_si



























