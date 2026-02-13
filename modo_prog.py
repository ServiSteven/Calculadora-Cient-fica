
def menu_programador():
    while True:
        print("\n=== Conversor de Sistemas ===")
        print("1. Binario a Hexadecimal")
        print("2. Hexadecimal a Binario")
        print("3. Regresar al menú principal")
        subop = input("Selecciona una opción: ").strip()
        if subop == "1":
            binario = input("Ingresa un número binario (ejemplo: 101011): ").strip()
            try:
                resultado = binario_a_hexadecimal(binario)
                if resultado is not None:
                    print(f"Hexadecimal: {resultado}")
                else:
                    print("Error: Entrada inválida para binario.")
            except Exception:
                print("Error: Entrada inválida.")
        elif subop == "2":
            hexadecimal = input("Ingresa un número hexadecimal (ejemplo: 1A3F): ").strip()
            try:
                resultado = hexadecimal_a_binario(hexadecimal)
                if resultado is not None:
                    print(f"Binario: {resultado}")
                else:
                    print("Error: Entrada inválida para hexadecimal.")
            except Exception:
                print("Error: Entrada inválida.")
        elif subop == "3":
            break
        else:
            print("Opción inválida.")

def binario_a_hexadecimal(binario):
    if not all(c in '01' for c in binario):
        return None
    try:
        decimal = int(binario, 2)
        return hex(decimal)[2:].upper()
    except Exception:
        return None

def hexadecimal_a_binario(hexadecimal):
    if not all(c in '0123456789abcdefABCDEF' for c in hexadecimal):
        return None
    try:
        decimal = int(hexadecimal, 16)
        return bin(decimal)[2:]
    except Exception:
        return None
