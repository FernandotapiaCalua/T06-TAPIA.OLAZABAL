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

#condicion simple
if (peso<100):
    print("El peso es aceptable")
#fin_si
