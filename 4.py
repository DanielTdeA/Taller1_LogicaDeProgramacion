#Ejercicio 4: Número mágico Crear un programa que determine si un número ingresado por el usuario es un número "especial". 
#Un número es "especial" si cumple con los siguientes criterios: 
#• Es divisible entre 5. 
#• No es divisible entre 2 ni 3

print("Numero especial")

DIVISIBLE = 5
NODIVISIBLE1 = 2
NODIVISIBLE2 = 3

num = input("Ingrese un numero: ")

if float(num)%int(DIVISIBLE) == 0 and float(num)%int(NODIVISIBLE1) != 0 and float(num)%int(NODIVISIBLE2) != 0:
  print(num, " Es un numero especial!")
else:
  print("No es un numero especial.")