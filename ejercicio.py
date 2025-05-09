def ejercicio1():
    nombre = input("Introduce tu nombre: ") 
    numero = int(input("Introduce un número entero: ")) 
    for i in range(numero): 
            print(nombre)

def ejercicio2():
    nombre_completo = input("Introduce tu nombre completo: ") 
    print("\nTodo en minúsculas:", nombre_completo.lower()) 
    print("Todo en mayúsculas:", nombre_completo.upper()) 
    palabras = nombre_completo.split() 
    resultado = [palabra.capitalize() for palabra in palabras] 
    print("Primera letra en mayúscula:", " ".join(resultado))

def ejercicio3():
    nombre = input("Introduce tu nombre: ") 
    nombre_mayus = nombre.upper() 
    print(f"{nombre_mayus} tiene {len(nombre)} letras")

def ejercicio4():
    telefono = input("Introduce un número de teléfono (formato prefijo-numero-extension): ") 
    partes = telefono.split('-') 
    if len(partes) == 3:
     numero = partes[1] 
     print("Número de teléfono sin prefijo ni extensión:", numero) 
    else: 
       print("Formato Incorrecto")

def ejercicio5():
    frase = input("Introduce una frase: ") 
    print("Frase invertida:", frase[::-1])

def ejercicio6():
    frase = input("Introduce una frase: ") 
    vocal = input("Introduce una vocal: ").lower() 
    resultado = '' 
    for letra in frase: 
        if letra.lower() == vocal: 
            resultado += letra.upper() 
        else: 
            resultado += letra 
    print("Resultado:", resultado)

def ejercicio7():
    correo = input("Ingrese su correo electrónico: ")
    if "@" in correo:
        nombre = correo.split('@')[0]
        nuevo_correo = nombre + "@upana.edu.gt"
        print("Nuevo correo:", nuevo_correo)
    else:
        print("Correo inválido (no contiene '@')")

def ejercicio8():
    precio = float(input("Ingrese el precio del producto en quetzales (con decimales): "))
    quetzales = int(precio)
    centavos = round((precio - quetzales) * 100)
    print(f"Quetzales: {quetzales}")
    print(f"Centavos: {centavos}")

def ejercicio9():
    fecha = input("Ingrese la fecha de nacimiento en formato dia/mes/año: ")
    partes = fecha.split('/')
    etiquetas = ["Día", "Mes", "Año"]

    for i in range(len(partes)):
        print(f"{etiquetas[i]}: {partes[i]}")

def ejercicio10():
    productos = input("Ingrese los productos de la lista de compra separados por comas: ")
    lista = productos.split(',')
    print("Productos:")
    for producto in lista:
        print(producto.strip())

def menu():
    while True:
        print("\n=== Menú de Ejercicios ===")
        for i in range(1, 11):
            print(f"{i}. Ejercicio {i}")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9()
        elif opcion == "10":
            ejercicio10()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo")

# Llamar al menú principal
menu()