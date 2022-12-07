import random

a=[]

for i in range (1,11):
    x=random.randint(1,50)
    a.append(x)
print("Los elementos del arreglo son:")
print(a)
print("\n")
print("En orden inverso:")
for i in reversed(a):
    print(i,end=" ")