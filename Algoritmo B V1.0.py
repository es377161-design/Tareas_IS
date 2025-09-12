#Algoritmo para el metodo de biseccion
def f(x):
    return 5*x+3

X1=int(input("Valor de x1 debe ser el menor: "))
X2=int(input("Valor de x2 debe ser el mayor: "))
if f(X1)*f(X2)<0:
   print("Procediendo con el metodo...")
   R=0
   W=100

   while((X1+X2)/2)and R<W:
       X3=(X1+X2)/2
       
       if f(X1)*f(X3)<0:
          X2=X3
       else:
          X1=X3
       R+=1

   Raiz=(X1+X2)/2  
   print(f"Raíz aproximada: ",Raiz)
   print(f"Valor de f(raíz): ",f(Raiz))
   print(f"Iteraciones realizadas: ",R)
   print(f"Intervalo final: ",X1, " ",X2)


else:
   print("Los limites tienen el mismo signo. Ampliando automaticamente el intervalo...")
   Aumento=2
   M_Intento=20
   Intentos=0
   X1=X1
   X2=X2

   while f(X1)*f(X2)>=0 and Intentos<M_Intento:
      rango=abs(X1-X2)
      X1=X1-rango*Aumento
      X2=X2-rango*Aumento
      Intentos+=1

      print("Intento ",Intentos, "Valor de X1 ", (X1) ,"  Valor de X2 ", X2)
      
      if f(X1)*f(X2)<0:
        print("Nuevos intervalos X1",X1," X2 ",X2)
        print("Procediendo con el metodo...")
        while(X1+X2)/2 and Intentos<M_Intento:
            X3=((X1+X2)/2)
            if f(X1)*f(X3)<0:
               X2=X3
            else:
               X1=X3
            R+=1
      Raiz=(X1+X2)/2  
      print(f"Raíz aproximada: ",Raiz)
      print(f"Valor de f(raíz): ",f(Raiz))
      print(f"Iteraciones realizadas: ",Intentos)
      print(f"Intervalo final: ",X1, " ",X2)
   
   if f(X1)*f(X2)>=0:
    print("No se pudo encontrar un intervalo con signos opuestos después de", Intentos , "intentos.")