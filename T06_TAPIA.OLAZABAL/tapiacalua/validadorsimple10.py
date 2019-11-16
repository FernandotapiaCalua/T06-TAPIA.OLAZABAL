import os

#INPUT
constante_elastica_del_resorte= float(os.sys.argv[1])
deformacion_del_resorte= float(os.sys.argv[2])

#PROCESSING
fuerza_elastica= constante_elastica_del_resorte*deformacion_del_resorte

#OUTPUT
print("===================================================================================")
print("============================= FUERZA ELASTICA =====================================")
print("===================================================================================")
print("=============== constante elastica del resorte:", constante_elastica_del_resorte,"==============")
print("=============== deformacion del resorte:", deformacion_del_resorte,"============================")
print("=============== fuerza elastica:", fuerza_elastica,"===============================================")
print("===================================================================================")

#condicion simple
if (fuerza_elastica>20):
    print("la fuerza elastica es minima")
#fin_si
