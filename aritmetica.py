import sys

def mostrar_menu():
    print("\n=== Calculadora Aritmética ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Regresar al menú principal")
    print("6. Salir")

def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada incorrecta. Por favor, ingresa un número.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "5":
            print("👋 Saliendo de la aplicación...")
            """Regresa al menú principal"""

        if opcion == "6":
            print("Saliendo de la aplicación...")
            sys.exit(0)

        if opcion not in {"1", "2", "3", "4"}:
            print("Opción inválida. Intenta de nuevo.")
            continue

        num1 = leer_numero("Ingresa el primer número: ")
        num2 = leer_numero("Ingresa el segundo número: ")

        if opcion == "1":
            print(f"✅ Resultado: {num1 + num2}")
        elif opcion == "2":
            print(f"✅ Resultado: {num1 - num2}")
        elif opcion == "3":
            print(f"✅ Resultado: {num1 * num2}")
        elif opcion == "4":
            if num2 == 0:
                print("⚠️ No se puede dividir entre cero.")
            else:
                print(f"✅ Resultado: {num1 / num2}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹ Interrupción detectada. Cerrando programa...")
        sys.exit(0)
