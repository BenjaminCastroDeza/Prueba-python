nombre=[]
while True:
    nombre.append(input("Ingrese nombre \n"))
    resp=input("Desea ingresar otro nombre: ").lower()
    if resp=="no":
        break
nombre_corto= min(nombre)
nombre.remove(nombre_corto)
print(nombre)