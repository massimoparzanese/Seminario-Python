#Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y
#luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.

Temperatura = int(input('Ingrese la temperatura en grados Celsius'))
print('La temperatura en grados celsius es: ', Temperatura)
Temperatura = ((Temperatura * 9/5) + 32)
print('La temperatura en grados  Fahrenheit es: ', Temperatura)