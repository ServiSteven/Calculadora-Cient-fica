import sys

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== Calculadora en Consola ===")
    print("A. Operaciones Aritméticas Básicas")
    print("B. Álgebra y Trigonometría")
    print("C. Conversor de Sistemas (Modo Programador)")
    print("S. Salir")

def leer_numero(mensaje):
    """Lee un número desde la consola con validación."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número.")

def main():
    """Función principal de la aplicación."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "5":
            print("👋 Saliendo de la aplicación...")
            sys.exit(0)

        if opcion not in {"1", "2", "3", "4"}:
            print("❌ Opción inválida. Intenta de nuevo.")
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
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")
        sys.exit(1)