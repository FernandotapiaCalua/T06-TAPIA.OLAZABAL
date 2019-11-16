import os

#INPUT
masa= float(os.sys.argv[1])
gravedad= float(os.sys.argv[2])

#PROCESSING
peso= masa*gravedad


#OUTPUT
print("######################################################")
print("###################### PESO ##########################")
print("######################################################")
print("################### masa:", masa,"#########################")
print("################ gravedad:", gravedad,"#####################")
print("################ peso:", peso,"#############################")
print("######################################################")

#condicion multiple
if (peso<100 and peso>50):
    print("El peso es aceptable")
elif (peso<50 and peso>32.6):
    print("el peso esta condicionado")
else :
    print("el el peso no es aceptado")
