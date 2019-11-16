import os

#INPUT
nombre= os.sys.argv[1]
nota1= float(os.sys.argv[2])
nota2=float(os.sys.argv[3])
nota3=float(os.sys.argv[4])
nota4=float(os.sys.argv[5])

#PROCESSING
promedio= (nota1+nota2+nota3+nota4)/4

#OUPUT
print("##########################################################")
print("############ PROMEDIO DE NOTAS DE MATEMATICA #############")
print("##########################################################")
print("############ NOTA 1:", nota1,"############################")
print("############ NOTA 2:", nota2,"############################")
print("############ NOTA 3:", nota3,"############################")
print("############ NOTA 4:", nota4,"############################")
print("############ PROMEDIO:", promedio,"########################")
print("##########################################################")

#condicion simple
if (promedio>10.5 and promedio>20):
    print("El alumno FERNANDO aprobo el ciclo")

#fin_si

