import math
resultado_anterior = None
Historia =[]

def Suma (a, b):
    return a + b

def Resta (a, b):
    return a - b

def Multiplicacion (a, b):
    return a * b

def Division (a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir por Cero (0)"
def Potencia (a, b):
    return a**b

def Raiz_cuadrada (a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "❌ No se puede la raiz de un numero negativo."
def Modulo (a, b):
    return a % b

def calculadora ():
    global resultado_anterior
    while True:
        print ( "\n📌 calculadora")
        print ("1. Suma")
        print ("2. Resta")
        print ("3. Multiplicacion")
        print ("4. Division")
        print ("5. Potrncia")
        print ("6. Raíz cuadrada")
        print ("7. Modulo")
        print ("8. ver historia")
        print ("9. Salir")
        
        opcion = input ("Elige una opción: ")
        
        if opcion == "9":
            print ("Saliendo de la calculador.")
            break
        if opcion in ["1", "2", "3", "4","5", "7"]:
            try:
                if resultado_anterior is not None:
                    usar_resultado = input ("¿Quieres usar el resultado anterior? (s/n): ").lower
                    if usar_resultado == "s":
                        num1 = resultado_anterior
                    else:
                        num1 = float(input("ingrese le primer número: "))
                else:
                    num1 = float(input("ingrese le primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                if opcion == "1":
                    resultado = Suma(num1, num2)
                    operacion = "+"
                elif opcion == "2":
                    resultado = Resta(num1, num2)
                    operacion = "-"
                elif opcion == "3":
                    resultado = Multiplicacion(num1, num2)
                    operacion = "*"
                elif opcion == "4":
                    resultado = Division(num1, num2)
                    operacion = "/"
                elif opcion == "5":
                    resultado = Potencia(num1, num2)
                    operacion = "**"
                elif opcion == "7":
                    resultado = Modulo(num1, num2)
                    operacion = "%"
                print (f"Resultado: {resultado}")
                Historia.append (f"{num1} {operacion} {num2} = {resultado}")
                resultado_anterior = resultado
                    
            except ValueError:
                print ("❌ Error: Iingrese valores númericos validos.")
        elif opcion == "6":
            try:
                num = float(input("Ingrese el numero para calcular la raíz cuadrada: "))
                resultado = Raiz_cuadrada(num)
                print(F"Resultado; {resultado}")
                Historia.append(f"√{num} = {resultado}")
                resultado_anterior = resultado
            except ValueError:
                print ("❌ Error: Iingrese valores númericos validos.")
        elif opcion == "8":
            print("\n📜 Historial de operaciones:")
            for operacion in Historia:
                print(operacion)
            if not Historia:
                print ("No hay operaciones registradas.")
        else:
            print ("❌ Opción no valida, intente de nuevo.")
calculadora()