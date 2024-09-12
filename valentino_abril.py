nro1 = float(input("Ingrese un numero"))
nro2 = float(input("Ingrese un numero"))

def multiplicar(nrnro101,nro2):
    resultado = nro1 * nro2
    return resultado

def dividir(nro1,nro2):
    resultado = nro1 / nro2
    return resultado


multiplicacion = multiplicar(nro1,nro2)
division = dividir(nro1,nro2)
print(f"resultado de la multiplicacion: {multiplicacion}")
print(f"resultado de la division: {division}")