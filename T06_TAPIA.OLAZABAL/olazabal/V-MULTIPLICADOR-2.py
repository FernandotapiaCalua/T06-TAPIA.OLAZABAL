import os

#INPUT
cliente=os.sys.argv[1]
mesero=os.sys.argv[2]
pollo_a_la_brasa=float(os.sys.argv[3])
botella_coca_cola=float(os.sys.argv[4])
cant1=pollo_a_la_brasa*2
cant2=botella_coca_cola

#PROCESSING
consumo=cant1+cant2

#OUTPUT
print("###########################################################")
print("#####################    ROCHY¨S     ######################")
print("###########################################################")
print("################# cliente:",     cliente, "#################")
print("################# mesero:",      mesero  ,"#################")
print("############## total consumo:",  consumo ,"#################")
print("###########################################################")

#CONDICION DOBLE
if  (consumo<500):
    print("el cliente ganó una gaseosa")
if  (consumo>500):
    print("siga intentandolo")
else:
    print("el cliente no esta enfermo")
