#Ejercicio 1: Calculadora de Fracciones.

#Crear una calculadora que maneje fracciones. El usuario ingresará dos fracciones y un operador. La calculadora deberá realizar la operación.
#Debes manejar sumas, restas, multiplicaciones y divisiones. Si el usuario intenta dividir entre cero, deberás mostrar un mensaje de error.

print("Calculadora de dos fracciones")

n1 = input("Ingrese el numerador de la primera fraccion: ")
d1 = input("Ingrese el denominador de la primera fraccion: ")
operador = input("Ingrese el operador de las fracciones: ")
n2 = input("Ingrese el numerador de la segunda fraccion: ")
d2 = input("Ingrese el denominador de la segunda fraccion: ")

if float(d1) != 0 and float(d2) != 0: 
    if operador == "+":
      print("Suma de fracciones!")
      resultadoNumerador = ((float(n1) * float(d2)) + (float(d1) * float(n2)))
      resultadoDenominador = (float(d1) * float(d2))
      resultadoFinal = resultadoNumerador / resultadoDenominador
      print("El resultado en fraccion es : ", resultadoNumerador, "/", resultadoDenominador)
      print("El resultado final es : ", resultadoFinal)
    elif operador == "-":
      print("Resta de fracciones!")
      resultadoNumerador = ((float(n1) * float(d2)) - (float(d1) * float(n2)))
      resultadoDenominador = (float(d1) * float(d2))
      resultadoFinal = resultadoNumerador / resultadoDenominador
      print("El resultado en fraccion es : ", resultadoNumerador, "/", resultadoDenominador)
      print("El resultado final es : ", resultadoFinal)
    elif operador == "*"  or operador == "." or operador == "x" or operador == "X":
      resultadoNumerador = (float(n1) * float(n2))
      resultadoDenominador = (float(d1) * float(d2))
      resultadoFinal = resultadoNumerador / resultadoDenominador
      print("El resultado en fraccion es : ", resultadoNumerador, "/", resultadoDenominador)
      print("El resultado final es : ", resultadoFinal)
    elif operador == "/":
      resultadoNumerador = (float(n1) * float(d2))
      resultadoDenominador = (float(d1) * float(n2))
      resultadoFinal = resultadoNumerador / resultadoDenominador
      print("El resultado en fraccion es : ", resultadoNumerador, "/", resultadoDenominador)
      print("El resultado final es : ", resultadoFinal)
    else:
      print("No se reconoce el operador!")
else:
    print("No se pueden operar fracciones con denominador 0")