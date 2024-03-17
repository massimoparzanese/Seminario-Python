#Cree un programa que dada una lista de números imprima sólo los que son pares.
lista =[ 2, 5, 6,8 , 1, 3, 10, 11 ]
for number in lista:
    prueba = number % 2
    if prueba == 0 : print(number)
