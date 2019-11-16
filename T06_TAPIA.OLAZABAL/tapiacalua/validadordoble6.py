import os

#INPUT
densidad= float(os.sys.argv[1])
aceleracion_por_la_gravedad= float(os.sys.argv[2])
volumen_del_liquido_desplazado= float(os.sys.argv[3])

#PROCESSING
empuje= (densidad*aceleracion_por_la_gravedad)*volumen_del_liquido_desplazado

#OUPUT}
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%% EMPUJE %%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("dendidad:", densidad)
print("aceleracion por la gravedad:", aceleracion_por_la_gravedad)
print("volumen del liquido desplazado:", volumen_del_liquido_desplazado)
print("empuje:", empuje)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion doble
if (empuje<12.9):
    print("el empuje es aceptable")
else:
    print("el empuje no es aceptable")
