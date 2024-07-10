# nombreApellido.py

LIBROS = []
REGISTROVENTA = []
GENERO = ['Ficcion', 'No Ficcion', 'Ciencia']

def registro_libros():
    titulo = input("Titulo: ").strip()
    while not titulo:
        print("El título no puede estar vacío.")
        titulo = input("Titulo: ").strip()
    
    autor = input("Autor: ").strip()
    while not autor:
        print("El autor no puede estar vacío.")
        autor = input("Autor: ").strip()

    genero = input("Genero: (Ficcion/No Ficcion/Ciencia) ").strip()
    while genero not in GENERO:
        print("Ingrese genero de libro válido.")
        genero = input("Genero: (Ficcion/No Ficcion/Ciencia) ").strip()

    precio = input("Precio: ").strip()
    while not precio.isdigit():
        print("El precio debe ser un número.")
        precio = input("Precio: ").strip()
    precio = int(precio)

    LIBROS.append({
        'Titulo': titulo,
        'Autor': autor,
        'Genero': genero,
        'Precio': precio
    })

def mostrar_libros():
    if not LIBROS:
        print("No hay libros registrados.")
    else:
        for libro in LIBROS:
            print(libro)

def registro_venta():
    libro_comprar = input("¿Qué libro desea comprar?: ").strip()
    libro_encontrado = None
    for libro in LIBROS:
        if libro['Titulo'].lower() == libro_comprar.lower():
            libro_encontrado = libro
            break
    
    if libro_encontrado:
        cantidad = input("¿Cuántos libros desea comprar?: ").strip()
        while not cantidad.isdigit():
            print("La cantidad debe ser un número.")
            cantidad = input("¿Cuántos libros desea comprar?: ").strip()
        cantidad = int(cantidad)
        
        precio_final = cantidad * libro_encontrado['Precio']
        print(f"El total a pagar es {precio_final}")
        REGISTROVENTA.append({
            'Titulo': libro_encontrado['Titulo'],
            'Cantidad': cantidad,
            'Precio Unidad': libro_encontrado['Precio'],
            'Precio Total': precio_final
        })
    else:
        print("Libro no encontrado.")

def imprimir_reporte_ventas():
    if not REGISTROVENTA:
        print("No hay ventas registradas.")
    else:
        opcion = input("¿Desea imprimir todas las ventas o por género? (todas/genero): ").strip().lower()
        if opcion == "todas":
            for venta in REGISTROVENTA:
                print(venta)
        elif opcion == "genero":
            genero = input("Ingrese el género (Ficcion/No Ficcion/Ciencia): ").strip()
            while genero not in GENERO:
                print("Género no válido.")
                genero = input("Ingrese el género (Ficcion/No Ficcion/Ciencia): ").strip()
            for venta in REGISTROVENTA:
                libro = next((libro for libro in LIBROS if libro['Titulo'] == venta['Titulo']), None)
                if libro and libro['Genero'] == genero:
                    print(venta)
        else:
            print("Opción no válida.")

def generar_txt():
    nombre_archivo = input("Ingrese el nombre del archivo: ").strip() + ".txt"
    with open(nombre_archivo, 'w') as archivo:
        for venta in REGISTROVENTA:
            archivo.write(f"Titulo: {venta['Titulo']}\n")
            archivo.write(f"Cantidad: {venta['Cantidad']}\n")
            archivo.write(f"Precio Unidad: {venta['Precio Unidad']}\n")
            archivo.write(f"Precio Total: {venta['Precio Total']}\n")
            archivo.write("\n")
    print(f"Archivo {nombre_archivo} generado exitosamente.")

def main():
    while True:
        print("\n1.- Registrar libro")
        print("2.- Listar todos los libros")
        print("3.- Registrar venta")
        print("4.- Imprimir reporte de ventas")
        print("5.- Generar txt")
        print("6.- Salir del Programa")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            registro_libros()
        elif opcion == '2':
            mostrar_libros()
        elif opcion == '3':
            registro_venta()
        elif opcion == '4':
            imprimir_reporte_ventas()
        elif opcion == '5':
            generar_txt()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
