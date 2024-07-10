libreria = []
registroVenta = []
generos = ["ficcion", "no ficcion", "ciencia"]
contador = 0


def registro_libros(titulo, autor, genero, precio):
    libro = {"Titulo": titulo, "Autor": autor, "Genero": genero, "Precio": precio}
    libreria.append(libro)


def verificar_libros():
    titulo = input("Ingrese libro:  ")
    autor = input("Ingrese autor: ")
    genero = input("Ingrese genero(ficcion, no ficcion, ciencia): ")
    while genero not in generos:
        print("Ingrese genero valido")
        genero = input("Ingrese genero(ficcion, no ficcion, ciencia): ")
    precio = input("Ingrese precio de libro: ")
    registro_libros(titulo, autor, genero, precio)


def mostrar_libros():
    for libros in libreria:
        print(f"Titulo = {libros['Titulo']}")
        print(f"Autor = {libros['Autor']}")
        print(f"Genero = {libros['Genero']}")
        print(f"Precio = {libros['Precio']}")


def mostrar_ventas():
    for venta in registroVenta:
        print(f"Titulo = {venta['Titulo']['Titulo']}")
        print(f"Cantidad = {venta['Cantidad Vendida']}")
        print(f"Unidad = {venta['Precio por unidad']}")
        print(f"Precio Total = {venta['Precio Total']}")


def verificar_ventas():
    libro_comprar = input("Ingrese titulo del libro: ")
    autor = input("Ingrese nombre del autor: ")
    for libro_encontrado in libreria:
        if (
            libro_encontrado["Titulo"] == libro_comprar
            and libro_encontrado["Autor"] == autor
        ):
            cantidadComprar = int(input("Ingrese cantidad de libros a comprar: "))
            precioTotal = cantidadComprar * int(libro_encontrado["Precio"])
            
        else:
            print("El titulo no se ha encontrado")
    registro_ventas(
        libro_encontrado, cantidadComprar, libro_encontrado["Precio"], precioTotal
    )
    


def registro_ventas(titulo, cantidad, unidad, precio):
    venta = {
        "Titulo": titulo,
        "Cantidad Vendida": cantidad,
        "Precio por unidad": unidad,
        "Precio Total": precio,
    }
    registroVenta.append(venta)
    print(registro_ventas)

def filtro_genero():
    print("Ha entrado a filtro genero")
    filtro = input("Que genero desea imprimir: ")
    while filtro not in generos:
        print("El genero ingresado no es el correcto")
        filtro = input("Que genero desea imprimir: ")
    for venta in registroVenta:
        if filtro == venta['Titulo']['Genero']:
            print(f"Titulo = {venta['Titulo']['Titulo']}")
            print(f"Cantidad = {venta['Cantidad Vendida']}")
            print(f"Unidad = {venta['Precio por unidad']}")
            print(f"Precio Total = {venta['Precio Total']}")

while True:
    print("-------------------------------")
    print("1.- Registrar libro")
    print("2.- Listar libros")
    print("3.- Registrar venta")
    print("4.- Imprimir reporte de ventas")
    print("5.- Generar txt")
    print("6.- Salir")
    print("-------------------------------")

    opc = int(input("Selecione una opcion \n"))
    if opc == 1:
        verificar_libros()
    elif opc == 2:
        mostrar_libros()
    elif opc == 3:
        verificar_ventas()
    elif opc == 4:
        print("1.- Imprimir todos los libros")
        print("2.- Imprimir por genero")
        opcion = int(input("Que opcion eliges "))
        if opcion == 1:
            mostrar_ventas()
        elif opcion == 2:
            filtro_genero()
        else:
            print("Ingrese opcion valida")

    elif opc == 5:

        nombreArchivo = 0
        with open(nombreArchivo, "w") as archivo:
            archivo.write("Reporte de ventas\n")
            for venta in registroVenta:
                archivo.write(f"Numero de venta: {venta['Numero de venta']}\n")
                archivo.write(f"Libro: {venta['Libro']}\n")
                archivo.write(f"Cantidad: {venta['Cantidad']}\n")
                archivo.write(f"Precio: {venta['Precio']}\n")
                archivo.write("-------------------------------\n")
