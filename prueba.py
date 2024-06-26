LIBROS=[]
REGISTROVENTA=[]
GENERO=['Ficcion','No Ficcion','Terror']
def registro_libros(LIBROS):
    titulo=input("Titulo: ")
    autor=input("Autor: ")
    genero=input("Genero: (Ficcion/No Ficcion/Terror) ")
    while genero not in GENERO:
        print("Ingrese genero de libro Valido")
        genero=input("Genero: (Ficcion/No Ficcion/Terror) ")
    precio=int(input("Precio: "))
    LIBROS.append({
            'Titulo':titulo,
            'Autor': autor,
            'Genero':genero,
            'Precio':precio
    })
def mostrar_libros():
    for libros in LIBROS:
       print(libros)    
       
def registro_venta():
    while True:
        libro_comprar=input("¿Que libro desea comprar?: ")
        if libro_comprar in LIBROS:
            cantidad=int(input("¿Cuantos libros desea comprar?"))
            precio_final= cantidad* LIBROS['Precio']
            print(f"El total a comprar es {precio_final}")
        
            
print("1.-Registrar libro")
print("2.-Listar libros")
print("3.- Registrar venta")
print("4.- Imprimir reporte de ventas")
print("5.- Generar txt")
print("6.- Salir")
while True:
    opc=int(input("Selecione una opcion "))
    if opc==1:
        registro_libros(LIBROS)
    elif opc==2:
        mostrar_libros()
    elif opc==3:
        registro_venta()
    elif opc==5:
        
        nombreArchivo=0
        with open(nombreArchivo,'w') as archivo:
            for libro in LIBROS:
                archivo.write(f"Libro {libro['Titulo']} \n")
                archivo.write(f"Autor {libro['Autor']} \n")
                archivo.write(f"Genero {libro['Genero']} \n")
                archivo.write(f"Precio: {libro['Precio']} \n")
            