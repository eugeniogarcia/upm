import utilidades

print(utilidades.euros_a_bitcoins(10000))

print(utilidades.bitcoins_a_euros(2))


valor=utilidades.euros_a_bitcoins(10000)

print(f"Compre y vendi: {utilidades.bitcoins_a_euros(valor)}")

valor=utilidades.euros_a_bitcoins(10)

print(f"Compre y vendi: {utilidades.bitcoins_a_euros(valor)}")








def mostrar_menu():
    print("Menú Interactivo")
    print("1. Convertir euros bitcoins <cantidad>")
    print("2. Convertir bitcoins euros <cantidad>")
    print("3. Contar <texto>")
    print("4. Palindromo <texto>")
    print("5. Temperaturas <varios números separados por comas> <umbral>")
    print("6. Cifrar <texto> <desplazamiento>")
    print("7. Descifrar <texto> <desplazamiento>")
    print("8. productos")
    print("9. productos nuevo <nombre>")
    print("0. productos borrar <índice>")
    print("S. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        euros=input('¿cantidad de euros? ')
        print(f"Total bitcoins: {utilidades.euros_a_bitcoins(float(euros))}")
    elif opcion == '2':
        euros=input('¿cantidad de bitcoins? ')
        print(f"Total euros: {utilidades.bitcoins_a_euros(float(euros))}")

    elif opcion.upper() == 'S':
        print("¡Adiós!")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")