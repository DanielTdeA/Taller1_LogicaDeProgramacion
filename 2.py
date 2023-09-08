#Ejercicio 2: Farenheit a Celcius. 

#Crear un sistema que solicite al usuario una temperatura en grados Farenheit e imprima como resultado su conversión a grados Celcius. 
#Para ello, usar la siguiente fórmula: ºC = (ºF-32) ÷ 1.8

print("Farenheit a Celcius")

Farenheit = input("Ingrese un valor en grados Farenheit: ")
Celcius = (float(Farenheit) - 32) / 1.8
print(Farenheit, " Grados Farenheit equivalen a ", Celcius, " Grados celcius.")