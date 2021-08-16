import os #limpiar maquina
os.system("cls")
nota=float(input("ingrese nota"))
if nota>=1 and nota<=7:
    if nota<4:
        print("reprobado")
    else:
        print("aprobado")
else:
    print("la nota debe ser entre 1 y 7")    