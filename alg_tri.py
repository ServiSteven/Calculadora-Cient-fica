import math

def mostrar_menu():
    print("\n=== Álgebra y Trigonometría ===")
    print("1. Potencia")
    print("2. Raíz Cuadrada")
    print("3. Cálculo de Porcentaje")
    print("4. Fórmula General (Ecuación Cuadrática)")
    print("5. Funciones Trigonométricas (Seno, Coseno, Tangente)")
    print("6. Regresar al menú principal")

def leer_numero(mensaje):
    while True:
        try:
            entrada = input(mensaje).strip()
            return float(entrada)
        except ValueError:
            print("Error: Entrada inválida. Por favor, ingresa un número válido.")

def calcular_potencia():
    print("\n--- Potencia ---")
    base = leer_numero("Ingresa la base: ")
    exponente = leer_numero("Ingresa el exponente: ")
    try:
        resultado = math.pow(base, exponente)
        print(f"Resultado: {resultado}")
    except OverflowError:
        print("Error: El resultado es demasiado grande para ser calculado.")
    except Exception as e:
        print(f"Error al calcular potencia: {e}")

def calcular_raiz_cuadrada():
    print("\n--- Raíz Cuadrada ---")
    numero = leer_numero("Ingresa el número: ")
    if numero < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo en los reales.")
    else:
        print(f"Resultado: {math.sqrt(numero)}")

def calcular_porcentaje():
    print("\n--- Cálculo de Porcentaje ---")
    # Lógica: Calcular el X% de Y
    porcentaje = leer_numero("Ingresa el porcentaje a calcular (ej. 20): ")
    total = leer_numero("Ingresa el valor total: ")
    resultado = (porcentaje / 100) * total
    print(f"El {porcentaje}% de {total} es: {resultado}")

def formula_general():
    print("\n--- Fórmula General (ax² + bx + c = 0) ---")
    a = leer_numero("Ingresa el coeficiente a: ")
    b = leer_numero("Ingresa el coeficiente b: ")
    c = leer_numero("Ingresa el coeficiente c: ")

    if a == 0:
        print("Error: El coeficiente 'a' no puede ser 0 (lo que sería una división por cero).")
        return

    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        print("Error: El discriminante es negativo. La ecuación no tiene soluciones reales.")
    else:
        try:
            x1 = (-b + math.sqrt(discriminante)) / (2*a)
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            print(f"Raíces encontradas:")
            print(f"   x1 = {x1}")
            print(f"   x2 = {x2}")
        except Exception as e:
            print(f"Error inesperado al calcular: {e}")

def funciones_trigonometricas():
    print("\n--- Funciones Trigonométricas ---")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    opcion = input("Selecciona una función (1-3): ").strip()

    if opcion not in ["1", "2", "3"]:
        print("Error: Opción inválida.")
        return

    angulo = leer_numero("Ingresa el ángulo: ")
    unidad = input("¿El ángulo está en Grados (G) o Radianes (R)? [G/R]: ").strip().upper()

    # Conversión interna: math de Python usa radianes
    if unidad == "G":
        angulo_rad = math.radians(angulo)
    elif unidad == "R":
        angulo_rad = angulo
    else:
        print("Aviso: Unidad no ha sido reconocida, se usará Radianes.")
        angulo_rad = angulo

    if opcion == "1":
        print(f"Seno: {math.sin(angulo_rad)}")
    elif opcion == "2":
        print(f"Coseno: {math.cos(angulo_rad)}")
    elif opcion == "3":
        # Validación simple para tangente indefinida en grados (90, 270...)
        if unidad == "G" and abs(angulo % 180 - 90) < 1e-9:
             print("Error: La tangente es indefinida para este ángulo.")
        else:
             print(f"Tangente: {math.tan(angulo_rad)}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            calcular_potencia()
        elif opcion == "2":
            calcular_raiz_cuadrada()
        elif opcion == "3":
            calcular_porcentaje()
        elif opcion == "4":
            formula_general()
        elif opcion == "5":
            funciones_trigonometricas()
        elif opcion == "6":
            break
        else:
            print("Error: Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
