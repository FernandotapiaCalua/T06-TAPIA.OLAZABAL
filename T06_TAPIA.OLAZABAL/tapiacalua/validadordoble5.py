import os

#INPUT
masa= float(os.sys.argv[1])
calor_latente= float(os.sys.argv[1])

#PROCESSING
cantidad_de_calor= masa*calor_latente

#OUTPUT
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%% ACELERACION CENTRIPETA %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("masa:", masa)
print("calor latente:", calor_latente)
print("cantidad de calor:", cantidad_de_calor)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#condicion doble
if (cantidad_de_calor>30):
    print("la cantidad de calor es alta")
else:
    print("la acantidad de calor no es baja")
