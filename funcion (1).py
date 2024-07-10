# Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
# Llamarla desde el bloque principal del programa 3 veces con string distintos.

def cantidadVocales(cadena):
    cant=0
    cadena.lower()
    for i in cadena:
        if i =="a" or i=="e" or i =="i" or i =="o" or i=="u":
            cant+=1
    print("cantidad de vocales de ", cant)


cantidadVocales("abelardo")
cantidadVocales("pepe")
cantidadVocales("mojojojo")

# Confeccionar una función que reciba tres enteros y los muestre ordenados 
# de menor a mayor. En otra función solicitar la carga de 3 enteros por 
# teclado y proceder a llamar a la primer función definida.

def ordenar(v1,v2,v3):
    if v1<v2 and v1<v3 and v2<v3:
        if v2<v3:
            print(v1,v2,v3)
        else:
            print(v1,v3,v2)
    else:
        if v2<v3:
            if v1<v3:
                print(v2,v1,v3)
            else:
                print(v2,v3,v1)
        else:
            if v1<v2:
                print(v3,v1,v2)
            else:
                print(v3,v2,v1)
ordenar(5,2,8)
        
        