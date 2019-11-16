import os

#INPUT
cliente=os.sys.argv[1]
mesero=os.sys.argv[2]
ceviche=float(os.sys.argv[3])
jarra_de_limonada=float(os.sys.argv[4])
cant1=ceviche*10
cant2=jarra_de_limonada*6

#PROCESSING
consumo=cant1+cant2

#OUTPUT
print("###########################################################")
print("#####################    COMEDOR     ######################")
print("###########################################################")
print("################# cliente:",     cliente, "#################")
print("################# mesero:",      mesero  ,"#################")
print("############## total consumo:",  consumo ,"#################")
print("###########################################################")

#CONDICION DOBLE
if  (consumo<4560):
    print("el cliente ganó la tarjeta de un vale de consumo gratis")
if  (consumo>4560):
    print("siga intentado")

else:
    print("el cliente no esta enfermo")
