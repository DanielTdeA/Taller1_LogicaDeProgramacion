#Ejercicio 3: Calculo de masa corporal. 
#Crear un sistema que permita calcular el índice de masa corporal de un usuario. Usar la siguiente formula peso (kg) / [estatura (m)]2

print("Calculadora de IMC")

kg = input("Ingrese su peso en Kilogramos: ")
h = input("Ingrese su altura en Metros: ")

resultadoIMC = float(kg) / (float(h)**2)

print("Tu indice de masa corporal es: ", resultadoIMC)