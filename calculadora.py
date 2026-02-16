import aritmetica
import os

def mostrar_menu_grafico():

    ancho = 40 #Ancho total de la "Ventana".
    
    print("=" * ancho)  #Línea doble superior.
    print("|" + "CALCULADORA CIENTÍFICA".center(ancho - 2) + "|") #Texto centrado.
    print("=" * ancho)
    print("|" + " " * (ancho - 2) + "|") #Espacio vacío.
    print(f"|  1. Sumar {' ' * 26}|")
    print(f"|  2. Restar {' ' * 25}|")
    print(f"|  3. Multiplicar {' ' * 20}|")
    print(f"|  4. Dividir {' ' * 24}|")
    print("-" * ancho) #Separador.
    print(f"|  5. Salir {' ' * 26}|")
    print("|" + " " * (ancho - 2) + "|")
    print("=" * ancho) #Línea doble inferior.

def main():

    while True:

        os.system('cls')
        mostrar_menu_grafico()

        opcion = input("\n>> Selecciona una opción por favor: ")

        if opcion == '5':
            print("\n" + "=" * 40)
            print("  ¡Gracias por usar The Calculeitor!  ")
            print("=" * 40)
            break

        #Lógica de operaciones.
        elif opcion in ['1', '2', '3', '4']:
            try:
                print("\n" + "-" * 40)
                n1 = float(input("   Ingresa el primer número por favor bro: "))
                n2 = float(input("   Ingresa el segundo número por favor bro: "))
                print("-" * 40)

                res = 0.0
                simbolo = "?"

                if opcion == '1':
                    res = aritmetica.sumar(n1, n2)
                    simbolo = "+"
                elif opcion == '2':
                    res = aritmetica.restar(n1, n2)
                    simbolo = "-"
                elif opcion == '3':
                    res = aritmetica.multiplicar(n1, n2)
                    simbolo = "*"
                elif opcion == '4':
                    res = aritmetica.dividir(n1, n2)
                    simbolo = "/"
                
                #Resultado con formato organizado.
                print(f"\n   RESULTADO: {n1} {simbolo} {n2} = {res}")
            
            except ValueError:
                print("\n   ERROR. Hermano, las calculadoras son para números, no para letras.")
            except ZeroDivisionError:
                print("\n   ERROR. Si vuelves a dividir entre cero se va a romper la realidad bro.")
            
        else:
            print("\n  Opción no válida.")

        #Pausa antes de repetir el ciclo.
        input("\nPresiona Enter para volver al menú...")

if __name__ == "__main__":
    main()
