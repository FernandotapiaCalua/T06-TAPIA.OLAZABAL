import os

#INPUT
cliente=os.sys.argv[1]
mesero=os.sys.argv[2]
arroz_con_pato=float(os.sys.argv[3])
jarra_de_chicha=float(os.sys.argv[4])
cant1=arroz_con_pato*3
cant2=jarra_de_chicha*2

#PROCESSING
consumo=cant1+cant2

#OUTPUT
print("##################################################3###")
print("#                      RESTAURANTE                   #")
print("######################################################")
print("# cliente:",cliente)
print("# mesero:",mesero)
print("# total consumo:",consumo)
print("######################################################")
#condicion doble
if (consumo<70):
    print("el cliente cuida su salud")
else:
    print("el cliente podria estar enfermo")
