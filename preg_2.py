dato = int(input("Ingrese la cantidad de datos: "))
prom = float()
acum = 0

for i in range(1,dato+1):#inicializa su conteo desde 0
    valor = int(input("Ingrese un numero: "))
    acum = acum + valor

prom = acum/dato

print("El promedio es:", prom)