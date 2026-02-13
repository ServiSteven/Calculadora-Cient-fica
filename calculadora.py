import sys

def mostrar_menu():
    print("\n=== Calculadora en Consola ===")
    print("1. Operaciones Aritméticas Básicas")
    print("2. Álgebra y Trigonometría")
    print("3. Conversor de Sistemas (Modo Programador)")
    print("4. Salir")

def leer_numero(mensaje):
    """Lee un número desde la consola con validación."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número.")

def main():
    import modo_prog
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "4":
            print("👋 Saliendo de la aplicación...")
            sys.exit(0)

        if opcion == "1":
            import aritmetica
            aritmetica.main()
        elif opcion == "2":
            import alg_tri
            if hasattr(alg_tri, 'main'):
                alg_tri.main()
            else:
                print("No implementado.")
        elif opcion == "3":
            try:
                modo_prog.menu_programador()
            except Exception:
                print("Error: Entrada inválida")
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹ Interrupción detectada. Cerrando programa...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")
        sys.exit(1)