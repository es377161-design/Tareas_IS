"Estrada Mendoza Esteban Uriel Agosto 2025"
Nombre=input("¿Cual es tu nombre? ")
A=float(input("¿Cual es tu peso en kilos? ")) #Asignacion de un valor a la variable 
C=float(input("¿Cual es tu altura en metros? ")) #Altura

IMC=A/C**2
if IMC < 18.5:
    print("Tiene Bajo peso")
elif 18.5 <= IMC < 25:
    print("Tiene Peso normal")
elif 25 <= IMC < 30:
    print("Tiene Sobrepeso")
elif 30 <= IMC < 35:
    print("Tiene Obesidad Tipo 1")
elif 35 <= IMC < 40:
    print("Tiene Obesidad Tipo 2")
else:  # IMC >= 40
    print("Tiene Obesidad Tipo 3 (Obesidad mórbida)")
print(Nombre ,"Tiene un indice de masa corporal de ", round(IMC))