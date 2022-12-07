def saludar():
    print("Hola mundo! ")
def CalcularDoble(num):
    res = num*2#una funcion para el doble y la funcion es con parametro:
    print(res)
def Triplicar(num):
    res = num*3
    print(res)
def menu():
    print("Llamada a la funcion Saludar:")
    saludar()
    num = int(input("Ingrese un valor numérico para x:"))
    print("Llamada a la función CalcularDoble")
    print("El doble de ",num," es:") 
    CalcularDoble(num)
    print("El valor original de x es ",num)
    print("Llamada a la función Triplicar")
    print("El nuevo valor de ",num, " es: ")
    Triplicar(num)
menu()
