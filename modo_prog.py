import math

def leer_numero(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Solo se permiten números. Intenta de nuevo.")

def menu():
    print("\n=== CALCULADORA CIENTÍFICA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Logaritmo")
    print("0. Salir")
    return input("Selecciona una opción: ")

def main():
    while True:
        opcion = menu()

        if opcion == "0":
            print("Saliendo de la calculadora.")
            break

        # Operaciones que requieren dos números
        if opcion in ["1", "2", "3", "4", "5"]:
            num1 = leer_numero("Ingresa el primer número: ")
            num2 = leer_numero("Ingresa el segundo número: ")

            if opcion == "1":
                print("Resultado:", num1 + num2)
            elif opcion == "2":
                print("Resultado:", num1 - num2)
            elif opcion == "3":
                print("Resultado:", num1 * num2)
            elif opcion == "4":
                try:
                    print("Resultado:", num1 / num2)
                except ZeroDivisionError:
                    print("Error: No se puede dividir entre cero.")
            elif opcion == "5":
                print("Resultado:", num1 ** num2)

        # Operaciones de un solo número
        elif opcion in ["6", "7", "8", "9", "10"]:
            num = leer_numero("Ingresa un número: ")

            if opcion == "6":
                if num < 0:
                    print("Error: No se puede sacar raíz de un número negativo.")
                else:
                    print("Resultado:", math.sqrt(num))
            elif opcion == "7":
                print("Resultado:", math.sin(num))
            elif opcion == "8":
                print("Resultado:", math.cos(num))
            elif opcion == "9":
                print("Resultado:", math.tan(num))
            elif opcion == "10":
                try:
                    print("Resultado:", math.log(num))
                except ValueError:
                    print("Error: El logaritmo solo está definido para números positivos.")

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
