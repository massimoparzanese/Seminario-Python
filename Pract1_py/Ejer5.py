list = []

for i in range(5):
    list.append(int(input("Ingrese un numero")))
for i in list:
    if(i < 0):
       break
    print(" El numero es :",i)