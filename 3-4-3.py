nuevaListaNumeros = []
listaPares = []
listaImpares = []

def ingresarNumeros():

    try: 
        numeros = input("INGRESE NÚMEROS ")
        listaNumeros = numeros.split()
        for i in listaNumeros:
            nuevaListaNumeros.append(int(i))
    except ValueError:
        print("ingrese sólo números")

def validarNumeros():
    for i in nuevaListaNumeros:
        if type(i)== str:
            mensaje = "uno o varios elementos no son numéricos"
        else:
            mensaje = "todos los elementos son numéricos"
    print(mensaje)

def ordenarNumeros():
    for i in nuevaListaNumeros:
        if i%2==0:
            listaPares.append(i)
        else:
            listaImpares.append(i)
    print(listaPares)
    print(listaImpares)


while True:
    print("(1)INGRESE NÚMEROS")
    print("(2)VALIDAR NÚMEROS")
    print("(3)ORDENAR NÚMEROS EN LISTAS")
    print("(4)SALIR")

    try:
        opcion = int(input("INGRESE OPCIÓN "))

        if opcion==1:
            ingresarNumeros()
        elif opcion==2:
            validarNumeros()
        elif opcion==3:
            ordenarNumeros()
        elif opcion==4:
            break
    except ValueError:
        print("ingrese sólo números")

