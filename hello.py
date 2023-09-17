#funcion principal
def mi_funcion():
   print("mi primer Hola con Git "+"\n"+"Usando funciones")
#llamado de la funcion
mi_funcion()

def suma(a,b):
   return print("La suma es  "+str(a+b))

suma(int(input("ingrese el primer numero: ")),int(input("ingrese el segundo numero: ")))

#funcion para restar
def resta(a,b):
   return print("La resta es  "+str(a-b))
resta(int(input("ingrese el primer numero: ")),int(input("ingrese el segundo numero: ")))



def multi(a,b):
   return print("La multiplicacion es " + str(a*b))
multi(int(input("Ingrese el primer numero: ")),int(input("Ingrese el segundo numero: ")))

def divi(a,b):
   return print("La division es " + str(a/b))
divi(int(input("Ingrese el primer numero: ")),int(input("Ingrese el segundo numero: ")))