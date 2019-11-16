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
if (peso>100 and peso>72.8):
    print("El peso se acepta")
elif (peso<72.8 and peso>52.7):
    print("el peso se necesita aumentar")
else :
    print("el peso no se acepta")
#fin_si
