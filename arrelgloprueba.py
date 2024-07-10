LIBROS=[]
REGISTROVENTA=[]
LIBROS = []
REGISTROVENTA = []
GENERO = ['Ficcion', 'No Ficcion', 'Terror']

def registro_libros(LIBROS):
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero: (Ficcion/No Ficcion/Terror) ")
    while genero not in GENERO:
        print("Ingrese genero de libro válido")
        genero = input("Genero: (Ficcion/No Ficcion/Terror) ")
    
    while True:
        try:
            precio = int(input("Precio: "))
            if precio > 0:
                break
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    LIBROS.append({
        'Titulo': titulo,
        'Autor': autor,
        'Genero': genero,
        'Precio': precio
    })
    print("Libro registrado con éxito.")

def mostrar_libros():
    if LIBROS:
        for libro in LIBROS:
            print(libro)
    else:
        print("No hay libros registrados.")

def registro_venta():
    while True:
        libro_comprar = input("¿Qué libro desea comprar?: ")
        libro_encontrado = None
        for libro in LIBROS:
            if libro['Titulo'].lower() == libro_comprar.lower():
                libro_encontrado = libro
                break
        
        if libro_encontrado:
            while True:
                try:
                    cantidad = int(input("¿Cuántos libros desea comprar? "))
                    if cantidad > 0:
                        break
                    else:
                        print("La cantidad debe ser un número positivo.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            
            precio_final = cantidad * libro_encontrado['Precio']
            print(f"El total a pagar es {precio_final}")
            REGISTROVENTA.append({
                'Titulo': libro_encontrado['Titulo'],
                'Cantidad': cantidad,
                'Total': precio_final
            })
            continuar = input("¿Desea comprar otro libro? (s/n): ").strip().lower()
            if continuar != 's':
                break
        else:
            print("El libro no está en el inventario. Por favor, ingrese un libro válido.")

def imprimir_reporte_ventas():
    if REGISTROVENTA:
        for venta in REGISTROVENTA:
            print(f"Libro: {venta['Titulo']}, Cantidad: {venta['Cantidad']}, Total: {venta['Total']}")
    else:
        print("No hay ventas registradas.")

def generar_txt():
    nombreArchivo = "reporte_libros.txt"
    with open(nombreArchivo, 'w') as archivo:
        for libro in LIBROS:
            archivo.write(f"Libro: {libro['Titulo']}\n")
            archivo.write(f"Autor: {libro['Autor']}\n")
            archivo.write(f"Genero: {libro['Genero']}\n")
            archivo.write(f"Precio: {libro['Precio']}\n")
            archivo.write("\n")
    print(f"Archivo {nombreArchivo} generado con éxito.")

print("1.-Registrar libro")
print("2.-Listar libros")
print("3.-Registrar venta")
print("4.-Imprimir reporte de ventas")
print("5.-Generar archivo txt")
print("6.-Salir")

while True:
    try:
        opc = int(input("Seleccione una opción: "))
        if opc == 1:
            registro_libros(LIBROS)
        elif opc == 2:
            mostrar_libros()
        elif opc == 3:
            registro_venta()
        elif opc == 4:
            imprimir_reporte_ventas()
        elif opc == 5:
            generar_txt()
        elif opc == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 6.")
    except ValueError:
        print("Por favor, ingrese un número válido.")